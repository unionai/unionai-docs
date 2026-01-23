import sys
import re
import os
import htmltabletomd

def process_file(file_path):
    # Read from stdin instead of a file
    try:
        content = sys.stdin.read()
    except Exception as e:
        print(f"Error reading from stdin: {e}", file=sys.stderr)
        sys.exit(1)

    # Convert absolute union.ai docs URLs to relative shortcode links
    # Pattern: https://www.union.ai/docs/v2/{variant}/{path}
    # Result: {{< docs_home {variant} v2 >}}/{path}
    docs_url_pattern = re.compile(
        r'https://www\.union\.ai/docs/(v\d+)/(flyte|byoc|serverless|selfmanaged)/([^\s\)\"\'>\]]+)'
    )
    def replace_docs_url(match):
        version = match.group(1)
        variant = match.group(2)
        path = match.group(3)
        return f'{{{{< docs_home {variant} {version} >}}}}/{path}'

    content = docs_url_pattern.sub(replace_docs_url, content)

    # Insert download link after the first heading (## or #)
    notebook_link = os.environ.get('NOTEBOOK_LINK')
    if notebook_link:
        first_heading_pattern = re.compile(r'^(#{1,2} .+)$', re.MULTILINE)
        match = first_heading_pattern.search(content)
        if match:
            # Convert GitHub blob URL to Colab URL
            # From: https://github.com/org/repo/blob/branch/path
            # To: https://colab.research.google.com/github/org/repo/blob/branch/path
            colab_link = notebook_link.replace('https://github.com/', 'https://colab.research.google.com/github/')
            download_shortcode = f'\n\n> [!NOTE]\n> [View source on GitHub]({notebook_link}) | [Run in Google Colab]({colab_link})\n'
            content = content[:match.end()] + download_shortcode + content[match.end():]

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
