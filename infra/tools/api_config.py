#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "tomli; python_version < '3.11'",
# ]
# ///
"""Read api-packages.toml and output config values for Make or shell consumption.

Usage:
  uv run tools/api_config.py <section> [<key>]

Examples:
  uv run tools/api_config.py plugins_config output_base
    -> content/api-reference/integrations

  uv run tools/api_config.py sdk_count
    -> 1

  uv run tools/api_config.py sdk 0 output_folder
    -> content/api-reference/flyte-sdk
"""

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


def main():
    if len(sys.argv) < 2:
        print("Usage: api_config.py <section> [<index>] [<key>]", file=sys.stderr)
        sys.exit(1)

    config = load_config()
    section = sys.argv[1]

    if section == "plugins_config":
        pc = config.get("plugins_config", {})
        if len(sys.argv) >= 3:
            key = sys.argv[2]
            val = pc.get(key, "")
            # Print booleans as lowercase true/false for shell consumption
            if isinstance(val, bool):
                print("true" if val else "false")
            else:
                print(val)
        else:
            for k, v in pc.items():
                print(f"{k}={v}")

    elif section == "sdk_count":
        print(len(config.get("sdks", [])))

    elif section == "cli_count":
        print(len(config.get("clis", [])))

    elif section == "plugin_count":
        print(len(config.get("plugins", [])))

    elif section == "sdk":
        if len(sys.argv) < 3:
            print("Usage: api_config.py sdk <index> [<key>]", file=sys.stderr)
            sys.exit(1)
        idx = int(sys.argv[2])
        sdks = config.get("sdks", [])
        if idx >= len(sdks):
            print(f"SDK index {idx} out of range (have {len(sdks)})", file=sys.stderr)
            sys.exit(1)
        sdk = sdks[idx]
        if len(sys.argv) >= 4:
            key = sys.argv[3]
            val = sdk.get(key, "")
            print(val)
        else:
            for k, v in sdk.items():
                print(f"{k}={v}")

    elif section == "cli":
        if len(sys.argv) < 3:
            print("Usage: api_config.py cli <index> [<key>]", file=sys.stderr)
            sys.exit(1)
        idx = int(sys.argv[2])
        clis = config.get("clis", [])
        if idx >= len(clis):
            print(f"CLI index {idx} out of range (have {len(clis)})", file=sys.stderr)
            sys.exit(1)
        cli = clis[idx]
        if len(sys.argv) >= 4:
            key = sys.argv[3]
            val = cli.get(key, "")
            print(val)
        else:
            for k, v in cli.items():
                print(f"{k}={v}")

    else:
        print(f"Unknown section: {section}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
