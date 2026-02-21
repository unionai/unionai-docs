#!/usr/bin/env python3
"""Check internal cross-page links in Hugo source content.

Scans content/ markdown files, resolves relative links against Hugo's routing
rules, and reports broken links per variant.  Also enforces link notation
standards (no .md extension, explicit _index for section references, etc.).

Usage:
    python tools/link_checker/check_internal_links.py [--variant byoc] [--exclude-file .link-checker-exclude]
"""

import argparse
import re
import sys
from pathlib import Path

VARIANTS = ["flyte", "byoc", "serverless", "selfmanaged"]
CONTENT_DIR = Path("content")


def parse_variants(content: str) -> dict[str, bool]:
    """Parse variants: frontmatter line into a dict of variant -> included."""
    # Extract YAML frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return {}

    for line in fm_match.group(1).splitlines():
        line = line.strip()
        if line.startswith("variants:"):
            tokens = line[len("variants:"):].strip().split()
            result = {}
            for token in tokens:
                if token.startswith("+"):
                    result[token[1:]] = True
                elif token.startswith("-"):
                    result[token[1:]] = False
            return result
    return {}


def build_page_index(content_dir: Path) -> dict[str, dict[str, set[str]]]:
    """Build per-variant page index.

    Returns:
        Dict mapping variant -> set of Hugo-style page paths (relative to content/).
        Each path is the "route" Hugo would assign, e.g. "user-guide/quickstart".
    """
    variant_pages: dict[str, set[str]] = {v: set() for v in VARIANTS}
    page_files: dict[str, Path] = {}  # route -> file path

    for md_file in sorted(content_dir.rglob("*.md")):
        rel = md_file.relative_to(content_dir)

        # Skip __docs_builder__ internal files
        if str(rel).startswith("__docs_builder__"):
            continue

        try:
            text = md_file.read_text(encoding="utf-8")
        except Exception:
            continue

        variants = parse_variants(text)

        # Compute the Hugo route for this file
        if md_file.name == "_index.md":
            # Section page: route is the directory
            route = str(rel.parent)
        else:
            # Leaf page: route is path without .md
            route = str(rel.with_suffix(""))

        # Normalize: "." becomes ""
        if route == ".":
            route = ""

        page_files[route] = md_file

        for v in VARIANTS:
            if variants.get(v, False):
                variant_pages[v].add(route)

    return variant_pages, page_files


def title_to_anchor(title: str) -> str:
    """Convert heading title to URL anchor format matching Hugo's behavior.

    Mirrors the algorithm in tools/llms_generator/build_llm_docs.py.
    """
    anchor = title.lower()
    # Remove special chars except alphanumeric, spaces, underscores, hyphens
    anchor = re.sub(r"[^a-zA-Z0-9\s_-]", "", anchor)
    # Replace whitespace with hyphens
    anchor = re.sub(r"\s", "-", anchor.strip())
    return anchor


def extract_headings(content: str) -> set[str]:
    """Extract all heading anchors from markdown content.

    Handles Hugo's duplicate-anchor suffixing (-1, -2, etc.).
    """
    # Strip YAML frontmatter
    fm_match = re.match(r"^---\s*\n.*?\n---\s*\n?", content, re.DOTALL)
    if fm_match:
        content = content[fm_match.end():]

    anchors = set()
    anchor_counts: dict[str, int] = {}

    for match in re.finditer(r"^#{1,6}\s+(.+?)(?:\s+\{#([^}]+)\})?\s*$", content, re.MULTILINE):
        heading_text = match.group(1).strip()
        custom_id = match.group(2)

        if custom_id:
            anchor = custom_id
        else:
            anchor = title_to_anchor(heading_text)

        if not anchor:
            continue

        # Handle duplicate anchors (Hugo appends -1, -2, etc.)
        if anchor in anchor_counts:
            anchor_counts[anchor] += 1
            suffixed = f"{anchor}-{anchor_counts[anchor]}"
            anchors.add(suffixed)
        else:
            anchor_counts[anchor] = 0
            anchors.add(anchor)

    return anchors


def extract_headings_from_file(file_path: Path) -> set[str]:
    """Extract heading anchors from a file."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return set()
    return extract_headings(content)


def extract_links(content: str) -> list[tuple[int, str, str]]:
    """Extract markdown links from content.

    Returns list of (line_number, link_text, link_url).
    Skips links inside Hugo shortcodes and code blocks.
    """
    links = []

    # Strip YAML frontmatter for line counting accuracy
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", content, re.DOTALL)
    fm_lines = 0
    body = content
    if fm_match:
        fm_lines = content[:fm_match.end()].count("\n")
        body = content[fm_match.end():]

    # Remove fenced code blocks to avoid false positives
    body_no_code = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), body, flags=re.DOTALL)

    # Remove inline code
    body_no_code = re.sub(r"`[^`]+`", "", body_no_code)

    # Pattern for markdown links, but not images
    link_pattern = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)")

    for match in link_pattern.finditer(body_no_code):
        line_num = fm_lines + body_no_code[:match.start()].count("\n") + 1
        link_text = match.group(1)
        link_url = match.group(2).strip()
        links.append((line_num, link_text, link_url))

    return links


def classify_link(url: str) -> str:
    """Classify a link URL.

    Returns one of: 'skip', 'external', 'absolute', 'anchor', 'relative'.
    """
    # Skip links containing Hugo shortcodes (not resolvable at source level)
    if "{{" in url:
        return "skip"

    # External links
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url):
        return "external"

    # Absolute paths within the docs
    if url.startswith("/"):
        return "absolute"

    # Anchor-only
    if url.startswith("#"):
        return "anchor"

    return "relative"


def resolve_relative_link(link_path: str, source_file: Path, content_dir: Path,
                          variant_pages: set[str], page_files: dict[str, Path]) -> tuple[bool, str, Path | None]:
    """Resolve a relative link and check if it exists in the given variant.

    Returns:
        (is_valid, error_message, target_file_path)
    """
    # Split off anchor
    parts = link_path.split("#", 1)
    file_part = parts[0]
    anchor = parts[1] if len(parts) > 1 else None

    source_dir = source_file.parent

    # Handle empty file_part (anchor-only was already classified separately)
    if not file_part:
        # This shouldn't happen since anchor-only is classified separately,
        # but handle defensively
        return True, "", source_file

    # Resolve the path
    # Handle .md extension links
    has_md_ext = file_part.endswith(".md")

    if has_md_ext:
        # Direct .md file reference
        target_path = (source_dir / file_part).resolve()

        if not target_path.is_file():
            return False, f"file not found: {file_part}", None

        rel_to_content = target_path.relative_to(content_dir.resolve())

        # Compute Hugo route: _index.md -> directory, other.md -> path without suffix
        if target_path.name == "_index.md":
            route = str(rel_to_content.parent)
            if route == ".":
                route = ""
        else:
            route = str(rel_to_content.with_suffix(""))

        if route not in variant_pages:
            return False, f"page not in variant: {file_part}", None

        # Validate anchor if present
        if anchor:
            headings = extract_headings_from_file(target_path)
            if anchor not in headings:
                return False, f"anchor #{anchor} not found in {file_part}", target_path

        return True, "", target_path

    # Skip links to non-markdown files (images, static assets)
    # These are not page links — they're handled by Hugo/the browser directly
    non_page_exts = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".pdf",
                     ".ico", ".css", ".js", ".json", ".yaml", ".yml", ".toml",
                     ".txt", ".csv", ".zip", ".tar", ".gz", ".ipynb"}
    if Path(file_part).suffix.lower() in non_page_exts:
        return True, "", None

    # Extensionless link - resolve via Hugo rules
    # Normalize trailing slash: ./section/ -> ./section
    clean_path = file_part.rstrip("/")

    # Handle explicit _index references: resolve to section directory
    is_index_ref = False
    if clean_path == "_index":
        clean_path = "."
        is_index_ref = True
    elif clean_path.endswith("/_index"):
        clean_path = clean_path[:-len("/_index")]
        is_index_ref = True

    # Handle "." from leaf pages: render hook resolves to self, not section index.
    # But if this is an _index reference (e.g. bare "_index"), resolve to section.
    if clean_path in (".", "./") and source_file.name != "_index.md" and not is_index_ref:
        # "." from a leaf page means "this page" (matching render hook behavior)
        if anchor:
            headings = extract_headings_from_file(source_file)
            if anchor not in headings:
                return False, f"anchor #{anchor} not found (in self)", source_file
        return True, "", source_file

    resolved = (source_dir / clean_path).resolve()

    try:
        rel_to_content = resolved.relative_to(content_dir.resolve())
    except ValueError:
        return False, f"resolves outside content/: {file_part}", None

    route = str(rel_to_content)

    # Normalize: "." becomes ""
    if route == ".":
        route = ""

    # Check if route exists in variant pages
    if route in variant_pages:
        target = page_files.get(route)
        if anchor and target:
            headings = extract_headings_from_file(target)
            if anchor not in headings:
                return False, f"anchor #{anchor} not found in {file_part}", target
        return True, "", target

    # Not found in variant
    # Check if it exists in any variant (helps with error messages)
    if route in page_files:
        return False, f"page exists but not in this variant: {file_part}", None

    return False, f"page not found: {file_part} (resolved to {route})", None


def lint_link(link_url: str, link_text: str, source_file: Path, content_dir: Path,
              page_files: dict[str, Path], target_file: Path | None) -> str | None:
    """Check link notation standards.  Returns an error message or None if OK."""
    file_part = link_url.split("#", 1)[0]

    # Rule 1: No .md extension in links
    if ".md" in file_part:
        fixed = link_url.replace(".md", "")
        return (f"remove .md extension from link: [{link_text}]({link_url})\n"
                f"    fix: [{link_text}]({fixed})")

    # Rule 2: No .#anchor or ./#anchor (ambiguous)
    if source_file.name != "_index.md":
        if file_part in (".", "./"):
            anchor_part = link_url.split("#", 1)
            if len(anchor_part) > 1:
                return (f"ambiguous .#anchor from leaf page: [{link_text}]({link_url})\n"
                        f"    fix: use [{link_text}](#{anchor_part[1]}) for self-anchor"
                        f" or [{link_text}](_index#{anchor_part[1]}) for section index")

    # Rule 3: Resolved target is _index.md but link doesn't use _index
    if target_file and target_file.name == "_index.md" and "_index" not in link_url:
        # Compute the suggested fix - preserve original prefix (e.g. ./ or ../)
        clean = file_part.rstrip("/")
        if clean in (".", "./", ""):
            suggested = "_index"
        else:
            suggested = clean + "/_index"
        # Preserve anchor
        anchor_part = link_url.split("#", 1)
        if len(anchor_part) > 1:
            suggested += f"#{anchor_part[1]}"
        return (f"link to section page should use explicit _index: [{link_text}]({link_url})\n"
                f"    fix: [{link_text}]({suggested})")

    # Rule 4: Bare relative name without ./ prefix
    if (file_part and
            not file_part.startswith("./") and
            not file_part.startswith("../") and
            not file_part.startswith("_index") and
            not file_part.startswith("/") and
            "/" not in file_part and
            not file_part.startswith(".")):
        return (f"use ./ prefix for relative links: [{link_text}]({link_url})\n"
                f"    fix: [{link_text}](./{link_url})")

    return None


def load_exclude_patterns(exclude_file: Path) -> list[re.Pattern]:
    """Load exclusion patterns from file.

    Each non-empty, non-comment line is a regex pattern matched against
    the string "source_file:link_url".
    """
    patterns = []
    if not exclude_file.is_file():
        return patterns

    for line in exclude_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            patterns.append(re.compile(line))
        except re.error as e:
            print(f"Warning: invalid exclude pattern '{line}': {e}", file=sys.stderr)

    return patterns


def is_excluded(source_rel: str, link_url: str, exclude_patterns: list[re.Pattern]) -> bool:
    """Check if a link should be excluded from reporting."""
    check_str = f"{source_rel}:{link_url}"
    return any(p.search(check_str) for p in exclude_patterns)


def check_variant(variant: str, content_dir: Path, variant_pages: dict[str, set[str]],
                  page_files: dict[str, Path], exclude_patterns: list[re.Pattern]) -> list[str]:
    """Check all internal links for a single variant.

    Returns list of error messages.
    """
    errors = []
    pages = variant_pages[variant]

    for route in sorted(pages):
        source_file = page_files.get(route)
        if not source_file:
            continue

        # Skip api-reference (auto-generated, has render hook passthrough)
        source_rel = str(source_file.relative_to(content_dir))
        if source_rel.startswith("api-reference"):
            continue

        try:
            content = source_file.read_text(encoding="utf-8")
        except Exception:
            continue

        links = extract_links(content)

        for line_num, link_text, link_url in links:
            link_type = classify_link(link_url)

            if link_type in ("skip", "external", "absolute"):
                continue

            if is_excluded(source_rel, link_url, exclude_patterns):
                continue

            if link_type == "anchor":
                # Check anchor exists in current file
                headings = extract_headings(content)
                anchor = link_url[1:]  # Strip leading #
                if anchor and anchor not in headings:
                    errors.append(
                        f"  {source_rel}:{line_num}: anchor #{anchor} not found"
                        f" [{link_text}]({link_url})"
                    )
                continue

            # Relative link — resolve and validate
            is_valid, err_msg, target_file = resolve_relative_link(
                link_url, source_file, content_dir, pages, page_files
            )

            if not is_valid:
                errors.append(
                    f"  {source_rel}:{line_num}: {err_msg}"
                    f" [{link_text}]({link_url})"
                )
                continue

            # Lint: check notation standards
            lint_msg = lint_link(link_url, link_text, source_file, content_dir,
                                page_files, target_file)
            if lint_msg:
                errors.append(f"  {source_rel}:{line_num}: {lint_msg}")

    return errors


def get_version_from_makefile_inc() -> str | None:
    """Read VERSION from makefile.inc (e.g. 'v1', 'v2')."""
    inc = Path("makefile.inc")
    if not inc.is_file():
        return None
    for line in inc.read_text().splitlines():
        line = line.strip()
        if line.startswith("VERSION") and ":=" in line:
            return line.split(":=", 1)[1].strip()
    return None


def main():
    parser = argparse.ArgumentParser(description="Check internal links in Hugo source content.")
    parser.add_argument("--variant", choices=VARIANTS, help="Check a single variant (default: all)")
    parser.add_argument("--exclude-file", type=Path, default=Path(".link-checker-exclude"),
                        help="File with exclusion patterns (default: .link-checker-exclude)")
    parser.add_argument("--content-dir", type=Path, default=CONTENT_DIR,
                        help="Content directory (default: content)")
    args = parser.parse_args()

    content_dir = args.content_dir
    if not content_dir.is_dir():
        print(f"Error: content directory not found: {content_dir}", file=sys.stderr)
        return 1

    # Build page index
    variant_pages, page_files = build_page_index(content_dir)

    # Load exclusion patterns (shared + version-specific if it exists)
    exclude_patterns = load_exclude_patterns(args.exclude_file)
    version = get_version_from_makefile_inc()
    if version:
        version_exclude = args.exclude_file.with_suffix(f".{version}")
        exclude_patterns.extend(load_exclude_patterns(version_exclude))

    # Determine which variants to check
    variants_to_check = [args.variant] if args.variant else VARIANTS

    total_errors = 0
    for variant in variants_to_check:
        errors = check_variant(variant, content_dir, variant_pages, page_files, exclude_patterns)
        if errors:
            print(f"\n{variant}: {len(errors)} error(s)")
            for err in errors:
                print(err)
            total_errors += len(errors)
        else:
            print(f"{variant}: all links OK")

    if total_errors:
        print(f"\nTotal: {total_errors} error(s) found")
        return 1

    print("\nAll internal links are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
