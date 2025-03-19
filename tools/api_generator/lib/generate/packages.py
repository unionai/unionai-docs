import io
import os
from typing import Dict, List

from lib.generate.classes import generate_class_details, generate_classes_and_error_list
from lib.generate.docstring import docstring_summary
from lib.generate.hugo import write_front_matter
from lib.ptypes import ClassPackageMap, PackageInfo

type PackageTree = Dict[str, List[str]]


def convert_package_list_to_tree(pkgs: List[PackageInfo]) -> PackageTree:
    result = {}

    for pkg in pkgs:
        parts = pkg["name"].split(".")
        glued = ""
        for p in parts:
            parent = glued
            glued = f"{glued}.{p}" if glued != "" else p
            if not glued in result:
                result[glued] = []
            if parent != "" and not glued in result[parent]:
                result[parent].append(glued)

    return result


def generate_package_index(
    pkg_root: str, packages: List[PackageInfo], classes: ClassPackageMap
):
    pkg_index = os.path.join(pkg_root, "_index.md")
    with open(pkg_index, "w") as index:
        write_front_matter("Packages", index)

        index.write("# Packages\n\n")

        index.write(f"| Package | Description |\n")
        index.write("|-|-|\n")

        for pkg in packages:
            clss = classes[pkg["name"]]
            if len(clss) == 0:
                continue
            index.write(f"| [`{pkg['name']}`]({pkg['name']}) | {docstring_summary(pkg["doc"] if "doc" in pkg else None)} |\n")


def generate_package_folders(
    packages: List[PackageInfo], classes: ClassPackageMap, pkg_root: str, flatten: bool, ignore_types: List[str]
):
    print("Generating package folders")

    for pkg in packages:
        if len(classes[pkg["name"]]) == 0:
            continue

        if flatten:
            pkg_index = os.path.join(pkg_root, f"{pkg['name']}.md")
        else:
            pkg_folder = os.path.join(pkg_root, pkg["name"])
            if not os.path.isdir(pkg_folder):
                os.mkdir(pkg_folder)
            pkg_index = os.path.join(pkg_folder, "_index.md")

        # print(f"Generating package index for {pkg['name']}")
        with open(pkg_index, "w") as index:
            write_front_matter(pkg["name"], index)

            index.write(f"# {pkg["name"]}\n\n")

            doc = pkg["doc"] if "doc" in pkg else ""
            if doc:
                index.write(f"{doc}\n")

            classDefs = classes[pkg["name"]]

            index.write("## Directory\n\n")

            generate_classes_and_error_list(
                pkg=pkg,
                clss=classDefs,
                output=index,
                pkg_root=pkg_root,
                doc_level=3,
                relative_to_file=pkg_index,
                flatten=flatten,
            )

            if flatten:
                for cls, clsInfo in classes[pkg["name"]].items():
                    if cls in ignore_types:
                        continue

                    index.write(f"## {cls}\n\n")

                    generate_class_details(
                        info=clsInfo,
                        output=index,
                        doc_level=3,
                    )