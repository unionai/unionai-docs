from importlib import metadata
from sys import stderr

from lib.parser.classes import get_classes
from lib.parser.packages import (
    get_functions,
    get_subpackages,
    get_variables,
    get_skipped_modules,
    clear_skipped_modules,
)
from lib.ptypes import ParsedInfo


def parse(package: str) -> ParsedInfo:
    # Clear any previously skipped modules
    clear_skipped_modules()

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

    # Print summary of skipped modules
    skipped = get_skipped_modules()
    if skipped:
        print(f"\n\033[93m{'='*60}\033[0m", file=stderr)
        print(f"\033[93mWARNING: {len(skipped)} module(s) were skipped due to import errors:\033[0m", file=stderr)
        for mod in skipped:
            print(f"  - {mod.name}: {mod.error}", file=stderr)
        print(f"\033[93m{'='*60}\033[0m", file=stderr)
        print(f"\nThese modules may require additional dependencies to be installed.", file=stderr)
    else:
        print(f"\n\033[92mAll modules imported successfully.\033[0m", file=stderr)

    return result
