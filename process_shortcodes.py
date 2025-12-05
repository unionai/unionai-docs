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
    def __init__(self, variant: str, base_path: str = "", input_dir: str = ""):
        self.variant = variant
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.input_dir = Path(input_dir) if input_dir else Path.cwd()
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
        processed_content = self.process_shortcodes_recursive(content)

        return processed_content

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
        content = self.process_download_shortcodes(content)
        content = self.process_youtube_shortcodes(content)

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
            # Use target URL as-is
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
                url = f"/docs/{version}/{variant}/"
            elif len(args) >= 1:
                variant = args[0]
                url = f"/docs/v2/{variant}/"
            else:
                url = "/docs/"
            return url

        return re.sub(pattern, replace_docs_home, content)

    def process_download_shortcodes(self, content: str) -> str:
        """Process {{< download >}} shortcodes by creating markdown download links."""
        # Match both positional and named parameter formats
        pattern = r'\{\{<\s*download\s+([^>]*)\s*>\}\}'

        def replace_download(match):
            params = match.group(1).strip()

            # Parse parameters
            url = None
            name = None
            description = None
            display = None

            # Handle named parameters
            if 'file=' in params:
                url_match = re.search(r'file="([^"]*)"|file=\'([^\']*)\'|file=([^\s]+)', params)
                if url_match:
                    url = url_match.group(1) or url_match.group(2) or url_match.group(3)

            # Handle positional parameters
            if not url:
                parts = re.findall(r'"([^"]*)"|\s*([^\s"]+)', params)
                flat_parts = [p[0] if p[0] else p[1] for p in parts if p[0] or p[1]]
                if len(flat_parts) > 0:
                    url = flat_parts[0]
                if len(flat_parts) > 1:
                    name = flat_parts[1]
                if len(flat_parts) > 2:
                    description = flat_parts[2]

            # Check for display parameter
            display_match = re.search(r'display="([^"]*)"|display=\'([^\']*)\'|display=([^\s]+)', params)
            if display_match:
                display = display_match.group(1) or display_match.group(2) or display_match.group(3)

            if not url:
                return match.group(0)  # Return original if no URL found

            # Default name to filename if not provided
            if not name:
                name = url.split('/')[-1] if '/' in url else url

            # Create markdown link
            # Use URL as-is
            download_link = f"📥 [{name}]({url})"

            # Add description if provided
            if description:
                if display == "paragraph":
                    return f"\n**{download_link}**\n\n*{description}*\n"
                else:
                    return f"{download_link} - {description}"
            else:
                if display == "paragraph":
                    return f"\n**{download_link}**\n"
                else:
                    return download_link

        return re.sub(pattern, replace_download, content)

    def process_youtube_shortcodes(self, content: str) -> str:
        """Process {{< youtube >}} shortcodes by creating markdown YouTube links."""
        pattern = r'\{\{<\s*youtube\s+([^>]*)\s*>\}\}'

        def replace_youtube(match):
            video_id = match.group(1).strip()
            # Remove quotes if present
            video_id = video_id.strip('"\'')

            # Create markdown link to YouTube video
            youtube_url = f"https://www.youtube.com/watch?v={video_id}"
            return f"📺 [Watch on YouTube]({youtube_url})"

        return re.sub(pattern, replace_youtube, content)

    def process_internal_links(self, content: str, current_file_path: Path) -> str:
        """Convert Hugo-style internal links to proper .md file references."""
        # Pattern to match markdown links that are not external (don't start with http/https/mailto/etc)
        link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'

        def replace_link(match):
            link_text, link_url = match.groups()

            # Skip external links (http/https/mailto/ftp/etc)
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link_url):
                return match.group(0)

            # Skip anchor-only links
            if link_url.startswith('#'):
                return match.group(0)

            # Split URL and anchor
            url_parts = link_url.split('#', 1)
            base_url = url_parts[0]
            anchor = '#' + url_parts[1] if len(url_parts) > 1 else ''

            if not base_url:  # Empty base URL means anchor-only
                return match.group(0)

            # Convert Hugo-style path to final .md file reference
            current_dir = current_file_path.parent
            try:
                if base_url.startswith('/'):
                    # Absolute path from site root - convert to relative
                    site_root = Path('dist/docs/v2') / self.variant / 'md-processed'
                    target_path = site_root / base_url.lstrip('/')
                else:
                    # Relative path from current file
                    target_path = (current_dir / base_url).resolve()

                # Predict what the final structure will look like after processing
                # We need to determine if this will be a single page or section page

                # First, check if there's a directory - this means it will be a section with index.md
                if target_path.exists() and target_path.is_dir():
                    # Will be a directory with index.md
                    rel_path = os.path.relpath(target_path / 'index.md', current_dir)
                    return f'[{link_text}]({rel_path}{anchor})'

                # If target_path doesn't exist as directory, it might become a single .md file
                # Check if there would be a corresponding .md file
                parent_dir = target_path.parent
                target_name = target_path.name

                # Check if there will be a {name}.md file in the parent directory
                potential_md_file = parent_dir / f"{target_name}.md"
                potential_index_dir = parent_dir / target_name

                # Priority: if there's a directory with that name, it becomes {dir}/index.md
                if potential_index_dir.exists() and potential_index_dir.is_dir():
                    rel_path = os.path.relpath(potential_index_dir / 'index.md', current_dir)
                    return f'[{link_text}]({rel_path}{anchor})'

                # Otherwise, assume it will become {name}.md
                rel_path = os.path.relpath(potential_md_file, current_dir)
                return f'[{link_text}]({rel_path}{anchor})'

            except Exception as e:
                print(f"Error processing link '{link_url}' in {current_file_path}: {e}")
                return match.group(0)

            except Exception as e:
                print(f"Error processing link '{link_url}' in {current_file_path}: {e}")
                return match.group(0)

        return re.sub(link_pattern, replace_link, content)


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

    # Create output directory (clear it first if it exists)
    if output_dir.exists():
        import shutil
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    processor = ShortcodeProcessor(args.variant, args.base_path, args.input_dir)

    # Process all markdown files
    for md_file in input_dir.rglob('*.txt'):  # Hugo outputs .txt for MD format
        # Calculate relative path to preserve directory structure
        rel_path = md_file.relative_to(input_dir)
        # Change .txt extension to .md for output
        output_rel_path = rel_path.with_suffix('.md')
        output_file = output_dir / output_rel_path

        # Create output directory if needed
        output_file.parent.mkdir(parents=True, exist_ok=True)

        print(f"Processing: {rel_path} -> {output_rel_path}")

        try:
            processed_content = processor.process_file(md_file)

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(processed_content)

        except Exception as e:
            print(f"Error processing {rel_path}: {e}")

    # Create root index.md if it doesn't exist
    root_index = output_dir / 'index.md'
    if not root_index.exists():
        print("Creating root index.md...")

        # Get top-level directories to list in root navigation
        top_level_dirs = []
        for item in output_dir.iterdir():
            if item.is_dir() and not item.name.startswith('_') and item.name != '404':
                top_level_dirs.append(item.name)

        # Sort directories (you could implement custom ordering here based on weight)
        top_level_dirs.sort()

        # Create root index content
        root_content = f"""# Documentation

Welcome to the documentation.

## Pages in this section
"""

        for dir_name in top_level_dirs:
            # Convert directory names to proper titles
            title = dir_name.replace('-', ' ').title()
            if dir_name == 'user-guide':
                title = 'User Guide'
            elif dir_name == 'api-reference':
                title = 'API Reference'
            elif dir_name == 'release-notes':
                title = 'Release Notes'

            root_content += f"- [{title}]({dir_name}/)\n"

        root_content += f"""
---
**Source**: _index.md
**URL**: /docs/v2/{args.variant}/
"""

        with open(root_index, 'w', encoding='utf-8') as f:
            f.write(root_content)

    # Restructure single pages (directories with only index.txt)
    # to be named files instead of directory/index.txt
    restructure_single_pages(output_dir)

    # Now that the final structure is in place, fix all internal links
    print("Converting internal links to proper .md references...")
    fix_internal_links_post_processing(output_dir, args.variant)

    # Check that all internal links have been properly converted
    check_internal_links(output_dir)

    print(f"Processing complete. Output in: {output_dir}")
    return 0


def restructure_single_pages(output_dir: Path):
    """
    Restructure single pages from {dir}/index.md to {parent}/{dirname}.md
    for directories that only contain index.md (no subdirectories or other files).
    """
    print("Restructuring single pages...")

    # Find all directories that contain only index.md
    single_page_dirs = []

    for root, dirs, files in os.walk(output_dir):
        root_path = Path(root)

        # Skip the root output directory itself
        if root_path == output_dir:
            continue

        # Check if this directory contains only index.md
        if len(files) == 1 and files[0] == 'index.md' and len(dirs) == 0:
            single_page_dirs.append(root_path)

    # Process each single page directory
    for dir_path in single_page_dirs:
        index_file = dir_path / 'index.md'
        parent_dir = dir_path.parent
        new_filename = f"{dir_path.name}.md"
        new_file_path = parent_dir / new_filename

        print(f"  Moving {index_file.relative_to(output_dir)} -> {new_file_path.relative_to(output_dir)}")

        try:
            # Move the index.md to the new location
            index_file.rename(new_file_path)

            # Remove the now-empty directory
            dir_path.rmdir()

        except Exception as e:
            print(f"    Error restructuring {dir_path}: {e}")


def fix_internal_links_post_processing(output_dir: Path, variant: str):
    """
    Fix all internal links after the final file structure is in place.
    """
    link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
    fixed_count = 0
    total_files = 0

    for md_file in output_dir.rglob('*.md'):
        total_files += 1
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content

            def replace_link(match):
                nonlocal fixed_count
                link_text, link_url = match.groups()

                # Skip external links (http/https/mailto/ftp/etc)
                if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link_url):
                    return match.group(0)

                # Skip anchor-only links
                if link_url.startswith('#'):
                    return match.group(0)

                # Split URL and anchor
                url_parts = link_url.split('#', 1)
                base_url = url_parts[0]
                anchor = '#' + url_parts[1] if len(url_parts) > 1 else ''

                if not base_url:  # Empty base URL means anchor-only
                    return match.group(0)

                # Skip if it already points to a .md file
                if base_url.endswith('.md'):
                    return match.group(0)

                # Convert Hugo-style path to final .md file reference
                current_dir = md_file.parent
                try:
                    if base_url.startswith('/'):
                        # Absolute path - convert to relative from current file
                        base_url = base_url.lstrip('/')
                        target_path = output_dir / base_url
                    else:
                        # Relative path from current file
                        target_path = (current_dir / base_url).resolve()

                    # Now check what actually exists in the final structure
                    if target_path.exists():
                        if target_path.is_dir():
                            # Directory exists, link to index.md
                            if (target_path / 'index.md').exists():
                                rel_path = os.path.relpath(target_path / 'index.md', current_dir)
                                fixed_count += 1
                                return f'[{link_text}]({rel_path}{anchor})'
                        elif target_path.is_file() and target_path.suffix == '.md':
                            # .md file exists
                            rel_path = os.path.relpath(target_path, current_dir)
                            fixed_count += 1
                            return f'[{link_text}]({rel_path}{anchor})'

                    # Check if there's a corresponding .md file
                    md_file_path = target_path.with_suffix('.md')
                    if md_file_path.exists():
                        rel_path = os.path.relpath(md_file_path, current_dir)
                        fixed_count += 1
                        return f'[{link_text}]({rel_path}{anchor})'

                    # Check if there's a directory with index.md
                    if (target_path / 'index.md').exists():
                        rel_path = os.path.relpath(target_path / 'index.md', current_dir)
                        fixed_count += 1
                        return f'[{link_text}]({rel_path}{anchor})'

                    # Special handling for directory links (ending with /)
                    if base_url.endswith('/'):
                        dir_path = target_path.parent / target_path.name.rstrip('/')
                        if (dir_path / 'index.md').exists():
                            rel_path = os.path.relpath(dir_path / 'index.md', current_dir)
                            fixed_count += 1
                            return f'[{link_text}]({rel_path}{anchor})'

                except Exception as e:
                    pass

                # If we can't resolve it, keep the original
                return match.group(0)

            # Apply the replacements
            content = re.sub(link_pattern, replace_link, content)

            # Write back if changed
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)

        except Exception as e:
            print(f"Error fixing links in {md_file.relative_to(output_dir)}: {e}")

    print(f"Fixed {fixed_count} internal links across {total_files} files")


def check_internal_links(output_dir: Path):
    """
    Check that all internal links in the processed markdown files point to actual files.
    """
    print("Checking internal links...")

    issues = []
    total_links = 0
    valid_links = 0

    # Pattern to match markdown links that are not external
    link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'

    for md_file in output_dir.rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            for match in re.finditer(link_pattern, content):
                link_text, link_url = match.groups()
                total_links += 1

                # Skip external links (http/https/mailto/ftp/etc)
                if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link_url):
                    valid_links += 1
                    continue

                # Skip anchor-only links
                if link_url.startswith('#'):
                    valid_links += 1
                    continue

                # Check if link points to an actual file
                url_parts = link_url.split('#', 1)
                base_url = url_parts[0]

                if not base_url:  # Empty base URL means anchor-only
                    valid_links += 1
                    continue

                # Resolve the link relative to the current file
                current_dir = md_file.parent
                try:
                    if base_url.startswith('/'):
                        # Absolute path - this shouldn't happen in our processed files
                        issues.append(f"{md_file.relative_to(output_dir)}: Absolute path link '{link_url}'")
                        continue
                    else:
                        # Relative path from current file
                        target_path = (current_dir / base_url).resolve()

                    # Check if target exists
                    if target_path.exists() and target_path.is_file():
                        if target_path.suffix == '.md':
                            valid_links += 1
                        else:
                            issues.append(f"{md_file.relative_to(output_dir)}: Link points to non-markdown file '{link_url}' -> {target_path.relative_to(output_dir)}")
                    else:
                        issues.append(f"{md_file.relative_to(output_dir)}: Broken link '{link_url}' -> target not found")

                except Exception as e:
                    issues.append(f"{md_file.relative_to(output_dir)}: Error checking link '{link_url}': {e}")

        except Exception as e:
            issues.append(f"Error reading {md_file.relative_to(output_dir)}: {e}")

    # Report results
    print(f"Link check complete: {valid_links}/{total_links} links are valid")

    if issues:
        print(f"Found {len(issues)} link issues:")
        for issue in issues[:20]:  # Show first 20 issues
            print(f"  {issue}")
        if len(issues) > 20:
            print(f"  ... and {len(issues) - 20} more issues")
    else:
        print("✅ All internal links are properly formatted and point to existing files!")


if __name__ == '__main__':
    exit(main())