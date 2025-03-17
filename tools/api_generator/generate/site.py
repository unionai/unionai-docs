import io
import os
from typing import Dict, List

from generate.hugo import set_variants, set_version, write_front_matter
from ptypes import ParsedInfo
from generate.packages import (
    convert_package_list_to_tree,
    generate_package_folders,
    generate_package_index,
    generate_package_summary,
)
from generate.classes import generate_class_index, generate_classes

type PackageTree = Dict[str, List[str]]


def generate_home(
    title: str,
    source: ParsedInfo,
    include: List[str],
    doc_level: int,
    pkg_root: str,
    output_folder: str,
):
    output = io.StringIO()
    pkgTree = convert_package_list_to_tree(source["packages"])

    for pkg in source["packages"]:
        generate_package_summary(
            pkg=pkg,
            clss=source["classes"][pkg],
            pkgTree=pkgTree,
            doc_level=doc_level,
            output=output,
            pkg_root=pkg_root,
        )

    with open(os.path.join(output_folder, "_index.md"), "w") as index:
        write_front_matter(title, index)

        index.write(f"# {title}\n\n")

        for inc in include:
            with open(inc, "r") as f:
                index.write(f.read())
                index.write("\n\n")

        index.write(f"## Packages\n\n")

        index.write(output.getvalue())


def generate_site(
    title: str,
    source: ParsedInfo,
    include: List[str],
    doc_level: int,
    output_folder: str,
    variants: List[str],
):
    set_variants(variants)
    set_version(source["version"])

    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)

    pkg_root = os.path.join(output_folder, "packages")
    if not os.path.isdir(pkg_root):
        os.mkdir(pkg_root)

    # Generate site
    generate_home(
        title=title,
        source=source,
        include=include,
        doc_level=doc_level,
        output_folder=output_folder,
        pkg_root=pkg_root,
    )

    # Create package structure
    generate_package_index(packages=source["packages"], pkg_root=pkg_root)
    generate_package_folders(
        packages=source["packages"],
        classes=source["classes"],
        pkg_root=pkg_root,
    )

    # Create class index
    cls_root = os.path.join(output_folder, "classes")
    if not os.path.isdir(cls_root):
        os.mkdir(cls_root)
    generate_class_index(
        classes=source["classes"], cls_root=cls_root, pkg_root=pkg_root
    )
    generate_classes(classes=source["classes"], pkg_root=pkg_root)
