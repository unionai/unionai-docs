# Project
project = 'union-docs'
copyright = '2024, Union'
author = 'Union'
release = '1.0'

# Sphinx basic
master_doc = 'index'
html_static_path = ['_static']
templates_path = ['_templates']
html_css_files = ['custom.css']
exclude_patterns = []
extensions = ['myst_parser', 'sphinx_design', 'sphinx_copybutton']
html_theme = 'sphinx_book_theme'

# Myst
myst_enable_extensions = ['colon_fence']
myst_heading_anchors = 6

# Sphinx book theme

# Union logo
html_logo = '_static/public/logo.svg'

# Add variant selector to sidebar
html_sidebars = {
    "**": ['navbar-logo.html', 'search-button-field.html', 'variant-selector.html', 'sbt-sidebar-nav.html']
}

# Sphinx copybutton

# Makes it so that only the command is copied, not the prompt
copybutton_prompt_text = "$ "

# Prevent CSS style tags from being copied by the copy button
copybutton_exclude = 'style[type="text/css"]'
