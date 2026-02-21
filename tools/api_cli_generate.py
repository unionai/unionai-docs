#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "tomli; python_version < '3.11'",
# ]
# ///
"""Iterate [[clis]] from api-packages.toml and generate CLI docs for each.

Supports two types of CLIs:
  - Python CLIs (default): uses gen_command from config, run in the SDK venv
  - Go CLIs (type = "go"): uses scripts/gen-cli-docs with the binary name

The SDK venv (.venv) must already exist with the relevant package installed.
When SKIP_VENV_SETUP=true, uses the current environment instead.
"""

import os
import subprocess
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore[no-redef]

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = REPO_ROOT / "api-packages.toml"
VENV_DIR = REPO_ROOT / ".venv"


def load_config() -> dict:
    with open(CONFIG_FILE, "rb") as f:
        return tomllib.load(f)


def generate_python_cli(cli: dict, python: Path) -> None:
    """Generate CLI docs for a Python-based CLI."""
    include = cli["include"]
    output_file = REPO_ROOT / cli["output_file"]
    import_name = cli.get("import", cli.get("package", cli["name"]))
    gen_command = cli["gen_command"]

    # Get version
    version_cmd = f"import {import_name}; print({import_name}.__version__)"
    result = subprocess.run(
        [str(python), "-c", version_cmd],
        capture_output=True, text=True, cwd=REPO_ROOT,
    )
    version = result.stdout.strip() if result.returncode == 0 else "unknown"

    # Read include template and substitute version
    include_path = REPO_ROOT / include
    header = include_path.read_text().replace("%%VERSION%%", version)

    # Generate CLI docs
    gen_parts = gen_command.split()
    # Use the venv's binary for the first part of the command
    if not (REPO_ROOT / gen_parts[0]).exists():
        # It's a binary in the venv
        venv_bin = python.parent / gen_parts[0]
        if venv_bin.exists():
            gen_parts[0] = str(venv_bin)

    result = subprocess.run(
        gen_parts,
        capture_output=True, text=True, cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        print(f"  Warning: CLI doc generation failed: {result.stderr}", file=sys.stderr)
        return

    # Write combined output
    tmp_file = str(output_file) + ".tmp"
    with open(tmp_file, "w") as f:
        f.write(header)
        f.write("\n")
        f.write(result.stdout)
    os.rename(tmp_file, output_file)
    print(f"  Generated {cli['output_file']}")


def generate_go_cli(cli: dict) -> None:
    """Generate CLI docs for a Go-based CLI."""
    binary = cli["binary"]
    include = cli["include"]

    # Go CLIs may use output_file (single file) or output_dir (multi-file, pre-committed)
    if "output_dir" in cli:
        output_dir = REPO_ROOT / cli["output_dir"]
        if output_dir.is_dir():
            print(f"  Skipping {binary}: output_dir already exists ({cli['output_dir']})")
        else:
            print(f"  Warning: {binary} output_dir missing ({cli['output_dir']}), "
                  f"but Go CLI generation is not supported on this branch")
        return

    output_file = REPO_ROOT / cli["output_file"]

    # Use the gen-cli-docs script
    gen_script = REPO_ROOT / "scripts" / "gen-cli-docs"
    if gen_script.exists():
        result = subprocess.run(
            [str(gen_script), binary],
            capture_output=True, text=True, cwd=REPO_ROOT,
        )
        if result.returncode != 0:
            print(f"  Warning: Go CLI doc generation failed: {result.stderr}", file=sys.stderr)
            return

        # Read include template
        include_path = REPO_ROOT / include
        header = include_path.read_text()

        # Write combined output
        tmp_file = str(output_file) + ".tmp"
        with open(tmp_file, "w") as f:
            f.write(header)
            f.write("\n")
            f.write(result.stdout)
        os.rename(tmp_file, output_file)
        print(f"  Generated {cli['output_file']}")
    else:
        print(f"  Warning: scripts/gen-cli-docs not found, skipping {binary}")


def main() -> None:
    config = load_config()
    clis = config.get("clis", [])
    skip_venv = os.environ.get("SKIP_VENV_SETUP", "false").lower() == "true"

    if not clis:
        print("No [[clis]] entries in api-packages.toml")
        return

    if skip_venv:
        python = Path(sys.executable)
    else:
        python = VENV_DIR / "bin" / "python"

    for cli in clis:
        if cli.get("frozen", False):
            print(f"Skipping {cli['name']}: frozen (committed content)")
            continue
        cli_type = cli.get("type", "python")
        print(f"Generating CLI docs for {cli['name']}...")

        if cli_type == "go":
            generate_go_cli(cli)
        else:
            if not skip_venv and not python.exists():
                print(f"  Warning: venv not found at {VENV_DIR}. "
                      f"Run SDK generation first or set SKIP_VENV_SETUP=true.")
                continue
            generate_python_cli(cli, python)


if __name__ == "__main__":
    main()
