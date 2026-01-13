#!/usr/bin/env python3
"""
Visual QA tool for documentation site.

Captures screenshots of rendered documentation pages and analyzes them
using Claude Vision API to detect rendering issues.

Usage:
    python -m tools.visual_qa.main --base-url http://localhost:9000

Requirements:
    - playwright: pip install playwright && playwright install chromium
    - anthropic: pip install anthropic
    - pyyaml: pip install pyyaml
    - ANTHROPIC_API_KEY environment variable
"""

import argparse
import asyncio
import sys
from pathlib import Path

import yaml

from .report_generator import (
    determine_exit_code,
    generate_github_summary,
    print_console_summary,
    save_json_report,
    write_github_summary,
)
from .screenshot_capture import ScreenshotCapture
from .vision_analyzer import VisionAnalyzer


def load_config(config_path: Path) -> dict:
    """Load pages configuration from YAML file."""
    with open(config_path) as f:
        return yaml.safe_load(f)


async def run_visual_qa(
    base_url: str,
    config_path: Path,
    output_dir: Path,
    fail_on: str = "critical",
    viewport: str = "desktop",
    variant: str | None = None,
    skip_analysis: bool = False,
) -> int:
    """
    Run the visual QA pipeline.

    Args:
        base_url: Base URL of the documentation server
        config_path: Path to pages.yaml configuration
        output_dir: Directory to save results
        fail_on: Severity level to fail on (critical, major, minor)
        viewport: Viewport(s) to test (desktop, all)
        variant: Optional specific variant to test (flyte, byoc, selfmanaged)
        skip_analysis: If True, only capture screenshots without analysis

    Returns:
        Exit code (0 for success, 1 for failure)
    """
    # Setup output directories
    output_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir = output_dir / "screenshots"
    screenshots_dir.mkdir(exist_ok=True)

    # Load configuration
    print(f"Loading configuration from {config_path}...")
    config = load_config(config_path)

    # Filter viewports if needed
    if viewport == "desktop":
        config["viewports"] = {"desktop": config["viewports"]["desktop"]}

    # Filter variant if specified
    if variant:
        if variant not in config["variants"]:
            print(f"Error: Unknown variant '{variant}'")
            print(f"Available variants: {list(config['variants'].keys())}")
            return 1
        config["variants"] = {variant: config["variants"][variant]}

    # Count total pages
    total_pages = sum(
        len(v.get("key_pages", [])) for v in config["variants"].values()
    )
    total_screenshots = total_pages * len(config["viewports"])
    print(f"Will capture {total_screenshots} screenshots ({total_pages} pages)")

    # Capture screenshots
    print("\nCapturing screenshots...")
    capture = ScreenshotCapture(base_url, screenshots_dir)
    screenshot_results = await capture.capture_all(config)

    # Report capture results
    successful = [r for r in screenshot_results if r.success]
    failed = [r for r in screenshot_results if not r.success]

    print(f"Captured {len(successful)} screenshots successfully")
    if failed:
        print(f"Failed to capture {len(failed)} screenshots:")
        for result in failed:
            print(f"  - {result.full_url}: {result.error}")

    if skip_analysis:
        print("\nSkipping vision analysis (--skip-analysis flag)")
        print(f"Screenshots saved to: {screenshots_dir}")
        return 0 if not failed else 1

    if not successful:
        print("\nNo screenshots captured successfully. Cannot proceed with analysis.")
        return 1

    # Analyze screenshots with Claude Vision
    print("\nAnalyzing screenshots with Claude Vision API...")
    analyzer = VisionAnalyzer()

    screenshots_to_analyze = [
        (result.screenshot_path, result.full_url)
        for result in successful
        if result.screenshot_path
    ]

    analysis_results = await analyzer.analyze_batch(screenshots_to_analyze)

    # Generate reports
    print("\nGenerating reports...")

    # GitHub Actions summary
    summary = generate_github_summary(analysis_results)
    write_github_summary(summary)

    # JSON report
    json_report_path = output_dir / "report.json"
    save_json_report(analysis_results, json_report_path)
    print(f"JSON report saved to: {json_report_path}")

    # Console summary
    print_console_summary(analysis_results)

    # Determine exit code
    exit_code = determine_exit_code(analysis_results, fail_on)

    if exit_code == 0:
        print("\nVisual QA passed!")
    else:
        print(f"\nVisual QA failed with {fail_on} issues")

    return exit_code


def main():
    """Main entry point for CLI."""
    parser = argparse.ArgumentParser(
        description="Visual QA tool for documentation site",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Run full visual QA
    python -m tools.visual_qa.main --base-url http://localhost:9000

    # Only capture screenshots (skip analysis)
    python -m tools.visual_qa.main --base-url http://localhost:9000 --skip-analysis

    # Test a specific variant
    python -m tools.visual_qa.main --base-url http://localhost:9000 --variant flyte

    # Fail on major issues (not just critical)
    python -m tools.visual_qa.main --base-url http://localhost:9000 --fail-on major
        """,
    )
    parser.add_argument(
        "--base-url",
        required=True,
        help="Base URL of the documentation server (e.g., http://localhost:9000)",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).parent / "pages.yaml",
        help="Path to pages.yaml configuration (default: tools/visual_qa/pages.yaml)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("/tmp/visual-qa-results"),
        help="Output directory for screenshots and reports (default: /tmp/visual-qa-results)",
    )
    parser.add_argument(
        "--fail-on",
        choices=["critical", "major", "minor"],
        default="critical",
        help="Severity level to fail on (default: critical)",
    )
    parser.add_argument(
        "--viewport",
        choices=["desktop", "all"],
        default="desktop",
        help="Viewport(s) to test (default: desktop)",
    )
    parser.add_argument(
        "--variant",
        choices=["flyte", "byoc", "selfmanaged"],
        help="Test only a specific variant",
    )
    parser.add_argument(
        "--skip-analysis",
        action="store_true",
        help="Only capture screenshots, skip Claude Vision analysis",
    )

    args = parser.parse_args()

    exit_code = asyncio.run(
        run_visual_qa(
            base_url=args.base_url,
            config_path=args.config,
            output_dir=args.output_dir,
            fail_on=args.fail_on,
            viewport=args.viewport,
            variant=args.variant,
            skip_analysis=args.skip_analysis,
        )
    )

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
