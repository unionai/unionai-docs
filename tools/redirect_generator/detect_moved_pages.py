#!/usr/bin/env python3
"""
Detect moved/renamed pages from git history and generate redirect entries.

Usage:
    python detect_moved_pages.py [--dry-run]

Scans the full branch history for file renames under content/, generates
redirect entries for all variants, and appends new ones to redirects.csv.
Existing redirects are skipped (deduplicated by source URL).

Use git diff/restore to review or undo changes.
"""

import argparse
import csv
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set


# CSV format flags (matching existing redirects.csv)
CSV_FLAGS = '302,TRUE,FALSE,TRUE,TRUE'

# Default output file
REDIRECTS_FILE = 'redirects.csv'

# Makefile include that defines VERSION
MAKEFILE_INC = 'makefile.inc'

# Hugo variant config file pattern: config.{variant}.toml
VARIANT_CONFIG_GLOB = 'config.*.toml'


def read_version(repo_path: Path) -> str:
    """Read VERSION from makefile.inc (e.g. 'v2' on main, 'v1' on v1 branch)."""
    inc_path = repo_path / MAKEFILE_INC
    for line in inc_path.read_text().splitlines():
        if line.startswith('VERSION'):
            # FORMAT: VERSION := v2
            return line.split(':=')[1].strip()
    print(f"Error: VERSION not found in {MAKEFILE_INC}", file=sys.stderr)
    sys.exit(1)


def read_variants(repo_path: Path) -> List[str]:
    """Read variant names from config.{variant}.toml files in the repo root."""
    variants = sorted(
        p.stem.split('.', 1)[1]
        for p in repo_path.glob(VARIANT_CONFIG_GLOB)
    )
    if not variants:
        print(f"Error: no {VARIANT_CONFIG_GLOB} files found in {repo_path}",
              file=sys.stderr)
        sys.exit(1)
    return variants


def run_git_command(args: List[str], cwd: Path) -> str:
    """Run a git command and return stdout."""
    result = subprocess.run(
        ['git'] + args,
        cwd=cwd,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"Git error: {result.stderr}", file=sys.stderr)
        return ""
    return result.stdout


def detect_renames(repo_path: Path) -> List[Tuple[str, str]]:
    """Detect file renames in git history.

    Returns list of (old_path, new_path) tuples.
    """
    args = ['log', '--diff-filter=R', '-M', '--name-status', '--format=',
            '--', 'content/']

    output = run_git_command(args, repo_path)

    renames = []
    for line in output.strip().split('\n'):
        if not line or not line.startswith('R'):
            continue

        # Format: R<similarity>\t<old_path>\t<new_path>
        parts = line.split('\t')
        if len(parts) >= 3:
            old_path = parts[1]
            new_path = parts[2]
            renames.append((old_path, new_path))

    return renames


def content_path_to_url(content_path: str, variant: str, version: str) -> str:
    """Convert a content path to a URL path.

    Examples (version='v2'):
        content/user-guide/foo.md -> www.union.ai/docs/v2/{variant}/user-guide/foo
        content/user-guide/bar/_index.md -> www.union.ai/docs/v2/{variant}/user-guide/bar
    """
    # Remove content/ prefix
    path = content_path
    if path.startswith('content/'):
        path = path[len('content/'):]

    # Remove .md extension
    if path.endswith('.md'):
        path = path[:-3]

    # Handle _index files (directory index pages)
    if path.endswith('/_index'):
        path = path[:-7]  # Remove /_index
    elif path.endswith('/index'):
        path = path[:-6]  # Remove /index

    # Build URL
    return f"www.union.ai/docs/{version}/{variant}/{path}"


def load_existing_redirects(csv_path: Path) -> Dict[str, str]:
    """Load existing redirects as source -> destination map."""
    existing = {}

    if not csv_path.exists():
        return existing

    with open(csv_path, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2:
                existing[row[0]] = row[1]

    return existing


def generate_redirect_entries(
    renames: List[Tuple[str, str]],
    existing: Dict[str, str],
    version: str,
    variants: List[str]
) -> List[str]:
    """Generate new redirect entries for all variants."""
    new_entries = []

    for old_path, new_path in renames:
        for variant in variants:
            old_url = content_path_to_url(old_path, variant, version)
            new_url = content_path_to_url(new_path, variant, version)

            # Skip self-redirects (rename resolved to same URL)
            if old_url == new_url:
                continue

            # Skip if redirect already exists
            if old_url in existing:
                expected_dest = f"https://{new_url}"
                existing_dest = existing[old_url]
                if existing_dest == expected_dest:
                    print(f"  [skip] redirect already exists: {old_url}")
                else:
                    print(f"  [skip] redirect exists with different destination: {old_url}")
                    print(f"         existing:  {existing_dest}")
                    print(f"         expected:  {expected_dest}")
                continue

            # Generate CSV entry
            entry = f"{old_url},https://{new_url},{CSV_FLAGS}"
            new_entries.append(entry)

    return new_entries


def collapse_chains(csv_path: Path) -> int:
    """Collapse multi-hop redirect chains so every source points to the final destination.

    Returns the number of redirects updated.
    """
    # Parse all rows, building a source -> (dest, rest_of_fields) map
    rows: List[List[str]] = []
    source_to_dest: Dict[str, str] = {}

    with open(csv_path, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
            if len(row) >= 2:
                source_to_dest[row[0]] = row[1]

    # For each redirect, follow the chain to the terminal destination.
    # The dest URL in the CSV has https:// prefix, but source URLs don't,
    # so we need to strip https:// from dest to look it up as a source.
    updated = 0
    for row in rows:
        if len(row) < 2:
            continue
        dest = row[1]
        # Follow the chain
        seen = {row[0]}  # track visited to detect cycles
        while True:
            # Strip https:// to match source URL format
            dest_as_source = dest.removeprefix('https://')
            if dest_as_source not in source_to_dest:
                break
            if dest_as_source in seen:
                print(f"  [warn] redirect cycle detected involving: {dest_as_source}",
                      file=sys.stderr)
                break
            seen.add(dest_as_source)
            dest = source_to_dest[dest_as_source]
        if dest != row[1]:
            row[1] = dest
            updated += 1

    # Remove self-redirects (source == destination)
    filtered = []
    removed = 0
    for row in rows:
        if len(row) >= 2 and row[0] == row[1].removeprefix('https://'):
            removed += 1
        else:
            filtered.append(row)

    if removed:
        print(f"  Removed {removed} self-redirects")

    if updated or removed:
        with open(csv_path, 'w', newline='') as f:
            for row in filtered:
                f.write(','.join(row) + '\n')

    return updated


def main():
    parser = argparse.ArgumentParser(
        description='Detect moved pages and generate redirect entries'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print new redirects without modifying the file'
    )
    parser.add_argument(
        '--output',
        default=REDIRECTS_FILE,
        help=f'Output CSV file (default: {REDIRECTS_FILE})'
    )
    args = parser.parse_args()

    repo_path = Path(__file__).parent.parent.parent
    output_path = repo_path / args.output
    version = read_version(repo_path)
    variants = read_variants(repo_path)

    print(f"Detecting file renames in git history...")
    renames = detect_renames(repo_path)
    print(f"  Found {len(renames)} renamed files")

    if not renames:
        print("No renames found")
        return 0

    print(f"Loading existing redirects from {args.output}...")
    existing = load_existing_redirects(output_path)
    print(f"  Found {len(existing)} existing redirects")

    print(f"Generating redirect entries for variants: {', '.join(variants)} (version: {version})...")
    new_entries = generate_redirect_entries(renames, existing, version, variants)

    if not new_entries:
        print("All renames already have redirects")
        return 0

    print(f"  Generated {len(new_entries)} new redirect entries")

    if args.dry_run:
        print("\nNew entries (dry run):\n")
        for entry in new_entries:
            print(entry)
        return 0

    # Append to redirects.csv
    print(f"Appending to {args.output}...")
    with open(output_path, 'a', newline='') as f:
        # Ensure file ends with newline before appending
        if output_path.stat().st_size > 0:
            with open(output_path, 'rb') as rb:
                rb.seek(-1, 2)
                if rb.read(1) != b'\n':
                    f.write('\n')
        for entry in new_entries:
            f.write(entry + '\n')

    print(f"Added {len(new_entries)} new redirects to {args.output}")

    # Collapse any multi-hop redirect chains
    print(f"Collapsing redirect chains...")
    collapsed = collapse_chains(output_path)
    if collapsed:
        print(f"  Updated {collapsed} redirects to point to final destination")
    else:
        print(f"  No chains found")

    return 0


if __name__ == '__main__':
    sys.exit(main())
