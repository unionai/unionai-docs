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
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.visited_files: Set[str] = set()
        self.title_lookup: dict[str, str] = {}  # Maps file paths to hierarchical titles

    def run_make_dist(self) -> bool:
        """Run make dist to regenerate all documentation variants."""
        print("🔧 Running 'make dist' to regenerate documentation...")
        try:
            result = subprocess.run(['make', 'dist'],
                                  cwd=self.base_path,
                                  capture_output=True,
                                  text=True,
                                  timeout=300)
            if result.returncode == 0:
                print("✅ Successfully regenerated documentation")
                return True
            else:
                print(f"❌ Make dist failed with return code {result.returncode}")
                return False
        except Exception as e:
            print(f"❌ Error running make dist: {e}")
            return False

    def read_file_content(self, file_path: Path) -> str:
        """Read and clean markdown file content."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Remove the footer metadata section
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
                anchor_key = f"{current_file_path.name}#{anchor}"
                if anchor_key in self.title_lookup:
                    hierarchical_title = self.title_lookup[anchor_key]
                    return f"**{hierarchical_title}**"
                # Fallback: use current page hierarchy + link text
                else:
                    current_page_title = self.strip_common_prefix(' > '.join(current_hierarchy))
                    return f"**{current_page_title} > {text}**"

            # For internal .md links (with or without anchors), convert to hierarchical reference
            if '.md' in url and not url.startswith(('http://', 'https://')):
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
        if current_hierarchy:
            full_title = f"{' > '.join(current_hierarchy)} > {link_text}"
            return self.strip_common_prefix(full_title)

        return link_text

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

            # Convert to lookup key
            key = str(resolved.name)
            if anchor:
                key = f"{key}#{anchor}"

            return key
        except:
            return url

    def extract_page_title(self, content: str, file_path: Path) -> str:
        """Extract the main title from a markdown page."""
        # Look for the first # title
        title_match = re.search(r'^#\s+(.+?)\s*$', content, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()

        # Fallback to filename
        name = file_path.stem
        if name == 'index':
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
        """Convert heading title to URL anchor format."""
        # Convert to lowercase, replace spaces with hyphens, remove special chars
        anchor = re.sub(r'[^a-zA-Z0-9\s-]', '', title)
        anchor = re.sub(r'\s+', '-', anchor.strip().lower())
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

    def build_consolidated_doc(self, variant: str, version: str = 'v2') -> str:
        """Build consolidated document by following subpage links depth-first."""
        md_dir = self.base_path / 'dist' / 'docs' / version / variant / 'md'

        if not md_dir.exists():
            print(f"❌ Directory not found: {md_dir}")
            return ""

        print(f"📖 Building consolidated document for {variant}")
        consolidated_content = []

        # Start with index.md
        self.process_page_depth_first(md_dir, 'index.md', consolidated_content, md_dir, [])

        return '\n'.join(consolidated_content)

    def process_page_depth_first(self, base_dir: Path, relative_path: str,
                                consolidated: List[str], md_root: Path, hierarchy: List[str] = None):
        """Process a page and its subpages in depth-first order."""

        if hierarchy is None:
            hierarchy = []

        # Resolve the full path
        if relative_path.endswith('/'):
            file_path = base_dir / relative_path / 'index.md'
            relative_path = relative_path + 'index.md'
        elif not relative_path.endswith('.md'):
            # Try both with and without .md extension
            if (base_dir / f"{relative_path}.md").exists():
                file_path = base_dir / f"{relative_path}.md"
                relative_path = f"{relative_path}.md"
            elif (base_dir / relative_path / 'index.md').exists():
                file_path = base_dir / relative_path / 'index.md'
                relative_path = f"{relative_path}/index.md"
            else:
                print(f"⚠️  Could not find file for: {relative_path}")
                return
        else:
            file_path = base_dir / relative_path        # Avoid infinite loops
        canonical_path = str(file_path.resolve())
        if canonical_path in self.visited_files:
            return
        self.visited_files.add(canonical_path)

        if not file_path.exists():
            print(f"⚠️  File not found: {file_path}")
            return

        # Get relative path from md root for the delimiter
        try:
            relative_from_md = str(file_path.relative_to(md_root))
        except ValueError:
            relative_from_md = str(file_path)

        print(f"  📄 Processing: {relative_from_md}")

        # Read the raw content
        raw_content = self.read_file_content(file_path)
        if not raw_content.strip():
            return

        # Extract page title and build hierarchy
        page_title = self.extract_page_title(raw_content, file_path)
        current_hierarchy = hierarchy + [page_title]
        hierarchical_title = ' > '.join(current_hierarchy)

        # Store page in lookup table
        self.title_lookup[relative_from_md] = hierarchical_title
        self.title_lookup[file_path.name] = hierarchical_title  # Also store by filename

        # Parse and store heading hierarchy for anchor links
        anchor_map = self.parse_heading_hierarchy(raw_content, file_path, current_hierarchy)
        for anchor, anchor_title in anchor_map.items():
            # Store with full file path + anchor
            anchor_key = f"{relative_from_md}#{anchor}"
            self.title_lookup[anchor_key] = anchor_title

            # Also store with just filename + anchor for relative links
            filename_key = f"{file_path.name}#{anchor}"
            self.title_lookup[filename_key] = anchor_title

        # Extract subpages BEFORE processing links (so links don't break extraction)
        subpage_links = self.extract_subpage_links(raw_content)

        # NOW process internal links with hierarchy context
        content = self.process_internal_links(raw_content, file_path, current_hierarchy)

        # Add page delimiter
        consolidated.append(f"\n=== PAGE: {relative_from_md} ===\n")
        consolidated.append(content)

        # Process subpages depth-first
        for link in subpage_links:
            print(f"    🔗 Following: {link}")
            # Resolve relative to the current file's directory
            current_dir = file_path.parent
            self.process_page_depth_first(current_dir, link, consolidated, md_root, current_hierarchy)

    def find_variants(self) -> List[str]:
        """Find available variants in the dist directory."""
        dist_path = self.base_path / "dist" / "docs" / "v2"
        if not dist_path.exists():
            return []

        variants = []
        for item in dist_path.iterdir():
            if item.is_dir() and (item / 'md').exists():
                variants.append(item.name)

        return sorted(variants)

    def create_redirect_content(self, variant: str) -> str:
        """Create content for the redirect llms.txt file."""
        variant_names = {
            'flyte': 'Flyte Open Source',
            'byoc': 'Union.ai BYOC (Bring Your Own Cloud)',
            'selfmanaged': 'Union.ai Self-managed',
            'serverless': 'Union.ai Serverless'
        }

        variant_display = variant_names.get(variant, variant.title())

        return f"""# {variant_display} Documentation (LLM-Optimized)

This is the LLM-optimized documentation redirect for **{variant_display}** (version 2).

## Full Documentation

For the complete consolidated documentation optimized for Large Language Models, see:

👉 **[llms-full.txt](llms-full.txt)**

The `llms-full.txt` file contains:
- Complete {variant_display} documentation in a single file
- All internal links converted to hierarchical references (e.g., `**Getting started > Local setup**`)
- Depth-first page organization following the documentation structure
- Perfect format for LLM consumption, RAG systems, and vector databases

## File Details

- **Variant**: {variant}
- **Version**: v2
- **Format**: LLM-optimized consolidated markdown
- **Size**: ~1.4MB+ of comprehensive documentation
- **Update frequency**: Generated automatically from source documentation

## Usage

This consolidated documentation is ideal for:
- Large Language Model context and training
- RAG (Retrieval-Augmented Generation) systems
- Vector database ingestion
- AI assistants and chatbots
- Automated documentation analysis

---

*Generated automatically from the Union.ai documentation system.*
"""

    def create_discovery_files(self, base_path: Path, variants: List[str]) -> None:
        """Create hierarchical discovery files for LLM documentation."""

        # Root level discovery file (/docs/llms.txt)
        root_content = self.create_root_discovery_content(variants)
        root_file = base_path / 'dist' / 'docs' / 'llms.txt'

        with open(root_file, 'w', encoding='utf-8') as f:
            f.write(root_content)
        print(f"✅ Created root discovery: {root_file}")

        # Version level discovery file (/docs/v2/llms.txt)
        v2_content = self.create_version_discovery_content(variants, 'v2')
        v2_file = base_path / 'dist' / 'docs' / 'v2' / 'llms.txt'

        with open(v2_file, 'w', encoding='utf-8') as f:
            f.write(v2_content)
        print(f"✅ Created v2 discovery: {v2_file}")

    def create_root_discovery_content(self, variants: List[str]) -> str:
        """Create content for the root-level discovery file."""
        variant_names = {
            'flyte': 'Flyte Open Source',
            'byoc': 'Union.ai BYOC (Bring Your Own Cloud)',
            'selfmanaged': 'Union.ai Self-managed',
            'serverless': 'Union.ai Serverless'
        }

        variant_descriptions = {
            'flyte': 'Free and open source workflow orchestration platform',
            'byoc': 'Commercial Union.ai product - bring your own cloud infrastructure',
            'selfmanaged': 'Commercial Union.ai product - fully managed deployment',
            'serverless': 'Commercial Union.ai product - serverless execution'
        }

        # All four variants for both versions
        all_variants = ['byoc', 'flyte', 'selfmanaged', 'serverless']

        # V2 variant links (current variants)
        v2_variant_links = []
        for variant in sorted(variants):
            name = variant_names.get(variant, variant.title())
            desc = variant_descriptions.get(variant, f'{variant.title()} variant documentation')
            v2_variant_links.append(f"  - **[{name}](v2/{variant}/llms-full.txt)** - {desc}")

        # V1 variant links (all four variants)
        v1_variant_links = []
        for variant in sorted(all_variants):
            name = variant_names.get(variant, variant.title())
            desc = variant_descriptions.get(variant, f'{variant.title()} variant documentation')
            v1_variant_links.append(f"  - **[{name}](v1/{variant}/llms-full.txt)** - {desc}")

        return f"""# Union.ai Documentation (LLM-Optimized)

This is the root discovery file for LLM-optimized documentation across all Union.ai and Flyte products.

## Available Documentation

### Version 2 (Current)

All documentation variants for **Version 2** (current):

{chr(10).join(v2_variant_links)}

**Version-level overview**: [v2/llms.txt](v2/llms.txt) - All v2 variants with detailed descriptions

### Version 1 (Legacy)

All documentation variants for **Version 1** (legacy):

{chr(10).join(v1_variant_links)}

**Version-level overview**: [v1/llms.txt](v1/llms.txt) - All v1 variants with detailed descriptions

## Navigation Guide

### For LLMs and RAG Systems
1. **Direct access**: Use the direct links above to access specific variant documentation
2. **Version browsing**: Use `v2/llms.txt` for detailed v2 variant information
3. **Variant browsing**: Use `v2/{variant}/llms.txt` for specific variant details

### Documentation Structure
- **Root** (`/docs/llms.txt`) - This file, overview of all versions and variants
- **Version** (`/docs/v2/llms.txt`) - All variants for version 2
- **Variant** (`/docs/v2/{variant}/llms.txt`) - Redirect to specific consolidated documentation
- **Content** (`/docs/v2/{variant}/llms-full.txt`) - Complete consolidated documentation

## File Characteristics

Each `llms-full.txt` file contains:
- **Complete documentation** for that variant (~1.4MB+ each)
- **Hierarchical internal links** - All `.md` and `#anchor` links converted to searchable references
- **Depth-first organization** - Content follows logical navigation structure
- **LLM-optimized format** - Perfect for RAG systems, vector databases, and AI assistants

## Product Information

- **Flyte**: Open source workflow orchestration platform maintained by Union.ai
- **Union.ai Products**: Commercial offerings built on Flyte with additional enterprise features
- **Version 2**: Current generation with pure Python execution and simplified API
- **All variants**: Share core Flyte functionality with product-specific enhancements

---

*Generated automatically from the Union.ai documentation system.*
*Last updated: {self.get_current_timestamp()}*
"""

    def create_version_discovery_content(self, variants: List[str], version: str) -> str:
        """Create content for version-level discovery file."""
        variant_names = {
            'flyte': 'Flyte Open Source',
            'byoc': 'Union.ai BYOC (Bring Your Own Cloud)',
            'selfmanaged': 'Union.ai Self-managed',
            'serverless': 'Union.ai Serverless'
        }

        variant_details = {
            'flyte': {
                'desc': 'Free and open source workflow orchestration platform',
                'features': ['Pure Python execution', 'Local development', 'Self-hosted deployment', 'Community support'],
                'audience': 'Developers, data scientists, ML engineers using open source tools'
            },
            'byoc': {
                'desc': 'Commercial Union.ai product with your cloud infrastructure',
                'features': ['All Flyte features', 'Reusable containers', 'Enterprise support', 'Multi-cluster management'],
                'audience': 'Enterprises with existing cloud infrastructure and compliance requirements'
            },
            'selfmanaged': {
                'desc': 'Commercial Union.ai product with managed infrastructure',
                'features': ['All BYOC features', 'Fully managed deployment', 'Union.ai infrastructure', 'SLA guarantees'],
                'audience': 'Teams wanting managed infrastructure without operational overhead'
            },
            'serverless': {
                'desc': 'Commercial Union.ai product with serverless execution',
                'features': ['All Union.ai features', 'Pay-per-execution', 'Zero infrastructure management', 'Auto-scaling'],
                'audience': 'Teams with variable workloads and minimal infrastructure requirements'
            }
        }

        variant_sections = []
        for variant in sorted(variants):
            name = variant_names.get(variant, variant.title())
            details = variant_details.get(variant, {
                'desc': f'{variant.title()} variant documentation',
                'features': ['Core Flyte functionality'],
                'audience': 'General users'
            })

            features_list = '\n'.join([f'  - {feature}' for feature in details['features']])

            variant_sections.append(f"""### {name}

**Description**: {details['desc']}

**Key Features**:
{features_list}

**Target Audience**: {details['audience']}

**Documentation**:
- **[{variant}/llms.txt]({variant}/llms.txt)** - Variant-specific redirect and information
- **[{variant}/llms-full.txt]({variant}/llms-full.txt)** - Complete consolidated documentation (~1.4MB+)""")

        return f"""# Version {version.upper()} Documentation (LLM-Optimized)

This is the version-level discovery file for all **Version {version.upper()}** documentation variants.

## Available Variants

{chr(10).join(variant_sections)}

## Navigation

- **[Root Documentation](../llms.txt)** - Overview of all versions and variants
- **Individual Variants** - Use the links above to access specific variant documentation
- **Direct Access** - Use `{variant}/llms-full.txt` URLs for direct LLM consumption

## Version {version.upper()} Overview

Version {version.upper()} represents the current generation of Flyte and Union.ai products, featuring:
- **Pure Python execution** - No more YAML workflows or complex decorators
- **Simplified API** - Intuitive task definition and execution patterns
- **Enhanced local development** - Seamless transition from local to remote execution
- **Native notebook support** - First-class Jupyter integration
- **Improved observability** - Fine-grained tracing and monitoring

## For LLMs and RAG Systems

Each consolidated documentation file is specifically optimized for AI consumption:
- **No broken links** - All internal references converted to hierarchical text
- **Complete content** - Single file contains all documentation for that variant
- **Searchable structure** - Hierarchical references like `**Getting started > Local setup**`
- **Consistent format** - Standardized page delimiters and link processing

## Usage Examples

```
# Access specific variant documentation
GET /docs/v2/flyte/llms-full.txt
GET /docs/v2/byoc/llms-full.txt

# Get variant information and redirect
GET /docs/v2/flyte/llms.txt
GET /docs/v2/byoc/llms.txt
```

---

*Generated automatically from the Union.ai documentation system.*
*Last updated: {self.get_current_timestamp()}*
"""

    def get_current_timestamp(self) -> str:
        """Get current timestamp for documentation."""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

def main():
    import sys
    base_path = Path.cwd()
    builder = LLMDocBuilder(base_path)

    # Step 1: Regenerate documentation (skip if --no-make-dist is passed)
    if '--no-make-dist' not in sys.argv and not builder.run_make_dist():
        return 1

    # Step 2: Find variants
    variants = builder.find_variants()
    if not variants:
        print("❌ No variants found")
        return 1

    print(f"📋 Found variants: {variants}")

    # Step 3: Build consolidated documents
    for variant in variants:
        consolidated_content = builder.build_consolidated_doc(variant)

        if consolidated_content.strip():
            # Create output file
            output_file = base_path / 'dist' / 'docs' / 'v2' / variant / 'llms-full.txt'

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(consolidated_content)

            file_size = len(consolidated_content)
            print(f"✅ Saved: {output_file} ({file_size:,} characters)")

            # Create redirect llms.txt file
            redirect_file = base_path / 'dist' / 'docs' / 'v2' / variant / 'llms.txt'
            redirect_content = builder.create_redirect_content(variant)

            with open(redirect_file, 'w', encoding='utf-8') as f:
                f.write(redirect_content)

            print(f"✅ Created redirect: {redirect_file}")
        else:
            print(f"❌ No content generated for {variant}")

    # Step 4: Create hierarchical discovery files
    builder.create_discovery_files(base_path, variants)

    return 0

if __name__ == '__main__':
    exit(main())