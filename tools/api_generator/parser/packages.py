import pkgutil
import importlib
from typing import List


def get_subpackages(package_name: str) -> List[str]:
    """
    Recursively enumerate all subpackages of a given Python package.

    Args:
        package_name: Name of the package to scan for subpackages

    Returns:
        List of fully qualified package names including all subpackages
    """
    subpackages = []

    try:
        # Import the package
        package = importlib.import_module(package_name)

        # Add the base package
        subpackages.append(package_name)

        # Walk through all modules in the package
        for loader, name, is_pkg in pkgutil.walk_packages(
            package.__path__, package_name + "."
        ):
            if is_pkg:
                # Add only if it's a package (not a module)
                subpackages.append(name)

        return sorted(subpackages)

    except ImportError:
        print(f"Could not import package {package_name}")
        return []


def main():
    # Test the get_subpackages function with a sample package
    test_package = "flytekit"
    print(f"Finding subpackages for {test_package}...")
    subpackages = get_subpackages(test_package)
    print(f"Found {len(subpackages)} subpackages:")
    for pkg in subpackages:
        print(f"  - {pkg}")


if __name__ == "__main__":
    main()
