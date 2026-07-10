import re
import json
import time
import urllib.request
import markdown
from pathlib import Path
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import Http404
from django.utils.safestring import mark_safe


def _render_markdown(text):
    """渲染 Markdown 为 HTML，同时提取目录。将 - **xxx** 转为带 bullet 的四级标题。"""
    text = re.sub(r'^- \*\*(.+?)\*\*\s*$', r'#### \1', text, flags=re.MULTILINE)
    md = markdown.Markdown(
        extensions=[
            'fenced_code', 'codehilite', 'tables', 'toc',
            'pymdownx.tilde', 'pymdownx.arithmatex', 'attr_list', 'md_in_html',
        ],
        extension_configs={
            'pymdownx.arithmatex': {'generic': True},
            'pymdownx.tilde': {'smart_delete': False},
            'codehilite': {'guess_lang': False, 'css_class': 'codehilite'},
        },
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
            current_key = None
            for line in parts[1].strip().split('\n'):
                if ':' in line:
                    k, v = line.split(':', 1)
                    k = k.strip()
                    v = v.strip()
                    if v:
                        meta[k] = v
                        current_key = None
                    else:
                        meta[k] = ''
                        current_key = k
                elif line.strip().startswith('- ') and current_key:
                    item = line.strip()[2:]
                    if meta[current_key]:
                        meta[current_key] += ', ' + item
                    else:
                        meta[current_key] = item
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


def _load_readme_cache():
    """读取项目 README 缓存文件。"""
    cache_path = settings.CONTENT_DIR / 'projects_readme.json'
    if cache_path.exists():
        return json.loads(cache_path.read_text(encoding='utf-8'))
    return {}


def _save_readme_cache(cache):
    """写入项目 README 缓存文件。"""
    cache_path = settings.CONTENT_DIR / 'projects_readme.json'
    cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding='utf-8')


def _fetch_readme(repo):
    """从 GitHub 拉取项目的 README.md。"""
    for branch in ('master', 'main'):
        try:
            url = f'https://raw.githubusercontent.com/{repo}/{branch}/README.md'
            with urllib.request.urlopen(url, timeout=5) as resp:
                return resp.read().decode('utf-8')
        except Exception:
            continue
    return None


def home(request):
    articles = _load_articles()
    projects_path = settings.CONTENT_DIR / 'projects.json'
    projects = []
    if projects_path.exists():
        projects = json.loads(projects_path.read_text(encoding='utf-8'))
    return render(request, 'blog/home.html', {
        'articles': articles[:5],
        'projects': projects[:6],
        'article_total': len(articles),
        'project_total': len(projects),
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

    repo = proj['repo']
    readme_cache = _load_readme_cache()
    if repo in readme_cache:
        readme_content = readme_cache[repo]
    else:
        readme_content = _fetch_readme(repo)
        if readme_content:
            readme_cache[repo] = readme_content
            _save_readme_cache(readme_cache)
        else:
            readme_content = f'无法加载 README。\n\n直接访问：[{proj["url"]}]({proj["url"]})'

    body_html, toc_html = _render_markdown(readme_content)
    return render(request, 'blog/project.html', {
        'title': proj['name'],
        'url': proj['url'],
        'lang': proj.get('lang', ''),
        'desc': proj.get('desc', ''),
        'content': body_html,
        'toc': toc_html,
    })


def about(request):
    return render(request, 'blog/about.html')


def search(request):
    """搜索文章和项目，加权打分，分 tab 展示。"""
    query = request.GET.get('q', '').strip()
    tab = request.GET.get('tab', 'all')
    articles_result = []
    projects_result = []
    elapsed = 0

    if query:
        t0 = time.perf_counter()
        keywords = [kw.lower() for kw in re.split(r'[\s,，]+', query) if kw]

        # 搜索文章
        for a in _load_articles():
            title_lower = a['title'].lower()
            tags_lower = a['tags'].lower()
            content_lower = a['content'].lower()
            score = 0
            for kw in keywords:
                if kw in title_lower:
                    score += 10
                if kw in tags_lower:
                    score += 5
                if kw in content_lower:
                    score += 1
            if score > 0:
                articles_result.append({**a, 'score': score})

        # 搜索项目（含 README 正文，自动缓存）
        projects_path = settings.CONTENT_DIR / 'projects.json'
        readme_cache = _load_readme_cache()
        cache_dirty = False
        if projects_path.exists():
            projects = json.loads(projects_path.read_text(encoding='utf-8'))
            for p in projects:
                repo = p.get('repo', '')
                # 自动拉取未缓存的项目 README
                if repo and repo not in readme_cache:
                    content = _fetch_readme(repo)
                    if content:
                        readme_cache[repo] = content
                        cache_dirty = True
                name_lower = p['name'].lower()
                desc_lower = p.get('desc', '').lower()
                lang_lower = p.get('lang', '').lower()
                readme_lower = readme_cache.get(repo, '').lower()
                score = 0
                for kw in keywords:
                    if kw in name_lower:
                        score += 10
                    if kw in desc_lower:
                        score += 5
                    if kw in lang_lower:
                        score += 3
                    if kw in readme_lower:
                        score += 1
                if score > 0:
                    projects_result.append({**p, 'score': score})

        # 按得分降序
        articles_result.sort(key=lambda x: x['score'], reverse=True)
        projects_result.sort(key=lambda x: x['score'], reverse=True)
        if cache_dirty:
            _save_readme_cache(readme_cache)
        elapsed = (time.perf_counter() - t0) * 1000

    return render(request, 'blog/search.html', {
        'query': query,
        'tab': tab,
        'articles': articles_result,
        'projects': projects_result,
        'article_count': len(articles_result),
        'project_count': len(projects_result),
        'total_count': len(articles_result) + len(projects_result),
        'elapsed': elapsed,
    })


def archive(request, tag=''):
    """归档页：按 tag 筛选文章和项目，分 tab 展示。"""
    if not tag:
        tag = request.GET.get('tag', '').strip()
    tab = request.GET.get('tab', 'all')
    articles_result = []
    projects_result = []

    if tag:
        tag_lower = tag.lower()
        # 筛选文章（tags 包含此标签）
        for a in _load_articles():
            tags_lower = a['tags'].lower()
            if tag_lower in [t.strip().lower() for t in a['tags'].split(',') if t.strip()]:
                articles_result.append(a)
        # 筛选项目（lang 匹配此标签，或 tags 匹配）
        projects_path = settings.CONTENT_DIR / 'projects.json'
        if projects_path.exists():
            projects = json.loads(projects_path.read_text(encoding='utf-8'))
            for p in projects:
                lang_lower = p.get('lang', '').lower()
                name_lower = p['name'].lower()
                if tag_lower in lang_lower or tag_lower in name_lower:
                    projects_result.append(p)

    # 收集所有标签用于云展示
    all_tags = set()
    for a in _load_articles():
        for t in a['tags'].split(','):
            t = t.strip()
            if t:
                all_tags.add(t)
    projects_path = settings.CONTENT_DIR / 'projects.json'
    if projects_path.exists():
        for p in json.loads(projects_path.read_text(encoding='utf-8')):
            lang = p.get('lang', '').strip()
            if lang:
                all_tags.add(lang)

    return render(request, 'blog/archive.html', {
        'tag': tag,
        'tab': tab,
        'articles': articles_result,
        'projects': projects_result,
        'article_count': len(articles_result),
        'project_count': len(projects_result),
        'all_tags': sorted(all_tags),
    })


def article_list(request):
    """文章列表页，分页。"""
    articles = _load_articles()
    paginator = Paginator(articles, 10)
    page = paginator.get_page(request.GET.get('page', 1))
    return render(request, 'blog/article_list.html', {
        'page': page,
        'total': len(articles),
    })


def project_list(request):
    """项目列表页，分页。"""
    projects_path = settings.CONTENT_DIR / 'projects.json'
    projects = []
    if projects_path.exists():
        projects = json.loads(projects_path.read_text(encoding='utf-8'))
    paginator = Paginator(projects, 12)
    page = paginator.get_page(request.GET.get('page', 1))
    return render(request, 'blog/project_list.html', {
        'page': page,
        'total': len(projects),
    })
