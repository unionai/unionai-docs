# Pre-processor for markdown files

import re
import os


def evaluate_boolean(boolean_expression, context):
    # Create a dictionary to hold the boolean values for the variables
    variables = {}

    # Extract variable names from the boolean expression
    for var in boolean_expression.split():
        if var.isidentifier() and var not in ["and", "or", "not", "True", "False"]:
            variables[var] = var in context

    # Evaluate the boolean expression in a restricted environment
    try:
        result = eval(E, {"__builtins__": None}, variables)
    except Exception as e:
        return str(e)  # Return the error message if evaluation fails

    return result


# Process conditional blocks
def process_conditionals(content, context):
    # RE that gets the boolean expression and if block from each if statement
    pattern = re.compile(r'{{ if (.*?) }}(.*?){{ end if }}', re.DOTALL)
    while True:
        # Get each if block
        match = pattern.search(content)
        if not match:
            break
        boolean_expression = match.group(1).strip()
        if_block = match.group(2)
        if evaluate_boolean(boolean_expression, context):
            content = content[:match.start()] + if_block + content[match.end():]
        else:
            content = content[:match.start()] + content[match.end():]
    return content


# Process substitutions
def process_substitutions(content, substitutions, context):
    pattern = re.compile(r'{{ sub (.*?) }}')
    content = pattern.sub(lambda match: substitutions[context].get(match.group(1).strip(), ''), content)
    return content

# Apply the pre-processing steps


def process_directory(directory_path, bool_vars, sub_vars):
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".md"):
                    template_path = os.path.join(root, file)
                    output_path = os.path.join(root, f"processed_{file}")
                    render_template(template_path, output_path, bool_vars, sub_vars)

def process_project():
    processed_content = process_conditionals(template_content)
    processed_content = process_substitutions(processed_content)

    # Check if content is only whitespace or empty
    if not processed_content.strip():
        print(f"After processing {template_path} is empty or only whitespace. Skipping.")
    else:
        # Write the processed content to the output file
        with open(output_path, 'w') as file:
            file.write(processed_content)

# Example usage
if __name__ == '__main__':

    # Call the function to process the directory
    process_directory('../source', bool_vars, sub_vars)

    sub_vars = {
        'value1': 'Hello, World!',
        'value2': 'Python Programming',
    }

    render_template('template.txt', 'output.txt', bool_vars, sub_vars)





def render_template(template_path, output_path, variant, subs):
    # Read the template content
    with open(template_path, 'r') as file:
        template_content = file.read()


# Example usage:
E = "A and B or not C"
L = ["A", "B"]
print(evaluate_boolean_expression(E, L))  # Output: True
