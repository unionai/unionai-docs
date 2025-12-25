#!/usr/bin/env python3
"""
Detect moved/renamed pages from git history and generate redirect entries.

Usage:
    python detect_moved_pages.py [--dry-run] [--since=COMMIT] [--reset]

The tool tracks which commit it was last run against using a checkpoint file.
On subsequent runs, it only processes renames since that checkpoint.
"""

import argparse
import csv
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple, Set, Optional


# Variants to generate redirects for
VARIANTS = ['flyte', 'byoc', 'selfmanaged']

# CSV format flags (matching existing redirects.csv)
CSV_FLAGS = '302,TRUE,FALSE,TRUE,TRUE'

# Checkpoint file name
CHECKPOINT_FILE = '.redirects-checkpoint'


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


def get_current_commit(repo_path: Path) -> str:
    """Get the current HEAD commit hash."""
    return run_git_command(['rev-parse', 'HEAD'], repo_path).strip()


def load_checkpoint(repo_path: Path) -> Optional[str]:
    """Load the last processed commit from checkpoint file."""
    checkpoint_path = repo_path / CHECKPOINT_FILE
    if checkpoint_path.exists():
        return checkpoint_path.read_text().strip()
    return None


def save_checkpoint(repo_path: Path, commit: str) -> None:
    """Save the current commit to checkpoint file."""
    checkpoint_path = repo_path / CHECKPOINT_FILE
    checkpoint_path.write_text(commit + '\n')
    print(f"💾 Saved checkpoint: {commit[:12]}")


def detect_renames(repo_path: Path, since: str = None) -> List[Tuple[str, str]]:
    """Detect file renames in git history.

    Returns list of (old_path, new_path) tuples.
    """
    args = ['log', '--diff-filter=R', '-M', '--name-status', '--format=']

    if since:
        args.append(f'{since}..HEAD')

    args.extend(['--', 'content/'])

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


def content_path_to_url(content_path: str, variant: str) -> str:
    """Convert a content path to a URL path.

    Examples:
        content/user-guide/foo.md -> /docs/{variant}/user-guide/foo
        content/user-guide/bar/_index.md -> /docs/{variant}/user-guide/bar
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
    return f"www.union.ai/docs/{variant}/{path}"


def load_existing_redirects(csv_path: Path) -> Set[str]:
    """Load existing redirect sources from CSV."""
    existing = set()

    if not csv_path.exists():
        return existing

    with open(csv_path, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 1:
                existing.add(row[0])

    return existing


def generate_redirect_entries(
    renames: List[Tuple[str, str]],
    existing: Set[str]
) -> List[str]:
    """Generate new redirect entries for all variants."""
    new_entries = []

    for old_path, new_path in renames:
        for variant in VARIANTS:
            old_url = content_path_to_url(old_path, variant)
            new_url = content_path_to_url(new_path, variant)

            # Skip if redirect already exists
            if old_url in existing:
                continue

            # Generate CSV entry
            entry = f"{old_url},https://{new_url},{CSV_FLAGS}"
            new_entries.append(entry)

    return new_entries


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
        '--since',
        help='Git commit/tag to start from (overrides checkpoint)'
    )
    parser.add_argument(
        '--reset',
        action='store_true',
        help='Reset checkpoint and process all history'
    )
    parser.add_argument(
        '--set-checkpoint',
        nargs='?',
        const='HEAD',
        metavar='COMMIT',
        help='Set checkpoint to COMMIT (default: HEAD) and exit'
    )
    parser.add_argument(
        '--output',
        default='redirects.csv',
        help='Output CSV file (default: redirects.csv)'
    )

    args = parser.parse_args()

    repo_path = Path(__file__).parent.parent.parent
    csv_path = repo_path / args.output

    # Handle --set-checkpoint
    if args.set_checkpoint:
        commit = args.set_checkpoint
        if commit == 'HEAD':
            commit = get_current_commit(repo_path)
        else:
            # Validate the commit exists
            result = run_git_command(['rev-parse', commit], repo_path)
            if not result:
                print(f"❌ Invalid commit: {commit}", file=sys.stderr)
                return 1
            commit = result.strip()
        save_checkpoint(repo_path, commit)
        print(f"✅ Checkpoint set to: {commit[:12]}")
        return 0

    # Determine the starting commit
    if args.reset:
        since = None
        print("🔄 Reset mode: processing all history")
    elif args.since:
        since = args.since
        print(f"📌 Using specified commit: {since[:12] if len(since) > 12 else since}")
    else:
        since = load_checkpoint(repo_path)
        if since:
            print(f"📌 Using checkpoint: {since[:12]}")
        else:
            print("📌 No checkpoint found, processing all history")

    current_commit = get_current_commit(repo_path)
    print(f"🎯 Current HEAD: {current_commit[:12]}")

    print(f"🔍 Detecting file renames in git history...")
    renames = detect_renames(repo_path, since)
    print(f"   Found {len(renames)} renamed files")

    if not renames:
        print("✅ No new renames to process")
        if not args.dry_run:
            save_checkpoint(repo_path, current_commit)
        return 0

    print(f"📖 Loading existing redirects from {args.output}...")
    existing = load_existing_redirects(csv_path)
    print(f"   Found {len(existing)} existing redirects")

    print(f"🔧 Generating redirect entries for {len(VARIANTS)} variants...")
    new_entries = generate_redirect_entries(renames, existing)

    if not new_entries:
        print("✅ All renames already have redirects")
        if not args.dry_run:
            save_checkpoint(repo_path, current_commit)
        return 0

    print(f"   Generated {len(new_entries)} new redirect entries")

    if args.dry_run:
        print("\n📋 New entries (dry run):\n")
        for entry in new_entries:
            print(entry)
        return 0

    # Append to CSV
    print(f"📝 Appending to {args.output}...")
    with open(csv_path, 'a', newline='') as f:
        for entry in new_entries:
            f.write(entry + '\n')

    print(f"✅ Added {len(new_entries)} new redirects")

    # Save checkpoint
    save_checkpoint(repo_path, current_commit)

    return 0


if __name__ == '__main__':
    sys.exit(main())
