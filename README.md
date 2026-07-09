# Graphcity Blog

基于 Django 的个人博客。文章以 Markdown 文件存储，项目页自动拉取 GitHub README，无需数据库。

## 功能

- **Markdown 渲染**：LaTeX 数学公式、代码高亮（JetBrains Mono）、删除线、表格
- **7 种主题色**：青绿 / 蓝 / 玫红 / 橘橙 / 紫 / 草绿 / 灰蓝，点击切换，自动记忆
- **图片网格**：`img-grid-1` ~ `img-grid-4`，自动排版
- **代码块复制**：hover 显示复制按钮
- **B 站外链**：自动撑满宽度，禁用自动播放
- **侧边目录**：文章/项目页自动生成目录，滚动高亮当前标题
- **GitHub Pages 部署**：一键构建静态站点

## 目录结构

```
graphcity_blog/
├── config/                 # Django 配置
├── blog/                   # 主应用
│   ├── views.py            # 首页、文章详情、项目详情、关于
│   ├── templatetags/       # markdown 渲染 filter
│   ├── templates/blog/     # HTML 模板（base / home / article / project / about）
│   └── static/blog/        # CSS + 字体（HarmonyOS Sans SC）
├── content/                # 内容目录
│   ├── articles/           # 文章（每个文件夹一篇）
│   │   └── <slug>/
│   │       ├── index.md    # 文章正文（YAML front matter）
│   │       └── *.png       # 附件图片
│   └── projects.json       # 项目配置
├── build.py                # 静态站点构建脚本
├── deploy.bat              # 一键部署到 GitHub Pages
└── requirements.txt
```

## 快速开始

```bash
pip install -r requirements.txt
python manage.py runserver
```

访问 http://127.0.0.1:8000/

## 添加文章

在 `content/articles/` 下新建文件夹（任意名称作为 slug），放入 `index.md`：

```markdown
---
title: 文章标题
date: 2026-07-10
tags: Python, 博客
---

正文内容...

![图片](image.png)
```

图片等附件放在同一文件夹，markdown 里用相对路径引用。

## 添加项目

编辑 `content/projects.json`：

```json
{
  "name": "项目名",
  "url": "https://github.com/...",
  "repo": "owner/repo",
  "desc": "一句话描述",
  "lang": "Python"
}
```

项目页自动拉取并渲染仓库的 README.md。

## Markdown 特性

| 语法 | 效果 |
|------|------|
| `$$E=mc^2$$` | LaTeX 数学公式 |
| `~~删除~~` | 删除线 |
| `` `code` `` | 行内代码（JetBrains Mono） |
| ` ```python ``` ` | 代码块 + 复制按钮 |
| `<div class="img-grid-2" markdown="1">` | 2 列图片网格 |
| 目录自动生成 | 文章内标题自动抽取为侧边栏目录 |

## 部署到 GitHub Pages

```bash
deploy.bat
```

或手动：

```bash
python build.py
cd _deploy
git add -A && git commit -m "update"
git push origin gh-pages --force
```

GitHub Pages 设置中 Source 选 `gh-pages` 分支。

## URL 路由

| 路径 | 说明 |
|------|------|
| `/` | 首页（文章列表 + 项目卡片） |
| `/article/<slug>/` | 文章详情 |
| `/project/<name>/` | 项目详情（拉取 GitHub README） |
| `/about/` | 关于页 |
