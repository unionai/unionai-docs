#!/usr/bin/env python3
"""
Check that deleted content pages have corresponding redirects.

Usage:
    python check_deleted_pages.py

Scans the full branch history for deleted files under content/, checks that
each has a redirect entry in redirects.csv for all variants, and reports
any missing redirects.

Paths can be excluded via .redirects-exclude (one path pattern per line).

Exit codes: 0 = all clear, 1 = missing redirects found.
"""

import csv
import fnmatch
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Set


# Makefile include that defines VERSION
MAKEFILE_INC = 'makefile.inc'

# Hugo variant config file pattern: config.{variant}.toml
VARIANT_CONFIG_GLOB = 'config.*.toml'

# Default files
REDIRECTS_FILE = 'redirects.csv'
EXCLUDE_FILE = '.redirects-exclude'


def read_version(repo_path: Path) -> str:
    """Read VERSION from makefile.inc."""
    inc_path = repo_path / MAKEFILE_INC
    for line in inc_path.read_text().splitlines():
        if line.startswith('VERSION'):
            return line.split(':=')[1].strip()
    print(f"Error: VERSION not found in {MAKEFILE_INC}", file=sys.stderr)
    sys.exit(1)


def read_variants(repo_path: Path) -> List[str]:
    """Read variant names from config.{variant}.toml files."""
    variants = sorted(
        p.stem.split('.', 1)[1]
        for p in repo_path.glob(VARIANT_CONFIG_GLOB)
    )
    if not variants:
        print(f"Error: no {VARIANT_CONFIG_GLOB} files found in {repo_path}",
              file=sys.stderr)
        sys.exit(1)
    return variants


def content_path_to_url(content_path: str, variant: str, version: str) -> str:
    """Convert a content path to a URL path.

    Examples (version='v2'):
        content/user-guide/foo.md -> www.union.ai/docs/v2/{variant}/user-guide/foo
        content/user-guide/bar/_index.md -> www.union.ai/docs/v2/{variant}/user-guide/bar
    """
    path = content_path
    if path.startswith('content/'):
        path = path[len('content/'):]

    if path.endswith('.md'):
        path = path[:-3]

    if path.endswith('/_index'):
        path = path[:-7]
    elif path.endswith('/index'):
        path = path[:-6]

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


def detect_deleted_files(repo_path: Path) -> List[str]:
    """Detect content files deleted in git history.

    Returns list of deleted content paths.
    """
    output = run_git_command(
        ['log', '--diff-filter=D', '--name-only', '--format=', '--', 'content/'],
        repo_path
    )

    deleted = set()
    for line in output.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.startswith('content/') and line.endswith('.md'):
            deleted.add(line)

    return sorted(deleted)


def load_exclude_patterns(repo_path: Path) -> List[str]:
    """Load exclusion patterns from .redirects-exclude."""
    exclude_path = repo_path / EXCLUDE_FILE
    if not exclude_path.exists():
        return []

    patterns = []
    for line in exclude_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        patterns.append(line)
    return patterns


def is_excluded(path: str, patterns: List[str]) -> bool:
    """Check if a path matches any exclusion pattern."""
    for pattern in patterns:
        if fnmatch.fnmatch(path, pattern):
            return True
        # Also match if the pattern is a prefix (directory exclusion)
        if not pattern.endswith('*') and path.startswith(pattern):
            return True
    return False


def main() -> int:
    repo_path = Path(__file__).parent.parent.parent
    version = read_version(repo_path)
    variants = read_variants(repo_path)

    print("Checking for deleted pages missing redirects...")

    # Detect deleted files
    deleted_files = detect_deleted_files(repo_path)
    print(f"  Found {len(deleted_files)} deleted content files in git history")

    if not deleted_files:
        print("No deleted content files found.")
        return 0

    # Exclude files that currently exist (delete-then-recreate)
    still_exist = []
    truly_deleted = []
    for path in deleted_files:
        if (repo_path / path).exists():
            still_exist.append(path)
        else:
            truly_deleted.append(path)

    if still_exist:
        print(f"  Excluding {len(still_exist)} files that were re-created")

    # Apply exclusion patterns
    exclude_patterns = load_exclude_patterns(repo_path)
    if exclude_patterns:
        print(f"  Loaded {len(exclude_patterns)} exclusion patterns from {EXCLUDE_FILE}")

    filtered = []
    excluded_count = 0
    for path in truly_deleted:
        if is_excluded(path, exclude_patterns):
            excluded_count += 1
        else:
            filtered.append(path)

    if excluded_count:
        print(f"  Excluded {excluded_count} files matching {EXCLUDE_FILE} patterns")

    if not filtered:
        print("All deleted files are accounted for.")
        return 0

    # Load existing redirects
    redirects = load_existing_redirects(repo_path / REDIRECTS_FILE)
    print(f"  Loaded {len(redirects)} existing redirects from {REDIRECTS_FILE}")

    # Check each deleted file for redirects across all variants
    missing_by_file: Dict[str, List[str]] = {}
    total_missing = 0

    for path in filtered:
        missing_urls = []
        for variant in variants:
            url = content_path_to_url(path, variant, version)
            if url not in redirects:
                missing_urls.append(url)
                total_missing += 1
        if missing_urls:
            missing_by_file[path] = missing_urls

    if not missing_by_file:
        print("All deleted pages have redirects.")
        return 0

    # Report missing redirects
    print("\nDeleted pages missing redirects:\n")
    for path, urls in sorted(missing_by_file.items()):
        print(f"  {path}")
        for url in urls:
            print(f"    missing: {url}")
        print()

    print(f"Found {total_missing} missing redirect(s) for {len(missing_by_file)} deleted page(s).")
    print(f"Add redirects to {REDIRECTS_FILE} or exclude paths in {EXCLUDE_FILE}.")
    return 1


if __name__ == '__main__':
    sys.exit(main())
