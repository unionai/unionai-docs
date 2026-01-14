#!/usr/bin/env python3
"""
Algolia Search Audit Tool

Comprehensive search quality auditing for Union.ai documentation.

Usage:
    python -m tools.search_audit [OPTIONS]

Examples:
    # Run full audit on all variants
    python -m tools.search_audit

    # Run on specific variant
    python -m tools.search_audit --variant byoc

    # Run only curated tests (skip auto-generated)
    python -m tools.search_audit --curated-only

    # Output JSON report
    python -m tools.search_audit --output report.json
"""

import argparse
import sys
from pathlib import Path

import yaml

from .algolia_client import AlgoliaClient
from .generators import LLMsFullTestGenerator, SitemapTestGenerator
from .reports import (
    generate_github_summary,
    generate_json_report,
    print_console_report,
    save_json_report,
    write_github_summary,
)
from .scoring import ResultAggregator, TestResult
from .test_runner import TestRunner


def load_config(config_path: Path) -> dict:
    """Load YAML configuration."""
    with open(config_path) as f:
        return yaml.safe_load(f)


def run_audit(
    config: dict,
    variants: list[str],
    version: str,
    dist_path: Path,
    run_curated: bool = True,
    run_auto: bool = True,
    verbose: bool = False,
) -> list[TestResult]:
    """
    Run the search audit.

    Args:
        config: Configuration dictionary
        variants: List of variants to test
        version: Documentation version
        dist_path: Path to dist directory
        run_curated: Whether to run curated tests
        run_auto: Whether to run auto-generated tests
        verbose: Verbose output

    Returns:
        List of all test results
    """
    # Initialize Algolia client
    algolia_config = config.get("algolia", {})
    client = AlgoliaClient(
        app_id=algolia_config.get("app_id", "ZK72K15QRI"),
        search_key=algolia_config.get("search_key", "59e5451a3db8540ee70dc8dd04fe6287"),
        index_name=algolia_config.get("index_name", "union"),
    )

    runner = TestRunner(client, verbose=verbose)
    all_results: list[TestResult] = []

    for variant in variants:
        print(f"\n{'='*50}")
        print(f"Testing variant: {variant}")
        print("=" * 50)

        # Run curated relevance tests
        if run_curated:
            print("\nRunning curated relevance tests...")
            relevance_tests = config.get("relevance_tests", [])

            # Add variant-specific tests
            variant_tests = config.get("variant_tests", {}).get(variant, [])
            all_tests = relevance_tests + variant_tests

            for test in all_tests:
                results = runner.run_relevance_test(test, variant=variant, version=version)
                all_results.extend(results)

                if verbose:
                    for r in results:
                        status = "PASS" if r.status.value == "pass" else "FAIL"
                        print(f"  [{status}] {r.name}: {r.details}")

            # Run zero-result tests
            print("\nRunning zero-result checks...")
            for check in config.get("zero_result_checks", []):
                query = check if isinstance(check, str) else check.get("query", "")
                result = runner.run_zero_result_test(query, variant=variant, version=version)
                all_results.append(result)

                if verbose:
                    status = "PASS" if result.status.value == "pass" else "FAIL"
                    print(f"  [{status}] {result.query}: {result.details}")

            # Run facet test
            print("\nRunning facet test...")
            result = runner.run_facet_test(variant=variant, version=version)
            all_results.append(result)
            if verbose:
                status = "PASS" if result.status.value == "pass" else "FAIL"
                print(f"  [{status}] {result.name}: {result.details}")

        # Run auto-generated tests
        if run_auto:
            auto_config = config.get("auto_coverage", {})
            if auto_config.get("enabled", True):
                print("\nGenerating and running coverage tests...")

                max_tests = auto_config.get("max_tests_per_variant", 50)
                skip_patterns = auto_config.get("skip_patterns", [])
                max_position = auto_config.get("max_expected_position", 5)

                # Generate from sitemap
                if dist_path.exists():
                    sitemap_gen = SitemapTestGenerator(dist_path, skip_patterns)
                    sitemap_tests = sitemap_gen.generate_tests(
                        variant=variant,
                        version=version,
                        max_expected_position=max_position,
                        max_tests=max_tests // 2,
                    )

                    print(f"  Running {len(sitemap_tests)} sitemap-based tests...")
                    for test in sitemap_tests:
                        result = runner.run_coverage_test(test)
                        all_results.append(result)

                    # Generate from llms-full.txt
                    llms_gen = LLMsFullTestGenerator(dist_path)
                    llms_tests = llms_gen.generate_tests(
                        variant=variant,
                        version=version,
                        max_tests=max_tests // 2,
                    )

                    print(f"  Running {len(llms_tests)} heading-based tests...")
                    for test in llms_tests:
                        result = runner.run_coverage_test(test)
                        all_results.append(result)
                else:
                    print(f"  Warning: dist path not found, skipping auto-generated tests")

    return all_results


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Algolia Search Audit Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).parent / "search_tests.yaml",
        help="Path to test configuration YAML",
    )

    parser.add_argument(
        "--variant",
        choices=["flyte", "byoc", "serverless", "selfmanaged", "all"],
        default="all",
        help="Variant to test (default: all)",
    )

    parser.add_argument(
        "--version",
        default="v2",
        help="Documentation version (default: v2)",
    )

    parser.add_argument(
        "--dist-path",
        type=Path,
        default=Path.cwd() / "dist",
        help="Path to dist directory for auto-generation",
    )

    parser.add_argument(
        "--curated-only",
        action="store_true",
        help="Only run curated tests (skip auto-generated)",
    )

    parser.add_argument(
        "--auto-only",
        action="store_true",
        help="Only run auto-generated tests (skip curated)",
    )

    parser.add_argument(
        "--output",
        type=Path,
        help="Output JSON report to file",
    )

    parser.add_argument(
        "--github-summary",
        action="store_true",
        help="Write GitHub Actions summary",
    )

    parser.add_argument(
        "--no-fail",
        action="store_true",
        help="Don't exit with error code on failures",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output",
    )

    args = parser.parse_args()

    # Load configuration
    if not args.config.exists():
        print(f"Error: Config file not found: {args.config}")
        return 1

    config = load_config(args.config)

    # Determine variants
    if args.variant == "all":
        variants = ["flyte", "byoc", "selfmanaged"]  # serverless often disabled
    else:
        variants = [args.variant]

    # Determine what to run
    run_curated = not args.auto_only
    run_auto = not args.curated_only

    # Run audit
    results = run_audit(
        config=config,
        variants=variants,
        version=args.version,
        dist_path=args.dist_path,
        run_curated=run_curated,
        run_auto=run_auto,
        verbose=args.verbose,
    )

    # Aggregate results
    aggregator = ResultAggregator()
    metrics = aggregator.aggregate(results)

    # Generate reports
    print_console_report(results, metrics)

    if args.output:
        report = generate_json_report(results, metrics, config)
        save_json_report(report, str(args.output))
        print(f"\nJSON report saved to: {args.output}")

    if args.github_summary:
        summary = generate_github_summary(results, metrics)
        write_github_summary(summary)
        print("\nGitHub summary written")

    # Exit code
    if not args.no_fail and metrics.failed > 0:
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
