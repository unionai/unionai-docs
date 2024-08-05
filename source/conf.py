import os
import re

# Project
project = "union-docs"
copyright = "2024, Union"
author = "Union"
release = "1.0"

# Sphinx basic
master_doc = "index"
html_static_path = ["_static"]
templates_path = ["_templates"]
html_css_files = [
    "custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
]
html_js_files = ["custom.js"]

exclude_patterns = []
extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.graphviz",
    "sphinx.ext.inheritance_diagram",
    "sphinxext.remoteliteralinclude",
    "sphinx_click",
    "sphinx_docsearch"
]
html_theme = "sphinx_book_theme"
graphviz_output_format = 'svg'

# Myst
myst_enable_extensions = ["colon_fence"]
myst_heading_anchors = 6

# Sphinx book theme

# Union logo
html_logo = "_static/public/logo.svg"
html_favicon = "_static/public/favicon.ico"

# Add variant selector to sidebar
html_sidebars = {
    "**": [
        "navbar-logo.html",
        "variant-selector.html",
        "searchbox.html",
        "sbt-sidebar-nav.html",
    ]
}

# autodoc config
autodoc_typehints = "description"
autosummary_generate = True

# Makes it so that only the command is copied, not the output
copybutton_prompt_text = "$ "

# prevent css style tags from being copied by the copy button
copybutton_exclude = 'style[type="text/css"]'

# algolia docsearch credentials
docsearch_app_id = os.getenv("DOCSEARCH_APP_ID")
docsearch_api_key = os.getenv("DOCSEARCH_API_KEY")
docsearch_index_name = os.getenv("DOCSEARCH_INDEX_NAME")


# replace flyte-specific text in docstrings pulled in
# with autodoc (automodule, autoclass, etc)
def process_docstring(app, what, name, obj, options, lines):
    for str in lines:
        idx = lines.index(str)
        str = str.replace('FlyteRemote ', 'UnionRemote ')\
            .replace('flyteremote', 'UnionRemote')\
            .replace('Flyte remote', 'Union remote')\
            .replace('FlyteRemote(', 'UnionRemote(')\
            .replace('flyte_workflow', 'union_workflow')\
            .replace('Flyte remote backend', 'Union remote backend')\
            .replace('Flyte platform', 'Union platform')\
            .replace('Flyte Admin', 'Union Admin')\
            .replace('Flyte backend', 'Union backend')\
            .replace('flyte backend', 'union backend')\
            .replace('flyte config', 'union config')\
            .replace('Flyte UI', 'UI')
        del lines[idx]
        lines.insert(idx, str)


def process_description(app, ctx, lines):
    for str in lines:
        idx = lines.index(str)
        str = str.replace("Flyte UI", "UI")\
            .replace("Flyte's execution system", "Union's execution system")\
            .replace("Flyte Execution", "Union execution")\
            .replace("Flyte Console", "UI")\
            .replace("Flyte Python CLI environment",
                     "Union Python CLI environment")\
            .replace("flyte-ready", "Union-ready")\
            .replace("Flyte backend registrable", "Union backend registrable")\
            .replace("entities in Flyte", "entities in Union")\
            .replace("remote flyte instance", "remote Union instance")\
            .replace("pyflyte package", "union package")\
            .replace("flytectl", "uctl")\
            .replace("pyflyte run", "union run")
        del lines[idx]
        lines.insert(idx, str)


def process_str(my_str):
    my_str = my_str.replace("flyteremote", "UnionRemote")\
        .replace("Flyte deployment", "Union deployment")\
        .replace("pyflyte serialize", "union serialize")\
        .replace("pyflyte utility", "union utility")\
        .replace("install flytekit", "install union and flytekit")
    return my_str


def process_options(app, ctx, lines):
    # process option docstrings to replace flyte-specific
    # language with union-specific language
    # and change str representations of functions
    # to default image and project values
    counter = 5
    default_project = "'default' (Serverless), 'flytesnacks' (BYOC)"
    default_image = "'cr.union.ai/union/unionai:py3.11-latest' (Serverless), 'cr.flyte.org/flyteorg/flytekit:py3.9-latest' (BYOC)"
    for line in lines:
        idx = lines.index(line)
        if ctx.command.name == 'build' or ctx.command.name == 'run':
            if "--image" in line:
                counter = 0
        if counter == 4:
            line = re.sub(r"<function.*>", default_image, line)
        else:
            line = re.sub(r"functools.partial.*'flytesnacks'\)",
                          default_project, line)
        line = process_str(line)
        del lines[idx]
        lines.insert(idx, line)
        counter += 1


def setup(app):
    app.connect('autodoc-process-docstring', process_docstring)
    app.connect("sphinx-click-process-description", process_description)
    app.connect("sphinx-click-process-options", process_options)
