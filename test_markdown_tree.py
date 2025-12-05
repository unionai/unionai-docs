#!/usr/bin/env python3
"""
Test script to regenerate markdown documentation and build a complete JSON tree
by traversing the ## Subpages links in each index.md file.

Usage:
    python test_markdown_tree.py
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set

class MarkdownTreeBuilder:
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.visited_files: Set[str] = set()

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
                print(f"STDOUT: {result.stdout}")
                print(f"STDERR: {result.stderr}")
                return False
        except subprocess.TimeoutExpired:
            print("❌ Make dist timed out after 5 minutes")
            return False
        except Exception as e:
            print(f"❌ Error running make dist: {e}")
            return False

    def find_variants(self) -> List[str]:
        """Find all available variants in the dist directory."""
        variants = []
        dist_path = self.base_path / "dist" / "docs" / "v2"

        if not dist_path.exists():
            print(f"❌ Distribution directory not found: {dist_path}")
            return variants

        for item in dist_path.iterdir():
            if item.is_dir() and (item / "md" / "index.md").exists():
                variants.append(item.name)

        print(f"📋 Found variants: {variants}")
        return variants

    def extract_subpages_links(self, md_file: Path) -> List[Dict[str, str]]:
        """Extract links from the ## Subpages section of a markdown file."""
        if not md_file.exists():
            return []

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"⚠️  Error reading {md_file}: {e}")
            return []

        # Find the ## Subpages section
        subpages_match = re.search(r'^## Subpages\s*\n\n(.*?)(?=\n##|\n---|\Z)',
                                 content, re.MULTILINE | re.DOTALL)

        if not subpages_match:
            return []

        subpages_content = subpages_match.group(1).strip()

        # Extract markdown links from the subpages section
        link_pattern = r'- \[([^\]]+)\]\(([^)]+)\)'
        links = []

        for match in re.finditer(link_pattern, subpages_content):
            title = match.group(1)
            link = match.group(2)
            links.append({
                'title': title,
                'link': link
            })

        return links

    def resolve_link_path(self, current_dir: Path, link: str) -> Optional[Path]:
        """Resolve a link relative to the current directory."""
        # Remove any anchors
        link = link.split('#')[0]

        # Handle different link formats
        if link.startswith('/'):
            # Absolute link - resolve from md root
            md_root = self.find_md_root(current_dir)
            if md_root:
                return (md_root / link.lstrip('/')).resolve()
        else:
            # Relative link
            target = (current_dir / link).resolve()

            # If link doesn't end with .md, it might be a directory
            if not link.endswith('.md'):
                # Check for directory with index.md
                if (target / 'index.md').exists():
                    return target / 'index.md'
                # Check for .md file with same name
                md_file = target.with_suffix('.md')
                if md_file.exists():
                    return md_file

            return target if target.exists() else None

    def find_md_root(self, current_path: Path) -> Optional[Path]:
        """Find the md root directory by walking up the path."""
        path = current_path
        while path != path.parent:
            if path.name == 'md':
                return path
            path = path.parent
        return None

    def get_file_info(self, file_path: Path) -> Dict:
        """Get information about a markdown file."""
        info = {
            'path': str(file_path.relative_to(self.base_path)),
            'exists': file_path.exists(),
            'size': 0,
            'title': None
        }

        if file_path.exists():
            try:
                info['size'] = file_path.stat().st_size

                # Extract title from file (first H1)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    h1_match = re.search(r'^# (.+)$', content, re.MULTILINE)
                    if h1_match:
                        info['title'] = h1_match.group(1).strip()
            except Exception as e:
                print(f"⚠️  Error getting file info for {file_path}: {e}")

        return info

    def build_tree(self, md_file: Path, current_depth: int = 0, max_depth: int = 10) -> Dict:
        """Recursively build the markdown tree starting from an index.md file."""
        if current_depth > max_depth:
            return {'error': 'Max depth exceeded'}

        # Avoid infinite loops
        file_key = str(md_file.resolve())
        if file_key in self.visited_files:
            return {'error': 'Circular reference detected', 'path': file_key}

        self.visited_files.add(file_key)

        print("  " * current_depth + f"📄 Processing: {md_file.relative_to(self.base_path)}")

        # Get file information
        file_info = self.get_file_info(md_file)

        # Get subpages
        subpages_links = self.extract_subpages_links(md_file)

        node = {
            'file_info': file_info,
            'subpages_count': len(subpages_links),
            'subpages': []
        }

        # Process each subpage
        for link_info in subpages_links:
            print("  " * (current_depth + 1) + f"🔗 Link: {link_info['title']} -> {link_info['link']}")

            # Resolve the link path
            target_path = self.resolve_link_path(md_file.parent, link_info['link'])

            subpage_node = {
                'title': link_info['title'],
                'link': link_info['link'],
                'resolved_path': str(target_path.relative_to(self.base_path)) if target_path else None,
                'exists': target_path.exists() if target_path else False
            }

            # If target exists and is an index.md, recurse
            if target_path and target_path.exists() and target_path.name == 'index.md':
                subpage_node['children'] = self.build_tree(target_path, current_depth + 1, max_depth)
            elif target_path and target_path.exists():
                # It's a regular markdown file
                subpage_node['file_info'] = self.get_file_info(target_path)

            node['subpages'].append(subpage_node)

        return node

    def build_variant_tree(self, variant: str) -> Dict:
        """Build the complete tree for a specific variant."""
        print(f"\n🌳 Building tree for variant: {variant}")

        # Reset visited files for each variant
        self.visited_files.clear()

        # Find the root index.md for this variant
        root_index = self.base_path / "dist" / "docs" / "v2" / variant / "md" / "index.md"

        if not root_index.exists():
            return {'error': f'Root index.md not found for variant {variant}'}

        return {
            'variant': variant,
            'root_path': str(root_index.relative_to(self.base_path)),
            'tree': self.build_tree(root_index)
        }

    def generate_report(self, trees: Dict[str, Dict]) -> Dict:
        """Generate a summary report of the trees."""
        report = {
            'total_variants': len(trees),
            'variants': {},
            'summary': {
                'total_files': 0,
                'total_subpages': 0,
                'broken_links': 0
            }
        }

        def count_nodes(node):
            """Recursively count files and links in a tree node."""
            counts = {'files': 0, 'subpages': 0, 'broken_links': 0}

            if 'file_info' in node:
                counts['files'] += 1

            if 'subpages' in node:
                counts['subpages'] += len(node['subpages'])
                for subpage in node['subpages']:
                    if not subpage.get('exists', True):
                        counts['broken_links'] += 1
                    if 'children' in subpage:
                        child_counts = count_nodes(subpage['children'])
                        counts['files'] += child_counts['files']
                        counts['subpages'] += child_counts['subpages']
                        counts['broken_links'] += child_counts['broken_links']

            return counts

        for variant, tree in trees.items():
            if 'tree' in tree:
                counts = count_nodes(tree['tree'])
                report['variants'][variant] = counts
                report['summary']['total_files'] += counts['files']
                report['summary']['total_subpages'] += counts['subpages']
                report['summary']['broken_links'] += counts['broken_links']

        return report

    def read_markdown_file(self, file_path: Path) -> str:
        """Read the content of a markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return ""

    def clean_markdown_content(self, content: str) -> str:
        """Clean markdown content by removing metadata sections."""
        # Remove the Source/URL/Date footer section
        content = re.sub(r'\n---\n\*\*Source\*\*:.*?(?=\n\n|\Z)', '', content, flags=re.DOTALL)

        # Ensure content ends with proper spacing
        content = content.rstrip() + '\n'

        return content

    def build_consolidated_document(self, tree: Dict, variant: str, path_breadcrumb: List[str] = None) -> str:
        """Build a consolidated markdown document from the tree structure."""
        if path_breadcrumb is None:
            path_breadcrumb = []

        consolidated = []

        # Process the current file if it exists
        if 'file_info' in tree and tree['file_info']['exists']:
            file_path = Path(tree['file_info']['path'])
            relative_source = str(file_path.relative_to(Path(f'dist/docs/v2/{variant}/md')))

            # Read the file content
            content = self.read_markdown_file(self.base_path / file_path)
            content = self.clean_markdown_content(content)

            # Add page metadata header (except for root)
            if path_breadcrumb:
                breadcrumb_path = ' > '.join(path_breadcrumb)
                page_header = f"""---
**PAGE: {breadcrumb_path}**
**SOURCE: {relative_source}**

"""
                consolidated.append(page_header)

            # Add the content
            consolidated.append(content)

        # Process subpages with depth-first traversal (avoid duplication)
        if 'subpages' in tree:
            for subpage in tree['subpages']:
                # Build new breadcrumb path
                new_breadcrumb = path_breadcrumb + [subpage['title']]

                # Process the subpage itself (if it exists as a file)
                if subpage.get('exists', False) and subpage.get('resolved_path'):
                    # Handle the subpage file
                    file_path = Path(subpage['resolved_path'])
                    content = self.read_markdown_file(self.base_path / file_path)
                    content = self.clean_markdown_content(content)

                    breadcrumb_path = ' > '.join(new_breadcrumb)
                    relative_source = str(file_path.relative_to(Path(f'dist/docs/v2/{variant}/md')))

                    page_header = f"""---
**PAGE: {breadcrumb_path}**
**SOURCE: {relative_source}**

"""
                    consolidated.append(page_header)
                    consolidated.append(content)

                # Then, recursively process its children (depth-first) - only if it has children
                if 'children' in subpage:
                    child_content = self.build_consolidated_document(
                        subpage['children'],
                        variant,
                        new_breadcrumb
                    )
                    if child_content.strip():  # Only append if there's actual content
                        consolidated.append(child_content)

        return '\n'.join(consolidated)

def main():
    base_path = Path.cwd()
    builder = MarkdownTreeBuilder(base_path)

    # Step 1: Regenerate documentation
    if not builder.run_make_dist():
        print("❌ Failed to regenerate documentation. Exiting.")
        sys.exit(1)

    # Step 2: Find variants
    variants = builder.find_variants()
    if not variants:
        print("❌ No variants found. Exiting.")
        sys.exit(1)

    # Step 3: Build trees for each variant
    trees = {}
    for variant in variants:
        trees[variant] = builder.build_variant_tree(variant)

    # Step 4: Generate report
    report = builder.generate_report(trees)

    # Step 5: Save results
    output_file = base_path / "markdown_tree_analysis.json"

    result = {
        'timestamp': '2025-12-05',
        'base_path': str(base_path),
        'report': report,
        'trees': trees
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\n📊 Analysis complete! Results saved to: {output_file}")
    print(f"📈 Summary:")
    print(f"  - Total variants: {report['total_variants']}")
    print(f"  - Total files processed: {report['summary']['total_files']}")
    print(f"  - Total subpage links: {report['summary']['total_subpages']}")
    print(f"  - Broken links found: {report['summary']['broken_links']}")

    for variant, counts in report['variants'].items():
        print(f"  - {variant}: {counts['files']} files, {counts['subpages']} links, {counts['broken_links']} broken")

    # Step 6: Generate consolidated documents for each variant
    for variant in variants:
        if variant in trees and 'tree' in trees[variant]:
            print(f"\n📖 Generating consolidated document for variant: {variant}")
            consolidated_content = builder.build_consolidated_document(trees[variant]['tree'], variant)

            # Add header
            header = f"""# Documentation
**Variant:** {variant}
**Generated:** 2025-12-05

This is a consolidated view of all documentation pages in hierarchical order.

"""
            full_content = header + consolidated_content

            # Save consolidated document
            consolidated_file = base_path / f"consolidated_{variant}_docs.md"
            with open(consolidated_file, 'w', encoding='utf-8') as f:
                f.write(full_content)

            print(f"  📊 Generated document with {len(consolidated_content.split('---'))-1} pages, {len(full_content):,} characters")
            print(f"📄 Saved consolidated document: {consolidated_file}")

    return 0

if __name__ == '__main__':
    sys.exit(main())