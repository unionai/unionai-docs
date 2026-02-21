import importlib
import inspect
import sys
from types import ModuleType
from typing import Any, Dict, Optional
from enum import Enum

import yaml

from lib.parser.docstring import parse_docstring
from lib.parser.packages import get_package, should_include
from lib.ptypes import ClassDetails, PackageInfo
from lib.parser.methods import parse_method, parse_property, parse_variable


def isclass(member: Any) -> bool:
    try:
        memberClass = getattr(member, "__class__", None)
        return inspect.isclass(member) and (memberClass is None or memberClass != Enum)
    except (ImportError, Exception):
        return False

def get_classes(source: PackageInfo, package: ModuleType) -> Dict[str, ClassDetails]:
    # Skip if any private packages
    if any(p.startswith("_") for p in source["name"].split(".")):
        return {}

    classes = {}

    package_name = source["name"]

    members = inspect.getmembers(package)

    # Get all members of the package
    for name, obj in members:
        if not should_include(name, obj, package, isclass):
            continue

        path = f"{package_name}.{name}"

        # Get class information
        class_info = get_class_details(path)
        if not class_info:
            continue

        # Add to the list
        classes[path] = class_info

    return classes


def get_class_details(class_path: str) -> Optional[ClassDetails]:
    try:
        # Split the path into module and class name
        module_path, class_name = class_path.rsplit(".", 1)

        # Import the module
        module = importlib.import_module(module_path)

        # Get the class
        cls = getattr(module, class_name)

        if not inspect.isclass(cls):
            return None

        # Basic class info
        doc_info = parse_docstring(cls.__doc__, source=cls)
        class_info = ClassDetails(
            name=class_name,
            path=class_path,
            doc=doc_info["docstring"] if doc_info else None,
            module=cls.__module__,
            parent=cls.__base__.__name__ if cls.__base__ else None,
            bases=[
                base.__name__ for base in cls.__bases__ if base.__name__ != "object"
            ],
            is_exception=issubclass(cls, Exception),
            methods=[],
            properties=[],
            class_variables=[],
        )

        # Get methods, properties, and class variables
        for name, member in inspect.getmembers(cls):
            # Skip private members (except __init__)
            if name.startswith("_") and name != "__init__":
                continue

            # Methods
            method_info = parse_method(name, member, class_name)
            if method_info:
                # For __init__ methods, use class-level parameter documentation if available
                if name == "__init__" and doc_info and "params" in doc_info and doc_info["params"]:
                    method_info["params_doc"] = doc_info["params"]
                class_info["methods"].append(method_info)

            # Properties
            property_info = parse_property(name, member)
            if property_info:
                class_info["properties"].append(property_info)

            # Class variables (excluding methods and properties)
            var_info = parse_variable(name, member)
            if var_info:
                class_info["class_variables"].append(var_info)

        # Sort members by name
        class_info["methods"].sort(key=lambda x: x["name"])
        class_info["properties"].sort(key=lambda x: x["name"])
        class_info["class_variables"].sort(key=lambda x: x["name"])

        return class_info

    except (ImportError, AttributeError) as e:
        print(f"Error getting class details for {class_path}: {e}")
        return None


def main():
    # Example usage
    if len(sys.argv) > 1:
        package_name = sys.argv[1]
    else:
        package_name = "calendar"

    print(f"Finding classes in {package_name}...")
    pkg_mod = get_package(package_name)
    if pkg_mod is None:
        print(f"Package {package_name} not found", file=sys.stderr)
        exit(1)
    info, pkg = pkg_mod
    classes = get_classes(info, pkg)

    yaml_output = yaml.dump(
        {
            "classes": classes,
        },
        sort_keys=True,
        default_flow_style=False,
    )

    print(yaml_output)


if __name__ == "__main__":
    main()
