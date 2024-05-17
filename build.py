import jinja2
import os
import subprocess
import shlex

SOURCE_DIR = './source'
TEMP_DIR = './temp'
BUILD_DIR = './build/html'

VARIANTS = ['serverless', 'byoc']
SUBS = {
    'product_name': {
        'byoc': 'Union BYOC',
        'serverless': 'Union Serverless',
    },
    'cli_name': 'uctl',
}


def process_template(variant, template_path, variables, output_path):
    print(f'{os.getcwd()}/{template_path}')
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
    template = env.get_template(template_path)
    output = template.render(variables)
    if output.strip() != '':
        with open(output_path, 'w') as file:
            file.write(output)


def get_var_list(variant) -> dict:
    var_list = {}
    for key, value in SUBS.items():
        if isinstance(value, dict):
            var_list[key] = value[variant]
        elif isinstance(value, str):
            var_list[key] = value
    var_list[variant] = True
    return var_list


def process_directory(variant, input_dir, output_dir, variables):
    os.makedirs(output_dir, exist_ok=True)
    for root, dirs, files in os.walk(input_dir):
        for name in files:
            if name.endswith('.md'):  # Check for markdown files
                file_path = os.path.join(root, name)
                rel_path = os.path.relpath(file_path, input_dir)
                output_file_path = os.path.join(output_dir, rel_path)
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                process_template(variant, file_path, variables, output_file_path)


def process_project():
    subprocess.run(shlex.split(f'rm -rf {BUILD_DIR}'))
    subprocess.run(shlex.split(f'rm -rf {TEMP_DIR}'))
    for variant in VARIANTS:
        process_directory(variant, SOURCE_DIR, os.path.join(TEMP_DIR, variant), get_var_list(variant))
        subprocess.run(shlex.split(f'sphinx-build {TEMP_DIR}/{variant} {BUILD_DIR}/{variant}'))
    subprocess.run(shlex.split(f'cp {SOURCE_DIR}/_static/index.html {BUILD_DIR}/index.html'))
    subprocess.run(shlex.split(f'cp {SOURCE_DIR}/_static/switcher.json {BUILD_DIR}/switcher.json'))


if __name__ == "__main__":
    process_project()
