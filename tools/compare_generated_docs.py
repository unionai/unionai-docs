#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "tomli; python_version < '3.11'",
# ]
# ///
"""Compare generated API docs between a git ref and the working tree.

Reads api-packages.toml to discover generated content paths, then compares
old files (from a git ref) against new files (in the working tree) to detect:
  - Removed files (potential 404s)
  - Added files (new pages)
  - Changed heading anchors (potential broken #fragment links)

Usage:
    uv run python tools/compare_generated_docs.py
    uv run python tools/compare_generated_docs.py --old-ref 62acd5d8
    uv run python tools/compare_generated_docs.py --old-ref v1
    uv run python tools/compare_generated_docs.py --content-only
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore[no-redef]

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = REPO_ROOT / "api-packages.toml"


def load_config() -> dict:
    with open(CONFIG_FILE, "rb") as f:
        return tomllib.load(f)


def run_git(args: List[str], quiet: bool = False) -> str:
    """Run a git command and return stdout."""
    result = subprocess.run(
        ["git"] + args,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        if not quiet:
            print(f"Git error: {result.stderr.strip()}", file=sys.stderr)
        return ""
    return result.stdout


def get_generated_paths(config: dict, content_only: bool = False) -> List[str]:
    """Compute all generated directory/file paths from api-packages.toml.

    Returns paths relative to repo root (e.g. 'content/api-reference/plugins/airflow').
    """
    paths = []

    # SDK docs
    for sdk in config.get("sdks", []):
        if sdk.get("frozen", False):
            continue
        output = sdk["output_folder"]
        paths.append(f"{output}/packages")
        paths.append(f"{output}/classes")
        if not content_only:
            gen_name = sdk["generator_name"]
            paths.append(f"data/{gen_name}.yaml")
            paths.append(f"static/{gen_name}-linkmap.json")

    # CLI docs
    for cli in config.get("clis", []):
        if cli.get("frozen", False):
            continue
        if "output_dir" in cli:
            paths.append(cli["output_dir"])
        elif "output_file" in cli:
            paths.append(cli["output_file"])

    # Plugin docs
    plugins_config = config.get("plugins_config", {})
    output_base = plugins_config.get("output_base", "content/api-reference/integrations")
    for plugin in config.get("plugins", []):
        if plugin.get("frozen", False):
            continue
        name = plugin["name"]
        paths.append(f"{output_base}/{name}")
        if not content_only:
            paths.append(f"data/{name}.yaml")
            paths.append(f"static/{name}-linkmap.json")

    return paths


def resolve_old_ref(explicit_ref: Optional[str]) -> str:
    """Resolve the old ref to compare against.

    If explicit_ref is given, use it directly.
    Otherwise, compute merge-base of v1 and HEAD.
    """
    if explicit_ref:
        # Verify it's valid
        sha = run_git(["rev-parse", "--verify", explicit_ref], quiet=True).strip()
        if not sha:
            print(f"Error: '{explicit_ref}' is not a valid git ref", file=sys.stderr)
            sys.exit(1)
        return explicit_ref

    # Try merge-base with v1
    for branch in ["v1", "origin/v1"]:
        sha = run_git(["merge-base", branch, "HEAD"], quiet=True).strip()
        if sha:
            return sha

    print("Error: could not find merge-base with v1. Use --old-ref explicitly.",
          file=sys.stderr)
    sys.exit(1)


def get_old_files(ref: str, paths: List[str]) -> Set[str]:
    """List all files under the given paths in the old ref."""
    # Pass all paths to a single git ls-tree call
    output = run_git(["ls-tree", "-r", "--name-only", ref, "--"] + paths, quiet=True)
    files = set()
    for line in output.strip().split("\n"):
        line = line.strip()
        if line:
            files.add(line)
    return files


def get_new_files(paths: List[str]) -> Set[str]:
    """List all files under the given paths in the working tree."""
    files = set()
    for p in paths:
        full = REPO_ROOT / p
        if full.is_file():
            files.add(p)
        elif full.is_dir():
            for f in full.rglob("*"):
                if f.is_file():
                    files.add(str(f.relative_to(REPO_ROOT)))
    return files


def get_old_file_content(ref: str, path: str) -> str:
    """Retrieve file content from the old ref."""
    return run_git(["show", f"{ref}:{path}"], quiet=True)


def slugify_heading(text: str) -> str:
    """Convert a markdown heading to a Hugo/Goldmark anchor ID.

    Hugo's Goldmark renderer: lowercase, spaces to hyphens, strip most
    special characters, collapse multiple hyphens.
    """
    s = text.strip()
    s = s.lower()
    # Remove inline code backticks
    s = s.replace("`", "")
    # Replace spaces and underscores with hyphens
    s = re.sub(r"[\s_]+", "-", s)
    # Keep only alphanumeric, hyphens, and dots (Hugo keeps dots)
    s = re.sub(r"[^a-z0-9.\-]", "", s)
    # Collapse multiple hyphens
    s = re.sub(r"-{2,}", "-", s)
    # Strip leading/trailing hyphens
    s = s.strip("-")
    return s


# Regex for markdown headings (ATX style)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)


def extract_anchors(content: str) -> Set[str]:
    """Extract slugified anchor IDs from markdown headings."""
    anchors = set()
    for match in HEADING_RE.finditer(content):
        heading_text = match.group(2).strip()
        anchors.add(slugify_heading(heading_text))
    return anchors


def compare_anchors(
    ref: str,
    common_files: Set[str],
) -> List[Tuple[str, Set[str], Set[str]]]:
    """For files present in both old and new, compare heading anchors.

    Returns list of (path, removed_anchors, added_anchors) for files with changes.
    Only checks .md files.
    """
    changes = []
    md_files = sorted(f for f in common_files if f.endswith(".md"))

    for path in md_files:
        old_content = get_old_file_content(ref, path)
        new_path = REPO_ROOT / path
        if not new_path.is_file():
            continue
        new_content = new_path.read_text(errors="replace")

        old_anchors = extract_anchors(old_content)
        new_anchors = extract_anchors(new_content)

        removed = old_anchors - new_anchors
        added = new_anchors - old_anchors

        if removed or added:
            changes.append((path, removed, added))

    return changes


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare generated API docs between a git ref and the working tree."
    )
    parser.add_argument(
        "--old-ref",
        help="Git ref (commit, branch, tag) to compare against. "
             "Default: merge-base of v1 and HEAD.",
    )
    parser.add_argument(
        "--content-only",
        action="store_true",
        help="Only compare content files (skip data/ and static/).",
    )
    args = parser.parse_args()

    config = load_config()
    old_ref = resolve_old_ref(args.old_ref)
    paths = get_generated_paths(config, content_only=args.content_only)

    # Resolve short ref for display
    display_ref = run_git(["rev-parse", "--short", old_ref], quiet=True).strip() or old_ref

    print("=== Generated Docs Comparison ===")
    print(f"Old ref: {display_ref}")
    print(f"Generated paths from: api-packages.toml ({len(paths)} entries)")
    print()

    old_files = get_old_files(old_ref, paths)
    new_files = get_new_files(paths)

    removed_files = sorted(old_files - new_files)
    added_files = sorted(new_files - old_files)
    common_files = old_files & new_files

    # --- Removed Files ---
    print(f"--- Removed Files ({len(removed_files)}) ---")
    if removed_files:
        for f in removed_files:
            print(f"  {f}")
    else:
        print("  (none)")
    print()

    # --- Added Files ---
    print(f"--- Added Files ({len(added_files)}) ---")
    if added_files:
        for f in added_files:
            print(f"  {f}")
    else:
        print("  (none)")
    print()

    # --- Changed Anchors ---
    anchor_changes = compare_anchors(old_ref, common_files)
    print(f"--- Changed Anchors ({len(anchor_changes)} files) ---")
    if anchor_changes:
        for path, removed, added in anchor_changes:
            print(f"  {path}")
            for r in sorted(removed):
                print(f"    Removed: #{r}")
            for a in sorted(added):
                print(f"    Added:   #{a}")
    else:
        print("  (none)")
    print()

    # --- Summary ---
    print("--- Summary ---")
    print(f"Removed files:  {len(removed_files)}")
    print(f"Added files:    {len(added_files)}")
    print(f"Anchor changes: {len(anchor_changes)} files")

    # Exit 1 if there are removals (potential breakage)
    if removed_files or anchor_changes:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
