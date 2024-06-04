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
extensions = ['myst_parser',
              'sphinx_design',
              'sphinx_copybutton',
              'sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.autosectionlabel',
              'sphinx_click']
html_theme = 'sphinx_book_theme'

# Myst
myst_enable_extensions = ['colon_fence']
myst_heading_anchors = 6

# Sphinx book theme

# Union logo
html_logo = '_static/public/logo.svg'

# Add variant selector to sidebar
html_sidebars = {
    "**": ['navbar-logo.html',
           'search-button-field.html',
           'variant-selector.html',
           'sbt-sidebar-nav.html']
}

# autodoc config
autodoc_typehints = "description"
autosummary_generate = True

# Makes it so that only the command is copied, not the output
copybutton_prompt_text = "$ "

# prevent css style tags from being copied by the copy button
copybutton_exclude = 'style[type="text/css"]'


# replace flyte-specific text in docstrings pulled in
# with autodoc (automodule, autoclass, etc)
def process_docstring(app, what, name, obj, options, lines):
    for str in lines:
        idx = lines.index(str)
        str = str.replace('FlyteRemote ', 'UnionRemote ')\
            .replace('FlyteRemote(', 'UnionRemote(')\
            .replace('flyte_workflow', 'union_workflow')\
            .replace('Flyte remote backend', 'Union remote backend')\
            .replace('Flyte platform', 'Union platform')\
            .replace('Flyte Admin', 'Union Admin')\
            .replace('Flyte backend', 'Union backend')\
            .replace('flyte backend', 'union backend')\
            .replace('flyte config', 'union config')\
            .replace('Flyte UI', 'web console')
        del lines[idx]
        lines.insert(idx, str)


def process_description(app, ctx, lines):
    for str in lines:
        idx = lines.index(str)
        str = str.replace("Flyte UI", "web console")\
            .replace("Flyte's execution system", "Union's execution system")\
            .replace("Flyte Execution", "Union execution")\
            .replace("Flyte Console", "web console")\
            .replace("Flyte Python CLI environment",
                     "Union Python CLI environment")\
            .replace("flyte-ready", "Union-ready")\
            .replace("Flyte backend registrable", "Union backend registrable")\
            .replace("entities in Flyte", "entities in Union")\
            .replace("remote flyte instance", "remote Union instance")
        del lines[idx]
        lines.insert(idx, str)


def process_options(app, ctx, lines):
    for str in lines:
        idx = lines.index(str)
        str = str.replace("flyteremote", "UnionRemote")\
            .replace("Flyte deployment", "Union deployment")\
            .replace("pyflyte serialize", "unionai serialize")\
            .replace("pyflyte utility", "unionai utility")
        del lines[idx]
        lines.insert(idx, str)


def setup(app):
    app.connect('autodoc-process-docstring', process_docstring)
    app.connect("sphinx-click-process-description", process_description)
    app.connect("sphinx-click-process-options", process_options)
