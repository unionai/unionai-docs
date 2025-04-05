from os import path, mkdir, remove
from typing import List
from metadata import Metadata, to_yaml

def generate(name: str, title_expanded: str, metadata: Metadata, plugin_source: str, output: str, variants: List[str]) -> None:
    if not path.exists(output):
        mkdir(output)
    md_yaml = to_yaml(metadata).strip().split("\n")
    found_header = False
    index_file = path.join(output, "_index.md")
    with open(index_file, "w") as f:
        f.write(f"---\n")
        f.write(f"title: {name}\n")
        f.write(f"layout: plugin\n")
        f.write(f"variants: {' '.join(variants)}\n")
        f.write(f"metadata:\n")
        for line in md_yaml:
            f.write(f"{' ' * 2}{line}\n")
        f.write(f"---\n\n")

        with open(path.join(plugin_source, "README.md"), "r") as r:
            for line in r:
                # Skip the title line if it matches "# <name>"
                if line.strip() == f"# {name}" or line.strip() == f"# {title_expanded}":
                    found_header = True
                    continue
                f.write(line)

    if not found_header:
        remove(index_file)
        raise ValueError(f"Could not find header '# {name}' in README.md")