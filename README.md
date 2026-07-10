# Graphcity Blog

基于 Django 的个人博客。文章以 Markdown 文件存储，项目页自动拉取 GitHub README，无需数据库。一键构建静态站点部署到 GitHub Pages。

## 功能

- **Markdown 渲染**：LaTeX 数学公式、代码高亮（Pygments Monokai 主题）、删除线、表格
- **8 种主题色**：青绿 / 蓝 / 玫红 / 橘橙 / 紫 / 草绿 / 灰蓝 / 天蓝，点击切换，自动记忆
- **图片网格**：`img-grid-1` ~ `img-grid-4`，自动排版
- **代码块复制**：hover 显示复制按钮
- **B 站外链**：自动撑满宽度，禁用自动播放
- **侧边目录**：自动生成，滚动高亮；无标题时展示文章名作为目录项
- **智能搜索**：导航栏搜索框 + 独立搜索页，多关键词加权打分（标题 > 标签 > 正文），文章/项目分 tab 展示。静态站点使用 JSON 索引 + 客户端 JS 搜索
- **标签归档**：点击文章标签或项目语言胶囊跳转归档页，标签云浏览，路径式 URL（`/archive/<tag>/`）
- **子弹标题**：`- **文本**` 自动转为带圆点的四级标题并加入目录
- **文章 / 项目主页**：独立列表页，分页导航
- **移动端适配**：响应式布局，导航栏/卡片/搜索均优化
- **GitHub Pages 部署**：一键构建 + GitHub Actions 自动部署

## 目录结构

```
graphcity_blog/
├── config/                 # Django 配置
├── blog/                   # 主应用
│   ├── views.py            # 首页、文章/项目列表、详情、搜索、归档、关于
│   ├── templatetags/       # markdown / split 自定义 filter
│   ├── templates/blog/     # HTML 模板
│   │   ├── base.html       # 基模板（导航栏、主题切换、TOC 高亮）
│   │   ├── home.html       # 首页（文章 + 项目 + 更多链接）
│   │   ├── article.html    # 文章详情
│   │   ├── article_list.html  # 文章列表（分页）
│   │   ├── project.html    # 项目详情
│   │   ├── project_list.html  # 项目列表（分页）
│   │   ├── search.html     # 搜索（服务端 + 客户端双模式）
│   │   ├── archive.html    # 标签归档（标签云 + 分 tab 结果）
│   │   ├── about.html      # 关于页
│   │   └── _pagination.html   # 分页组件
│   └── static/blog/        # CSS + 字体（HarmonyOS Sans SC）
├── content/                # 内容目录
│   ├── articles/           # 文章（每个文件夹一篇）
│   │   └── <slug>/
│   │       ├── index.md    # 文章正文（YAML front matter）
│   │       └── *.png       # 附件图片
│   ├── projects.json       # 项目配置
│   └── projects_readme.json # 项目 README 缓存（自动生成）
├── .github/workflows/      # GitHub Actions 自动部署
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
tags:
  - 博客
  - 技术
---

正文内容...

![图片](image.png)
```

图片等附件放在同一文件夹，markdown 里用相对路径引用。

tags 支持两种格式：
- 单行：`tags: Python, 博客`
- 列表（YAML）：
  ```yaml
  tags:
    - Python
    - 博客
  ```

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

项目页自动拉取并渲染仓库的 README.md，首次拉取后缓存到 `projects_readme.json`，后续搜索和访问直接读缓存。

## Markdown 特性

| 语法 | 效果 |
|------|------|
| `$$E=mc^2$$` | LaTeX 数学公式 |
| `~~删除~~` | 删除线（中文字符紧贴也支持） |
| `` `code` `` | 行内代码（JetBrains Mono） |
| ` ```python ``` ` | 代码块 + 语法高亮 + 复制按钮 |
| `<div class="img-grid-2" markdown="1">` | 2 列图片网格 |
| `- **文本**` | 子弹标题（带圆点的四级标题，自动加入目录） |
| 目录自动生成 | 文章内标题自动抽取为侧边栏目录，滚动高亮 |

## URL 路由

| 路径 | 说明 |
|------|------|
| `/` | 首页（最新 5 篇文章 + 6 个项目 + 更多链接） |
| `/articles/` | 文章主页（分页，10 篇/页） |
| `/articles/page/<n>/` | 文章列表第 n 页 |
| `/projects/` | 项目主页（分页，12 个/页） |
| `/projects/page/<n>/` | 项目列表第 n 页 |
| `/article/<slug>/` | 文章详情 |
| `/project/<name>/` | 项目详情 |
| `/search/` | 搜索页（全部 / 文章 / 项目 tab） |
| `/archive/` | 标签云 |
| `/archive/<tag>/` | 标签归档（全部 / 文章 / 项目 tab） |
| `/about/` | 关于页 |

## 搜索

导航栏搜索框 + `/search/` 独立搜索页。支持多关键词（空格/逗号分隔），加权打分：

| 匹配位置 | 文章 | 项目 |
|----------|------|------|
| 标题/名称 | +10 | +10 |
| 标签/描述 | +5 | +5 |
| 语言 | — | +3 |
| 正文 | +1 | +1（README 缓存） |

结果按相关度降序，文章/项目分 tab 展示（全部 / 文章 / 项目）。开发服务器走 Django 后端搜索，静态站点走 JSON 索引 + 客户端 JS 搜索。

## 部署

### 一键部署

```bash
deploy.bat
```

### GitHub Actions

推送 `master` 分支自动触发构建部署，无需手动操作。

### 手动部署

```bash
python build.py
cd _deploy
git add -A && git commit -m "update"
git push origin gh-pages --force
```

GitHub Pages 设置中 Source 选 `gh-pages` 分支。

## 依赖

- Django 6.0
- Python-Markdown
- Pygments（代码高亮）
- PyMdown Extensions（删除线、LaTeX 等）
