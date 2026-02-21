"""Shared helpers for locating the repository root and infra directory."""

import os
import subprocess
from pathlib import Path

# infra/ directory (parent of tools/)
INFRA_ROOT = Path(__file__).resolve().parent.parent

def get_repo_root() -> Path:
    """Return the repository root directory.

    Uses REPO_ROOT env var (set by Makefile) when available,
    falls back to git discovery.
    """
    root = os.environ.get("REPO_ROOT")
    if root:
        return Path(root)
    # Fallback: git discovery
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    )
    return Path(result.stdout.strip())
