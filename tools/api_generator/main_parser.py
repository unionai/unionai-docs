import argparse
from typing import Dict, List
import yaml
from parser.packages import get_subpackages
from parser.classes import get_classes
from ptypes import ParsedInfo
from importlib import metadata


def main():
    parser = argparse.ArgumentParser(
        description="Generate API documentation from Python package"
    )
    parser.add_argument("--package", help="Package to parse")
    args = parser.parse_args()

    pkgs = get_subpackages(args.package)

    root_package = args.package.split(".")[0]
    version = metadata.version(root_package)

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
