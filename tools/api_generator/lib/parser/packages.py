import pkgutil
import importlib
from sys import stderr
from types import ModuleType
from typing import Dict, List, Optional, Tuple

from lib.ptypes import PackageInfo


def get_package(name: str) -> Optional[Tuple[PackageInfo, ModuleType]]:
    try:
        # Import the package
        package = importlib.import_module(name)
    except:
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
