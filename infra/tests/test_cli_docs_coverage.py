#!/usr/bin/env python3
"""
CLI Documentation Coverage Test

This script compares the live CLI help output with the generated markdown documentation
to identify missing static commands and ensure comprehensive coverage.
"""

import subprocess
import re
import sys
from typing import Dict, List, Set, Tuple
from pathlib import Path
import json


class CLICommand:
    """Represents a CLI command with its metadata."""

    def __init__(self, path: str, help_text: str = "", options: List[str] = None):
        self.path = path  # e.g., "flyte run"
        self.help_text = help_text
        self.options = options or []
        self.subcommands = []

    def __str__(self):
        return f"CLICommand({self.path})"

    def __repr__(self):
        return self.__str__()


class CLIDocsTester:
    """Test framework for comparing live CLI help vs generated markdown docs."""

    def __init__(self, flyte_executable: str = "flyte"):
        self.flyte_executable = flyte_executable
        self.live_commands: Dict[str, CLICommand] = {}
        self.markdown_commands: Dict[str, CLICommand] = {}

    def get_live_cli_help(self, command_path: str = "") -> str:
        """Get live CLI help output for a given command path."""
        try:
            cmd = [self.flyte_executable]
            if command_path:
                cmd.extend(command_path.split())
            cmd.append("--help")

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode != 0:
                print(f"Warning: Command '{' '.join(cmd)}' failed with return code {result.returncode}")
                print(f"Stderr: {result.stderr}")
                return ""

            return result.stdout
        except subprocess.TimeoutExpired:
            print(f"Warning: Command '{' '.join(cmd)}' timed out")
            return ""
        except Exception as e:
            print(f"Error running command '{' '.join(cmd)}': {e}")
            return ""

    def parse_live_help_commands(self, help_output: str, parent_path: str = "") -> List[str]:
        """Extract subcommands from live CLI help output."""
        commands = []

        # Look for ALL command sections in rich-click format (including grouped ones)
        command_sections = re.findall(r'╭─[^╯]*?╯', help_output, re.DOTALL)

        for section in command_sections:
            # Skip non-command sections
            if '│ --' in section or 'Options' in section:
                continue

            # Extract command names (only those that start at the beginning of the line after │)
            lines = section.split('\n')
            for line in lines:
                # Match lines that have command format: │ command_name  description
                match = re.match(r'│\s+([a-zA-Z0-9_-]+)\s+(.+)', line)
                if match:
                    cmd_name = match.group(1).strip()
                    # Ensure it's actually a command line (not continuation text)
                    if (cmd_name and
                        not cmd_name.startswith('─') and
                        cmd_name != 'Commands' and
                        # Check that this looks like a command definition line
                        not line.strip().startswith('│          ')):  # continuation lines are indented more
                        commands.append(cmd_name)

        # Also look for simpler format (non-rich output)
        if not commands:
            # Look for "Commands:" section
            commands_match = re.search(r'Commands:\s*\n((?:\s+\w+.*\n?)+)', help_output)
            if commands_match:
                commands_text = commands_match.group(1)
                command_matches = re.findall(r'^\s+(\w+)', commands_text, re.MULTILINE)
                commands.extend(command_matches)

        return commands

    def parse_live_help_options(self, help_output: str) -> List[str]:
        """Extract options from live CLI help output."""
        options = []

        # Look for Options section in rich-click format
        options_section_match = re.search(r'╭─ Options.*?╰────+╯', help_output, re.DOTALL)
        if options_section_match:
            options_section = options_section_match.group(0)
            # Extract option names
            option_matches = re.findall(r'│\s+(--[\w-]+(?:\s+-\w)?)', options_section)
            for option_match in option_matches:
                option_name = option_match.strip().split()[0]  # Take first option if multiple
                if option_name and option_name not in ['--help']:
                    options.append(option_name)

        # Also look for simpler format
        if not options:
            option_matches = re.findall(r'^\s+(--[\w-]+)', help_output, re.MULTILINE)
            options.extend([opt for opt in option_matches if opt != '--help'])

        return options

    def discover_live_commands(self, max_depth: int = 3) -> None:
        """Discover all live CLI commands recursively."""
        def discover_recursive(command_path: str, depth: int):
            if depth > max_depth:
                return

            print(f"Discovering: {command_path or 'flyte'}")
            help_output = self.get_live_cli_help(command_path)

            if not help_output:
                return

            # Extract help text (first paragraph usually)
            help_lines = help_output.split('\n')
            help_text = ""
            for line in help_lines:
                if line.strip() and not line.startswith('Usage:') and not line.startswith('╭'):
                    help_text = line.strip()
                    break

            # Extract options
            options = self.parse_live_help_options(help_output)

            # Store command with consistent naming
            if command_path:
                cmd_key = f"flyte {command_path}"
            else:
                cmd_key = "flyte"
            self.live_commands[cmd_key] = CLICommand(cmd_key, help_text, options)

            # Find subcommands
            subcommands = self.parse_live_help_commands(help_output, command_path)

            # Filter out dynamic/directory-based commands that we expect to be missing
            static_subcommands = []
            dynamic_patterns = ['tools', 'dist', 'include', 'archetypes', 'content', 'public',
                              'layouts', 'static', 'scripts', 'external', 'themes',
                              # Dynamic environments from deployed-task
                              'root_env', 'spark_env', 'torch_env', 'env_1', 'env_2', 'trigger_env',
                              'my_task_env', 'async_example_env', 'my_env']

            for subcmd in subcommands:
                if subcmd not in dynamic_patterns:
                    static_subcommands.append(subcmd)

            self.live_commands[cmd_key].subcommands = static_subcommands

            # Recursively discover subcommands
            for subcmd in static_subcommands:
                next_path = f"{command_path} {subcmd}" if command_path else subcmd
                discover_recursive(next_path, depth + 1)

        print("Discovering live CLI commands...")
        discover_recursive("", 0)

    def parse_markdown_commands(self, markdown_file: Path) -> None:
        """Parse commands from generated markdown documentation."""
        if not markdown_file.exists():
            print(f"Markdown file not found: {markdown_file}")
            return

        content = markdown_file.read_text()

        # Extract all command sections
        command_sections = re.findall(r'^(#{2,})\s+(.+?)$\n\n?(.*?)(?=^#{2,}|\Z)', content, re.MULTILINE | re.DOTALL)

        for header_level, command_path, section_content in command_sections:
            # Clean up command path
            command_path = command_path.strip()

            # Skip non-command sections
            if not command_path.startswith('flyte'):
                continue

            # Extract help text (first paragraph)
            help_lines = section_content.split('\n')
            help_text = ""
            for line in help_lines:
                line = line.strip()
                if line and not line.startswith('|') and not line.startswith('```'):
                    help_text = line
                    break

            # Extract options from table
            options = []
            option_matches = re.findall(r'\|\s*`(--[\w-]+)`', section_content)
            options.extend(option_matches)

            self.markdown_commands[command_path] = CLICommand(command_path, help_text, options)

        print(f"Parsed {len(self.markdown_commands)} commands from markdown")

    def compare_commands(self) -> Dict[str, List[str]]:
        """Compare live CLI commands with markdown documentation."""
        results = {
            'missing_in_markdown': [],
            'missing_in_live': [],
            'option_mismatches': [],
            'help_text_differences': []
        }

        # Find commands missing in markdown
        for cmd_path in self.live_commands:
            if cmd_path not in self.markdown_commands:
                results['missing_in_markdown'].append(cmd_path)

        # Find commands missing in live (shouldn't happen, but check anyway)
        for cmd_path in self.markdown_commands:
            if cmd_path not in self.live_commands:
                results['missing_in_live'].append(cmd_path)

        # Compare options for common commands
        for cmd_path in self.live_commands:
            if cmd_path in self.markdown_commands:
                live_cmd = self.live_commands[cmd_path]
                md_cmd = self.markdown_commands[cmd_path]

                live_options = set(live_cmd.options)
                md_options = set(md_cmd.options)

                if live_options != md_options:
                    missing_in_md = live_options - md_options
                    extra_in_md = md_options - live_options
                    results['option_mismatches'].append({
                        'command': cmd_path,
                        'missing_in_markdown': list(missing_in_md),
                        'extra_in_markdown': list(extra_in_md)
                    })

        return results

    def run_test(self, markdown_file: Path) -> bool:
        """Run the complete test suite."""
        print("=" * 80)
        print("CLI DOCUMENTATION COVERAGE TEST")
        print("=" * 80)

        # Discover live commands
        self.discover_live_commands()
        print(f"Discovered {len(self.live_commands)} live commands")

        # Parse markdown
        self.parse_markdown_commands(markdown_file)

        # Compare
        results = self.compare_commands()

        # Report results
        has_issues = False

        print("\n" + "=" * 40)
        print("TEST RESULTS")
        print("=" * 40)

        if results['missing_in_markdown']:
            has_issues = True
            print(f"\n❌ MISSING IN MARKDOWN ({len(results['missing_in_markdown'])}):")
            for cmd in sorted(results['missing_in_markdown']):
                print(f"   • {cmd}")

        if results['missing_in_live']:
            has_issues = True
            print(f"\n⚠️  MISSING IN LIVE CLI ({len(results['missing_in_live'])}):")
            for cmd in sorted(results['missing_in_live']):
                print(f"   • {cmd}")

        if results['option_mismatches']:
            has_issues = True
            print(f"\n⚠️  OPTION MISMATCHES ({len(results['option_mismatches'])}):")
            for mismatch in results['option_mismatches']:
                print(f"   • {mismatch['command']}")
                if mismatch['missing_in_markdown']:
                    print(f"     Missing in markdown: {', '.join(mismatch['missing_in_markdown'])}")
                if mismatch['extra_in_markdown']:
                    print(f"     Extra in markdown: {', '.join(mismatch['extra_in_markdown'])}")

        if not has_issues:
            print("\n✅ ALL TESTS PASSED!")
            print("Live CLI help and markdown documentation are in sync.")

        # Summary statistics
        print(f"\n" + "=" * 40)
        print("SUMMARY")
        print("=" * 40)
        print(f"Live commands discovered: {len(self.live_commands)}")
        print(f"Markdown commands found: {len(self.markdown_commands)}")
        print(f"Commands in sync: {len(self.live_commands) - len(results['missing_in_markdown'])}")
        print(f"Coverage: {((len(self.live_commands) - len(results['missing_in_markdown'])) / max(len(self.live_commands), 1)) * 100:.1f}%")

        return not has_issues


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        markdown_file = Path(sys.argv[1])
    else:
        markdown_file = Path("content/api-reference/flyte-cli.md")

    tester = CLIDocsTester()
    success = tester.run_test(markdown_file)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()