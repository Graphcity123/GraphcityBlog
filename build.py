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
    css = css.replace("url('/static/", "url('../")
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
        # GitHub Pages subdirectory fix: convert absolute paths to relative
        html = html.replace('href="/', 'href="./')
        html = html.replace('src="/', 'src="./')
        html = html.replace('<head>', '<head><base href="/GraphcityBlog/">')
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

    # 项目页 — 预取 README
    projects_path = BASE / 'content' / 'projects.json'
    projects = json.loads(projects_path.read_text(encoding='utf-8'))
    for p in projects:
        name = p['name']
        print(f'  Fetching README for {name}...')
        try:
            readme_url = f'https://raw.githubusercontent.com/{p["repo"]}/master/README.md'
            with urllib.request.urlopen(readme_url) as resp:
                readme_content = resp.read().decode('utf-8')
        except Exception:
            # fallback: try main branch
            try:
                readme_url = f'https://raw.githubusercontent.com/{p["repo"]}/main/README.md'
                with urllib.request.urlopen(readme_url) as resp:
                    readme_content = resp.read().decode('utf-8')
            except Exception:
                readme_content = f'无法加载 README。\n\n直接访问：[{p["url"]}]({p["url"]})'

        # 用 Django 模板渲染项目页
        from django.template.loader import render_to_string
        html = render_to_string('blog/project.html', {
            'title': p['name'],
            'url': p['url'],
            'lang': p.get('lang', ''),
            'desc': p.get('desc', ''),
            'content': markdown_filter(readme_content),
        })
        html = html.replace('href="/', 'href="../')
        html = html.replace('src="/', 'src="../')
        html = html.replace('<head>', '<head><base href="/GraphcityBlog/">')
        dst = SITE / 'project' / name / 'index.html'
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(html, encoding='utf-8')
        print(f'  /project/{name}/ → project/{name}/index.html')

    # 关于页
    render_to_file('/about/', 'about/index.html')

    # 复制 CNAME（如果有）
    cname = BASE / 'CNAME'
    if cname.exists():
        shutil.copy(cname, SITE / 'CNAME')

    print(f'\nDone! Static site built to {SITE}')


if __name__ == '__main__':
    build()
