#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "tomli; python_version < '3.11'",
# ]
# ///
"""Remove all generated content paths defined in api-packages.toml.

Reads [[sdks]], [[clis]], and [[plugins]] to determine which directories
and files to clean. Also removes generated data YAML and linkmap JSON files.
"""

import shutil
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore[no-redef]

from _repo import get_repo_root

REPO_ROOT = get_repo_root()
CONFIG_FILE = REPO_ROOT / "api-packages.toml"


def load_config() -> dict:
    with open(CONFIG_FILE, "rb") as f:
        return tomllib.load(f)


def remove_path(path: Path, label: str) -> None:
    """Remove a file or directory, printing what was removed."""
    if path.is_dir():
        shutil.rmtree(path)
        print(f"  Removed directory: {label}")
    elif path.is_file():
        path.unlink()
        print(f"  Removed file: {label}")


def main() -> None:
    config = load_config()

    # --- SDK generated content ---
    for sdk in config.get("sdks", []):
        if sdk.get("frozen", False):
            print(f"Skipping {sdk['generator_name']}: frozen (committed content)")
            continue
        output = REPO_ROOT / sdk["output_folder"]
        packages_dir = output / "packages"
        classes_dir = output / "classes"
        remove_path(packages_dir, f"{sdk['output_folder']}/packages")
        remove_path(classes_dir, f"{sdk['output_folder']}/classes")

        # Data YAML and linkmap JSON
        gen_name = sdk["generator_name"]
        remove_path(REPO_ROOT / "data" / f"{gen_name}.yaml", f"data/{gen_name}.yaml")
        remove_path(REPO_ROOT / "static" / f"{gen_name}-linkmap.json", f"static/{gen_name}-linkmap.json")

    # --- CLI generated content ---
    for cli in config.get("clis", []):
        if cli.get("frozen", False):
            continue
        if "output_file" in cli:
            remove_path(REPO_ROOT / cli["output_file"], cli["output_file"])
        elif "output_dir" in cli:
            remove_path(REPO_ROOT / cli["output_dir"], cli["output_dir"])

    # --- Plugin generated content ---
    plugins_config = config.get("plugins_config", {})
    output_base = plugins_config.get("output_base", "content/api-reference/integrations")

    for plugin in config.get("plugins", []):
        if plugin.get("frozen", False):
            print(f"Skipping plugin {plugin['name']}: frozen (committed content)")
            continue
        name = plugin["name"]
        plugin_dir = REPO_ROOT / output_base / name
        remove_path(plugin_dir, f"{output_base}/{name}")

        # Data YAML and linkmap JSON
        remove_path(REPO_ROOT / "data" / f"{name}.yaml", f"data/{name}.yaml")
        remove_path(REPO_ROOT / "static" / f"{name}-linkmap.json", f"static/{name}-linkmap.json")

    print("Clean complete.")


if __name__ == "__main__":
    main()
