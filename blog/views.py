import json
import re
import urllib.request
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.http import Http404


def _load_articles():
    """读取 content/articles/ 下所有 .md 文件，解析 front matter，按日期倒序。"""
    articles_dir = settings.CONTENT_DIR / 'articles'
    articles = []
    for f in sorted(articles_dir.glob('*.md'), reverse=True):
        text = f.read_text(encoding='utf-8')
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
        m = re.match(r'(\d{4}-\d{2}-\d{2})-(.+)', f.stem)
        articles.append({
            'slug': f.stem,
            'title': meta.get('title', f.stem),
            'date': meta.get('date', m.group(1) if m else ''),
            'tags': meta.get('tags', ''),
            'content': content,
        })
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
    filepath = settings.CONTENT_DIR / 'articles' / f'{slug}.md'
    if not filepath.exists():
        raise Http404('文章不存在')
    text = filepath.read_text(encoding='utf-8')
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
    m = re.match(r'(\d{4}-\d{2}-\d{2})-(.+)', slug)
    return render(request, 'blog/article.html', {
        'title': meta.get('title', slug),
        'date': meta.get('date', m.group(1) if m else ''),
        'tags': meta.get('tags', ''),
        'content': content,
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
            content = resp.read().decode('utf-8')
    except Exception:
        content = f'无法加载 README。\n\n直接访问：[{proj["url"]}]({proj["url"]})'

    return render(request, 'blog/project.html', {
        'title': proj['name'],
        'url': proj['url'],
        'lang': proj.get('lang', ''),
        'desc': proj.get('desc', ''),
        'content': content,
    })


def about(request):
    return render(request, 'blog/about.html')
