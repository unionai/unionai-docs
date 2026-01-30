#!/usr/bin/env python3
"""
Deploy redirects from redirects.csv to a Cloudflare Bulk Redirect List via API.

Usage:
    python deploy_redirects.py [--dry-run] [--csv PATH]

Reads redirects.csv, converts each row to the Cloudflare redirect item format,
and replaces all items in the configured Bulk Redirect List using:
    PUT /accounts/{account_id}/rules/lists/{list_id}/items

Environment variables (required unless --dry-run):
    CLOUDFLARE_API_TOKEN   - API token with "Account Filter Lists Edit" permission
    CLOUDFLARE_ACCOUNT_ID  - Cloudflare account identifier
    CLOUDFLARE_LIST_ID     - Bulk Redirect List identifier
"""

import argparse
import csv
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

REDIRECTS_FILE = "redirects.csv"
CF_API_BASE = "https://api.cloudflare.com/client/v4"
POLL_INTERVAL_SECONDS = 2
POLL_MAX_ATTEMPTS = 60


def parse_csv(csv_path: Path) -> list[dict]:
    """Parse redirects.csv into a list of Cloudflare redirect item dicts.

    CSV columns (no header row):
        0: source_url
        1: target_url
        2: status_code
        3: include_subdomains (TRUE/FALSE)
        4: subpath_matching (TRUE/FALSE)
        5: preserve_query_string (TRUE/FALSE)
        6: preserve_path_suffix (TRUE/FALSE)
    """
    items = []
    with open(csv_path, "r", newline="") as f:
        reader = csv.reader(f)
        for lineno, row in enumerate(reader, start=1):
            if not row or all(cell.strip() == "" for cell in row):
                continue
            if len(row) < 7:
                print(
                    f"Warning: skipping line {lineno}: expected 7 columns, got {len(row)}",
                    file=sys.stderr,
                )
                continue
            subpath_matching = row[4].strip().upper() == "TRUE"
            preserve_path_suffix = row[6].strip().upper() == "TRUE"
            # CF API rejects preserve_path_suffix when subpath_matching is off
            if preserve_path_suffix and not subpath_matching:
                preserve_path_suffix = False
            items.append(
                {
                    "redirect": {
                        "source_url": row[0].strip(),
                        "target_url": row[1].strip(),
                        "status_code": int(row[2].strip()),
                        "include_subdomains": row[3].strip().upper() == "TRUE",
                        "subpath_matching": subpath_matching,
                        "preserve_query_string": row[5].strip().upper() == "TRUE",
                        "preserve_path_suffix": preserve_path_suffix,
                    }
                }
            )
    return items


def cf_api_request(
    method: str, path: str, token: str, body: object = None
) -> dict:
    """Make a Cloudflare API request and return the parsed JSON response."""
    url = f"{CF_API_BASE}{path}"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"Cloudflare API error ({e.code}): {error_body}", file=sys.stderr)
        sys.exit(1)


def deploy(items: list[dict], account_id: str, list_id: str, token: str) -> None:
    """Replace all items in the Cloudflare Bulk Redirect List."""
    path = f"/accounts/{account_id}/rules/lists/{list_id}/items"

    print(f"Uploading {len(items)} redirect items to Cloudflare...")
    result = cf_api_request("PUT", path, token, body=items)

    if not result.get("success"):
        errors = result.get("errors", [])
        print(f"API returned failure: {errors}", file=sys.stderr)
        sys.exit(1)

    operation_id = result.get("result", {}).get("operation_id")
    if not operation_id:
        print("Upload accepted (no async operation ID returned).")
        return

    # Poll for completion
    print(f"Async operation started: {operation_id}")
    poll_path = f"/accounts/{account_id}/rules/lists/bulk_operations/{operation_id}"

    for attempt in range(1, POLL_MAX_ATTEMPTS + 1):
        time.sleep(POLL_INTERVAL_SECONDS)
        status_result = cf_api_request("GET", poll_path, token)
        status = status_result.get("result", {}).get("status", "unknown")
        print(f"  Poll {attempt}: {status}")

        if status == "completed":
            print("Redirects deployed successfully.")
            return
        elif status == "failed":
            error = status_result.get("result", {}).get("error", "unknown error")
            print(f"Operation failed: {error}", file=sys.stderr)
            sys.exit(1)

    print(
        f"Operation did not complete after {POLL_MAX_ATTEMPTS} attempts.",
        file=sys.stderr,
    )
    sys.exit(1)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deploy redirects.csv to Cloudflare Bulk Redirect List"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse CSV and print stats without making API calls",
    )
    parser.add_argument(
        "--csv",
        default=REDIRECTS_FILE,
        help=f"Path to redirects CSV (default: {REDIRECTS_FILE})",
    )
    args = parser.parse_args()

    # Resolve CSV path relative to repo root
    repo_root = Path(__file__).parent.parent.parent
    csv_path = repo_root / args.csv

    if not csv_path.exists():
        print(f"Error: {csv_path} not found", file=sys.stderr)
        return 1

    items = parse_csv(csv_path)
    print(f"Parsed {len(items)} redirect items from {args.csv}")

    if not items:
        print("No redirect items found. Nothing to deploy.")
        return 0

    if args.dry_run:
        print("\nDry run — no API calls made.")
        print(f"  Total items: {len(items)}")
        print(f"  First item: {items[0]['redirect']['source_url']} -> {items[0]['redirect']['target_url']}")
        print(f"  Last item:  {items[-1]['redirect']['source_url']} -> {items[-1]['redirect']['target_url']}")
        return 0

    # Require env vars for actual deployment
    token = os.environ.get("CLOUDFLARE_API_TOKEN")
    account_id = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
    list_id = os.environ.get("CLOUDFLARE_LIST_ID")

    missing = []
    if not token:
        missing.append("CLOUDFLARE_API_TOKEN")
    if not account_id:
        missing.append("CLOUDFLARE_ACCOUNT_ID")
    if not list_id:
        missing.append("CLOUDFLARE_LIST_ID")

    if missing:
        print(
            f"Error: missing environment variables: {', '.join(missing)}",
            file=sys.stderr,
        )
        print("Set these or use --dry-run to test CSV parsing.", file=sys.stderr)
        return 1

    deploy(items, account_id, list_id, token)
    return 0


if __name__ == "__main__":
    sys.exit(main())
