import inspect
import pkgutil
import importlib
from sys import stderr
from types import ModuleType
from typing import Dict, List, Optional, Tuple

from lib.ptypes import MethodInfo, PackageInfo, VariableInfo
from lib.parser.methods import parse_method, parse_variable


def get_package(name: str) -> Optional[Tuple[PackageInfo, ModuleType]]:
    try:
        # Import the package
        print(f"Importing package: {name}", file=stderr)
        package = importlib.import_module(name)
    except Exception as e:
        print(
            f"\033[93m[WARNING]:\033[0m Could not import package '{name}': {e}",
            file=stderr,
        )
        return None

    # Add the base package
    pkg = PackageInfo(
        name=package.__name__,
        doc=package.__doc__,
    )

    return pkg, package


def get_subpackages(package_name: str) -> List[Tuple[PackageInfo, ModuleType]]:
    """
    Recursively enumerate all subpackages of a given Python package.

    Args:
        package_name: Name of the package to scan for subpackages

    Returns:
        List of fully qualified package names including all subpackages
    """
    subpackages = []

    try:
        # Add the base package
        pkg_mod = get_package(package_name)
        if pkg_mod is None:
            return []
        pkgInfo, pkg = pkg_mod
        subpackages.append((pkgInfo, pkg))

        # Walk through all modules in the package
        for loader, name, is_pkg in pkgutil.walk_packages(
            pkg.__path__, pkgInfo["name"] + "."
        ):
            if any(p.startswith("_") for p in name.split(".")):
                continue

            if not name.startswith("_"):
                # Add only if it's a package (not a module)
                pkg_mod = get_package(name)
                if pkg_mod is None:
                    continue
                pkgInfo, pkg = pkg_mod
                subpackages.append((pkgInfo, pkg))

        return subpackages

    except ImportError as e:
        print(f"FATAL: Could not import package '{package_name}': {e}", file=stderr)
        exit(1)


def get_functions(info, pkg) -> List[MethodInfo]:
    result = []
    for name, member in inspect.getmembers(pkg):
        method_info = parse_method(name, member)
        if method_info:
            result.append(method_info)
    return result


def get_variables(info, pkg) -> List[VariableInfo]:
    result = []
    for name, member in inspect.getmembers(pkg):
        variable_info = parse_variable(name, member)
        if variable_info:
            result.append(variable_info)
    return result


def main():
    # Test the get_subpackages function with a sample package
    test_package = "flytekit"
    print(f"Finding subpackages for {test_package}...")
    subpackages = get_subpackages(test_package)
    print(f"Found {len(subpackages)} subpackages:")
    for pp in subpackages:
        pkg, _ = pp
        print(f"  - {pkg['name']}")


if __name__ == "__main__":
    main()
