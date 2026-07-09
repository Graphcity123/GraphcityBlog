# Graphcity Blog

基于 Django 的个人博客。Markdown 文件存储文章，JSON 配置项目展示，无需数据库。

## 目录结构

```
graphcity_blog/
├── config/                 # Django 配置
├── blog/                   # 主应用
│   ├── views.py            # 首页、文章详情、关于
│   ├── templatetags/       # markdown 渲染 filter
│   ├── templates/blog/     # HTML 模板
│   └── static/blog/        # CSS
├── content/                # 内容
│   ├── articles/*.md       # Markdown 文章
│   └── projects.json       # 项目配置
└── requirements.txt
```

## 使用

```bash
pip install -r requirements.txt
python manage.py runserver
```

## 添加文章

在 `content/articles/` 下新建 `YYYY-MM-DD-slug.md`：

```markdown
---
title: 文章标题
date: 2026-07-09
tags: Python, 爬虫
---

正文内容...
```

## 添加项目

编辑 `content/projects.json`，添加 `repo` 字段（GitHub 仓库路径），项目页会自动拉取并渲染仓库的 `README.md`：

```json
{
  "name": "项目名",
  "url": "https://github.com/...",
  "repo": "owner/repo",
  "desc": "一句话描述",
  "lang": "Python"
}
```

## URL 路由

| 路径 | 说明 |
|------|------|
| `/` | 首页（文章列表 + 项目卡片） |
| `/article/<slug>/` | 文章详情 |
| `/project/<name>/` | 项目详情（拉取 GitHub README） |
| `/about/` | 关于页 |
