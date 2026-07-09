import re
import json
import urllib.request
import markdown
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.http import Http404
from django.utils.safestring import mark_safe


def _render_markdown(text):
    """渲染 Markdown 为 HTML，同时提取目录。"""
    md = markdown.Markdown(
        extensions=[
            'fenced_code', 'codehilite', 'tables', 'toc',
            'pymdownx.tilde', 'pymdownx.arithmatex', 'attr_list', 'md_in_html',
        ],
        extension_configs={'pymdownx.arithmatex': {'generic': True}},
    )
    body = md.convert(text)
    toc = md.toc if hasattr(md, 'toc') else ''
    return mark_safe(body), mark_safe(toc)


def _parse_front_matter(text):
    """解析 YAML front matter，返回 (meta, content)。"""
    meta = {}
    content = text
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            for line in parts[1].strip().split('\n'):
                if ':' in line:
                    k, v = line.split(':', 1)
                    meta[k.strip()] = v.strip()
            content = parts[2].strip()
    return meta, content


def _load_articles():
    """读取 content/articles/*/index.md，按日期倒序。"""
    articles_dir = settings.CONTENT_DIR / 'articles'
    articles = []
    for folder in sorted(articles_dir.glob('*/'), reverse=True):
        md_file = folder / 'index.md'
        if not md_file.exists():
            continue
        text = md_file.read_text(encoding='utf-8')
        meta, content = _parse_front_matter(text)
        articles.append({
            'slug': folder.name,
            'title': meta.get('title', folder.name),
            'date': meta.get('date', ''),
            'tags': meta.get('tags', ''),
            'content': content,
        })
    articles.sort(key=lambda a: a['date'], reverse=True)
    return articles


def home(request):
    articles = _load_articles()
    projects_path = settings.CONTENT_DIR / 'projects.json'
    projects = []
    if projects_path.exists():
        projects = json.loads(projects_path.read_text(encoding='utf-8'))
    return render(request, 'blog/home.html', {
        'articles': articles,
        'projects': projects,
    })


def article(request, slug):
    filepath = settings.CONTENT_DIR / 'articles' / slug / 'index.md'
    if not filepath.exists():
        raise Http404('文章不存在')
    text = filepath.read_text(encoding='utf-8')
    meta, md_content = _parse_front_matter(text)
    # 相对路径图片→本地路径，外链跳过
    image_base = f'/content/articles/{slug}/'
    md_content = re.sub(r'\]\((?!https?://)([^)]+)\)', rf']({image_base}\1)', md_content)
    body_html, toc_html = _render_markdown(md_content)
    return render(request, 'blog/article.html', {
        'title': meta.get('title', slug),
        'date': meta.get('date', ''),
        'tags': meta.get('tags', ''),
        'content': body_html,
        'toc': toc_html,
    })


def project(request, name):
    projects_path = settings.CONTENT_DIR / 'projects.json'
    if not projects_path.exists():
        raise Http404('项目不存在')
    projects = json.loads(projects_path.read_text(encoding='utf-8'))
    proj = next((p for p in projects if p['name'] == name), None)
    if not proj or 'repo' not in proj:
        raise Http404('项目不存在')

    readme_url = f'https://raw.githubusercontent.com/{proj["repo"]}/master/README.md'
    try:
        with urllib.request.urlopen(readme_url) as resp:
            readme_content = resp.read().decode('utf-8')
    except Exception:
        try:
            readme_url = f'https://raw.githubusercontent.com/{proj["repo"]}/main/README.md'
            with urllib.request.urlopen(readme_url) as resp:
                readme_content = resp.read().decode('utf-8')
        except Exception:
            readme_content = f'无法加载 README。\n\n直接访问：[{proj["url"]}]({proj["url"]})'

    return render(request, 'blog/project.html', {
        'title': proj['name'],
        'url': proj['url'],
        'lang': proj.get('lang', ''),
        'desc': proj.get('desc', ''),
        'content': readme_content,
    })


def about(request):
    return render(request, 'blog/about.html')
