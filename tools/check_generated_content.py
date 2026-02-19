#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "tomli; python_version < '3.11'",
# ]
# ///
"""
Check that all generated content files exist in the repository.

Reads api-packages.toml and verifies expected files for:
  - SDK API docs (packages/ and classes/ under each SDK's output_folder)
  - CLI docs (each CLI's output_file or output_dir)
  - Plugin API docs (under plugins_config.output_base/{name}/)
  - Data YAML files (data/{generator_name}.yaml, data/{plugin_name}.yaml)
  - Linkmap JSON files (static/{generator_name}-linkmap.json, static/{plugin_name}-linkmap.json)

Exit codes: 0 = all present, 1 = missing content detected.
"""

import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore[no-redef]

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = REPO_ROOT / "api-packages.toml"


def load_config() -> dict:
    with open(CONFIG_FILE, "rb") as f:
        return tomllib.load(f)


def has_md_files(directory: Path) -> bool:
    """Check if a directory exists and contains .md files beyond its own _index.md."""
    if not directory.is_dir():
        return False
    top_index = directory / "_index.md"
    return any(p.suffix == ".md" and p != top_index for p in directory.rglob("*.md"))


def check_all(config: dict) -> list[str]:
    """Check all categories of generated content. Returns list of error messages."""
    errors = []

    # --- SDK API docs ---
    for sdk in config.get("sdks", []):
        output_folder = sdk["output_folder"]
        sdk_packages = REPO_ROOT / output_folder / "packages"
        sdk_classes = REPO_ROOT / output_folder / "classes"

        if not has_md_files(sdk_packages):
            errors.append(f"SDK API packages: no .md files in {output_folder}/packages/")
        if not sdk_classes.is_dir():
            errors.append(f"SDK API classes: directory missing: {output_folder}/classes/")

        # Data YAML
        gen_name = sdk["generator_name"]
        yaml_file = REPO_ROOT / "data" / f"{gen_name}.yaml"
        if not yaml_file.is_file():
            errors.append(f"Data YAML: missing data/{gen_name}.yaml")

        # Linkmap JSON
        linkmap_file = REPO_ROOT / "static" / f"{gen_name}-linkmap.json"
        if not linkmap_file.is_file():
            errors.append(f"Linkmap: missing static/{gen_name}-linkmap.json")

    # --- CLI docs ---
    for cli in config.get("clis", []):
        if "output_file" in cli:
            cli_path = REPO_ROOT / cli["output_file"]
            if not cli_path.is_file():
                errors.append(f"CLI docs: missing {cli['output_file']}")
        elif "output_dir" in cli:
            cli_path = REPO_ROOT / cli["output_dir"]
            if not cli_path.is_dir():
                errors.append(f"CLI docs: directory missing: {cli['output_dir']}/")
            elif not has_md_files(cli_path):
                errors.append(f"CLI docs: no .md files in {cli['output_dir']}/")

    # --- Plugin API docs ---
    plugins_config = config.get("plugins_config", {})
    output_base = plugins_config.get("output_base", "content/api-reference/integrations")
    check_plugin_linkmaps = plugins_config.get("check_linkmaps", True)

    plugins = config.get("plugins", [])
    for plugin in plugins:
        name = plugin["name"]
        plugin_dir = REPO_ROOT / output_base / name
        if not plugin_dir.is_dir():
            errors.append(f"Plugin '{name}': directory missing: {output_base}/{name}/")
        elif not has_md_files(plugin_dir):
            errors.append(f"Plugin '{name}': no .md files in {output_base}/{name}/")

        if check_plugin_linkmaps:
            # Data YAML
            yaml_file = REPO_ROOT / "data" / f"{name}.yaml"
            if not yaml_file.is_file():
                errors.append(f"Data YAML: missing data/{name}.yaml")

            # Linkmap JSON
            linkmap_file = REPO_ROOT / "static" / f"{name}-linkmap.json"
            if not linkmap_file.is_file():
                errors.append(f"Linkmap: missing static/{name}-linkmap.json")

    return errors


def main():
    config = load_config()
    errors = check_all(config)

    if errors:
        print(f"Found {len(errors)} missing generated content item(s):\n")
        for error in errors:
            print(f"  ::error::{error}")
        print(f"\nRun 'make dist' to regenerate missing content.")
        sys.exit(1)
    else:
        print("All generated content is present.")
        sys.exit(0)


if __name__ == "__main__":
    main()
