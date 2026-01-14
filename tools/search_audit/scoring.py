"""Scoring algorithms and metrics for search audit results."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class TestStatus(Enum):
    """Test result status."""

    PASS = "pass"
    FAIL = "fail"
    WARN = "warn"
    SKIP = "skip"


@dataclass
class TestResult:
    """Result of a single test case."""

    name: str
    test_type: str  # relevance, coverage, zero_result, facet, performance
    status: TestStatus
    query: str
    expected_url: Optional[str] = None
    found_url: Optional[str] = None
    found_position: Optional[int] = None
    expected_position_range: Optional[tuple[int, int]] = None
    response_time_ms: int = 0
    total_hits: int = 0
    score: float = 0.0  # 0.0 to 1.0
    details: str = ""
    variant: Optional[str] = None
    auto_generated: bool = False


@dataclass
class AggregateMetrics:
    """Aggregated metrics across all tests."""

    total_tests: int = 0
    passed: int = 0
    failed: int = 0
    warnings: int = 0
    skipped: int = 0

    # By type
    by_type: dict[str, dict[str, int]] = field(default_factory=dict)

    # Performance
    avg_response_time_ms: float = 0.0
    max_response_time_ms: int = 0
    p95_response_time_ms: float = 0.0

    # Scores
    avg_relevance_score: float = 0.0
    coverage_percentage: float = 0.0
    zero_result_count: int = 0

    @property
    def pass_rate(self) -> float:
        """Calculate overall pass rate."""
        if self.total_tests == 0:
            return 0.0
        return self.passed / self.total_tests

    @property
    def overall_status(self) -> TestStatus:
        """Determine overall audit status."""
        if self.failed > 0:
            return TestStatus.FAIL
        if self.warnings > 0:
            return TestStatus.WARN
        return TestStatus.PASS


class RelevanceScorer:
    """Calculate relevance scores based on position."""

    # Reciprocal rank scoring
    DEFAULT_WEIGHTS = {
        1: 1.0,
        2: 0.5,
        3: 0.33,
        4: 0.25,
        5: 0.2,
        6: 0.17,
        7: 0.14,
        8: 0.125,
        9: 0.11,
        10: 0.1,
    }

    def __init__(self, position_weights: Optional[dict[int, float]] = None):
        self.position_weights = position_weights or self.DEFAULT_WEIGHTS

    def score_position(self, position: int) -> float:
        """
        Score a result based on its position.

        Returns:
            Score between 0.0 and 1.0
        """
        if position in self.position_weights:
            return self.position_weights[position]
        elif position > 10:
            return 1.0 / position  # Reciprocal rank
        return 0.0

    def url_matches(self, actual_url: str, expected_url: str) -> bool:
        """Check if URLs match, handling variations."""
        # Normalize URLs
        actual = actual_url.rstrip("/").lower()
        expected = expected_url.rstrip("/").lower()

        # Exact match
        if actual == expected:
            return True

        # Suffix match (expected is a path suffix)
        if actual.endswith(expected):
            return True

        # Expected is contained in actual
        if expected in actual:
            return True

        return False


class ResultAggregator:
    """Aggregate test results into summary metrics."""

    def aggregate(self, results: list[TestResult]) -> AggregateMetrics:
        """Aggregate a list of test results."""
        metrics = AggregateMetrics()

        if not results:
            return metrics

        metrics.total_tests = len(results)

        response_times = []
        relevance_scores = []
        coverage_found = 0
        coverage_total = 0
        type_counts: dict[str, dict[str, int]] = {}

        for result in results:
            # Initialize type counter if needed
            if result.test_type not in type_counts:
                type_counts[result.test_type] = {"pass": 0, "fail": 0, "warn": 0, "skip": 0}

            # Count by status
            if result.status == TestStatus.PASS:
                metrics.passed += 1
                type_counts[result.test_type]["pass"] += 1
            elif result.status == TestStatus.FAIL:
                metrics.failed += 1
                type_counts[result.test_type]["fail"] += 1
            elif result.status == TestStatus.WARN:
                metrics.warnings += 1
                type_counts[result.test_type]["warn"] += 1
            else:
                metrics.skipped += 1
                type_counts[result.test_type]["skip"] += 1

            # Performance tracking
            if result.response_time_ms > 0:
                response_times.append(result.response_time_ms)

            # Relevance scores
            if result.score > 0:
                relevance_scores.append(result.score)

            # Coverage tracking
            if result.test_type == "coverage":
                coverage_total += 1
                if result.status == TestStatus.PASS:
                    coverage_found += 1

            # Zero result tracking
            if result.total_hits == 0 and result.test_type != "zero_result":
                metrics.zero_result_count += 1

        # Calculate aggregates
        if response_times:
            response_times.sort()
            metrics.avg_response_time_ms = sum(response_times) / len(response_times)
            metrics.max_response_time_ms = max(response_times)
            p95_idx = int(len(response_times) * 0.95)
            metrics.p95_response_time_ms = (
                response_times[p95_idx] if p95_idx < len(response_times) else response_times[-1]
            )

        if relevance_scores:
            metrics.avg_relevance_score = sum(relevance_scores) / len(relevance_scores)

        if coverage_total > 0:
            metrics.coverage_percentage = coverage_found / coverage_total

        metrics.by_type = type_counts

        return metrics
