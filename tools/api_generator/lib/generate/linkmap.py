from typing import List

import yaml

from lib.ptypes import ClassPackageMap, PackageInfo


def generate_linkmap_metadata(
    packages: List[PackageInfo],
    classes: ClassPackageMap,
    pkg_root: str,
    api_name: str,
):
    # Skip the content root (remove first path component: content/a/b/c -> a/b/c)
    site_root = "/".join(pkg_root.split("/")[1:])

    # Build packages metadata from the packages list
    packages_dict = {pkg["name"]: f"/{site_root}/{pkg['name']}/" for pkg in packages}

    # Build identifiers metadata from classes
    methods_dict = {}
    for pkg in packages:
        for m in pkg["methods"]:
            methods_dict[f"{pkg['name']}.{m['name']}"] = f"/{site_root}/{pkg['name']}/#{m['name']}"


    identifiers_dict = {}
    for pkg in classes:
        for clz in classes[pkg]:
            # Assuming clz has name and url attributes
            identifiers_dict[clz] = f"/{site_root}/{pkg}/{clz.split(".")[-1:][0].lower()}/"



    metadata = {
        "packages": packages_dict,
        "identifiers": identifiers_dict,
        "methods": methods_dict
    }

    with open(f"data/{api_name}.yaml", "w") as file:
        yaml.dump(metadata, file, default_flow_style=False, sort_keys=False)
