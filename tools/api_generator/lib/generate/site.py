import os
from typing import Dict, List

from lib.generate.classes import generate_class_index, generate_classes
from lib.generate.hugo import FrontMatterExtra, set_variants, set_version, write_front_matter
from lib.generate.packages import (
    generate_package_folders,
    generate_package_index,
)
from lib.generate.linkmap import generate_linkmap_metadata
from lib.ptypes import ParsedInfo

PackageTree = Dict[str, List[str]]


def generate_home(
    title: str,
    source: ParsedInfo,
    include: List[str],
    doc_level: int,
    pkg_root: str,
    output_folder: str,
    weight: int,
    expanded: bool,
):
    with open(os.path.join(output_folder, "_index.md"), "w") as output:
        write_front_matter(title, output, {
            "expand_sidebar": expanded,
            "weight": weight,
        })
        output.write(f"# {title}\n\n")

        for inc in include:
            with open(inc, "r") as f:
                output.write(f.read())
                output.write("\n\n")

def generate_site(
    title: str,
    source: ParsedInfo,
    include: List[str],
    doc_level: int,
    output_folder: str,
    variants: List[str],
    flatten: bool,
    ignore_types: List[str],
    weight: int,
    expanded: bool,
    api_name: str | None,
    include_short_names: bool = False,
):
    set_variants(variants)
    set_version(source["version"])

    os.makedirs(output_folder, exist_ok=True)

    pkg_root = os.path.join(output_folder, "packages")
    os.makedirs(pkg_root, exist_ok=True)

    # Generate site
    generate_home(
        title=title,
        source=source,
        include=include,
        doc_level=doc_level,
        output_folder=output_folder,
        pkg_root=pkg_root,
        weight=weight,
        expanded=expanded,
    )

    subpages_frontmatter_extra: FrontMatterExtra = {
        "expand_sidebar": expanded,
        "weight": None,
    }

    generate_package_index(
        packages=source["packages"],
        classes=source["classes"],
        pkg_root=pkg_root,
        frontmatter_extra=subpages_frontmatter_extra,
    )

    generate_class_index(
        classes=source["classes"],
        output_folder=output_folder,
        pkg_root=pkg_root,
        flatten=flatten,
        ignore_types=ignore_types,
        frontmatter_extra=subpages_frontmatter_extra,
    )

    generate_package_folders(
        packages=source["packages"],
        classes=source["classes"],
        pkg_root=pkg_root,
        flatten=flatten,
        ignore_types=ignore_types,
        frontmatter_extra=subpages_frontmatter_extra,
    )

    if flatten:
        pass
    else:
        generate_classes(classes=source["classes"], pkg_root=pkg_root, ignore_types=ignore_types)

    if api_name:
        generate_linkmap_metadata(
            packages=source["packages"],
            classes=source["classes"],
            pkg_root=pkg_root,
            api_name=api_name,
            include_short_names=include_short_names,
        )