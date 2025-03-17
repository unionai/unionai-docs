import io
import os
from typing import Dict, List

from generate.classes import generate_class_link, sift_class_and_errors
from generate.hugo import write_front_matter
from ptypes import ClassDetails, ClassPackageMap

type PackageTree = Dict[str, List[str]]


def convert_package_list_to_tree(pkgs: List[str]) -> PackageTree:
    result = {}

    for pkg in pkgs:
        parts = pkg.split(".")
        glued = ""
        for p in parts:
            parent = glued
            glued = f"{glued}.{p}" if glued != "" else p
            if not glued in result:
                result[glued] = []
            if parent != "" and not glued in result[parent]:
                result[parent].append(glued)

    return result


def generate_package_summary(
    pkg: str,
    clss: Dict[str, ClassDetails],
    pkgTree: PackageTree,
    doc_level: int,
    output: io.StringIO,
    pkg_root: str,
):
    if len(clss) == 0:
        return

    # We will wrap in dropdown, so we can promote the levels 1-up
    doc_level = doc_level - 1

    output.write('{{< dropdown title="%s" >}}\n' % pkg)
    output.write("{{< markdown >}}")

    output.write(f"{'#' * (doc_level+1)} Classes\n\n")

    classes, exceptions = sift_class_and_errors(clss)

    for classNameFull in classes:
        clsInfo = clss[classNameFull]
        classLink = generate_class_link(
            fullname=classNameFull,
            relative_to_file=os.path.join(pkg_root, "..", "home"),
            pkg_root=pkg_root,
        )

        output.write(f"* [`{classNameFull.replace(f"{pkg}.", "")}`]({classLink})\n")

        # for method in clsInfo["methods"]:
        #     output.write(f"{" " * 2} * `{generate_signature_simple(method)}`\n")

        output.write("\n")

    output.write("\n")

    if len(exceptions) > 0:
        output.write(f"{'#' * (doc_level+1)} Errors\n\n")

        for exc in exceptions:
            clsInfo = clss[exc]
            classLink = generate_class_link(
                fullname=clsInfo["path"],
                relative_to_file=os.path.join(pkg_root, "..", "home"),
                pkg_root=pkg_root,
            )
            output.write(f"* [`{clsInfo["name"]}`]({classLink})\n")

        output.write("\n")

    output.write("{{< /markdown >}}")
    output.write("{{< /dropdown >}}")


def generate_package_index(pkg_root: str, packages: List[str]):
    pkg_index = os.path.join(pkg_root, "_index.md")
    with open(pkg_index, "w") as index:
        write_front_matter("Packages", index)

        index.write("# Packages\n\n")

        for pkg in packages:
            index.write(f"* [`{pkg}`]({pkg})\n")


def generate_package_folders(
    packages: List[str], classes: ClassPackageMap, pkg_root: str
):
    print("Generating package folders")

    for pkg in packages:
        if len(classes[pkg]) == 0:
            continue

        pkg_folder = os.path.join(pkg_root, pkg)
        if not os.path.isdir(pkg_folder):
            os.mkdir(pkg_folder)

        pkg_index = os.path.join(pkg_folder, "_index.md")
        with open(pkg_index, "w") as index:
            write_front_matter(pkg, index)

            index.write(f"# {pkg}\n\n")

            index.write("## Classes\n")

            classList, exceptions = sift_class_and_errors(classes[pkg])
            for classNameFull in classList:
                class_link = generate_class_link(
                    fullname=classNameFull,
                    relative_to_file=pkg_index,
                    pkg_root=pkg_root,
                )
                index.write(f"* [`{classNameFull}`]({class_link})\n")

            if len(exceptions) > 0:
                index.write("## Errors\n")

                for exc in exceptions:
                    index.write(f"* {exc}\n")
