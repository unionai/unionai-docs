import io
import os
from typing import Dict, List, Tuple

from generate.hugo import write_front_matter
from generate.methods import generate_decl, generate_params
from ptypes import ClassDetails, ClassMap, ClassPackageMap

type PackageTree = Dict[str, List[str]]


def generate_class_link(fullname: str, pkg_root: str, relative_to_file: str) -> str:
    nameParts = fullname.split(".")
    pkg_base = os.path.relpath(pkg_root, os.path.dirname(relative_to_file))
    result = os.path.join(pkg_base, ".".join(nameParts[0:-1]), nameParts[-1]).lower()
    return result


def generate_class_filename(fullname: str, pkg_root: str) -> str:
    nameParts = fullname.split(".")
    return os.path.join(pkg_root, ".".join(nameParts[0:-1]), f"{nameParts[-1]}.md")


def sift_class_and_errors(classes: ClassMap) -> Tuple[List[str], List[str]]:
    classList = []
    exceptions = []
    for cls, clsInfo in classes.items():
        if clsInfo["is_exception"]:
            exceptions.append(cls)
        else:
            classList.append(cls)
    return classList, exceptions


def generate_class_index(cls_root: str, classes: ClassPackageMap, pkg_root: str):
    pkg_index = os.path.join(cls_root, "_index.md")
    with open(pkg_index, "w") as index:
        write_front_matter("Classes", index)

        index.write("# Classes\n\n")

        for _, pkgInfo in classes.items():
            for cls, _ in pkgInfo.items():
                class_link = generate_class_link(
                    fullname=cls, relative_to_file=pkg_index, pkg_root=pkg_root
                )
                index.write(f"* [`{cls}`]({class_link})\n")


def generate_class(fullname: str, info: ClassDetails, pkg_root: str):
    class_file = generate_class_filename(fullname=fullname, pkg_root=pkg_root)
    with open(class_file, "w") as output:
        write_front_matter(info["name"], output)

        output.write(f"# {info["name"]}\n\n")
        output.write(f"**Package:** `{'.'.join(info['path'].split('.')[:-1])}`\n\n")

        if info["docstring"]:
            output.write(f"{info['docstring']}\n\n")

        # Find the __init__ method if it exists
        init_method = next(
            (m for m in info["methods"] if m["name"] == "__init__"),
            None,
        )

        if init_method:
            generate_decl(info["name"], init_method, output)
            if init_method["docstring"]:
                output.write(f"{init_method['docstring']}\n\n")
            generate_params(init_method, output)

        if info["methods"]:
            output.write("## Methods\n\n")
            for method in info["methods"]:
                if method["name"] == "__init__":
                    continue

                output.write(f"### {method['name']}()\n\n")
                generate_decl(method["name"], method, output)
                if method["docstring"]:
                    output.write(f"{method['docstring']}\n\n")
                generate_params(method, output)


def generate_classes(classes: ClassPackageMap, pkg_root: str):
    for _, pkgInfo in classes.items():
        for cls, clsInfo in pkgInfo.items():
            generate_class(fullname=cls, info=clsInfo, pkg_root=pkg_root)
