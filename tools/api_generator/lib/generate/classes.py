import io
import os
from typing import Dict, List, Tuple, Optional

from lib.generate.docstring import docstring_summary
from lib.generate.hugo import FrontMatterExtra, write_front_matter
from lib.generate.methods import (
    generate_method,
    generate_method_decl,
    generate_method_list,
    generate_params,
)
from lib.generate.properties import generate_props
from lib.ptypes import ClassDetails, ClassMap, ClassPackageMap, PackageInfo
from lib.generate.helper import generate_anchor_from_name

PackageTree = Dict[str, List[str]]

ProtocolBaseClass = "Protocol"


def generate_class_filename(fullname: str, pkg_root: str) -> str:
    nameParts = fullname.split(".")
    return os.path.join(pkg_root, ".".join(nameParts[0:-1]), f"{nameParts[-1].lower()}.md")


def sift_class_and_errors(classes: ClassMap) -> Tuple[List[str], List[str]]:
    classList = []
    exceptions = []
    for cls, clsInfo in classes.items():
        if clsInfo["is_exception"]:
            exceptions.append(cls)
        else:
            classList.append(cls)
    return classList, exceptions


def generate_class_link(
    fullname: str, pkg_root: str, relative_to_file: str, flatten: bool
) -> str:
    nameParts = fullname.split(".")
    pkg_base = os.path.relpath(pkg_root, os.path.dirname(relative_to_file))
    if flatten:
        anchor = generate_anchor_from_name(fullname)
        result = f"{os.path.join('..', pkg_base, '.'.join(nameParts[0:-1])).lower()}#{anchor}"
        return result
    else:
        result = os.path.join(
            pkg_base, ".".join(nameParts[0:-1]), nameParts[-1].lower()
        )
        return result


def generate_class_index(
    output_folder: str,
    classes: ClassPackageMap,
    pkg_root: str,
    flatten: bool,
    ignore_types: List[str],
    frontmatter_extra: Optional[FrontMatterExtra],
):
    # Check if any package has classes defined
    has_classes = any(
        any(cls not in ignore_types for cls in pkg_classes)
        for pkg_classes in classes.values()
    )
    if not has_classes:
        return

    if flatten:
        pkg_index = os.path.join(output_folder, "classes.md")
        frontmatter_extra = None
    else:
        cls_root = os.path.join(output_folder, "classes")
        if not os.path.isdir(cls_root):
            os.mkdir(cls_root)
        pkg_index = os.path.join(cls_root, "_index.md")

    with open(pkg_index, "w") as index:
        classList = {}
        protocolList = {}

        for _, pkgInfo in classes.items():
            for cls, clsInfo in pkgInfo.items():
                if cls in ignore_types:
                    continue
                if clsInfo["parent"] == ProtocolBaseClass:
                    protocolList[cls] = clsInfo
                else:
                    classList[cls] = clsInfo

        if len(protocolList) > 0 and len(classList) > 0:
            write_front_matter("Classes & Protocols", index, frontmatter_extra)
        elif len(classList) > 0:
            write_front_matter("Classes", index, frontmatter_extra)
        else:
            write_front_matter("Protocols", index, frontmatter_extra)

        if len(classList) > 0:
            index.write("# Classes\n\n")

            index.write("| Class | Description |\n")
            index.write("|-|-|\n")

            for cls, clsInfo in classList.items():
                if cls in ignore_types:
                    continue
                class_link = generate_class_link(
                    fullname=cls,
                    relative_to_file=pkg_index,
                    pkg_root=pkg_root,
                    flatten=flatten,
                )
                index.write(
                    f"| [`{cls}`]({class_link}) |{docstring_summary(clsInfo['doc'])} |\n"
                )

        if len(protocolList) > 0:
            index.write("# Protocols\n\n")

            index.write("| Protocol | Description |\n")
            index.write("|-|-|\n")

            for cls, clsInfo in protocolList.items():
                if cls in ignore_types:
                    continue
                class_link = generate_class_link(
                    fullname=cls,
                    relative_to_file=pkg_index,
                    pkg_root=pkg_root,
                    flatten=flatten,
                )
                index.write(
                    f"| [`{cls}`]({class_link}) |{docstring_summary(clsInfo['doc'])} |\n"
                )


def generate_class(fullname: str, info: ClassDetails, pkg_root: str):
    class_file = generate_class_filename(fullname=fullname, pkg_root=pkg_root)
    with open(class_file, "w") as output:
        write_front_matter(info["name"], output)

        output.write(f"# {info['name']}\n\n")
        output.write(f"**Package:** `{'.'.join(info['path'].split('.')[:-1])}`\n\n")

        generate_class_details(info, output, doc_level=2)


def generate_class_details(
    info: ClassDetails, output: io.TextIOWrapper, doc_level: int
):
    if info["doc"]:
        # Escape HTML characters in class documentation
        doc = info["doc"].replace("<", "&lt;").replace(">", "&gt;")
        output.write(f"{doc}\n\n")

    # Find the __init__ method if it exists
    init_method = next(
        (m for m in info["methods"] if m["name"] == "__init__"),
        None,
    )

    if init_method:
        generate_method_decl(
            info["name"],
            init_method,
            output,
            is_class=True,
            is_protocol=info["parent"] == ProtocolBaseClass,
        )
        if init_method["doc"]:
            # Escape HTML characters in __init__ method documentation
            doc = init_method["doc"].replace("<", "&lt;").replace(">", "&gt;")
            output.write(f"{doc}\n\n")
        if info["parent"] != ProtocolBaseClass:
            generate_params(init_method, output)

    methods = [method for method in info["methods"] if method["name"] != "__init__"]

    if methods:
        generate_method_list(methods, output, doc_level)

        for method in methods:
            generate_method(method, output, doc_level)

    if info["properties"]:
        output.write(f"{'#' * (doc_level)} Properties\n\n")
        generate_props(info["properties"], output)


def generate_classes(classes: ClassPackageMap, pkg_root: str, ignore_types: List[str]):
    for _, pkgInfo in classes.items():
        for cls, clsInfo in pkgInfo.items():
            if cls in ignore_types:
                continue
            generate_class(fullname=cls, info=clsInfo, pkg_root=pkg_root)


def generate_classes_and_error_list(
    pkg: PackageInfo,
    clss: Dict[str, ClassDetails],
    output: io.TextIOWrapper,
    pkg_root: str,
    doc_level: int,
    relative_to_file: str,
    flatten: bool,
    ignore_types: List[str],
):
    classes, exceptions = sift_class_and_errors(clss)

    # Filter out ignored types from classes
    filtered_classes = [cls for cls in classes if cls not in ignore_types]

    class_list = [
        cls for cls in filtered_classes if clss[cls]["parent"] != ProtocolBaseClass
    ]
    protocol_list = [
        cls for cls in filtered_classes if clss[cls]["parent"] == ProtocolBaseClass
    ]

    if len(class_list) > 0:
        output.write(f"{'#' * (doc_level)} Classes\n\n")

        output.write("| Class | Description |\n")
        output.write("|-|-|\n")

        for classNameFull in class_list:
            clsInfo = clss[classNameFull]
            classLink = generate_class_link(
                fullname=classNameFull,
                relative_to_file=relative_to_file,
                pkg_root=pkg_root,
                flatten=flatten,
            )

            classNameWithoutPackage = classNameFull.replace(f"{pkg['name']}.", "")
            output.write(
                f"| [`{classNameWithoutPackage}`]({classLink}) | {docstring_summary(clsInfo['doc'])} |\n"
            )

        output.write("\n")

    if len(protocol_list) > 0:
        output.write(f"{'#' * (doc_level)} Protocols\n\n")

        output.write("| Protocol | Description |\n")
        output.write("|-|-|\n")

        for classNameFull in protocol_list:
            clsInfo = clss[classNameFull]
            classLink = generate_class_link(
                fullname=classNameFull,
                relative_to_file=relative_to_file,
                pkg_root=pkg_root,
                flatten=flatten,
            )

            classNameWithoutPackage = classNameFull.replace(f"{pkg['name']}.", "")
            output.write(
                f"| [`{classNameWithoutPackage}`]({classLink}) | {docstring_summary(clsInfo['doc'])} |\n"
            )

        output.write("\n")

    if len(exceptions) > 0:
        output.write(f"{'#' * (doc_level)} Errors\n\n")

        output.write("| Exception | Description |\n")
        output.write("|-|-|\n")

        for exc in exceptions:
            clsInfo = clss[exc]
            classLink = generate_class_link(
                fullname=clsInfo["path"],
                relative_to_file=relative_to_file,
                pkg_root=pkg_root,
                flatten=flatten,
            )
            output.write(
                f"| [`{clsInfo['name']}`]({classLink}) | {docstring_summary(clsInfo['doc'])} |\n"
            )

        output.write("\n")
