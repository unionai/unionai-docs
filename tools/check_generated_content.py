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
  - SDK API docs (packages/ and classes/ under content/api-reference/flyte-sdk/)
  - CLI docs (content/api-reference/flyte-cli.md)
  - Plugin API docs (content/api-reference/integrations/{name}/)
  - Data YAML files (data/{name}.yaml)
  - Linkmap JSON files (static/{name}-linkmap.json)

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
    sdk_packages = REPO_ROOT / "content" / "api-reference" / "flyte-sdk" / "packages"
    sdk_classes = REPO_ROOT / "content" / "api-reference" / "flyte-sdk" / "classes"

    if not has_md_files(sdk_packages):
        errors.append("SDK API packages: no .md files in content/api-reference/flyte-sdk/packages/")
    if not sdk_classes.is_dir():
        errors.append("SDK API classes: directory missing: content/api-reference/flyte-sdk/classes/")

    # --- CLI docs ---
    cli_doc = REPO_ROOT / "content" / "api-reference" / "flyte-cli.md"
    if not cli_doc.is_file():
        errors.append("CLI docs: missing content/api-reference/flyte-cli.md")

    # --- Plugin API docs ---
    plugins = config.get("plugins", [])
    for plugin in plugins:
        name = plugin["name"]
        plugin_dir = REPO_ROOT / "content" / "api-reference" / "integrations" / name
        if not plugin_dir.is_dir():
            errors.append(f"Plugin '{name}': directory missing: content/api-reference/integrations/{name}/")
        elif not has_md_files(plugin_dir):
            errors.append(f"Plugin '{name}': no .md files in content/api-reference/integrations/{name}/")

    # --- Data YAML files ---
    data_names = ["flytesdk"] + [p["name"] for p in plugins]
    for name in data_names:
        yaml_file = REPO_ROOT / "data" / f"{name}.yaml"
        if not yaml_file.is_file():
            errors.append(f"Data YAML: missing data/{name}.yaml")

    # --- Linkmap JSON files ---
    linkmap_names = ["flytesdk"] + [p["name"] for p in plugins]
    for name in linkmap_names:
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
