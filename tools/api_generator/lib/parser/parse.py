from importlib import metadata
from sys import stderr

from lib.parser.classes import get_classes
from lib.parser.packages import get_functions, get_subpackages, get_variables
from lib.ptypes import ParsedInfo


def parse(package: str) -> ParsedInfo:
    try:
        version = metadata.version(package)
    except metadata.PackageNotFoundError:
        print(
            f"FATAL: Package {package} not found. Did you have it installed?",
            file=stderr,
        )
        exit(1)

    pkgAndMods = get_subpackages(package)

    clss = {}
    for pp in pkgAndMods:
        info, pkg = pp
        clss[info["name"]] = get_classes(info, pkg)
        info["methods"] = get_functions(info, pkg)
        info["variables"] = get_variables(info, pkg)
        print(f"Parsed {info['name']}", file=stderr)

    pkgs = [info for info, _ in pkgAndMods]

    result = ParsedInfo(version=version, packages=pkgs, classes=clss)

    return result
