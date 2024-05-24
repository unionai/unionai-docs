import jinja2
import os
import subprocess
import shlex


SOURCE_DIR = './source'
TEMP_DIR = './temp'
BUILD_DIR = './build/html'
SITEMAP = './sitemap.md'
VARIANTS = ['serverless', 'byoc']
SUBS = {
    'product_name': {
        'byoc': 'Union BYOC',
        'serverless': 'Union Serverless',
    },
    'cli_name': 'uctl',
}


# Call a shell command.
# Supports interpolation of global variables.
def shell_command(command):
    subprocess.run(shlex.split(command))


# Process a single unionai-docs Markdown file.
# A unionai-docs file is a Sphinx/Myst Markdown file augmented
# with Jinja2 templating but without any `toctree` directives.
def process_md_file(input_path, variables, output_path):
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
    output = template.render(variables)
    with open(output_path, 'w') as file:
        if output.strip() == '':
            file.write(f'<html><head></head><body>{output_path} is an empty page</body></html>')
        else:
            file.write(output)


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


def get_indent(line):
    return len(line) - len(line.lstrip(' ')) // 4


# Parses a single line of the sitemap file
def get_tuple(line):
    stripped_line = line.lstrip(line)
    parts = stripped_line.split('<')
    if len(parts) < 2:
        raise ValueError('Error in sitemap. Expected `<`')
    title_part = parts[0].strip()
    title = title_part if title_part else None
    slug_and_tags = parts[1].split('>')
    if len(slug_and_tags) < 2:
        raise ValueError('Error in sitemap. Expected `>`')
    slug = slug_and_tags[0].strip()
    if slug == '':
        raise ValueError('Error in sitemap. Slug must be non-empty')
    tags_part = slug_and_tags[1].strip(' `')
    tags = VARIANTS
    if tags_part != '':
        tags = tags_part.split()
    return title, slug, tags


# Processes the lines of the sitemap file starting at the current index.
# Return a list holding a tree structure of the sitemap.
def get_tree(lines: list, current_indent: int)-> list:
    tree: list = []
    while lines:
        line: str = lines[0]
        line_indent: int = get_indent(line)
        stripped: str = line
        if line_indent < current_indent:
            break
        lines.pop(0)
        if line_indent == current_indent:
            tree.append(stripped)
        elif line_indent > current_indent:
            tree.append([stripped].append(get_tree(lines, line_indent + 1)))
    return tree


def process_project():
    shell_command(f'rm -rf {BUILD_DIR}')
    shell_command(f'rm -rf {TEMP_DIR}')
    with open(SITEMAP, 'r') as file:
        lines = file.readlines()
    tree = get_tree(lines)
    for variant in VARIANTS:
        shell_command(f'sphinx-build {TEMP_DIR}/{variant} {BUILD_DIR}/{variant}')
    shell_command(f'cp ./index.html {BUILD_DIR}/index.html')


if __name__ == "__main__":
    with open(SITEMAP, 'r') as file:
        lines = file.readlines()
    tree = get_tree(lines, 0)
    print(tree)

