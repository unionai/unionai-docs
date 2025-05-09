import sys
import re
import htmltabletomd

def process_file(file_path):
    # Read from stdin instead of a file
    try:
        content = sys.stdin.read()
    except Exception as e:
        print(f"Error reading from stdin: {e}", file=sys.stderr)
        sys.exit(1)

    # Remove all <style>...</style> blocks
    style_pattern = re.compile(r'<style.*?>.*?</style>', re.DOTALL)
    content = style_pattern.sub('', content)

    # Remove all <div> and </div> tags
    div_pattern = re.compile(r'<div.*?>', re.DOTALL)
    content = div_pattern.sub('', content)
    div_pattern = re.compile(r'</div>', re.DOTALL)
    content = div_pattern.sub('', content)

    # Replace <p>...</p> tags with newlines
    p_pattern = re.compile(r'<p.*?>', re.DOTALL)
    content = p_pattern.sub('\n', content)
    p_pattern = re.compile(r'</p>', re.DOTALL)
    content = p_pattern.sub('\n', content)

    # Find all tables in the content
    table_pattern = re.compile(r'<table.*?>.*?</table>', re.DOTALL)
    tables = table_pattern.findall(content)

    # Replace each table with a placeholder
    placeholders = []
    for i, table in enumerate(tables):
        placeholder = f"__TABLE_PLACEHOLDER_{i}__"
        placeholders.append(placeholder)
        content = content.replace(table, placeholder, 1)

    # Convert each table to markdown
    markdown_tables = []
    for table in tables:
        try:
            md_table = htmltabletomd.convert_table(table)
            markdown_tables.append(md_table)
        except Exception as e:
            print(f"Error converting table: {e}", file=sys.stderr)
            markdown_tables.append("*Error converting table*")

    # Replace placeholders with markdown tables
    for i, placeholder in enumerate(placeholders):
        content = content.replace(placeholder, markdown_tables[i])

    return content

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("Usage: python gen_jupyter_cleanup.py < input.html", file=sys.stderr)
        print("This script now reads from stdin instead of a file argument", file=sys.stderr)
        sys.exit(1)

    result = process_file(None)  # No file path needed
    print(result)
