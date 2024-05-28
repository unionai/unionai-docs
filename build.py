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
def shell(command: str) -> None:
    subprocess.run(shlex.split(command))


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


# Process a single unionai-docs Markdown file.
# A unionai-docs file is a Sphinx/Myst Markdown file augmented
# with Jinja2 templating but without any `toctree` directives.
def create_sphinx_file(path: str, variant: str, tags: list[str], toctree: str = '') -> None:
    print(f'creating sphinx file for variant: {variant}')
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
    print(f'input_path: {input_path}')

    output_path: str = f'{SPHINX_SOURCE_DIR}/{variant}/{path}'
    print(f'output_path: {output_path}')

    template: jinja2.Template = None
    try:
        template = env.get_template(input_path)
    except jinja2.exceptions.TemplateNotFound:
        print(f'File not found at {input_path}')

    output: str = template.render(get_vars(variant))

    # TODO: figure out how to add the tags to the top of the output
    output = str(tags) + output + toctree

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(output)


def process_page_node(page_node: dict, variant: str, parent_path: str, parent_tags: list) -> str:
    name = page_node.get('name')
    title = page_node.get('title', None)
    tags = page_node.get('tags')
    children = page_node.get('children', None)
    print(f'node: [{name} {title} {tags} {"... " if children else ""}]')

    path = os.path.join(parent_path, name).rstrip(' /')
    print(f'path: [{path}]')

    # If tree is malformed, exit.
    if set(tags) > set(parent_tags):
        raise ValueError(f'Error processing {path}: tags of current page include element not present in parent page tags. A page for a variant cannot exist unless its parent page also exists for that variant.')

    # If this page does not appear in the current variant site return `None`.
    if variant not in tags:
        print(f'This page has no variant [{variant}]')
        return None

    # If this page has no children:
    # The file path for this page `{path}.md`.
    # Create the Sphinx file for this page, processed for the current variant.
    # Do not add a toctree to this page.
    # Return the toctree entry of this page in its parent page: `{name}`.
    if not children:
        print('This page has no children')
        create_sphinx_file(f'{path}.md', variant, tags)
        toc_entry = title + '<' + name + '>' if title else name
        print(f'toc_entry: [{toc_entry}]')
        print()
        return toc_entry

    # This page does have children:
    # Call `process_page_node` on each child, assembling the returned toctree entries into a toctree
    # The file path for this page is `{path}/index.md`.
    # Create the Sphinx file for this page, processed for the current variant.
    # Add the assembled toctree to this page.
    # Return the toctree entry of this page in its parent page: `{name}/index`
    else:
        print('This page has children')
        print()
        toctree: str = '```{toctree}\n:maxdepth: 2\n:hidden:\n\n'
        for child_page_node in children:
            toctree += process_page_node(child_page_node, variant, path, tags) + '\n'
        toctree += '```\n'
        create_sphinx_file(f'{path}/index.md', variant, tags, toctree)
        toc_entry = title + '<' + name + '/index' + '>' if title else name + '/index'
        print(f'toc_entry: [{toc_entry}]')
        return toc_entry


def process_project():
    shell(f'rm -rf {BUILD_DIR}')
    shell(f'rm -rf {SPHINX_SOURCE_DIR}')
    with open(SITEMAP, "r") as sm:
        page_node = json.load(sm)
    for tag in ALL_TAGS:
        process_page_node(page_node, tag, "", ALL_TAGS)
    for tag in ALL_TAGS:
        shell(f'sphinx-build {SPHINX_SOURCE_DIR}/{tag} {BUILD_DIR}/{tag}')
    shell(f'cp ./index.html {BUILD_DIR}/index.html')


if __name__ == "__main__":
    process_project()
