import jinja2
import os
import subprocess
import shlex
import json


SOURCE_DIR: str = './source'
SPHINX_SOURCE_DIR: str = './sphinx_source'
BUILD_DIR: str = './build/html'
SITEMAP: str = './sitemap.json'
ALL_TAGS: list[str] = ['serverless', 'byoc']
SUBS: dict[str: dict[str: str] | str: str] = {
    'product_name': {
        'byoc': 'Union BYOC',
        'serverless': 'Union Serverless',
    },
    'cli_name': 'uctl',
}


# Call a shell command.
# Supports interpolation of global variables.
def shell(command: str) -> None:
    subprocess.run(shlex.split(command))


# Process a single unionai-docs Markdown file.
# A unionai-docs file is a Sphinx/Myst Markdown file augmented
# with Jinja2 templating but without any `toctree` directives.
def create_sphinx_file(path: str, variant: str, tags: list[str], toctree: str = None) -> None:
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
    output_path: str = f'{SPHINX_SOURCE_DIR}/{variant}/{path}'
    template: jinja2.Template = env.get_template(input_path)
    output:str = template.render(get_vars(variant))

    # TODO: figure out how to add the tags to the top of the output
    output = tags + output + toctree
    
    with open(output_path, 'w') as f:
        f.write(output)


# Returns a dictionary of variables based on the global SUBS dictionary,
# filtered for the specified variant and augmented with the variant itself
# as a boolean variable set to True.
def get_vars(variant: str) -> dict:
    vl = {}
    for key, value in SUBS.items():
        if isinstance(value, dict):
            vl[key] = value[variant]
        elif isinstance(value, str):
            vl[key] = value
    vl[variant] = True
    return vl


def process_page_node(page_node: dict, variant: str, path: str = None, parent_tags: str = None) -> str:
    name = page_node['name']
    title = page_node['title']
    tags = page_node['tags']
    children = page_node['children']
    path = os.path.join(path, name).rstrip(' /')

    # If tree is malformed, exit.
    if set(tags) > set(parent_tags):
        raise ValueError(f'Error processing {path}: tags of current page include element not present in parent page tags. A page for a variant cannot exist unless its parent page also exists for that variant.')

    # If this page does not appear in the current variant site return `None`.
    if variant not in tags:
        return None

    # If this page has no children:
    # The file path for this page `{path}.md`.
    # Create the Sphinx file for this page, processed for the current variant.
    # Do not add a toctree to this page.
    # Return the toctree entry of this page in its parent page: `{name}`.
    if not children:
        create_sphinx_file(f'{path}.md', variant, tags)
        return name

    # This page does have children:
    # Call `process_page_node` on each child, assembling the returned toctree entries into a toctree
    # The file path for this page is `{path}/index.md`.
    # Create the Sphinx file for this page, processed for the current variant.
    # Add the assembled toctree to this page.
    # Return the toctree entry of this page in its parent page: `{name}/index`
    else:
        toctree: str = '```{toctree}\n:maxdepth: 2\n:hidden:\n\n'
        for child_page_node in children:
            toctree += process_page_node(child_page_node, path, tags, variant) + '\n'
        toctree += '```\n'
        create_sphinx_file(f'{path}/index.md', variant, tags, toctree)
        return name + '/index'


def process_project():
    shell(f'rm -rf {BUILD_DIR}')
    shell(f'rm -rf {SPHINX_SOURCE_DIR}')
    with open(SITEMAP, "r") as sm:
        page_node = json.load(sm)
    for tag in ALL_TAGS:
        process_page_node(page_node, tag)
    for tag in ALL_TAGS:
        shell(f'sphinx-build {TEMP_DIR}/{tag} {BUILD_DIR}/{tag}')
    shell(f'cp ./index.html {BUILD_DIR}/index.html')


if __name__ == "__main__":
    process_project()
