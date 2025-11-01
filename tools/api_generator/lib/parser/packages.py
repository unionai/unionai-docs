import inspect
import pkgutil
import importlib
from sys import stderr
from types import ModuleType
from typing import Any, List, Optional, Tuple

from lib.ptypes import MethodInfo, PackageInfo, VariableInfo
from lib.parser.methods import parse_method, parse_variable
from lib.parser.synchronicity import is_synchronicity_method, parse_synchronicity_method
from lib.parser.syncify import is_syncify_method, parse_syncify_method


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
        methods=[],
        variables=[],
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


def get_functions(info: PackageInfo, pkg: ModuleType) -> List[MethodInfo]:
    result = []
    for name, member in inspect.getmembers(pkg):
        method_info = None
        if is_synchronicity_method(name, member):
            method_info = parse_synchronicity_method(name, member)
        if is_syncify_method(name, member):
            method_info = parse_syncify_method(name, member)
        if should_include(name, member, pkg, inspect.isfunction):
            method_info = parse_method(name, member)
        # TODO Handle the case in which the member is a class, then methods of the class
        # should be shown, if it has a __call__ method, then show that as the regular method
        # Example is flyte.map
        if method_info:
            result.append(method_info)
    return result


def is_variable(member: Any) -> bool:
    return not (not (not callable(member) and not isinstance(member, type)))


def get_variables(info, pkg) -> List[VariableInfo]:
    result = []
    for name, member in inspect.getmembers(pkg):
        if not should_include(name, member, pkg, is_variable):
            continue

        variable_info = parse_variable(name, member)
        if variable_info:
            result.append(variable_info)
    return result


def should_include(name: str, obj: Any, package: ModuleType, filter=None) -> bool:
    if filter is not None and not filter(obj):
        # print(f"[should_include] Skipping {name} as it doesn't match filter", file=stderr)
        return False

    all_allow_list = getattr(package, "__all__", None)

    # If __all__ is defined, skip members not in the allow list
    if all_allow_list is not None:
        if name not in all_allow_list:
            # print(f"[should_include] Skipping {name} as it's not in __all__", file=stderr)
            return False
        else:
            # print(f"[should_include] Keeping {name} as it's in __all__", file=stderr)
            return True

    # Skip private members, modules, and non-classes
    if name.startswith("_"):
        # print(f"[should_include] Skipping {name} as it's private", file=stderr)
        return False

    # Check if the class is imported or defined in the module
    try:
        imported = obj.__module__ != package.__name__
        if imported:
            if all_allow_list is None or name not in all_allow_list:
                # print(f"[should_include] Resource {name} is {obj.__module__} imported @ [{all_allow_list}]", file=stderr)
                return False
    except AttributeError:
        pass

    # print(f"[should_include] Keeping {name}", file=stderr)
    return True


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
