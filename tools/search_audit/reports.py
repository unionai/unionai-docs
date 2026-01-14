"""Report generation for search audit results."""

import json
import os
from datetime import datetime
from typing import Any

from .scoring import AggregateMetrics, TestResult, TestStatus


def print_console_report(results: list[TestResult], metrics: AggregateMetrics) -> None:
    """Print a summary report to console."""
    # Status emoji
    status_char = {
        TestStatus.PASS: "[PASS]",
        TestStatus.FAIL: "[FAIL]",
        TestStatus.WARN: "[WARN]",
        TestStatus.SKIP: "[SKIP]",
    }

    print("\n" + "=" * 60)
    print("SEARCH AUDIT RESULTS")
    print("=" * 60)

    # Overall status
    overall = status_char.get(metrics.overall_status, "[????]")
    print(f"\nOverall Status: {overall}")

    # Summary table
    print(f"\n{'Metric':<25} {'Value':>10}")
    print("-" * 37)
    print(f"{'Total Tests':<25} {metrics.total_tests:>10}")
    print(f"{'Passed':<25} {metrics.passed:>10}")
    print(f"{'Failed':<25} {metrics.failed:>10}")
    print(f"{'Warnings':<25} {metrics.warnings:>10}")
    print(f"{'Pass Rate':<25} {metrics.pass_rate:>9.1%}")
    print(f"{'Coverage':<25} {metrics.coverage_percentage:>9.1%}")
    print(f"{'Avg Response Time':<25} {metrics.avg_response_time_ms:>7.0f}ms")
    print(f"{'Zero-Result Queries':<25} {metrics.zero_result_count:>10}")

    # By type breakdown
    if metrics.by_type:
        print(f"\n{'Test Type':<20} {'Pass':>8} {'Fail':>8} {'Warn':>8}")
        print("-" * 46)
        for test_type, counts in metrics.by_type.items():
            print(
                f"{test_type:<20} {counts.get('pass', 0):>8} "
                f"{counts.get('fail', 0):>8} {counts.get('warn', 0):>8}"
            )

    # Failed tests
    failed = [r for r in results if r.status == TestStatus.FAIL]
    if failed:
        print(f"\n{'FAILED TESTS':=^60}")
        for result in failed[:20]:
            print(f"\n  {result.name}")
            print(f"    Query: {result.query}")
            print(f"    Expected: {result.expected_url or 'N/A'}")
            print(f"    Found: {result.found_url or 'Not found'} (pos: {result.found_position or '-'})")
            print(f"    Details: {result.details}")

        if len(failed) > 20:
            print(f"\n  ... and {len(failed) - 20} more failed tests")

    # Zero-result queries
    zero_results = [r for r in results if r.total_hits == 0 and r.test_type != "zero_result"]
    if zero_results:
        print(f"\n{'ZERO-RESULT QUERIES':=^60}")
        for result in zero_results[:10]:
            print(f"  - '{result.query}'")

    print("\n" + "=" * 60)


def generate_github_summary(
    results: list[TestResult],
    metrics: AggregateMetrics,
) -> str:
    """Generate GitHub Actions summary in Markdown format."""
    lines = []

    # Header with status
    status_emoji = {
        TestStatus.PASS: ":white_check_mark:",
        TestStatus.FAIL: ":x:",
        TestStatus.WARN: ":warning:",
    }
    overall = status_emoji.get(metrics.overall_status, ":grey_question:")
    lines.append(f"# {overall} Search Audit Results\n")

    # Summary table
    lines.append("## Summary\n")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Total Tests | {metrics.total_tests} |")
    lines.append(f"| Passed | {metrics.passed} |")
    lines.append(f"| Failed | {metrics.failed} |")
    lines.append(f"| Warnings | {metrics.warnings} |")
    lines.append(f"| Pass Rate | {metrics.pass_rate:.1%} |")
    lines.append(f"| Coverage | {metrics.coverage_percentage:.1%} |")
    lines.append(f"| Avg Response Time | {metrics.avg_response_time_ms:.0f}ms |")
    lines.append(f"| Zero-Result Queries | {metrics.zero_result_count} |")
    lines.append("")

    # Failed tests
    failed = [r for r in results if r.status == TestStatus.FAIL]
    if failed:
        lines.append("## :x: Failed Tests\n")
        lines.append("<details>")
        lines.append("<summary>Click to expand</summary>\n")
        lines.append("| Test | Query | Expected | Found | Details |")
        lines.append("|------|-------|----------|-------|---------|")

        for test in failed[:30]:
            expected = test.expected_url or "N/A"
            found = f"pos {test.found_position}" if test.found_position else "Not found"
            lines.append(
                f"| {test.name[:35]} | `{test.query[:20]}` | "
                f"{expected[:25]} | {found} | {test.details[:30]} |"
            )

        if len(failed) > 30:
            lines.append(f"\n*...and {len(failed) - 30} more*")

        lines.append("</details>\n")

    # Zero results
    zero_results = [r for r in results if r.total_hits == 0 and r.test_type != "zero_result"]
    if zero_results:
        lines.append("## :warning: Zero-Result Queries\n")
        for test in zero_results[:10]:
            lines.append(f"- `{test.query}`")
        lines.append("")

    # By type
    if metrics.by_type:
        lines.append("## Results by Type\n")
        lines.append("| Type | Pass | Fail | Warn |")
        lines.append("|------|------|------|------|")
        for test_type, counts in metrics.by_type.items():
            lines.append(
                f"| {test_type} | {counts.get('pass', 0)} | "
                f"{counts.get('fail', 0)} | {counts.get('warn', 0)} |"
            )
        lines.append("")

    return "\n".join(lines)


def write_github_summary(summary: str) -> None:
    """Write summary to GitHub Actions summary file."""
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a") as f:
            f.write(summary)


def generate_json_report(
    results: list[TestResult],
    metrics: AggregateMetrics,
    config: dict[str, Any],
) -> dict[str, Any]:
    """Generate comprehensive JSON report."""
    report = {
        "metadata": {
            "timestamp": datetime.utcnow().isoformat(),
            "algolia_index": config.get("algolia", {}).get("index_name", "unknown"),
            "tool_version": "1.0.0",
        },
        "summary": {
            "total_tests": metrics.total_tests,
            "passed": metrics.passed,
            "failed": metrics.failed,
            "warnings": metrics.warnings,
            "skipped": metrics.skipped,
            "pass_rate": metrics.pass_rate,
            "overall_status": metrics.overall_status.value,
        },
        "metrics": {
            "coverage_percentage": metrics.coverage_percentage,
            "avg_relevance_score": metrics.avg_relevance_score,
            "zero_result_count": metrics.zero_result_count,
            "performance": {
                "avg_response_time_ms": metrics.avg_response_time_ms,
                "max_response_time_ms": metrics.max_response_time_ms,
                "p95_response_time_ms": metrics.p95_response_time_ms,
            },
        },
        "by_type": metrics.by_type,
        "results": [],
    }

    for result in results:
        report["results"].append(
            {
                "name": result.name,
                "type": result.test_type,
                "status": result.status.value,
                "query": result.query,
                "expected_url": result.expected_url,
                "found_url": result.found_url,
                "found_position": result.found_position,
                "expected_position_range": result.expected_position_range,
                "response_time_ms": result.response_time_ms,
                "total_hits": result.total_hits,
                "score": result.score,
                "details": result.details,
                "variant": result.variant,
                "auto_generated": result.auto_generated,
            }
        )

    return report


def save_json_report(report: dict[str, Any], output_path: str) -> None:
    """Save JSON report to file."""
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)
