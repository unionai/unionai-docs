import io
from typing import List

from lib.ptypes import PropertyInfo


def generate_props(props: List[PropertyInfo], output: io.TextIOWrapper):
    if not props:
        return

    multiline_start = "{{< multiline >}}"
    multiline_end = "{{< /multiline >}}"

    output.write("| Property | Type | Description |\n")
    output.write("|-|-|-|\n")

    for prop in props:
        propType = f"`{prop["type"]}`" if "type" in prop else ""
        docs = prop["doc"] if "doc" in prop else ""
        docs_cell = f"{multiline_start}{docs}{multiline_end}" if docs else ""
        output.write(f"| `{prop['name']}` | {propType} | {docs_cell} |\n")

    output.write("\n")
