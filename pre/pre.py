from jinja2 import Environment, FileSystemLoader
import os

source_dir = './source'
dest_dir_prefix = './temp'
variants = ['byoc', 'serverless']
substitutions = {
    'product_name': {
        'byoc': 'Union BYOC',
        'serverless': 'Union Serverless',
    },
    'cli_name': 'uctl',
}


def process_template(template_path, variables, output_path):
    env = Environment(loader=FileSystemLoader('/'))
    template = env.get_template(template_path)
    output = template.render(variables)

    with open(output_path, 'w') as file:
        file.write(output)


def get_var_list(variant) -> dict:
    var_list = {}
    for key, value in substitutions:
        if isinstance(value, dict):
            var_list[key] = value[variant]
        elif isinstance(value, str):
            var_list[key] = value
    var_list[variant] = True
    return var_list


def process_directory(input_dir, output_dir, variables):
    os.makedirs(output_dir, exist_ok=True)
    for root, dirs, files in os.walk(input_dir):
        for name in files:
            if name.endswith('.md'):  # Check for markdown files
                file_path = os.path.join(root, name)
                rel_path = os.path.relpath(file_path, input_dir)
                output_file_path = os.path.join(output_dir, rel_path)
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                process_template(file_path, variables, output_file_path)


def process_project():
    for variant in variants:
        process_directory(source_dir, os.path.join(dest_dir_prefix, variant), get_var_list(variant))


if __name__ == "__main__":
    process_project()