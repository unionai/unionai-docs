# New Theme Documentation

This README file documents the customization journey from the existing theme to the [new theme](https://www.figma.com/design/JuYrgIf8h3ALSH8tgQfZy8/Docs?node-id=1-2839&node-type=text&m=dev).

## TLDR;
### 1. Root dir:

```bash
(docs) ➜  docs git:(shalom/add-navbar-changes) ✗ ls -l
total 1120
-rw-r--r--@       189 Oct 12 04:54 CODEOWNERS
-rw-r--r--@       502 Oct 25 14:50 Makefile
-rw-r--r--@       179 Oct 17 11:36 Pipfile
-rw-r--r--@      2319 Oct 17 11:36 Pipfile.lock
-rw-r--r--        229 Oct 25 17:35 README - New Theme.md
-rw-r--r--@      9041 Oct 25 14:50 README.md
-rw-r--r--@    245912 Oct 17 00:27 _overflow
-rw-r--r--@    207506 Oct 17 00:27 _redirects
-rw-r--r--@     13067 Oct 25 14:50 build.py
-rw-r--r--@       388 Oct 12 04:54 docs-requirements.in
-rw-r--r--@     21052 Oct 12 04:54 docs-requirements.txt
-rw-r--r--@         0 Oct 25 17:06 pygments.py
-rw-r--r--@     33527 Oct 24 22:04 sitemap.json
drwxr-xr-x@ 10    320 Oct 25 17:06 source
drwxr-xr-x@ 12    384 Oct 24 11:11 unionai-examples
```
 #### 1.1 Source dir:

```bash
(docs) ➜  source git:(shalom/add-navbar-changes) ✗ ls -l
total 40
drwxr-xr-x@  9  288 Oct 25 17:06 _static
drwxr-xr-x@ 1   352 Oct 25 17:06 _templates
drwxr-xr-x@  9  288 Oct 17 00:27 api-reference
-rw-r--r--@    7986 Oct 25 17:43 conf.py
-rw-r--r--@    1687 Oct 17 00:27 index.md
-rw-r--r--@    7182 Oct 17 00:27 quick-start.md
drwxr-xr-x@  9  288 Oct 24 22:04 tutorials
drwxr-xr-x@ 13  416 Oct 17 00:27 user-guide
```

### 2. Theme config:

`/source/conf.py`:

```python

# path: source/conf.py

html_static_path = ["_static"]
templates_path = ["_templates"]

# CSS file locations
html_css_files = [
    # Current Theme CSS:
    "custom.css",
    # New Theme CSS:
    "new-theme.css",
    # Font Awesome
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
]

...

# JS file locations
html_js_files = ["custom.js"]

...

# Theme options
html_theme_options = {
    "navbar_start": ["navbar-logo", "variant-selector", "navbar-nav"],
    "navbar_center": [],
    "navbar_end": ["navbar-icon-links"],
    "navbar_persistent": ["navbar-nav", "search-button"],
    "secondary_sidebar_items": ["custom-page-toc"],
    "logo": {
        "text": "Union Docs",
        "image_dark": "_static/public/icon-logo.svg",
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/flyteorg/flyte",
            "icon": "fab fa-github",
        },
        {
            "name": "Slack",
            "url": "https://flyte-org.slack.com/",
            "icon": "fab fa-slack",
        },
    ],
    "footer_start": [],
    "footer_end": [],
}
```

### 3. CSS
`/source/_static/new-theme.css`

```css

/* path: source/_static/new-theme.css */

/* New Theme CSS */
:root {
    /* Color Palette, fonts, and font sizes */
    /* Overrides the -- variables here */
}

/* Light Theme */
html[data-theme="light"] {
    /* Override light theme styles here */
}

/* Dark Theme */
html[data-theme="dark"] {
    /* Override dark theme styles here */
}

/* Rest of the CSS */
```

### 4. Templates

```bash
(docs) ➜  _templates git:(shalom/add-navbar-changes) ✗ ls -l
total 64
drwxr-xr-x@ 4  128 Oct 25 17:06 components
-rw-r--r--@    343 Oct 12 04:54 custom-page-toc.html
-rw-r--r--@    665 Oct 12 04:54 custom-sidebar.html
-rw-r--r--@    675 Oct 12 04:54 custom.rst
-rw-r--r--@    347 Oct 25 17:06 layout.html
-rw-r--r--@    289 Oct 25 17:06 navbar-links.html
-rw-r--r--@   5961 Oct 25 17:06 page.html
drwxr-xr-x@ 8  256 Oct 25 17:06 sections
-rw-r--r--@    418 Oct 25 17:06 variant-selector.html
```

#### `/source/_templates/page.html`:

```html
{% extends "!page.html" %}
{{ super() }}

{% block extrahead %}
...
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Roboto+Mono:ital,wght@0,100..700;1,100..700&display=swap" rel="stylesheet">
...
{% endblock %}
```
#### `/source/_templates/layout.html`:
```html
{%- extends "!layout.html" %}

{{ super() }}

<!-- Start of override of the sections/header.html block to add the custom design -->
{% block docs_navbar %}
<header class="bd-header navbar navbar-expand-lg bd-navbar d-print-none">
    {%- include "sections/header.html" %}
</header>
{% endblock %}
<!-- End of section/header.html block override -->
```

components:

```bash
(docs) ➜  components git:(shalom/add-navbar-changes) ✗ ls -l
total 16
-rw-r--r--@   861 Oct 25 17:06 prev-next-old.html
-rw-r--r--@   910 Oct 25 17:06 prev-next.html -> previous and next buttons
```

sections:

```bash
(docs) ➜  sections git:(shalom/add-navbar-changes) ✗ ls -l
total 48
-rw-r--r--@   3142 Oct 25 17:06 header-old.html
-rw-r--r--@   3858 Oct 25 17:06 header.html
-rw-r--r--@   2638 Oct 25 17:06 header_working.html
-rw-r--r--@   1870 Oct 25 17:06 sidebar-primary-old.html
-rw-r--r--@   2148 Oct 25 17:06 sidebar-primary.html
-rw-r--r--@    331 Oct 25 17:06 sidebar-secondary.html
(docs) ➜  sections git:(shalom/add-navbar-changes) ✗
```
#### Checklist
- [x] Colors
- [x] Typography
- [x] Spacing
- [x] Borders
- [x] Shadows
- [x] Icons
- [] Animations
- [x] Buttons
- [x] Dropdowns
- [] Forms
- [] Tables
- [x] Code blocks
- [x] Alerts
- [x] Banners
- [] Breadcrumbs
- [] Cards
- [] Carousels
- [] Collapses
- [] Dropdowns
- [] Figures
- [] Jumbotrons
- [] List groups
- [] Modals
- [] Navbars
- [] Navs
- [] Pagination
- [] Popovers
- [] Progress bars
- [] Scrollbars
- [] Tooltips





