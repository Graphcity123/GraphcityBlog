import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='split')
def split_filter(value, sep=','):
    """按分隔符拆分字符串为列表。"""
    return [s.strip() for s in value.split(sep) if s.strip()]


@register.filter(name='markdown')
def markdown_filter(text):
    """将 Markdown 文本渲染为 HTML。"""
    return mark_safe(markdown.markdown(
        text,
        extensions=[
            'fenced_code', 'codehilite', 'tables', 'toc',
            'pymdownx.tilde',         # ~~删除线~~
            'pymdownx.arithmatex',    # LaTeX 数学公式
            'attr_list',              # 属性支持 {.class}
            'md_in_html',             # HTML 内渲染 markdown
        ],
        extension_configs={
            'pymdownx.arithmatex': {'generic': True},
            'pymdownx.tilde': {'smart_delete': False},
            'codehilite': {'guess_lang': False, 'css_class': 'codehilite'},
        },
    ))
