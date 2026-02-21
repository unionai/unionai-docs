#!/usr/bin/env python3
"""
Check that llm_readable_bundle frontmatter and llm-bundle-note shortcode are in sync.

Usage:
    python check_llm_bundle_notes.py

Scans all _index.md files under content/ and verifies:
- Every file with `llm_readable_bundle: true` contains `{{< llm-bundle-note >}}`
- Every file with `{{< llm-bundle-note >}}` has `llm_readable_bundle: true`

Exit codes: 0 = all clear, 1 = mismatches found.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _repo import get_repo_root

CONTENT_DIR = get_repo_root() / 'content'
FRONTMATTER_PARAM = 'llm_readable_bundle'
SHORTCODE = '{{< llm-bundle-note >}}'


def check_files() -> list[str]:
    """Check all _index.md files for frontmatter/shortcode consistency."""
    errors = []

    for index_file in sorted(CONTENT_DIR.rglob('_index.md')):
        content = index_file.read_text(encoding='utf-8')
        rel_path = index_file.relative_to(CONTENT_DIR)

        # Parse frontmatter
        fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        has_param = False
        if fm_match:
            for line in fm_match.group(1).splitlines():
                if re.match(rf'^{FRONTMATTER_PARAM}\s*:\s*true\s*$', line):
                    has_param = True
                    break

        has_shortcode = SHORTCODE in content

        if has_param and not has_shortcode:
            errors.append(
                f"{rel_path}: has `{FRONTMATTER_PARAM}: true` but missing `{SHORTCODE}`"
            )
        elif has_shortcode and not has_param:
            errors.append(
                f"{rel_path}: has `{SHORTCODE}` but missing `{FRONTMATTER_PARAM}: true`"
            )

    return errors


def main():
    errors = check_files()

    if errors:
        print(f"Found {len(errors)} llm-bundle-note issue(s):\n")
        for error in errors:
            print(f"  ::error::{error}")
        print(f"\nRun `make check-llm-bundle-notes` locally to verify.")
        sys.exit(1)
    else:
        print("All llm_readable_bundle pages have matching shortcodes.")
        sys.exit(0)


if __name__ == '__main__':
    main()
