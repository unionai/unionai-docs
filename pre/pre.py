# Pre-processor for markdown files

import re
import os

def render_template(template_path, output_path, bool_vars, sub_vars):
    # Read the template content
    with open(template_path, 'r') as file:
        template_content = file.read()

    # Define a function to evaluate boolean expressions
    def eval_expr(expr):
        try:
            return eval(expr, {}, bool_vars)
        except Exception as e:
            print(f"Error evaluating expression '{expr}': {e}")
            return False

    # Process conditional blocks
    def process_conditionals(content):
        conditional_pattern = re.compile(r'{{ if (.*?) }}(.*?){{ end if }}', re.DOTALL)
        while True:
            match = conditional_pattern.search(content)
            if not match:
                break
            condition = match.group(1).strip()
            block_content = match.group(2)
            if eval_expr(condition):
                content = content[:match.start()] + block_content + content[match.end():]
            else:
                content = content[:match.start()] + content[match.end():]
        return content

    # Process substitutions
    def process_substitutions(content):
        sub_pattern = re.compile(r'{{ sub (.*?) }}')
        content = sub_pattern.sub(lambda match: sub_vars.get(match.group(1).strip(), ''), content)
        return content

    # Apply the pre-processing steps
    processed_content = process_conditionals(template_content)
    processed_content = process_substitutions(processed_content)

    # Check if content is only whitespace or empty
    if not processed_content.strip():
        print(f"After processing {template_path} is empty or only whitespace. Skipping.")
    else:
        # Write the processed content to the output file
        with open(output_path, 'w') as file:
            file.write(processed_content)

def process_directory(directory_path, bool_vars, sub_vars):
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".md"):
                    template_path = os.path.join(root, file)
                    output_path = os.path.join(root, f"processed_{file}")
                    render_template(template_path, output_path, bool_vars, sub_vars)

def process_project():
    

# Example usage
if __name__ == '__main__':


    # Call the function to process the directory
    process_directory('../source', bool_vars, sub_vars)

    sub_vars = {
        'value1': 'Hello, World!',
        'value2': 'Python Programming',
    }

    render_template('template.txt', 'output.txt', bool_vars, sub_vars)
