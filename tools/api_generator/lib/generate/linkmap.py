from typing import List

import json
import os
import yaml

from lib.ptypes import ClassPackageMap, PackageInfo


def generate_linkmap_metadata(
    packages: List[PackageInfo],
    classes: ClassPackageMap,
    pkg_root: str,
    api_name: str,
    include_short_names: bool = False,
):
    # Skip the content root (remove first path component: content/a/b/c -> a/b/c)
    site_root = "/".join(pkg_root.split("/")[1:])

    # Build packages metadata from the packages list
    packages_dict = {pkg["name"]: f"/{site_root}/{pkg['name']}/" for pkg in packages}

    # Build methods metadata
    methods_dict = {}
    for pkg in packages:
        for m in pkg["methods"]:
            url = f"/{site_root}/{pkg['name']}/#{m['name']}"
            # Add fully qualified name
            methods_dict[f"{pkg['name']}.{m['name']}"] = url
            # Add short name for easier matching in docs (plugins only)
            if include_short_names:
                methods_dict[m['name']] = url

    # Build identifiers metadata from classes
    identifiers_dict = {}
    for pkg in classes:
        for clz in classes[pkg]:
            url = f"/{site_root}/{pkg}/{clz.split('.')[-1].lower()}/"
            # Add fully qualified name
            identifiers_dict[clz] = url
            # Add short name for easier matching in docs (plugins only)
            if include_short_names:
                short_name = clz.split('.')[-1]
                identifiers_dict[short_name] = url



    metadata = {
        "packages": packages_dict,
        "identifiers": identifiers_dict,
        "methods": methods_dict
    }

    # Write YAML file
    os.makedirs("data", exist_ok=True)
    with open(f"data/{api_name}.yaml", "w") as file:
        yaml.dump(metadata, file, default_flow_style=False, sort_keys=False)

    # Write JSON file for client-side use (identifiers and methods only)
    os.makedirs("static", exist_ok=True)
    client_linkmap = {
        "identifiers": identifiers_dict,
        "methods": methods_dict
    }
    with open(f"static/{api_name}-linkmap.json", "w") as file:
        json.dump(client_linkmap, file, indent=2)
