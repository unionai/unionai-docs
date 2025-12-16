import io
import re
from typing import List

from lib.ptypes import PropertyInfo


def escape_html_preserve_code_blocks(text):
    """Escape HTML characters in text while preserving code blocks."""
    if not text:
        return text
    
    # Split on code block delimiters (```)
    parts = re.split(r'(```.*?```)', text, flags=re.DOTALL)
    
    result = []
    for i, part in enumerate(parts):
        # Even indices are regular text, odd indices are code blocks
        if i % 2 == 0:  # Regular text - escape HTML
            escaped_part = part.replace("<", "&lt;").replace(">", "&gt;")
            result.append(escaped_part)
        else:  # Code block - don't escape
            result.append(part)
    
    return ''.join(result)


def generate_props(props: List[PropertyInfo], output: io.TextIOWrapper):
    if not props:
        return

    output.write("| Property | Type | Description |\n")
    output.write("|-|-|-|\n")

    for prop in props:
        propType = f"`{prop['type']}`" if "type" in prop else ""
        docs = prop["doc"] if "doc" in prop else ""
        # Clean up the doc string - replace newlines with spaces and escape markdown table characters and HTML
        if docs:
            docs_cell = escape_html_preserve_code_blocks(docs)
            docs_cell = docs_cell.replace("\n", " ").replace("|", "\\|").strip()
        else:
            docs_cell = ""
        output.write(f"| `{prop['name']}` | {propType} | {docs_cell} |\n")

    output.write("\n")
