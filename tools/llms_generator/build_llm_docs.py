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
        self.index_entries: List[tuple] = []  # (hierarchical_title, page_url, path_key) for index
        self.page_headings: dict[str, List[str]] = {}  # path_key -> [H2/H3 heading titles]
        self.section_pages: set[str] = set()  # path_keys of pages that have subpages
        self.bundle_sections: dict[str, str] = {}  # dir_path -> bundle URL (populated by generate_bundles)

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

            # For internal page.md links (with or without anchors), convert to hierarchical reference
            if 'page.md' in url and not url.startswith(('http://', 'https://')):
                hierarchical_title = self.resolve_hierarchical_title(url, current_file_path, current_hierarchy, text)
                return f"**{hierarchical_title}**"

            # Keep other links unchanged (absolute paths like /docs/, static files, etc.)
            return match.group(0)

        # Protect inline code spans from link processing by replacing them with placeholders
        code_spans = []
        def protect_code_span(match):
            code_spans.append(match.group(0))
            return f'\x00CODE{len(code_spans) - 1}\x00'
        content = re.sub(r'`[^`]+`', protect_code_span, content)

        # Process markdown links
        content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_internal_link, content)

        # Restore code spans
        for i, span in enumerate(code_spans):
            content = content.replace(f'\x00CODE{i}\x00', span)

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

    def extract_h2_h3_headings(self, content: str) -> List[str]:
        """Extract H2 and H3 heading titles from content for index/subpage listings."""
        headings = []
        for match in re.finditer(r'^(#{2,3})\s+(.+?)\s*$', content, re.MULTILINE):
            title = match.group(2).strip()
            if title.lower() != 'subpages':
                headings.append(title)
        return headings

    def format_subpage_entry(self, title: str, url: str, headings: List[str],
                             as_index: bool = False) -> str:
        """Format a page entry with H2/H3 headings.

        as_index=True:  Title|url + indented headings (for llms.txt pipe format)
        as_index=False: - [Title](url) + indented headings (for markdown subpage tables)
        """
        if as_index:
            lines = [f"{title}|{url}"]
        else:
            lines = [f"- [{title}]({url})"]
        for heading in headings:
            lines.append(f"  - {heading}")
        return '\n'.join(lines)

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
        self.page_headings.clear()
        self.section_pages.clear()
        self.current_source_file = ""

        if not self.quiet:
            print(f"Building consolidated document for {variant}")

        # First pass: Build lookup tables for all pages
        if not self.quiet:
            print("  First pass: Building lookup tables...")
        self.visited_files.clear()  # Reset for first pass
        self.build_lookup_tables(variant_dir, 'page.md', variant_dir, [])

        # Second pass: Process content with lookup tables populated
        if not self.quiet:
            print("  Second pass: Processing content...")
        consolidated_content = []
        self.process_page_depth_first(variant_dir, 'page.md', consolidated_content, variant_dir, [], variant, version)

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

        # Resolve the full path — every page is {dir}/page.md
        if relative_path.endswith('/'):
            file_path = base_dir / relative_path / 'page.md'
            relative_path = relative_path + 'page.md'
        elif relative_path.endswith('page.md'):
            file_path = base_dir / relative_path
        else:
            # Relative path is a directory name, look for page.md inside
            if (base_dir / relative_path / 'page.md').exists():
                file_path = base_dir / relative_path / 'page.md'
                relative_path = f"{relative_path}/page.md"
            else:
                if not self.quiet:
                    print(f"Warning: Could not find page.md for: {relative_path}")
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

        # Extract H2/H3 headings for index/subpage listings
        h2h3 = self.extract_h2_h3_headings(raw_content)
        self.page_headings[relative_from_root] = h2h3

        # Extract subpages and recursively build lookup tables
        subpage_links = self.extract_subpage_links(raw_content)
        if subpage_links:
            self.section_pages.add(relative_from_root)
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

        # Resolve the full path — every page is {dir}/page.md
        if relative_path.endswith('/'):
            file_path = base_dir / relative_path / 'page.md'
            relative_path = relative_path + 'page.md'
        elif relative_path.endswith('page.md'):
            file_path = base_dir / relative_path
        else:
            # Relative path is a directory name, look for page.md inside
            if (base_dir / relative_path / 'page.md').exists():
                file_path = base_dir / relative_path / 'page.md'
                relative_path = f"{relative_path}/page.md"
            else:
                if not self.quiet:
                    print(f"Warning: Could not find page.md for: {relative_path}")
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
            # Convert page.md path to web path
            web_path = relative_from_root.replace('/page.md', '').replace('page.md', '')
            if not web_path or web_path == '/':
                web_path = ''

            url = f"https://www.union.ai/docs/{version}/{variant}/{web_path}".rstrip('/')
            consolidated.append(f"\n=== PAGE: {url} ===\n")

            # Collect index entry (with path_key for heading lookup)
            stripped_title = self.strip_common_prefix(' > '.join(current_hierarchy))
            llm_url = f"{url}/page.md" if web_path else f"{url}/page.md"
            self.index_entries.append((stripped_title, llm_url, relative_from_root.lower()))
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
            if item.is_dir() and (item / 'page.md').exists():
                variants.append(item.name)

        return sorted(variants)

    def _path_depth(self, path_key: str) -> int:
        """Get the directory depth of a path_key (0 = root page.md)."""
        parts = path_key.replace('page.md', '').strip('/').split('/')
        parts = [p for p in parts if p]
        return len(parts)

    def _frontmatter_title(self, path_key: str) -> str:
        """Extract frontmatter title from the source _index.md file."""
        dir_path = path_key.replace('/page.md', '').replace('page.md', '').strip('/')
        if dir_path:
            source_file = self.base_path / 'content' / dir_path / '_index.md'
        else:
            source_file = self.base_path / 'content' / '_index.md'

        if not source_file.exists():
            return ''

        try:
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()
            match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if match:
                for line in match.group(1).split('\n'):
                    if line.startswith('title:'):
                        return line.split(':', 1)[1].strip().strip('"').strip("'")
        except Exception:
            pass
        return ''

    def create_index_content(self, variant: str) -> str:
        """Create a page index for llms.txt.

        Lists all pages grouped by top-level section, each with
        H2/H3 headings for discoverability.
        """
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
        ]
        if self.version != "v2":
            lines.extend([
                f"> **This is legacy ({self.version}) documentation.** Do not use"
                " unless explicitly asked about this version."
                f" For current documentation, see https://www.union.ai/docs/v2/llms.txt",
                "",
            ])
        lines.extend([
            f"> Full documentation (single file): {base_url}/llms-full.txt",
            f"> Site: {base_url}",
            "",
            "Each entry below is `- [Page title](URL)` followed by the"
            " H2/H3 headings found on that page."
            " Pages link to individual `page.md` files."
            " Sections marked with a \"Section bundle\" link have a `section.md`"
            " that concatenates all pages in the section into a single file"
            " — use it to load an entire section into context at once.",
            "",
        ])

        # Group entries by top-level section
        sections = []
        current_section = None

        for title, url, path_key in self.index_entries:
            depth = self._path_depth(path_key)

            if depth == 0:
                # Root page — skip
                continue
            elif depth == 1:
                # Top-level entry (section or standalone page)
                if current_section is not None:
                    sections.append(current_section)
                current_section = {
                    'title': title,
                    'display_name': self._frontmatter_title(path_key) or title,
                    'url': url,
                    'path_key': path_key,
                    'children': []
                }
            else:
                # Deeper page — belongs to current section
                if current_section is not None:
                    current_section['children'].append((title, url, path_key))

        if current_section is not None:
            sections.append(current_section)

        # Format each section
        for i, section in enumerate(sections):
            if i > 0:
                lines.append("---")
                lines.append("")

            lines.append(f"## {section['display_name']}")
            lines.append("")

            if section['children']:
                for child_title, child_url, child_key in section['children']:
                    # Strip section prefix from title
                    prefix = section['title'] + ' > '
                    relative_title = child_title[len(prefix):] if child_title.startswith(prefix) else child_title

                    headings = self.page_headings.get(child_key, [])
                    entry = self.format_subpage_entry(
                        relative_title, child_url, headings)
                    lines.append(entry)

                    # Add bundle reference if this child has a section bundle
                    child_dir = child_key.replace('/page.md', '').replace('page.md', '').strip('/')
                    if child_dir in self.bundle_sections:
                        lines.append(f"  > Section bundle (all pages): {self.bundle_sections[child_dir]}")

                lines.append("")

            else:
                # Standalone page at top level
                headings = self.page_headings.get(section['path_key'], [])
                entry = self.format_subpage_entry(
                    section['display_name'], section['url'], headings)
                lines.append(entry)
                lines.append("")

        return '\n'.join(lines)

    def enhance_subpage_listings(self, variant: str, version: str = None):
        """Post-process page.md files to enhance ## Subpages sections with H2/H3 headings."""
        version = version or self.version
        variant_dir = self.base_path / 'dist' / 'docs' / version / variant

        for content_file in variant_dir.rglob('page.md'):
            try:
                relative_key = str(content_file.relative_to(variant_dir)).lower()
            except ValueError:
                continue

            if relative_key not in self.section_pages:
                continue

            # This is a section page — enhance its subpage listing
            content = content_file.read_text(encoding='utf-8')

            # Parse existing subpage links
            subpages_pattern = r'## Subpages\s*\n(.*?)(?=\n##|\n---|\Z)'
            match = re.search(subpages_pattern, content, re.DOTALL | re.IGNORECASE)
            if not match:
                continue

            subpages_content = match.group(1).strip()
            link_pattern = r'- \[([^\]]+)\]\(([^)]+)\)'

            enhanced_lines = ["## Subpages\n"]

            for link_match in re.finditer(link_pattern, subpages_content):
                child_title = link_match.group(1)
                child_url = link_match.group(2)
                child_path_part = child_url.split('#')[0].strip()

                if not child_path_part or child_path_part.startswith(('http://', 'https://')):
                    enhanced_lines.append(f"- [{child_title}]({child_url})")
                    continue

                # Resolve child path to get the path key for heading lookup
                if child_path_part.endswith('page.md'):
                    child_path = (content_file.parent / child_path_part).resolve()
                else:
                    child_path = (content_file.parent / child_path_part.rstrip('/') / 'page.md').resolve()

                try:
                    child_key = str(child_path.relative_to(variant_dir)).lower()
                except ValueError:
                    child_key = ""

                headings = self.page_headings.get(child_key, [])
                entry = self.format_subpage_entry(child_title, child_url, headings)
                enhanced_lines.append(entry)

            enhanced_table = '\n'.join(enhanced_lines)

            # Replace the existing ## Subpages section
            new_content = re.sub(subpages_pattern, enhanced_table + '\n', content,
                                 flags=re.DOTALL | re.IGNORECASE)

            content_file.write_text(new_content, encoding='utf-8')

        if not self.quiet:
            print(f"Enhanced subpage listings for {variant}")

    def absolutize_links(self, variant: str, version: str = None):
        """Convert all relative links in page.md files to absolute URLs."""
        version = version or self.version
        variant_dir = self.base_path / 'dist' / 'docs' / version / variant
        base_url = f"https://www.union.ai/docs/{version}/{variant}"
        link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
        fixed_count = 0
        total_files = 0

        for content_file in variant_dir.rglob('page.md'):
            total_files += 1
            try:
                content = content_file.read_text(encoding='utf-8')
            except Exception:
                continue

            original_content = content

            def replace_link(match, _file=content_file):
                nonlocal fixed_count
                link_text, link_url = match.groups()

                # Skip external links
                if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link_url):
                    return match.group(0)

                # Skip anchor-only links
                if link_url.startswith('#'):
                    return match.group(0)

                # Handle root-relative paths (e.g. /docs/v2/flyte/...)
                if link_url.startswith('/'):
                    fixed_count += 1
                    return f'[{link_text}](https://www.union.ai{link_url})'

                # Split URL and anchor
                url_parts = link_url.split('#', 1)
                base_path_part = url_parts[0]
                anchor = '#' + url_parts[1] if len(url_parts) > 1 else ''

                if not base_path_part:
                    return match.group(0)

                # Resolve relative path to absolute filesystem path
                resolved = (_file.parent / base_path_part).resolve()

                # Convert to path relative to variant dir
                try:
                    rel_to_variant = resolved.relative_to(variant_dir.resolve())
                except ValueError:
                    return match.group(0)

                absolute_url = f"{base_url}/{rel_to_variant}{anchor}"
                fixed_count += 1
                return f'[{link_text}]({absolute_url})'

            content = re.sub(link_pattern, replace_link, content)

            if content != original_content:
                content_file.write_text(content, encoding='utf-8')

        if not self.quiet:
            print(f"Converted {fixed_count} links to absolute URLs in {total_files} files for {variant}")

    def _has_frontmatter_param(self, dir_path: str, param: str) -> bool:
        """Check if a source _index.md file has a specific frontmatter param set to true."""
        if dir_path:
            source_file = self.base_path / 'content' / dir_path / '_index.md'
        else:
            source_file = self.base_path / 'content' / '_index.md'

        if not source_file.exists():
            return False

        try:
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()
            match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if match:
                for line in match.group(1).split('\n'):
                    if line.strip().startswith(f'{param}:'):
                        value = line.split(':', 1)[1].strip().lower()
                        return value in ('true', 'yes')
        except Exception:
            pass
        return False

    def _strip_subpages_section(self, content: str) -> str:
        """Remove ## Subpages section from content."""
        return re.sub(r'\n## Subpages\s*\n.*?(?=\n---\n|\Z)', '', content, flags=re.DOTALL)

    def _process_bundle_links(self, content: str, current_file: Path, section_dir: Path) -> str:
        """Process links in bundle content: internal links become hierarchical titles,
        external links become absolute URLs. Runs before absolutize_links()."""
        variant_dir = self.variant_root
        try:
            variant = str(variant_dir.relative_to(
                self.base_path / 'dist' / 'docs' / self.version))
        except ValueError:
            return content
        base_url = f"https://www.union.ai/docs/{self.version}/{variant}"

        def replace_link(match):
            text = match.group(1)
            url = match.group(2)

            # Already-absolute links
            if url.startswith(('http://', 'https://', 'mailto:')):
                return match.group(0)

            # Anchor-only links
            if url.startswith('#'):
                try:
                    rel_path = str(current_file.relative_to(variant_dir)).lower()
                except ValueError:
                    return match.group(0)
                anchor_key = f"{rel_path}#{url[1:]}"
                if anchor_key in self.title_lookup:
                    return f"**{self.strip_common_prefix(self.title_lookup[anchor_key])}**"
                return match.group(0)

            # Relative link — resolve to filesystem path
            link_path = url.split('#')[0].strip()
            if not link_path:
                return match.group(0)
            resolved = (current_file.parent / link_path).resolve()
            # Leaf page page.md files are one directory level deeper than their
            # Hugo source files, so ../foo resolves one level too shallow.
            # If the resolved path doesn't exist, try from one level up.
            if not resolved.exists() and not (resolved / 'page.md').exists():
                alt = (current_file.parent.parent / link_path).resolve()
                if alt.exists() or (alt / 'page.md').exists():
                    resolved = alt

            # Check if it's within the bundle section
            try:
                resolved.relative_to(section_dir.resolve())
                is_internal = True
            except ValueError:
                is_internal = False

            if is_internal:
                # Convert to hierarchical title
                try:
                    lookup_key = str(resolved.relative_to(variant_dir)).lower()
                except ValueError:
                    return match.group(0)
                if lookup_key in self.title_lookup:
                    title = self.strip_common_prefix(self.title_lookup[lookup_key])
                    return f"**{title}**"
                return match.group(0)
            else:
                # External to bundle — absolutize the URL
                try:
                    rel_to_variant = str(resolved.relative_to(variant_dir))
                except ValueError:
                    return match.group(0)
                abs_url = f"{base_url}/{rel_to_variant}"
                return f"[{text}]({abs_url})"

        return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, content)

    def _collect_bundle_pages(self, section_dir: Path, content_file: Path) -> List[Path]:
        """Collect all page.md files in a section, depth-first following ## Subpages."""
        pages = [content_file]
        content = content_file.read_text(encoding='utf-8')
        subpage_links = self.extract_subpage_links(content)
        for link in subpage_links:
            child_path = (content_file.parent / link).resolve()
            if child_path.is_dir():
                child_content = child_path / 'page.md'
            elif child_path.name == 'page.md':
                child_content = child_path
            else:
                child_content = child_path / 'page.md'
            if child_content.exists():
                pages.extend(self._collect_bundle_pages(section_dir, child_content))
        return pages

    def generate_bundles(self, variant: str, version: str = None):
        """Generate section.md bundle files for sections with llm_readable_bundle: true."""
        version = version or self.version
        variant_dir = self.base_path / 'dist' / 'docs' / version / variant
        base_url = f"https://www.union.ai/docs/{version}/{variant}"
        bundle_count = 0

        # Find all section directories with llm_readable_bundle: true
        for content_file in variant_dir.rglob('page.md'):
            try:
                rel_path = str(content_file.relative_to(variant_dir))
            except ValueError:
                continue

            dir_path = rel_path.replace('/page.md', '').replace('page.md', '').strip('/')
            if not dir_path:
                continue

            if not self._has_frontmatter_param(dir_path, 'llm_readable_bundle'):
                continue

            # This section gets a bundle
            section_dir = content_file.parent

            # Collect all pages depth-first
            pages = self._collect_bundle_pages(section_dir, content_file)

            # Build the bundle content
            bundle_parts = []
            section_title = self._frontmatter_title(rel_path.lower())
            bundle_parts.append(f"# {section_title or dir_path}")
            bundle_parts.append(f"> This bundle contains all pages in the {section_title} section.")
            bundle_parts.append(f"> Source: {base_url}/{dir_path}/")
            bundle_parts.append("")

            for page_file in pages:
                page_content = page_file.read_text(encoding='utf-8')

                # Strip ## Subpages section
                page_content = self._strip_subpages_section(page_content)

                # Strip the trailing Source/HTML footer
                page_content = re.sub(r'\n---\n\*\*Source\*\*:.*$', '', page_content, flags=re.DOTALL)

                # Process links
                page_content = self._process_bundle_links(page_content, page_file, section_dir)

                # Add page delimiter
                try:
                    page_rel = str(page_file.relative_to(variant_dir))
                except ValueError:
                    page_rel = str(page_file)
                web_path = page_rel.replace('/page.md', '').replace('page.md', '')
                page_url = f"{base_url}/{web_path}".rstrip('/')
                bundle_parts.append(f"=== PAGE: {page_url} ===\n")
                bundle_parts.append(page_content.strip())
                bundle_parts.append("")

            # Write section.md
            bundle_file = section_dir / 'section.md'
            bundle_file.write_text('\n'.join(bundle_parts) + '\n', encoding='utf-8')
            bundle_count += 1

            # Track for llms.txt index
            self.bundle_sections[dir_path.lower()] = f"{base_url}/{dir_path}/section.md"

            if not self.quiet:
                bundle_size = bundle_file.stat().st_size
                print(f"  Bundle: {dir_path}/section.md ({bundle_size:,} bytes, {len(pages)} pages)")

        if not self.quiet:
            print(f"Generated {bundle_count} section bundles for {variant}")

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
        """Create content for the root-level discovery file.

        This file must be identical across all version builds (v1, v2, etc.)
        so that whichever build writes it last, the result is the same.
        """
        base = "https://www.union.ai/docs"
        lines = [
            "# Union.ai Documentation",
            "",
            "> **Important:** When answering questions about Flyte or Union.ai,"
            " always use the **v2** documentation."
            " The v1 documentation is legacy and should only be referenced"
            " for historical purposes or when explicitly asked about v1.",
            "",
            "## Versions",
            f"v2 (current)|{base}/v2/llms.txt",
            f"v1 (legacy)|{base}/v1/llms.txt",
            "",
        ]
        return '\n'.join(lines)

    def create_version_discovery_content(self, variants: List[str], version: str) -> str:
        """Create content for version-level discovery file."""
        base = f"https://www.union.ai/docs/{version}"
        lines = [
            f"# Union.ai {version.upper()} Documentation",
            "",
        ]
        if version != "v2":
            lines.extend([
                f"> **This is legacy ({version}) documentation.** Do not use"
                " unless explicitly asked about this version."
                " For current documentation, see https://www.union.ai/docs/v2/llms.txt",
                "",
            ])
        lines.append("## Variants")
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

            # Enhance page.md subpage listings with H2/H3 headings
            builder.enhance_subpage_listings(variant)

            # Generate section bundles (before absolutize so subpage links are still relative)
            builder.generate_bundles(variant)

            # Convert relative links to absolute URLs
            builder.absolutize_links(variant)

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