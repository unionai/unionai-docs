#!/usr/bin/env python3

# Quick test of the link processing function
import re

def build_hierarchical_title(url: str, current_path: str, link_text: str) -> str:
    """Build a hierarchical title from URL path."""
    # Clean the URL
    clean_url = url.replace('../', '').replace('./', '').replace('.md', '')

    # Handle index files
    if clean_url.endswith('/index'):
        clean_url = clean_url.replace('/index', '')

    # Split into path segments
    segments = [seg for seg in clean_url.split('/') if seg]

    if not segments:
        return link_text

    # Build hierarchical title
    title_parts = []
    for segment in segments:
        # Convert kebab-case and snake_case to title case
        part = segment.replace('-', ' ').replace('_', ' ').title()
        title_parts.append(part)

    # Use the original link text for the final part if it's more descriptive
    if len(title_parts) > 0 and link_text.strip() and link_text != title_parts[-1]:
        title_parts[-1] = link_text.strip()

    return ' > '.join(title_parts)

# Test cases
test_links = [
    ("[Getting started](../getting-started/index.md)", "user-guide/flyte-2/index.md"),
    ("[Local setup](local-setup.md)", "user-guide/getting-started/index.md"),
    ("[Flyte CLI reference](../../api-reference/flyte-cli.md)", "user-guide/task-configuration/secrets.md"),
    ("[Image object](../../api-reference/flyte-sdk/packages/flyte/image.md)", "user-guide/task-configuration/container-images.md"),
    ("[Secrets](secrets.md)", "user-guide/task-configuration/index.md"),
]

print("Link transformation examples:")
print("=" * 50)

for link_text, current_path in test_links:
    # Extract link components
    match = re.search(r'\[([^\]]+)\]\(([^)]+)\)', link_text)
    if match:
        text = match.group(1)
        url = match.group(2)

        hierarchical = build_hierarchical_title(url, current_path, text)

        print(f"Original: {link_text}")
        print(f"Result:   **{hierarchical}**")
        print()