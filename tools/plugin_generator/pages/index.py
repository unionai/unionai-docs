from os import path, mkdir
from typing import Dict, List

from metadata import Metadata

def generate(output: str, generated_plugins: Dict[str, Metadata], variants: List[str]):
    if not path.exists(output):
        mkdir(output)
    with open(path.join(output, "_index.md"), "w") as f:
        f.write("---\n")
        f.write("title: FlyteKit Plugins\n")
        f.write(f"variants: {' '.join(variants)}\n")
        f.write("weight: 99\n")
        f.write("---\n\n")

        f.write("# FlyteKit Plugins\n\n")
        f.write("This is a list of all plugins that are available in FlyteKit.\n\n")
        f.write("| Plugin | Description |\n")
        f.write("| ------ | ----------- |\n")
        for plugin_name, plugin_md in generated_plugins.items():
            name = plugin_md['title'] if "title" in plugin_md else plugin_name
            desc = plugin_md['description'] if "description" in plugin_md else ""
            f.write(f"| [{name}]({plugin_name}/) | {desc} |\n")
