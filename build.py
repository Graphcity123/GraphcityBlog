"""生成静态 HTML 站点到 _site/ 目录，用于 GitHub Pages 部署。"""
import json
import os
import shutil
import urllib.request
from pathlib import Path
from django.core.wsgi import get_wsgi_application
from django.test import RequestFactory

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

BASE = Path(__file__).resolve().parent
SITE = BASE / '_deploy'


def build():
    # 初始化 Django
    import django
    django.setup()

    from blog.views import _load_articles
    from blog.templatetags.blog_tags import markdown_filter

    # 清空输出目录（保留 .git）
    if not SITE.exists():
        SITE.mkdir()
    for item in sorted(SITE.iterdir()):
        if item.name == '.git':
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()

    # 复制静态文件并修复 CSS 路径
    static_src = BASE / 'blog' / 'static' / 'blog'
    static_dst = SITE / 'static' / 'blog'
    shutil.copytree(static_src, static_dst)
    css = (static_dst / 'style.css').read_text(encoding='utf-8')
    css = css.replace("url('/static/", "url('/GraphcityBlog/static/")
    (static_dst / 'style.css').write_text(css, encoding='utf-8')

    # Django test client 渲染模板
    from django.test import Client
    client = Client()

    def render_to_file(url, path, image_base=None):
        resp = client.get(url)
        html = resp.content.decode('utf-8')
        # Fix article image paths for static build (skip external URLs)
        if image_base:
            import re as _re
            html = _re.sub(r'src="(?!https?://)([^"]+)"', rf'src="{image_base}\1"', html)
        # GitHub Pages subdirectory fix
        html = html.replace('href="/', 'href="/GraphcityBlog/')
        html = html.replace('src="/', 'src="/GraphcityBlog/')
        html = html.replace('action="/', 'action="/GraphcityBlog/')
        html = html.replace("location.href='/", "location.href='/GraphcityBlog/")
        dst = SITE / path
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(html, encoding='utf-8')
        print(f'  {url} → {path}')

    print('Rendering pages...')
    # 首页
    render_to_file('/', 'index.html')

    # 文章页 + 复制文章附件
    articles = _load_articles()
    for a in articles:
        slug = a['slug']
        render_to_file(f'/article/{slug}/', f'article/{slug}/index.html')
        # 复制文章附件（图片等）到部署目录
        article_dir = BASE / 'content' / 'articles' / slug
        dst_dir = SITE / 'content' / 'articles' / slug
        if article_dir.exists():
            shutil.copytree(article_dir, dst_dir, dirs_exist_ok=True)

    # 项目页 — 优先读缓存，缓存未命中才联网
    projects_path = BASE / 'content' / 'projects.json'
    projects = json.loads(projects_path.read_text(encoding='utf-8'))
    readme_cache_path = BASE / 'content' / 'projects_readme.json'
    readme_cache = json.loads(readme_cache_path.read_text(encoding='utf-8')) if readme_cache_path.exists() else {}
    for p in projects:
        name = p['name']
        repo = p['repo']
        if repo in readme_cache:
            readme_content = readme_cache[repo]
            print(f'  README for {name} (cached)')
        else:
            print(f'  Fetching README for {name}...')
            readme_content = None
            for branch in ('master', 'main'):
                try:
                    readme_url = f'https://raw.githubusercontent.com/{repo}/{branch}/README.md'
                    with urllib.request.urlopen(readme_url, timeout=10) as resp:
                        readme_content = resp.read().decode('utf-8')
                    break
                except Exception:
                    continue
            if readme_content:
                readme_cache[repo] = readme_content
            else:
                readme_content = f'无法加载 README。\n\n直接访问：[{p["url"]}]({p["url"]})'

        # 用 Django 模板渲染项目页（含 TOC）
        from blog.views import _render_markdown
        body_html, toc_html = _render_markdown(readme_content)
        from django.template.loader import render_to_string
        html = render_to_string('blog/project.html', {
            'title': p['name'],
            'url': p['url'],
            'lang': p.get('lang', ''),
            'desc': p.get('desc', ''),
            'content': body_html,
            'toc': toc_html,
        })
        html = html.replace('href="/', 'href="/GraphcityBlog/')
        html = html.replace('src="/', 'src="/GraphcityBlog/')
        html = html.replace('action="/', 'action="/GraphcityBlog/')
        html = html.replace("location.href='/", "location.href='/GraphcityBlog/")
        dst = SITE / 'project' / name / 'index.html'
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(html, encoding='utf-8')
        print(f'  /project/{name}/ → project/{name}/index.html')
    # 保存更新后的 README 缓存
    with open(readme_cache_path, 'w', encoding='utf-8') as f:
        json.dump(readme_cache, f, ensure_ascii=False, indent=2)

    # 关于页
    render_to_file('/about/', 'about/index.html')

    # 文章列表页（所有分页）
    import math
    total_articles = len(articles)
    article_pages = math.ceil(total_articles / 10) if total_articles > 0 else 1
    render_to_file('/articles/', 'articles/index.html')
    for pg in range(1, article_pages + 1):
        render_to_file(f'/articles/page/{pg}/', f'articles/page/{pg}/index.html')

    # 项目列表页（所有分页）
    total_projects = len(projects)
    project_pages = math.ceil(total_projects / 12) if total_projects > 0 else 1
    render_to_file('/projects/', 'projects/index.html')
    for pg in range(1, project_pages + 1):
        render_to_file(f'/projects/page/{pg}/', f'projects/page/{pg}/index.html')

    # 搜索页
    render_to_file('/search/', 'search/index.html')

    # 归档页（标签云）
    render_to_file('/archive/', 'archive/index.html')
    # 为每个标签生成归档页
    all_tags = set()
    for a in articles:
        for t in a['tags'].split(','):
            t = t.strip()
            if t:
                all_tags.add(t)
    for p in projects:
        lang = p.get('lang', '').strip()
        if lang:
            all_tags.add(lang)
    for tag in sorted(all_tags):
        from django.utils.http import urlencode
        import urllib.parse
        tag_encoded = urllib.parse.quote(tag, safe='')
        render_to_file(f'/archive/{tag_encoded}/', f'archive/{tag}/index.html')

    # 搜索索引（JSON，供静态站点客户端搜索）
    search_index = []
    for a in articles:
        search_index.append({
            'type': 'article',
            'title': a['title'],
            'date': a['date'],
            'tags': a['tags'],
            'slug': a['slug'],
            'content': a['content'][:500],
        })
    for p in projects:
        search_index.append({
            'type': 'project',
            'title': p['name'],
            'desc': p.get('desc', ''),
            'lang': p.get('lang', ''),
            'url': p['url'],
        })
    (SITE / 'search_index.json').write_text(json.dumps(search_index, ensure_ascii=False), encoding='utf-8')

    # 复制 CNAME（如果有）
    cname = BASE / 'CNAME'
    if cname.exists():
        shutil.copy(cname, SITE / 'CNAME')

    print(f'\nDone! Static site built to {SITE}')


if __name__ == '__main__':
    build()
