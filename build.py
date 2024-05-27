import jinja2
import os
import subprocess
import shlex
import json


SOURCE_DIR = './source'
TEMP_DIR = './temp'
BUILD_DIR = './build/html'
SITEMAP = './sitemap.json'
ALL_TAGS = ['serverless', 'byoc']
SUBS = {
    'product_name': {
        'byoc': 'Union BYOC',
        'serverless': 'Union Serverless',
    },
    'cli_name': 'uctl',
}


# Call a shell command.
# Supports interpolation of global variables.
def shell(command):
    subprocess.run(shlex.split(command))


# Process a single unionai-docs Markdown file.
# A unionai-docs file is a Sphinx/Myst Markdown file augmented
# with Jinja2 templating but without any `toctree` directives.
def process_md_file(input_path, output_path, var_list, toctree=None):
    env = jinja2.Environment(
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
    template = env.get_template(input_path)
    output = template.render(var_list)
    append_toctree(output, toctree)
    with open(output_path, 'w') as f:
        f.write(output)


# Returns a dictionary of variables based on the global SUBS dictionary,
# filtered for the specified variant and augmented with the variant itself
# as a boolean variable set to True.
def get_var_list(variant) -> dict:
    var_list = {}
    for key, value in SUBS.items():
        if isinstance(value, dict):
            var_list[key] = value[variant]
        elif isinstance(value, str):
            var_list[key] = value
    var_list[variant] = True
    return var_list


def process_page(page, parent_path=None, parent_tags=None):
    name = page['name']
    tags = page['tags']
    children = page['children']
    path = os.path.join(parent_path, name).rstrip(' /')

    # If tags of current page include element not present in parent page tags raise error.
    # A page for a variant cannot exist unless its parent page also exists for that variant.
    if not set(tags) > set(parent_tags):
        raise ValueError(f'Error processing {path}: tags of current page include element not present in parent page tags. A page for a variant cannot exist unless its parent page also exists for that variant.')

    for tag in tags:
        var_list = get_var_list(tag)

        # If the page has no children then its file location is {path}.md and it has no toctree
        if not children:
            process_md_file(
                f'{SOURCE_DIR}/{path}.md',
                f'{TEMP_DIR}/{tag}/{path}.md',
                var_list
            )

        # If the page has children then its file location is {parent_path}/{name}/index.md
        else:
            process_md_file(
                f'{SOURCE_DIR}/{path}/index.md',
                f'{TEMP_DIR}/{tag}/{path}.md',
                var_list,
                toctree
            )


def process_project():
    shell(f'rm -rf {BUILD_DIR}')
    shell(f'rm -rf {TEMP_DIR}')
    with open(SITEMAP, "r") as sm:
        page = json.load(sm)
    process_page(page)
    for tag in ALL_TAGS:
        shell_command(f'sphinx-build {TEMP_DIR}/{tag} {BUILD_DIR}/{tag}')
    shell_command(f'cp ./index.html {BUILD_DIR}/index.html')


if __name__ == "__main__":
    with open(SITEMAP, 'r') as file:
        lines = file.readlines()
    tree = get_tree(lines, 0)
    print(tree)
