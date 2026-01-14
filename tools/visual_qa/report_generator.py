"""Report generation for visual QA results."""

import json
import os
from datetime import datetime
from pathlib import Path

from .vision_analyzer import AnalysisResult


def generate_github_summary(results: list[AnalysisResult]) -> str:
    """
    Generate a GitHub Actions summary markdown report.

    Args:
        results: List of AnalysisResult objects

    Returns:
        Markdown formatted summary
    """
    passed = [r for r in results if r.overall_status == "pass"]
    failed = [r for r in results if r.overall_status == "fail"]

    critical_results = [r for r in results if r.has_critical]
    major_results = [r for r in results if r.has_major and not r.has_critical]
    minor_results = [
        r
        for r in results
        if r.issues and not r.has_critical and not r.has_major
    ]
    error_results = [r for r in results if r.error]

    summary = f"""## Visual QA Results

| Status | Count |
|--------|-------|
| Passed | {len(passed)} |
| Failed | {len(failed)} |
| Critical Issues | {len(critical_results)} |
| Major Issues | {len(major_results)} |
| Minor Issues | {len(minor_results)} |
| Errors | {len(error_results)} |

"""

    if error_results:
        summary += "### Errors\n\n"
        summary += "The following pages could not be analyzed:\n\n"
        for result in error_results:
            summary += f"- **{result.page_url}**: {result.error}\n"
        summary += "\n"

    if critical_results:
        summary += "### Critical Issues\n\n"
        summary += "These issues block page usability and must be fixed:\n\n"
        for result in critical_results:
            summary += f"#### {result.page_url}\n\n"
            for issue in result.issues:
                if issue.severity == "critical":
                    summary += f"- **{issue.category}** ({issue.location}): {issue.description}\n"
            summary += "\n"

    if major_results:
        summary += "### Major Issues\n\n"
        summary += "Significant visual problems that should be addressed:\n\n"
        for result in major_results:
            summary += f"#### {result.page_url}\n\n"
            for issue in result.issues:
                if issue.severity == "major":
                    summary += f"- **{issue.category}** ({issue.location}): {issue.description}\n"
            summary += "\n"

    if minor_results:
        summary += "<details>\n<summary>Minor Issues (click to expand)</summary>\n\n"
        for result in minor_results:
            summary += f"#### {result.page_url}\n\n"
            for issue in result.issues:
                if issue.severity == "minor":
                    summary += f"- **{issue.category}** ({issue.location}): {issue.description}\n"
            summary += "\n"
        summary += "</details>\n\n"

    if passed and not (critical_results or major_results or minor_results):
        summary += "All pages rendered correctly with no visual issues detected.\n"

    return summary


def write_github_summary(summary: str) -> None:
    """
    Write summary to GitHub Actions summary file.

    Args:
        summary: Markdown formatted summary
    """
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a") as f:
            f.write(summary)


def save_json_report(results: list[AnalysisResult], output_path: Path) -> None:
    """
    Save detailed JSON report.

    Args:
        results: List of AnalysisResult objects
        output_path: Path to save the JSON report
    """
    report = {
        "timestamp": datetime.now().isoformat(),
        "total_pages": len(results),
        "passed": len([r for r in results if r.overall_status == "pass"]),
        "failed": len([r for r in results if r.overall_status == "fail"]),
        "by_severity": {
            "critical": len([r for r in results if r.has_critical]),
            "major": len([r for r in results if r.has_major]),
            "minor": len(
                [r for r in results if r.issues and not r.has_critical and not r.has_major]
            ),
        },
        "results": [
            {
                "page_url": r.page_url,
                "screenshot_path": str(r.screenshot_path),
                "overall_status": r.overall_status,
                "summary": r.summary,
                "error": r.error,
                "issues": [
                    {
                        "severity": i.severity,
                        "category": i.category,
                        "description": i.description,
                        "location": i.location,
                    }
                    for i in r.issues
                ],
            }
            for r in results
        ],
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)


def determine_exit_code(results: list[AnalysisResult], fail_on: str = "critical") -> int:
    """
    Determine exit code based on issue severity.

    Args:
        results: List of AnalysisResult objects
        fail_on: Severity level to fail on (critical, major, minor)

    Returns:
        0 for success, 1 for failure
    """
    has_critical = any(r.has_critical for r in results)
    has_major = any(r.has_major for r in results)
    has_minor = any(r.issues for r in results)
    has_error = any(r.error for r in results)

    # Errors always cause failure
    if has_error:
        return 1

    if fail_on == "critical" and has_critical:
        return 1
    if fail_on == "major" and (has_critical or has_major):
        return 1
    if fail_on == "minor" and (has_critical or has_major or has_minor):
        return 1

    return 0


def print_console_summary(results: list[AnalysisResult]) -> None:
    """
    Print a brief summary to console.

    Args:
        results: List of AnalysisResult objects
    """
    passed = len([r for r in results if r.overall_status == "pass"])
    failed = len([r for r in results if r.overall_status == "fail"])
    critical = len([r for r in results if r.has_critical])
    major = len([r for r in results if r.has_major])
    errors = len([r for r in results if r.error])

    print(f"\nVisual QA Summary:")
    print(f"  Total pages: {len(results)}")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    if critical:
        print(f"  Critical issues: {critical}")
    if major:
        print(f"  Major issues: {major}")
    if errors:
        print(f"  Errors: {errors}")
