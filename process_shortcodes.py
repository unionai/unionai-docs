#!/usr/bin/env python3
"""
Hugo Shortcode Processor for Markdown Output

This script post-processes Hugo-generated markdown files to convert shortcodes
into clean markdown equivalents.

Usage:
    python process_shortcodes.py --variant=byoc --input-dir=dist/docs/v2/byoc/md --output-dir=dist/docs/v2/byoc/md-processed
"""

import argparse
import os
import re
from pathlib import Path
from typing import Dict, Any, Optional

# Handle TOML parsing with fallbacks
try:
    import tomllib  # Python 3.11+
    def load_toml(file_handle):
        return tomllib.load(file_handle)
except ImportError:
    try:
        import tomli as tomllib
        def load_toml(file_handle):
            return tomllib.load(file_handle)
    except ImportError:
        try:
            import toml as tomllib
            def load_toml(file_handle):
                return tomllib.load(file_handle)
        except ImportError:
            print("Error: No TOML library available. Please install tomli or toml.")
            def load_toml(file_handle):
                return {}


class ShortcodeProcessor:
    def __init__(self, variant: str, base_path: str = ""):
        self.variant = variant
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.key_mappings = self._load_key_mappings()

    def _load_key_mappings(self) -> Dict[str, Dict[str, str]]:
        """Load key mappings from hugo.site.toml dynamically."""
        try:
            toml_path = self.base_path / "hugo.site.toml"
            if not toml_path.exists():
                print(f"Warning: hugo.site.toml not found at {toml_path}")
                return {}

            # Try binary mode first (for tomllib), then text mode (for toml/tomli)
            try:
                with open(toml_path, 'rb') as f:
                    config = load_toml(f)
            except (TypeError, UnicodeDecodeError):
                with open(toml_path, 'r', encoding='utf-8') as f:
                    config = load_toml(f)

            # Extract key mappings from params.key
            key_params = config.get('params', {}).get('key', {})

            # Transform the nested structure to a flat mapping per variant
            mappings = {}
            variants = ['flyte', 'byoc', 'selfmanaged']

            for variant in variants:
                mappings[variant] = {}
                for key_type, variant_values in key_params.items():
                    if isinstance(variant_values, dict) and variant in variant_values:
                        mappings[variant][key_type] = variant_values[variant]

            return mappings

        except Exception as e:
            print(f"Error loading key mappings from hugo.site.toml: {e}")
            return {}

    def process_file(self, file_path: Path) -> str:
        """Process a single markdown file and return the processed content."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Process shortcodes recursively to handle nesting
        return self.process_shortcodes_recursive(content)

    def process_shortcodes_recursive(self, content: str, max_depth: int = 10) -> str:
        """Recursively process shortcodes to handle arbitrary nesting depth."""
        if max_depth <= 0:
            return content  # Prevent infinite recursion

        original_content = content

        # Process container shortcodes first (they may contain other shortcodes)
        content = self.process_variant_shortcodes_recursive(content)
        content = self.process_markdown_shortcodes_recursive(content)
        content = self.process_grid_shortcodes_recursive(content)
        content = self.process_dropdown_shortcodes_recursive(content)
        content = self.process_tabs_shortcodes_recursive(content)

        # Then process leaf shortcodes
        content = self.process_code_shortcodes(content)
        content = self.process_note_shortcodes_recursive(content)
        content = self.process_warning_shortcodes_recursive(content)
        content = self.process_link_card_shortcodes_recursive(content)
        content = self.process_multiline_shortcodes(content)
        content = self.process_icon_shortcodes(content)
        content = self.process_button_link_shortcodes_recursive(content)
        content = self.process_key_shortcodes(content)
        content = self.process_docs_home_shortcodes(content)

        # If content changed, recurse to handle any newly exposed shortcodes
        if content != original_content:
            content = self.process_shortcodes_recursive(content, max_depth - 1)

        return content

    def process_code_shortcodes(self, content: str) -> str:
        """Process {{< code file="..." lang="..." >}} shortcodes."""
        pattern = r'\{\{<\s*code\s+file="([^"]*)"(?:\s+lang="([^"]*)")?(?:\s+fragment="([^"]*)")?[^>]*>\}\}'

        def replace_code(match):
            file_path, lang, fragment = match.groups()

            # Read file content
            try:
                full_path = self.resolve_file_path(file_path)
                with open(full_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()

                # Handle fragments if specified
                if fragment:
                    file_content = self.extract_fragment(file_content, fragment)

                # Generate markdown code block
                lang_str = lang or ""
                return f"```{lang_str}\n{file_content.rstrip()}\n```\n\n*Source: {file_path}*"

            except Exception as e:
                return f"```\n# Error reading file: {file_path}\n# {str(e)}\n```"

        return re.sub(pattern, replace_code, content)

    def process_note_shortcodes_recursive(self, content: str) -> str:
        """Process {{< note >}} shortcodes with support for nested shortcodes."""
        return self.process_note_shortcodes(content)  # Delegate to main function

    def process_note_shortcodes(self, content: str) -> str:
        """Process {{< note >}} shortcodes."""
        pattern = r'\{\{<\s*note(?:\s+title="([^"]*)")?[^>]*>\}\}(.*?)\{\{<\s*/note\s*>\}\}'

        def replace_note(match):
            title, note_content = match.groups()
            title = title or "Note"

            # Convert to markdown blockquote
            lines = note_content.strip().split('\n')
            quoted_lines = [f"> {line}" if line.strip() else ">" for line in lines]

            return f"> **📝 {title}**\n>\n" + "\n".join(quoted_lines)

        return re.sub(pattern, replace_note, content, flags=re.DOTALL)

    def process_warning_shortcodes_recursive(self, content: str) -> str:
        """Process {{< warning >}} shortcodes with support for nested shortcodes."""
        return self.process_warning_shortcodes(content)  # Delegate to main function

    def process_warning_shortcodes(self, content: str) -> str:
        """Process {{< warning >}} shortcodes."""
        pattern = r'\{\{<\s*warning(?:\s+title="([^"]*)")?[^>]*>\}\}(.*?)\{\{<\s*/warning\s*>\}\}'

        def replace_warning(match):
            title, warning_content = match.groups()
            title = title or "Warning"

            # Convert to markdown blockquote
            lines = warning_content.strip().split('\n')
            quoted_lines = [f"> {line}" if line.strip() else ">" for line in lines]

            return f"> **⚠️ {title}**\n>\n" + "\n".join(quoted_lines)

        return re.sub(pattern, replace_warning, content, flags=re.DOTALL)

    def process_tabs_shortcodes_recursive(self, content: str) -> str:
        """Process {{< tabs >}} shortcodes with support for nested shortcodes."""
        return self.process_tabs_shortcodes(content)  # Delegate to main function

    def process_tabs_shortcodes(self, content: str) -> str:
        """Process {{< tabs >}} and {{< tab >}} shortcodes."""
        # First extract all tab content
        tab_pattern = r'\{\{<\s*tab\s+"([^"]*)"\s*>\}\}(.*?)\{\{<\s*/tab\s*>\}\}'
        tabs_pattern = r'\{\{<\s*tabs[^>]*>\}\}(.*?)\{\{<\s*/tabs\s*>\}\}'

        def replace_tabs(match):
            tabs_content = match.group(1)

            # Find all tabs within this tabs block
            tab_matches = re.findall(tab_pattern, tabs_content, flags=re.DOTALL)

            if not tab_matches:
                return "<!-- Empty tabs block -->"

            # Convert to markdown with headers
            result = []
            for i, (tab_title, tab_content) in enumerate(tab_matches):
                if i == 0:
                    result.append(f"### {tab_title}")
                else:
                    result.append(f"\n### {tab_title}")
                result.append(f"\n{tab_content.strip()}\n")

            return "\n".join(result)

        return re.sub(tabs_pattern, replace_tabs, content, flags=re.DOTALL)

    def process_icon_shortcodes(self, content: str) -> str:
        """Process {{< icon >}} shortcodes."""
        pattern = r'\{\{<\s*icon\s+"([^"]*)"\s*>\}\}'

        # Icon mapping to unicode equivalents
        icon_map = {
            "info-circle": "ℹ️",
            "exclamation-triangle": "⚠️",
            "check": "✅",
            "times": "❌",
            "arrow-right": "→",
            "arrow-left": "←",
            "download": "📥",
            "upload": "📤",
            "home": "🏠",
            "settings": "⚙️",
            "search": "🔍",
        }

        def replace_icon(match):
            icon_name = match.group(1)
            return icon_map.get(icon_name, f"[{icon_name}]")

        return re.sub(pattern, replace_icon, content)

    def process_button_link_shortcodes_recursive(self, content: str) -> str:
        """Process {{< button-link >}} shortcodes with support for nested shortcodes."""
        return self.process_button_link_shortcodes(content)  # Delegate to main function

    def process_button_link_shortcodes(self, content: str) -> str:
        """Process {{< button-link >}} shortcodes."""
        pattern = r'\{\{<\s*button-link\s+href="([^"]*)"\s*>\}\}(.*?)\{\{<\s*/button-link\s*>\}\}'

        def replace_button_link(match):
            href, link_text = match.groups()
            return f"[{link_text.strip()}]({href})"

        return re.sub(pattern, replace_button_link, content, flags=re.DOTALL)

    def process_variant_shortcodes(self, content: str) -> str:
        """Process {{< variant >}} shortcodes for conditional content based on variant."""
        pattern = r'\{\{<\s*variant\s+([^>]*)>\}\}(.*?)\{\{<\s*/variant\s*>\}\}'

        def replace_variant(match):
            variant_spec, variant_content = match.groups()

            # Parse variant specification (e.g., "byoc selfmanaged" or "!flyte")
            # Handle space-separated variants and negation
            variants = [v.strip() for v in variant_spec.split()]

            include_variants = [v for v in variants if not v.startswith('!')]
            exclude_variants = [v[1:] for v in variants if v.startswith('!')]

            # Check if current variant should include this content
            should_include = True

            # If there are include variants specified, current variant must be in the list
            if include_variants:
                should_include = self.variant in include_variants

            # If there are exclude variants specified, current variant must NOT be in the list
            if exclude_variants:
                should_include = should_include and (self.variant not in exclude_variants)

            return variant_content.strip() if should_include else ""

        return re.sub(pattern, replace_variant, content, flags=re.DOTALL)

    def process_variant_shortcodes_recursive(self, content: str) -> str:
        """Process {{< variant >}} shortcodes with support for nested shortcodes."""
        return self.process_variant_shortcodes(content)  # Delegate to main function

    def process_markdown_shortcodes(self, content: str) -> str:
        """Process {{< markdown >}} shortcodes by removing them (they serve no purpose in markdown output)."""
        # Remove markdown shortcode containers, keeping only the content
        pattern = r'\{\{<\s*markdown[^>]*>\}\}(.*?)\{\{<\s*/markdown\s*>\}\}'

        def replace_markdown(match):
            return match.group(1)

        return re.sub(pattern, replace_markdown, content, flags=re.DOTALL)

    def process_markdown_shortcodes_recursive(self, content: str) -> str:
        """Process {{< markdown >}} shortcodes with support for nested shortcodes."""
        return self.process_markdown_shortcodes(content)  # Delegate to main function

    def process_grid_shortcodes_recursive(self, content: str) -> str:
        """Process {{< grid >}} shortcodes with support for nested shortcodes."""
        return self.process_grid_shortcodes(content)  # Delegate to main function

    def process_grid_shortcodes(self, content: str) -> str:
        """Process {{< grid >}} shortcodes by converting them to markdown structure."""
        pattern = r'\{\{<\s*grid[^>]*>\}\}(.*?)\{\{<\s*/grid\s*>\}\}'

        def replace_grid(match):
            grid_content = match.group(1).strip()
            # Just return the content without the grid wrapper
            # The nested shortcodes (like link-card) will be processed separately
            return grid_content

        return re.sub(pattern, replace_grid, content, flags=re.DOTALL)

    def resolve_file_path(self, file_path: str) -> Path:
        """Resolve shortcode file paths to actual file system paths."""
        # Handle different prefixes
        if file_path.startswith('/external/'):
            # External files are in the external/ subdirectory
            return self.base_path / file_path.lstrip('/')
        elif file_path.startswith('/static/'):
            return self.base_path / 'static' / file_path[8:]
        elif file_path.startswith('/_static/'):
            return self.base_path / 'content' / '_static' / file_path[9:]
        else:
            return self.base_path / file_path.lstrip('/')

    def extract_fragment(self, content: str, fragment_name: str) -> str:
        """Extract a fragment from file content using Hugo fragment markers."""
        start_marker = f"{{{{docs-fragment {fragment_name}}}}}"
        end_marker = f"{{{{/docs-fragment {fragment_name}}}}}"

        lines = content.split('\n')
        in_fragment = False
        fragment_lines = []

        for line in lines:
            # Check for markers in comments (removing common comment prefixes)
            clean_line = re.sub(r'^\s*(#|//|/\*+|\*+)?\s*', '', line)

            if clean_line == start_marker:
                in_fragment = True
            elif clean_line == end_marker:
                break
            elif in_fragment:
                fragment_lines.append(line)

        return '\n'.join(fragment_lines)

    def process_grid_shortcodes_recursive(self, content: str) -> str:
        """Process {{< grid >}} shortcodes with support for nested shortcodes."""
        return self.process_grid_shortcodes(content)  # Delegate to main function

    def process_grid_shortcodes(self, content: str) -> str:
        """Process {{< grid >}} shortcodes by converting them to markdown structure."""
        pattern = r'\{\{<\s*grid[^>]*>\}\}(.*?)\{\{<\s*/grid\s*>\}\}'

        def replace_grid(match):
            grid_content = match.group(1).strip()
            # Just return the content without the grid wrapper
            # The nested shortcodes (like link-card) will be processed separately
            return grid_content

        return re.sub(pattern, replace_grid, content, flags=re.DOTALL)

    def process_dropdown_shortcodes_recursive(self, content: str) -> str:
        """Process {{< dropdown >}} shortcodes with support for nested shortcodes."""
        return self.process_dropdown_shortcodes(content)  # Delegate to main function

    def process_dropdown_shortcodes(self, content: str) -> str:
        """Process {{< dropdown >}} shortcodes by converting them to markdown collapsible sections."""
        pattern = r'\{\{<\s*dropdown\s+title="([^"]*?)"[^>]*>\}\}(.*?)\{\{<\s*/dropdown\s*>\}\}'

        def replace_dropdown(match):
            title, dropdown_content = match.groups()
            # Convert to markdown collapsible section
            return f"\n<details>\n<summary>{title}</summary>\n\n{dropdown_content.strip()}\n\n</details>\n"

        return re.sub(pattern, replace_dropdown, content, flags=re.DOTALL)

    def process_link_card_shortcodes_recursive(self, content: str) -> str:
        """Process {{< link-card >}} shortcodes with support for nested shortcodes."""
        return self.process_link_card_shortcodes(content)  # Delegate to main function

    def process_link_card_shortcodes(self, content: str) -> str:
        """Process {{< link-card >}} shortcodes by converting them to markdown links."""
        pattern = r'\{\{<\s*link-card\s+target="([^"]*)"\s*(?:icon="([^"]*)")?\s*(?:title="([^"]*)")?\s*[^>]*>\}\}(.*?)\{\{<\s*/link-card\s*>\}\}'

        def replace_link_card(match):
            target, icon, title, card_content = match.groups()

            # Convert icon to emoji if available
            icon_map = {
                "lightbulb": "💡",
                "123": "🔢",
                "book": "📚",
                "code": "💻",
                "settings": "⚙️",
                "rocket": "🚀",
                "chart": "📊"
            }
            icon_emoji = icon_map.get(icon, "🔗") if icon else "🔗"

            # Create markdown card representation
            title = title or "Link"
            return f"\n### {icon_emoji} [{title}]({target})\n\n{card_content.strip()}\n"

        return re.sub(pattern, replace_link_card, content, flags=re.DOTALL)

    def process_multiline_shortcodes(self, content: str) -> str:
        """Process {{< multiline >}} shortcodes by preserving the content without formatting."""
        pattern = r'\{\{<\s*multiline[^>]*>\}\}(.*?)\{\{<\s*/multiline\s*>\}\}'

        def replace_multiline(match):
            multiline_content = match.group(1).strip()
            # For multiline content (often CLI options), just return the content
            # This preserves line breaks and formatting
            return multiline_content

        return re.sub(pattern, replace_multiline, content, flags=re.DOTALL)

    def process_key_shortcodes(self, content: str) -> str:
        """Process {{< key >}} shortcodes by replacing them with variant-specific values."""
        pattern = r'\{\{<\s*key\s+([^>]*)\s*>\}\}'

        def replace_key(match):
            key_name = match.group(1).strip()

            # Get the mapping for the current variant from dynamically loaded config
            variant_mappings = self.key_mappings.get(self.variant, {})

            # Return the mapped value or the key name if not found
            return variant_mappings.get(key_name, f"{{{{< key {key_name} >}}}}")

        return re.sub(pattern, replace_key, content)

    def process_docs_home_shortcodes(self, content: str) -> str:
        """Process {{< docs_home >}} shortcodes by creating variant-specific links."""
        pattern = r'\{\{<\s*docs_home\s+([^>]*)\s*>\}\}'

        def replace_docs_home(match):
            args = match.group(1).strip().split()
            if len(args) >= 2:
                variant = args[0]
                version = args[1]
                return f"/docs/{version}/{variant}/"
            elif len(args) >= 1:
                variant = args[0]
                return f"/docs/v2/{variant}/"
            else:
                return "/docs/"

        return re.sub(pattern, replace_docs_home, content)


def main():
    parser = argparse.ArgumentParser(description='Process Hugo shortcodes in markdown files')
    parser.add_argument('--variant', required=True, help='Site variant (e.g., byoc, flyte)')
    parser.add_argument('--input-dir', required=True, help='Input directory with markdown files')
    parser.add_argument('--output-dir', required=True, help='Output directory for processed files')
    parser.add_argument('--base-path', help='Base path for resolving file references', default='')

    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)

    if not input_dir.exists():
        print(f"Error: Input directory {input_dir} does not exist")
        return 1

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    processor = ShortcodeProcessor(args.variant, args.base_path)

    # Process all markdown files
    for md_file in input_dir.rglob('*.txt'):  # Hugo outputs .txt for MD format
        # Calculate relative path to preserve directory structure
        rel_path = md_file.relative_to(input_dir)
        output_file = output_dir / rel_path

        # Create output directory if needed
        output_file.parent.mkdir(parents=True, exist_ok=True)

        print(f"Processing: {rel_path}")

        try:
            processed_content = processor.process_file(md_file)

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(processed_content)

        except Exception as e:
            print(f"Error processing {rel_path}: {e}")

    print(f"Processing complete. Output in: {output_dir}")
    return 0


if __name__ == '__main__':
    exit(main())