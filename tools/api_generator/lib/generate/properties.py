import io
from typing import List

from lib.ptypes import PropertyInfo


def generate_props(props: List[PropertyInfo], output: io.TextIOWrapper):
    if not props:
        return

    output.write("| Property | Type | Description |\n")
    output.write("|-|-|-|\n")

    for prop in props:
        propType = f"`{prop['type']}`" if "type" in prop else ""
        docs = prop["doc"] if "doc" in prop else ""
        # Clean up the doc string - replace newlines with spaces and escape markdown table characters and HTML
        docs_cell = docs.replace("\n", " ").replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;").strip() if docs else ""
        output.write(f"| `{prop['name']}` | {propType} | {docs_cell} |\n")

    output.write("\n")
