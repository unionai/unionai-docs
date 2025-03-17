import argparse
from importlib import metadata
from sys import stderr

import yaml

from parser.classes import get_classes
from parser.packages import get_subpackages
from ptypes import ParsedInfo


def main():
    parser = argparse.ArgumentParser(
        description="Generate API documentation from Python package"
    )
    parser.add_argument("--package", help="Package to parse", required=True)
    args = parser.parse_args()

    root_package = args.package.split(".")[0]

    try:
        version = metadata.version(root_package)
    except metadata.PackageNotFoundError:
        print(f"FATAL: Package {root_package} not found. Did you have it installed?", file=stderr)
        exit(1)

    pkgs = get_subpackages(args.package)

    clss = {}
    for pkg in pkgs:
        clss[pkg] = get_classes(pkg)

    result = ParsedInfo(version=version, packages=pkgs, classes=clss)

    yaml_output = yaml.dump(
        result,
        sort_keys=True,
        default_flow_style=False,
    )
    print(yaml_output)


if __name__ == "__main__":
    main()
