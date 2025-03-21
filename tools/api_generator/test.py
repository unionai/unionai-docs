import pkgutil
from importlib import metadata
import importlib
from sys import stderr

root_package = "union"

try:
    version = metadata.version(root_package)
except metadata.PackageNotFoundError:
    print(f"FATAL: Package {root_package} not found. Did you have it installed?", file=stderr)
    exit(1)

package = importlib.import_module(root_package)
print(package.__path__)

for loader, name, is_pkg in pkgutil.walk_packages(
    package.__path__, root_package + "."
):
    print (loader, name, is_pkg)
