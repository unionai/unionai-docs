#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "packaging",
#     "tomli; python_version < '3.11'",
# ]
# ///
"""
Check if committed API docs are up-to-date with PyPI releases.

Modes:
  --check   Compare committed versions vs PyPI latest. Exit 0 if current, 1 if outdated.
  --update  Same check, but prompt to regenerate if outdated (interactive only).

Reads api-packages.toml for the list of packages and their version files.
"""

import argparse
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

from packaging.version import Version

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore[no-redef]

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_FILE = REPO_ROOT / "api-packages.toml"


def load_config() -> dict:
    with open(CONFIG_FILE, "rb") as f:
        return tomllib.load(f)


def extract_frontmatter_version(version_file: Path) -> str | None:
    """Extract version: field from Hugo YAML frontmatter."""
    if not version_file.exists():
        return None
    text = version_file.read_text()
    # Match YAML frontmatter between --- delimiters
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    for line in m.group(1).splitlines():
        if line.startswith("version:"):
            return line.split(":", 1)[1].strip()
    return None


def get_pypi_latest(package: str) -> str | None:
    """Get latest version from PyPI."""
    url = f"https://pypi.org/pypi/{package}/json"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"  Warning: failed to query PyPI for {package}: {e}", file=sys.stderr)
        return None

    # Find the latest stable version from all releases
    versions = []
    for ver_str, files in data.get("releases", {}).items():
        # Skip yanked releases and releases with no files
        if not files:
            continue
        if all(f.get("yanked", False) for f in files):
            continue
        try:
            v = Version(ver_str)
            if not v.is_prerelease:
                versions.append(v)
        except Exception:
            continue

    if not versions:
        return None

    return str(max(versions))


def check_all(config: dict) -> list[dict]:
    """Check all packages. Returns list of dicts with package info and status."""
    results = []
    plugins_config = config.get("plugins_config", {})
    output_base = plugins_config.get("output_base", "content/api-reference/integrations")

    # SDKs
    for sdk in config.get("sdks", []):
        version_file = REPO_ROOT / sdk["version_file"]
        committed = extract_frontmatter_version(version_file)
        latest = get_pypi_latest(sdk["package"])
        output = REPO_ROOT / sdk["output_folder"]
        content_missing = not (output / "packages").is_dir() or not (output / "classes").is_dir()
        results.append({
            "type": "sdk",
            "package": sdk["package"],
            "committed": committed,
            "latest": latest,
            "outdated": _is_outdated(committed, latest) or content_missing,
            "version_file": sdk["version_file"],
        })

    # Plugins
    for plugin in config.get("plugins", []):
        version_file = REPO_ROOT / output_base / plugin["name"] / "_index.md"
        committed = extract_frontmatter_version(version_file)
        latest = get_pypi_latest(plugin["package"])
        results.append({
            "type": "plugin",
            "package": plugin["package"],
            "plugin": plugin["plugin"],
            "name": plugin["name"],
            "title": plugin["title"],
            "extras": plugin.get("extras", []),
            "committed": committed,
            "latest": latest,
            "outdated": _is_outdated(committed, latest),
            "version_file": f"{output_base}/{plugin['name']}/_index.md",
        })

    # CLIs
    for cli in config.get("clis", []):
        if "output_file" in cli:
            content_missing = not (REPO_ROOT / cli["output_file"]).is_file()
        elif "output_dir" in cli:
            content_missing = not (REPO_ROOT / cli["output_dir"]).is_dir()
        else:
            content_missing = False
        results.append({
            "type": "cli",
            "name": cli["name"],
            "package": cli.get("package", cli["name"]),
            "committed": None if content_missing else "present",
            "latest": None,
            "outdated": content_missing,
        })

    return results


def _is_outdated(committed: str | None, latest: str | None) -> bool:
    """Return True if committed version is older than latest, or docs don't exist yet."""
    if latest is None:
        return False
    if committed is None:
        # No committed docs yet — outdated if there's a version on PyPI
        return True
    try:
        return Version(committed) < Version(latest)
    except Exception:
        return False


def print_results(results: list[dict]) -> None:
    for r in results:
        if r["type"] == "cli":
            status = "MISSING" if r["outdated"] else "present"
            print(f"  {r['name']}-cli: [{status}]")
        else:
            status = "OUTDATED" if r["outdated"] else "up-to-date"
            committed = r["committed"] or "not generated"
            latest = r["latest"] or "unknown"
            print(f"  {r['package']}: committed={committed} latest={latest} [{status}]")


def regenerate(results: list[dict]) -> None:
    """Invoke existing Makefiles to regenerate outdated docs."""
    # Regenerate all SDKs together (the sdks target handles all [[sdks]] entries)
    has_outdated_sdk = any(r["outdated"] and r["type"] == "sdk" for r in results)
    if has_outdated_sdk:
        outdated_sdks = [r["package"] for r in results if r["outdated"] and r["type"] == "sdk"]
        print(f"\nRegenerating SDK docs ({', '.join(outdated_sdks)})...")
        subprocess.run(
            ["make", "-f", "Makefile.api.sdk", "sdks"],
            cwd=REPO_ROOT,
            check=True,
        )

    # Regenerate all CLIs together
    has_outdated_cli = any(r["outdated"] and r["type"] == "cli" for r in results)
    if has_outdated_cli:
        outdated_clis = [r["name"] for r in results if r["outdated"] and r["type"] == "cli"]
        print(f"\nRegenerating CLI docs ({', '.join(outdated_clis)})...")
        subprocess.run(
            ["make", "-f", "Makefile.api.sdk", "clis"],
            cwd=REPO_ROOT,
            check=True,
        )

    for r in results:
        if not r["outdated"]:
            continue
        if r["type"] == "plugin":
            print(f"\nRegenerating plugin docs ({r['package']})...")
            cmd = [
                "make", "-f", "Makefile.api.plugins",
                f"PLUGIN={r['plugin']}", f"TITLE={r['title']}", f"NAME={r['name']}",
            ]
            if r.get("extras"):
                extras_str = ",".join(r["extras"])
                cmd.append(f"INSTALL={r['package']}[{extras_str}]")
            subprocess.run(cmd, cwd=REPO_ROOT, check=True)


def main():
    parser = argparse.ArgumentParser(description="Check API doc versions against PyPI")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true",
                       help="Check versions and exit with status code")
    group.add_argument("--update", action="store_true",
                       help="Check versions and prompt to regenerate if outdated")
    args = parser.parse_args()

    config = load_config()
    print("Checking API doc versions against PyPI...")
    results = check_all(config)
    print_results(results)

    outdated = [r for r in results if r["outdated"]]

    if not outdated:
        print("All API docs are up-to-date.")
        return

    if args.check:
        outdated_versioned = [r for r in outdated if r["type"] != "cli"]
        outdated_cli = [r for r in outdated if r["type"] == "cli"]
        msgs = []
        if outdated_versioned:
            msgs.append(f"{len(outdated_versioned)} package(s) have newer versions on PyPI")
        if outdated_cli:
            msgs.append(f"{len(outdated_cli)} CLI doc(s) are missing")
        print(f"\n{'. '.join(msgs)}.")
        print("Run 'make update-api-docs' locally to regenerate.")
        sys.exit(1)

    # --update mode
    print(f"\n{len(outdated)} item(s) need regeneration:")
    for r in outdated:
        if r["type"] == "cli":
            print(f"  {r['name']}-cli: missing")
        else:
            print(f"  {r['package']}: {r['committed'] or 'not generated'} -> {r['latest']}")
    regenerate(outdated)

    print("\nDone. Review and commit the updated docs.")


if __name__ == "__main__":
    main()
