# Hugo Tech-Blog Starter — Retr0

This is a ready-to-clone Hugo repo skeleton designed for a tech blog hosted on GitHub Pages. It includes a minimal `config.toml`, an example post, an archetype, a GitHub Actions workflow to build & deploy to the `gh-pages` branch, and a short checklist to get you live quickly.

---

## What this repo contains (paste these files into a new repo)

### 1) `README.md` (explain how to use)

````
# Retr0 Tech Notes — Hugo Starter

This repo is a minimal Hugo starter for a tech blog. It uses a theme as a git submodule (recommended) and GitHub Actions to build and deploy to GitHub Pages (branch: `gh-pages`).

## Quick start (on your machine)

1. Clone this repo:

```bash
git clone https://github.com/<username>/<repo>.git
cd <repo>
````

2. Initialize submodules for theme (if you added a theme submodule):

```bash
git submodule update --init --recursive
```

3. Install Hugo ([https://gohugo.io/getting-started/install/](https://gohugo.io/getting-started/install/)).

4. Serve locally while editing:

```bash
hugo server -D
# open http://localhost:1313
```

5. When ready to publish, commit & push to `main`. GitHub Actions will build and push the generated `public/` to the `gh-pages` branch.

## Notes

* If you want a user site (username.github.io) you can configure Pages to use `gh-pages` branch or the `main` branch's `/docs` folder; this workflow publishes to `gh-pages`.
* Replace `<username>` and site `baseURL` in `config.toml` before pushing for correct URLs.

```

---

### 2) `config.toml` (minimal, replace username/url)
```

baseURL = "https://<username>.github.io/"
languageCode = "en-us"
title = "Retr0 Tech Notes"
theme = "ananke"
paginate = 5
enableRobotsTXT = true

# Optional: set params for theme (customize per theme docs)

[params]
description = "Tech solutions, tutorials, and tinkering notes."
author = "Retr0"

```

---

### 3) `archetypes/default.md` (new post template)
```

---

title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: true
categories: ["tech"]
tags: ["misc"]
--------------

Write your post here. Use fenced code blocks for snippets.

```

---

### 4) `content/posts/2025-11-10-first-post.md` (example post)
```

---

title: "First post — Setting up Hugo"
date: 2025-11-10T23:00:00+05:30
draft: false
categories: ["setup"]
tags: ["hugo","github-pages"]
-----------------------------

Welcome to my Hugo-powered tech blog. This is a test post proving that Markdown, code fences, and front matter work.

Example shell snippet:

```bash
# build
hugo --minify
```

```

---

### 5) `.github/workflows/hugo-deploy.yml` (GitHub Actions)
```

name: Build and deploy Hugo site to GitHub Pages

on:
push:
branches: [ main ]

permissions:
contents: write

jobs:
build:
runs-on: ubuntu-latest
steps:
- name: Checkout repository
uses: actions/checkout@v4
with:
submodules: true
fetch-depth: 0

```
  - name: Setup Hugo
    uses: peaceiris/actions-hugo@v3
    with:
      hugo-version: '0.116.0'

  - name: Build
    run: hugo --minify

  - name: Deploy to gh-pages
    uses: peaceiris/actions-gh-pages@v4
    with:
      publish_dir: ./public
      publish_branch: gh-pages
      user_name: 'github-actions[bot]'
      user_email: 'github-actions[bot]@users.noreply.github.com'
      keep_history: true
```

```

---

### 6) `.gitignore`
```

/public/
/resources/_gen/
.DS_Store
.node_modules/
.env

````

---

### 7) Optional: Add a submodule theme (recommended)
Pick a theme (e.g. `ananke`, `PaperMod`, `hyde`, etc.). To add `ananke` as a submodule:

```bash
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
````

Then ensure `theme = "ananke"` is in `config.toml`.

---

## Extra tips & configuration suggestions

* Syntax highlighting: Hugo uses Chroma. To enable line numbers and style, customize your theme's `config.toml` per theme docs.
* Add `CNAME` to `static/` if you plan a custom domain.
* For search, add a client-side index like Lunr.js or use a theme with built-in search assets.
* For math (LaTeX), include KaTeX or MathJax in your layout `/layouts/partials/head.html`.

---

## Short deployment checklist

1. Replace `<username>` in `config.toml`.
2. Add a theme (submodule) or copy a theme into `/themes`.
3. Commit everything to `main` and push.
4. Go to GitHub Settings → Pages and set source to `gh-pages` branch (if not auto-configured).
5. Visit `https://<username>.github.io` after the first Actions run completes.

---