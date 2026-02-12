#!/usr/bin/env python3
"""
Simple script to build consolidated LLM-optimized documents by following ## Subpages links
in depth-first order starting from md/index.md.

Usage: python build_llm_docs.py
"""

import os
import re
import subprocess
from pathlib import Path
from typing import Set, List

class LLMDocBuilder:
    def __init__(self, base_path: Path, quiet: bool = False):
        self.base_path = base_path
        self.quiet = quiet
        self.visited_files: Set[str] = set()
        self.title_lookup: dict[str, str] = {}  # Maps file paths to hierarchical titles
        self.version = self._detect_version()
        self.resolution_issues: List[dict] = []  # Track failed link resolutions
        self.current_source_file: str = ""  # Track current file being processed
        self.variant_root: Path = Path()  # Set per-variant in build_consolidated_doc
        self.index_entries: List[tuple] = []  # (hierarchical_title, page_url) for index

    def _detect_version(self) -> str:
        """Detect version from environment or makefile.inc."""
        # Check environment variable first (set by Makefile)
        version = os.environ.get('VERSION')
        if version:
            return version

        # Read from makefile.inc as fallback
        makefile_inc = self.base_path / 'makefile.inc'
        if makefile_inc.exists():
            try:
                with open(makefile_inc, 'r') as f:
                    for line in f:
                        if line.startswith('VERSION :='):
                            return line.split(':=')[1].strip()
            except Exception:
                pass

        # Default fallback
        return 'v2'

    def run_make_dist(self) -> bool:
        """Run make dist to regenerate all documentation variants."""
        if not self.quiet:
            print("Running 'make dist' to regenerate documentation...")
        try:
            result = subprocess.run(['make', 'dist'],
                                  cwd=self.base_path,
                                  capture_output=True,
                                  text=True,
                                  timeout=300)
            if result.returncode == 0:
                if not self.quiet:
                    print("Successfully regenerated documentation")
                return True
            else:
                print(f"Error: Make dist failed with return code {result.returncode}")
                return False
        except Exception as e:
            print(f"Error running make dist: {e}")
            return False

    def read_file_content(self, file_path: Path) -> str:
        """Read and clean markdown file content."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Transform source file references to GitHub URLs
            def transform_source_ref(match):
                source_line = match.group(0)
                # Replace /external/unionai-examples with GitHub URL
                transformed = source_line.replace('/external/unionai-examples', 'https://github.com/unionai/unionai-examples/blob/main')
                # Remove all asterisks and make it more explicit with parentheses
                transformed = transformed.replace('*Source:', '(Source code for the above example:')
                transformed = transformed.replace('*', ')')  # Replace trailing asterisk with closing parenthesis
                return transformed

            content = re.sub(r'\*Source: /external/unionai-examples[^\*]*\*', transform_source_ref, content)

            # Move source references directly after code blocks (remove blank line between them)
            content = re.sub(r'```\n\n\(Source code for the above example:', '```\n(Source code for the above example:', content)

            # Remove any other footer metadata section that might remain
            content = re.sub(r'\n---\n\*\*Source\*\*:.*?(?=\n\n|\Z)', '', content, flags=re.DOTALL)

            # This will be updated in process_page_depth_first to pass hierarchy
            # content = self.process_internal_links(content, file_path, hierarchy)

            # Clean up excessive whitespace but preserve structure
            content = content.rstrip() + '\n'

            return content
        except Exception as e:
            print(f"❌ Error reading {file_path}: {e}")
            return ""

    def process_internal_links(self, content: str, current_file_path: Path, current_hierarchy: List[str]) -> str:
        """Convert internal documentation links to hierarchical bold references."""
        def replace_internal_link(match):
            text = match.group(1)
            url = match.group(2)

            # Keep external links unchanged
            if url.startswith(('http://', 'https://', 'mailto:')):
                return match.group(0)

            # Convert same-page anchor links to hierarchical references
            if url.startswith('#'):
                anchor = url[1:]  # Remove the # prefix
                try:
                    rel_path = str(current_file_path.relative_to(self.variant_root)).lower()
                except ValueError:
                    rel_path = current_file_path.name.lower()
                anchor_key = f"{rel_path}#{anchor}"
                if anchor_key in self.title_lookup:
                    hierarchical_title = self.title_lookup[anchor_key]
                    return f"**{hierarchical_title}**"
                # Fallback: use current page hierarchy + link text
                else:
                    current_page_title = self.strip_common_prefix(' > '.join(current_hierarchy))
                    return f"**{current_page_title} > {text}**"

            # For internal content.md links (with or without anchors), convert to hierarchical reference
            if 'content.md' in url and not url.startswith(('http://', 'https://')):
                hierarchical_title = self.resolve_hierarchical_title(url, current_file_path, current_hierarchy, text)
                return f"**{hierarchical_title}**"

            # Keep other links unchanged (absolute paths like /docs/, static files, etc.)
            return match.group(0)

        # Process markdown links
        content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_internal_link, content)
        return content

    def resolve_hierarchical_title(self, url: str, current_file_path: Path, current_hierarchy: List[str], link_text: str) -> str:
        """Resolve hierarchical title using lookup table."""
        # Resolve the target file path
        target_path = self.resolve_link_path(url, current_file_path)

        # Look up in our title mapping
        if target_path in self.title_lookup:
            title = self.title_lookup[target_path]
            # Skip "Documentation > {VARIANT}" prefix
            return self.strip_common_prefix(title)

        # Fallback: use current hierarchy + link text (also strip prefix)
        # Track this as a resolution failure
        if current_hierarchy:
            full_title = f"{' > '.join(current_hierarchy)} > {link_text}"
            fallback_title = self.strip_common_prefix(full_title)
        else:
            fallback_title = link_text

        # Record the resolution failure
        self.resolution_issues.append({
            'source_file': self.current_source_file,
            'link_url': url,
            'link_text': link_text,
            'resolved_path': target_path,
            'fallback_title': fallback_title,
        })

        return fallback_title

    def strip_common_prefix(self, title: str) -> str:
        """Remove 'Documentation > {variant}' prefix from hierarchical titles."""
        parts = title.split(' > ')
        # Skip first two parts if they match the expected pattern
        if len(parts) >= 2 and parts[0] == 'Documentation':
            return ' > '.join(parts[2:]) if len(parts) > 2 else parts[-1]
        return title

    def resolve_link_path(self, url: str, current_file_path: Path) -> str:
        """Resolve a relative URL to an absolute path key."""
        # Split URL and anchor
        if '#' in url:
            file_part, anchor = url.split('#', 1)
        else:
            file_part, anchor = url, None

        try:
            # Handle relative paths
            if file_part.startswith('../') or file_part.startswith('./'):
                resolved = (current_file_path.parent / file_part).resolve()
            elif file_part:  # Non-empty file part
                resolved = (current_file_path.parent / file_part).resolve()
            else:  # Just anchor, same file
                resolved = current_file_path

            # Get path relative to variant root (matches our lookup table keys)
            try:
                key = str(resolved.relative_to(self.variant_root)).lower()
            except ValueError:
                # Fallback to filename only
                key = str(resolved.name).lower()

            if anchor:
                key = f"{key}#{anchor}"

            return key
        except:
            return url.lower()

    def extract_page_title(self, content: str, file_path: Path) -> str:
        """Extract the main title from a markdown page."""
        # Look for the first # title
        title_match = re.search(r'^#\s+(.+?)\s*$', content, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()

        # Fallback to filename
        name = file_path.stem
        if name in ('index', 'content'):
            name = file_path.parent.name
        return name.replace('-', ' ').replace('_', ' ').title()

    def parse_heading_hierarchy(self, content: str, file_path: Path, page_hierarchy: List[str]) -> dict[str, str]:
        """Parse all headings and build anchor lookup table."""
        anchor_map = {}

        # Find all markdown headings
        heading_pattern = r'^(#{1,6})\s+(.+?)\s*$'
        headings = []

        for match in re.finditer(heading_pattern, content, re.MULTILINE):
            level = len(match.group(1))  # Number of # characters
            title = match.group(2).strip()
            anchor = self.title_to_anchor(title)
            headings.append((level, title, anchor))

        # Build hierarchical structure
        heading_stack = []  # Stack to track current hierarchy

        for level, title, anchor in headings:
            # Skip the main page title (# heading) since it's already in page_hierarchy
            if level == 1:
                heading_stack = [(level, title)]  # Reset stack with main title
                # Don't add to anchor_map for level 1 headings since they duplicate page title
                continue

            # Pop headings that are at same or deeper level
            while heading_stack and heading_stack[-1][0] >= level:
                heading_stack.pop()

            # Add current heading to stack
            heading_stack.append((level, title))

            # Build full hierarchical title - skip the first heading in stack (main title)
            heading_hierarchy = [h[1] for h in heading_stack[1:]]  # Skip first element
            full_hierarchy = page_hierarchy + heading_hierarchy
            hierarchical_title = ' > '.join(full_hierarchy)

            # Store in anchor map (strip common prefix)
            clean_title = self.strip_common_prefix(hierarchical_title)
            anchor_map[anchor] = clean_title

        return anchor_map

    def title_to_anchor(self, title: str) -> str:
        """Convert heading title to URL anchor format matching Hugo's behavior."""
        anchor = title.lower()
        # Remove special chars except alphanumeric, spaces, underscores, hyphens
        # Hugo removes chars like () but keeps spaces which become hyphens
        anchor = re.sub(r'[^a-zA-Z0-9\s_-]', '', anchor)
        # Replace whitespace with hyphens (each space becomes one hyphen)
        anchor = re.sub(r'\s', '-', anchor.strip())
        return anchor

    def extract_subpage_links(self, content: str) -> List[str]:
        """Extract links from ## Subpages section."""
        # Find the ## Subpages section
        subpages_pattern = r'## Subpages\s*\n(.*?)(?=\n##|\n---|\Z)'
        match = re.search(subpages_pattern, content, re.DOTALL | re.IGNORECASE)

        if not match:
            return []

        subpages_content = match.group(1).strip()

        # Extract markdown links
        links = []
        link_pattern = r'- \[([^\]]+)\]\(([^)]+)\)'

        for link_match in re.finditer(link_pattern, subpages_content):
            link_url = link_match.group(2)
            # Clean the URL (remove anchors, etc.)
            link_url = link_url.split('#')[0].strip()
            if link_url and not link_url.startswith(('http://', 'https://')):
                links.append(link_url)

        return links

    def build_consolidated_doc(self, variant: str, version: str = None) -> str:
        """Build consolidated document by following subpage links depth-first."""
        version = version or self.version
        variant_dir = self.base_path / 'dist' / 'docs' / version / variant

        if not variant_dir.exists():
            print(f"Error: Directory not found: {variant_dir}")
            return ""

        self.variant_root = variant_dir

        # Reset state for this variant
        self.resolution_issues.clear()
        self.index_entries.clear()
        self.current_source_file = ""

        if not self.quiet:
            print(f"Building consolidated document for {variant}")

        # First pass: Build lookup tables for all pages
        if not self.quiet:
            print("  First pass: Building lookup tables...")
        self.visited_files.clear()  # Reset for first pass
        self.build_lookup_tables(variant_dir, 'content.md', variant_dir, [])

        # Second pass: Process content with lookup tables populated
        if not self.quiet:
            print("  Second pass: Processing content...")
        consolidated_content = []
        self.process_page_depth_first(variant_dir, 'content.md', consolidated_content, variant_dir, [], variant, version)

        return '\n'.join(consolidated_content)

    def write_resolution_report(self, variant: str, version: str = None) -> Path:
        """Write a report of link resolution issues to a file."""
        version = version or self.version
        report_file = self.base_path / 'dist' / 'docs' / version / variant / 'link-issues.txt'

        with open(report_file, 'w', encoding='utf-8') as f:
            if self.resolution_issues:
                f.write(f"Found {len(self.resolution_issues)} link resolution issues:\n\n")
                for issue in self.resolution_issues:
                    f.write(f"{issue['source_file']}: Link [{issue['link_text']}]({issue['link_url']}) -> "
                           f"could not resolve, used fallback: \"{issue['fallback_title']}\"\n")
            else:
                f.write("No link resolution issues found.\n")

        return report_file

    def build_lookup_tables(self, base_dir: Path, relative_path: str, md_root: Path, hierarchy: List[str] = None):
        """Build lookup tables for all pages without processing content."""
        if hierarchy is None:
            hierarchy = []

        # Resolve the full path — every page is {dir}/content.md
        if relative_path.endswith('/'):
            file_path = base_dir / relative_path / 'content.md'
            relative_path = relative_path + 'content.md'
        elif relative_path.endswith('content.md'):
            file_path = base_dir / relative_path
        else:
            # Relative path is a directory name, look for content.md inside
            if (base_dir / relative_path / 'content.md').exists():
                file_path = base_dir / relative_path / 'content.md'
                relative_path = f"{relative_path}/content.md"
            else:
                if not self.quiet:
                    print(f"Warning: Could not find content.md for: {relative_path}")
                return

        # Avoid infinite loops
        canonical_path = str(file_path.resolve())
        if canonical_path in self.visited_files:
            return
        self.visited_files.add(canonical_path)

        if not file_path.exists():
            if not self.quiet:
                print(f"Warning: File not found: {file_path}")
            return

        # Get relative path from variant root for the lookup key
        # Normalize to lowercase for case-insensitive matching (macOS filesystem is case-insensitive)
        try:
            relative_from_root = str(file_path.relative_to(md_root)).lower()
        except ValueError:
            relative_from_root = str(file_path).lower()

        # Read the raw content
        raw_content = self.read_file_content(file_path)
        if not raw_content.strip():
            return

        # Extract page title and build hierarchy
        page_title = self.extract_page_title(raw_content, file_path)
        current_hierarchy = hierarchy + [page_title]
        hierarchical_title = ' > '.join(current_hierarchy)

        # Store page in lookup table (keys normalized to lowercase)
        self.title_lookup[relative_from_root] = hierarchical_title

        # Parse and store heading hierarchy for anchor links
        anchor_map = self.parse_heading_hierarchy(raw_content, file_path, current_hierarchy)
        for anchor, anchor_title in anchor_map.items():
            anchor_key = f"{relative_from_root}#{anchor}"
            self.title_lookup[anchor_key] = anchor_title

        # Extract subpages and recursively build lookup tables
        subpage_links = self.extract_subpage_links(raw_content)
        for link in subpage_links:
            # Resolve relative to the current file's directory
            current_dir = file_path.parent
            self.build_lookup_tables(current_dir, link, md_root, current_hierarchy)

    def process_page_depth_first(self, base_dir: Path, relative_path: str,
                                consolidated: List[str], md_root: Path, hierarchy: List[str] = None,
                                variant: str = None, version: str = None):
        """Process a page and its subpages in depth-first order."""

        if hierarchy is None:
            hierarchy = []

        # Resolve the full path — every page is {dir}/content.md
        if relative_path.endswith('/'):
            file_path = base_dir / relative_path / 'content.md'
            relative_path = relative_path + 'content.md'
        elif relative_path.endswith('content.md'):
            file_path = base_dir / relative_path
        else:
            # Relative path is a directory name, look for content.md inside
            if (base_dir / relative_path / 'content.md').exists():
                file_path = base_dir / relative_path / 'content.md'
                relative_path = f"{relative_path}/content.md"
            else:
                if not self.quiet:
                    print(f"Warning: Could not find content.md for: {relative_path}")
                return

        if not file_path.exists():
            if not self.quiet:
                print(f"Warning: File not found: {file_path}")
            return

        # Get relative path from variant root for the delimiter
        try:
            relative_from_root = str(file_path.relative_to(md_root))
        except ValueError:
            relative_from_root = str(file_path)

        if not self.quiet:
            print(f"  Processing: {relative_from_root}")

        # Track current source file for resolution issue reporting
        self.current_source_file = relative_from_root

        # Read the raw content
        raw_content = self.read_file_content(file_path)
        if not raw_content.strip():
            return

        # Extract page title and build hierarchy (for current processing)
        page_title = self.extract_page_title(raw_content, file_path)
        current_hierarchy = hierarchy + [page_title]

        # Extract subpages BEFORE processing links
        subpage_links = self.extract_subpage_links(raw_content)

        # Process internal links with lookup tables populated
        content = self.process_internal_links(raw_content, file_path, current_hierarchy)

        # Add page delimiter with URL
        if variant and version:
            # Convert content.md path to web path
            web_path = relative_from_root.replace('/content.md', '').replace('content.md', '')
            if not web_path or web_path == '/':
                web_path = ''

            url = f"https://www.union.ai/docs/{version}/{variant}/{web_path}".rstrip('/')
            consolidated.append(f"\n=== PAGE: {url} ===\n")

            # Collect index entry
            stripped_title = self.strip_common_prefix(' > '.join(current_hierarchy))
            llm_url = f"{url}/content.md" if web_path else f"{url}/content.md"
            self.index_entries.append((stripped_title, llm_url))
        else:
            consolidated.append(f"\n=== PAGE: {relative_from_root} ===\n")
        consolidated.append(content)

        # Process subpages depth-first
        for link in subpage_links:
            if not self.quiet:
                print(f"    Following: {link}")
            # Resolve relative to the current file's directory
            current_dir = file_path.parent
            self.process_page_depth_first(current_dir, link, consolidated, md_root, current_hierarchy, variant, version)

    def find_variants(self) -> List[str]:
        """Find available variants in the dist directory."""
        dist_path = self.base_path / "dist" / "docs" / self.version
        if not dist_path.exists():
            return []

        variants = []
        for item in dist_path.iterdir():
            if item.is_dir() and (item / 'content.md').exists():
                variants.append(item.name)

        return sorted(variants)

    def create_index_content(self, variant: str) -> str:
        """Create a compact page index with absolute URLs for llms.txt."""
        variant_names = {
            'flyte': 'Flyte Open Source',
            'byoc': 'Union.ai BYOC (Bring Your Own Cloud)',
            'selfmanaged': 'Union.ai Self-managed',
            'serverless': 'Union.ai Serverless'
        }

        variant_display = variant_names.get(variant, variant.title())
        base_url = f"https://www.union.ai/docs/{self.version}/{variant}"

        lines = [
            f"# {variant_display} Documentation",
            f"> Full documentation (single file): {base_url}/llms-full.txt",
            f"> Site: {base_url}",
            "",
            "## Pages",
        ]

        for title, url in self.index_entries:
            lines.append(f"{title}|{url}")

        lines.append("")
        return '\n'.join(lines)

    def create_discovery_files(self, base_path: Path, variants: List[str]) -> None:
        """Create hierarchical discovery files for LLM documentation."""

        # Root level discovery file (/docs/llms.txt)
        root_content = self.create_root_discovery_content()
        root_file = base_path / 'dist' / 'docs' / 'llms.txt'

        with open(root_file, 'w', encoding='utf-8') as f:
            f.write(root_content)
        if not self.quiet:
            print(f"Created root discovery: {root_file}")

        # Version level discovery file
        version_content = self.create_version_discovery_content(variants, self.version)
        version_file = base_path / 'dist' / 'docs' / self.version / 'llms.txt'

        with open(version_file, 'w', encoding='utf-8') as f:
            f.write(version_content)
        if not self.quiet:
            print(f"Created {self.version} discovery: {version_file}")

    def create_root_discovery_content(self) -> str:
        """Create content for the root-level discovery file."""
        base = "https://www.union.ai/docs"
        lines = [
            "# Union.ai Documentation",
            f"> Current version: {self.version}",
            "",
            "## Versions",
            f"{self.version}|{base}/{self.version}/llms.txt",
            "",
        ]
        return '\n'.join(lines)

    def create_version_discovery_content(self, variants: List[str], version: str) -> str:
        """Create content for version-level discovery file."""
        base = f"https://www.union.ai/docs/{version}"
        lines = [
            f"# Union.ai {version.upper()} Documentation",
            "",
            "## Variants",
        ]
        for variant in sorted(variants):
            lines.append(f"{variant}|{base}/{variant}/llms.txt")
        lines.append("")
        return '\n'.join(lines)

    def get_current_timestamp(self) -> str:
        """Get current timestamp for documentation."""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

def main():
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Build LLM-optimized documentation')
    parser.add_argument('--no-make-dist', action='store_true', help='Skip running make dist')
    parser.add_argument('--quiet', '-q', action='store_true', help='Suppress progress output')
    args = parser.parse_args()

    base_path = Path.cwd()
    builder = LLMDocBuilder(base_path, quiet=args.quiet)

    # Step 1: Regenerate documentation (skip if --no-make-dist is passed)
    if not args.no_make_dist and not builder.run_make_dist():
        return 1

    # Step 2: Find variants
    variants = builder.find_variants()
    if not variants:
        print("Error: No variants found")
        return 1

    if not args.quiet:
        print(f"Found variants: {variants}")

    # Step 3: Build consolidated documents
    for variant in variants:
        consolidated_content = builder.build_consolidated_doc(variant)

        if consolidated_content.strip():
            # Create output file
            output_file = base_path / 'dist' / 'docs' / builder.version / variant / 'llms-full.txt'

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(consolidated_content)

            if not args.quiet:
                file_size = len(consolidated_content)
                print(f"Saved: {output_file} ({file_size:,} characters)")

            # Create llms.txt page index
            redirect_file = base_path / 'dist' / 'docs' / builder.version / variant / 'llms.txt'
            redirect_content = builder.create_index_content(variant)

            with open(redirect_file, 'w', encoding='utf-8') as f:
                f.write(redirect_content)

            if not args.quiet:
                print(f"Created redirect: {redirect_file}")

            # Write resolution issues report
            report_file = builder.write_resolution_report(variant)
            issue_count = len(builder.resolution_issues)
            if issue_count > 0:
                print(f"Found {issue_count} link resolution issues for {variant}:")
                for issue in builder.resolution_issues[:10]:  # Show first 10
                    print(f"  {issue['source_file']}: [{issue['link_text']}]({issue['link_url']})")
                if issue_count > 10:
                    print(f"  ... and {issue_count - 10} more issues")
                print(f"  Full list: {report_file}")
            elif not args.quiet:
                print(f"No link resolution issues for {variant}")
        else:
            print(f"Error: No content generated for {variant}")

    # Step 4: Create hierarchical discovery files
    builder.create_discovery_files(base_path, variants)

    return 0

if __name__ == '__main__':
    exit(main())