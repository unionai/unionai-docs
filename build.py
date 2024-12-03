import os
import subprocess
import shlex
import json
import re
import shutil
from pathlib import Path

import jinja2
import jupytext
import yaml
from nbformat.notebooknode import NotebookNode

# Source directory containing content in the Markdown augmented with Jinja2 templating.
# These files also lack toctree directives, as the `sitemap.json` defines the structure of the documentation
# and the toctrees are added during the template processing step
# These files are processed by this python script to create proper Sphinx files.
SOURCE_DIR: str = './source'

# Destination after Jinja2 template processing the source into proper Sphinx files.
# Each variant has its own directory comprising a complete Sphinx project.
# Sphinx build is then run on these files to generate the final HTML.
SPHINX_SOURCE_DIR: str = './sphinx_source'

# Destination of the final HTML.
# Each variant has its own directory containing the final HTML tree for that variant.
BUILD_DIR: str = './build/html'

# The sitemap defines the structure of the documentation and defines which pages appear in which variants
# The Sphinx toctrees are generated based on this sitemap and added to the Sphinx files in SPHINX_SOURCE_DIR.
SITEMAP: str = './sitemap.json'

# path of the examples submodule repository in the docs repo.
EXAMPLES_REPO: str = "./unionai-examples"

# github url of the examples repo
EXAMPLES_GITHUB_REPO: str = "https://www.github.com/unionai/unionai-examples"

# The run commands defines how to run the example code.
RUN_COMMANDS: str = './unionai-examples/run_commands.yaml'

# The set of variants.
ALL_VARIANTS: list[str] = ['serverless', 'byoc']

# The display names of the variants
VARIANT_DISPLAY_NAMES: dict[str, str] = {'serverless': 'Serverless', 'byoc': 'BYOC'}

# Global substitutions for Jinja2 templating.
# Currently unused, but can be used to substitute variables in the Markdown files.
# using the Jinja2 templating syntax `{@= variable =@}`.
SUBS: dict[str, dict[str, str] | str] = {
    'default_project': {
        'byoc': 'flytesnacks',
        'serverless': 'default',
    }
}

INSTALL_SDK_PACKAGE = "union"

DOCSEARCH_CREDENTIALS = {
    "byoc": {
        "DOCSEARCH_APP_ID": "IG23OUCJRL",
        "DOCSEARCH_API_KEY": os.getenv("DOCSEARCH_API_KEY_BYOC", ""),
        "DOCSEARCH_INDEX_NAME": "union",
    },
    "serverless": {
        "DOCSEARCH_APP_ID": "DQDAK9LPRV",
        "DOCSEARCH_API_KEY": os.getenv("DOCSEARCH_API_KEY_SERVERLESS", ""),
        "DOCSEARCH_INDEX_NAME": "union",
    },
}

BYOC_RUN_COMMANDS = """Export the following environment variable to build and push
images to your own container registry:

```{code}
# replace with your registry name
export IMAGE_SPEC_REGISTRY="<your-container-registry>"
```
"""

RUN_COMMAND_START_SERVERLESS = """::::{{dropdown}} {{fas}}`circle-play` Run on {variant}
:open:
:color: warning

:::{{button-link}} https://signup.union.ai/

Create an account
:::
"""

RUN_COMMAND_START_BYOC = """::::{{dropdown}} {{fas}}`circle-play` Run on {variant}
:open:
:color: warning

"""

RUN_COMMAND_REST = """

Once you have a Union account, install `{sdk_package}`:

```{{code}}
{pip_install_command}
```

{byoc_commands}

Then run the following commands to run the workflow:

```{{code}}
{run_commands}
```

The source code for this tutorial can be found [here {{octicon}}`mark-github`]({github_url}).

::::
"""

LOGGING_ENABLED = False

# Print to stdout
def log(msg: str) -> None:
    if LOGGING_ENABLED:
        print(msg)

# Call a shell command.
def shell(command: str, env: dict | None = None) -> None:
    _env = os.environ.copy()
    if env:
        _env.update(env)
    subprocess.run(shlex.split(command), env=_env)


# Returns a dictionary of variables based on the global SUBS dictionary,
# filtered for the specified variant and augmented with the variant itself
# as a boolean variable set to True.
def get_vars(variant: str) -> dict:
    vd: dict = {}
    for key, value in SUBS.items():
        if isinstance(value, dict):
            vd[key] = value[variant]
        elif isinstance(value, str):
            vd[key] = value
    vd[variant] = True
    return vd


def contains_metadata(src: str):
    return src.startswith('"""\n---') and src.endswith('---\n"""')


def create_run_command_node(run_commands: list[str], current_variant: str, github_url: str) -> NotebookNode:
    variant_display = SUBS["product_name"][current_variant]
    sdk_package = INSTALL_SDK_PACKAGE
    pip_install_command = f"pip install {sdk_package}"

    if current_variant == "byoc":
        byoc_commands = BYOC_RUN_COMMANDS
        pip_install_command += " flytekitplugins-envd"
        run_cmd_start = RUN_COMMAND_START_BYOC.format(
            variant=variant_display
        )
    else:
        byoc_commands = ""
        run_cmd_start = RUN_COMMAND_START_SERVERLESS.format(
            variant=variant_display
        )
    run_cmd_rest = RUN_COMMAND_REST.format(
        variant=variant_display,
        sdk_package=sdk_package,
        pip_install_command=pip_install_command,
        byoc_commands=byoc_commands,
        run_commands="\n".join(run_commands),
        github_url=github_url,
    )
    src = run_cmd_start + run_cmd_rest
    return NotebookNode(cell_type="markdown", source=src, metadata={})


def import_static_files_from_tutorial(
    name: str,
    from_path: Path,
    static_file_dir: str,
    notebook: NotebookNode,
):
    """Imports static files from a tutorial subdirectory and replaces the paths in the notebook."""
    # copy over any static files over to the sphinx source
    from_static_path = from_path.parent / static_file_dir
    if not from_static_path.exists():
        return

    # copy static files over to the _static directory
    static_dir = Path(SOURCE_DIR) / "_static" / "_tutorials" / name
    shutil.copytree(from_static_path, static_dir, dirs_exist_ok=True)

    # replace any image paths in markdown cells with the new path
    for cell in notebook["cells"]:
        if cell["cell_type"] != "markdown":
            continue

        src = cell["source"]
        # match markdown image paths, with a group for the image path
        result = re.search(r"!\[.+\]\((static\/.+)\)", src)
        if not result:
            continue

        image_path = Path(result.group(1))
        replace_image_path = Path("/", *static_dir.parts[1:]) / image_path.name
        cell["source"] = re.sub(result.group(1), str(replace_image_path), src)


def convert_tutorial_py_file_to_md(
    name: str,
    from_path: Path,
    to_path: Path,
    current_variant: str,
    run_commands: dict[str, list[str]],
):
    """Converts a tutorial Python file to a Markdown file along with its static assets."""
    log(f"converting {from_path} to {to_path}")
    notebook = jupytext.read(from_path, fmt="py:light")

    key = from_path.relative_to(Path(EXAMPLES_REPO))
    run_cmd_src = run_commands.get(str(key), None)
    github_url = f"{EXAMPLES_GITHUB_REPO}/tree/main/{key}"

    if run_cmd_src is not None:
        run_command_node = create_run_command_node(run_cmd_src, current_variant, github_url)
        notebook["cells"].insert(1, run_command_node)

    for fname in ("static", "images"):
        import_static_files_from_tutorial(name, from_path, fname, notebook)

    jupytext.write(notebook, to_path, fmt="md")


# Process a single Markdown/Jinja2 file.
# Note that the Jinja2 templating syntax is customized and differs from standard Jinja2 syntax.
# This is to avoid conflict with content that uses they standard Jinja2 syntax
def create_sphinx_file(path: str, variant: str, variants: list[str], toctree: str = '') -> None:
    n = path.count('/')
    n = n - 1 if n > 0 else 0
    indent: str = "    " * n
    log(f'{indent}Creating sphinx file for variant: {variant}')
    env: jinja2.Environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.getcwd()),
        block_start_string='{@@',
        block_end_string='@@}',
        variable_start_string='{@=',
        variable_end_string='=@}',
        comment_start_string='{@#',
        comment_end_string='#@}',
        trim_blocks=True,
        lstrip_blocks=True,
    )
    input_path: str = f'{SOURCE_DIR}/{path}'
    log(f'{indent}input_path: {input_path}')

    output_path: str = f'{SPHINX_SOURCE_DIR}/{variant}/{path}'
    log(f'{indent}output_path: {output_path}')

    try:
        template: jinja2.Template = env.get_template(input_path)
    except jinja2.exceptions.TemplateNotFound:
        log(f'{indent}File not found at {input_path}')
    else:
        output: str = template.render(get_vars(variant)).strip()
        frontmatter = f'---\nvariant-display-names: {str(VARIANT_DISPLAY_NAMES)}\navailable-variants: {str(variants)}\ncurrent-variant: {variant}\n---\n\n'
        output = frontmatter + output + toctree
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(output)


def process_page_node(
    page_node: dict,
    current_variant: str,
    parent_path: str,
    parent_variants: list,
    run_commands: dict,
) -> str:
    """Recursively process a page node in the sitemap from jinja template into sphinx format."""
    name: str = page_node.get('name', '')
    title: str = page_node.get('title', '')
    variants: list = page_node.get('variants', '')
    children: list = page_node.get('children', None)
    indent: str = parent_path.count('/') * "    "
    path: str = os.path.join(parent_path, name).rstrip(' /')

    py_file = page_node.get("from_py_file", None)
    if py_file is not None:
        py_file = Path(py_file)
        md_path = Path(SOURCE_DIR) / Path(path).with_suffix('.md')
        convert_tutorial_py_file_to_md(name, py_file, md_path, current_variant, run_commands)

    variants = [*reversed(variants)]  # make sure that serverless is the first element
    log(f'\n{indent}node: [{name} {title} {variants} {"... " if children else ""}]')
    log(f'{indent}path: [{path}]')

    # If tree is malformed, exit.
    if set(variants) > set(parent_variants):
        raise ValueError(f'Error processing {path}: variants of current page include element not present in parent page variants. A page for a variant cannot exist unless its parent page also exists for that variant.')

    # If this page does not appear in the current variant site return `None`.
    if current_variant not in variants:
        log(f'This page has no variant [{current_variant}]')
        return ''

    # If this page has no children:
    # The file path for this page `{path}.md`.
    # Create the Sphinx file for this page, processed for the current variant.
    # Do not add a toctree to this page.
    # Return the toctree entry of this page in its parent page: `{name}`.
    if not children:
        log(f'{indent}This page has no children')
        create_sphinx_file(f'{path}.md', current_variant, variants)
        toc_entry = title + ' <' + name + '>' if title else name
        log(f'{indent}toc_entry: [{toc_entry}]')
        return toc_entry

    # This page does have children:
    # Call `process_page_node` on each child, assembling the returned toctree entries into a toctree
    # The file path for this page is `{path}/index.md`.
    # Create the Sphinx file for this page, processed for the current variant.
    # Add the assembled toctree to this page.
    # Return the toctree entry of this page in its parent page: `{name}/index`
    else:
        log(f'{indent}This page has children')
        toctree: str = '\n\n```{toctree}\n:maxdepth: 2\n:hidden:\n\n'
        for child_page_node in children:
            toc_entry = process_page_node(
                child_page_node,
                current_variant,
                path,
                variants,
                run_commands,
            )
            if toc_entry:
                toctree += toc_entry + '\n'
        toctree += '```\n'
        create_sphinx_file(f'{path}/index.md', current_variant, variants, toctree)
        toc_entry = title + ' <' + name + '/index' + '>' if title else name + '/index'
        log(f'{indent}toc_entry: [{toc_entry}]')
        return toc_entry


def process_project():
    shell(f'rm -rf {BUILD_DIR}')
    shell(f'rm -rf {SPHINX_SOURCE_DIR}')

    with open(SITEMAP, "r") as sm:
        page_node = json.load(sm)

    with open(RUN_COMMANDS, "r") as rc:
        run_commands = yaml.safe_load(rc)

    for variant in ALL_VARIANTS:
        process_page_node(page_node, variant, "", ALL_VARIANTS, run_commands)
    for variant in ALL_VARIANTS:
        shell(f'cp {SOURCE_DIR}/conf.py {SPHINX_SOURCE_DIR}/{variant}')
        shell(f'cp -r {SOURCE_DIR}/_static {SPHINX_SOURCE_DIR}/{variant}')
        shell(f'cp -r {SOURCE_DIR}/_templates {SPHINX_SOURCE_DIR}/{variant}')
    for variant in ALL_VARIANTS:
        shell(
            f'sphinx-build -j auto {SPHINX_SOURCE_DIR}/{variant} {BUILD_DIR}/{variant}',
            env=DOCSEARCH_CREDENTIALS[variant],
        )
    shell(f'cp ./_redirects {BUILD_DIR}/_redirects')


if __name__ == "__main__":
    import time
    start = time.time()
    process_project()
    end = time.time()
    print(f"Total time: {end - start} seconds")
