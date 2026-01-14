"""Test execution logic for search audit."""

from typing import Any

from .algolia_client import AlgoliaClient, SearchResponse
from .scoring import RelevanceScorer, TestResult, TestStatus


class TestRunner:
    """Execute search audit tests."""

    def __init__(
        self,
        client: AlgoliaClient,
        scorer: RelevanceScorer | None = None,
        verbose: bool = False,
    ):
        self.client = client
        self.scorer = scorer or RelevanceScorer()
        self.verbose = verbose

    def run_relevance_test(
        self,
        test: dict[str, Any],
        variant: str,
        version: str = "v2",
    ) -> list[TestResult]:
        """
        Run a relevance test - verify expected URLs appear in top positions.

        Args:
            test: Test definition with query, expected_urls, etc.
            variant: Variant to test
            version: Version to test

        Returns:
            List of TestResult (one per expected URL)
        """
        query = test["query"]
        results = []

        # Execute search
        response = self.client.search(
            query=query,
            variant=variant,
            version=version,
        )

        if self.verbose:
            print(f"  Query: '{query}' -> {response.total_hits} hits")

        # Check each expected URL
        for expected in test.get("expected_urls", []):
            expected_url = expected["url"]
            min_pos, max_pos = expected.get("position_range", [1, 10])

            # Find expected URL in results
            found_position = None
            found_url = None
            for hit in response.hits:
                if self.scorer.url_matches(hit.url, expected_url):
                    found_position = hit.position
                    found_url = hit.url
                    break

            # Determine status
            if found_position is None:
                status = TestStatus.FAIL
                score = 0.0
                details = f"Not found in top {len(response.hits)} results"
            elif min_pos <= found_position <= max_pos:
                status = TestStatus.PASS
                score = self.scorer.score_position(found_position)
                details = f"Found at position {found_position}"
            else:
                status = TestStatus.FAIL
                score = self.scorer.score_position(found_position) * 0.5
                details = f"Position {found_position}, expected {min_pos}-{max_pos}"

            results.append(
                TestResult(
                    name=test.get("name", f"Relevance: {query}"),
                    test_type="relevance",
                    status=status,
                    query=query,
                    expected_url=expected_url,
                    found_url=found_url,
                    found_position=found_position,
                    expected_position_range=(min_pos, max_pos),
                    response_time_ms=response.response_time_ms,
                    total_hits=response.total_hits,
                    score=score,
                    details=details,
                    variant=variant,
                )
            )

        return results

    def run_coverage_test(
        self,
        test: dict[str, Any],
    ) -> TestResult:
        """
        Run a coverage test - verify page is findable by its title/heading.

        Args:
            test: Test definition with query, expected_url, max_position

        Returns:
            TestResult
        """
        query = test["query"]
        variant = test.get("variant")
        version = test.get("version", "v2")
        expected_url = test["expected_url"]
        max_position = test.get("max_position", 5)

        # Execute search
        response = self.client.search(
            query=query,
            variant=variant,
            version=version,
        )

        # Find expected URL
        found_position = None
        found_url = None
        for hit in response.hits:
            if self.scorer.url_matches(hit.url, expected_url):
                found_position = hit.position
                found_url = hit.url
                break

        # Determine status
        if found_position is None:
            status = TestStatus.FAIL
            score = 0.0
            details = f"Page not found for query '{query}'"
        elif found_position <= max_position:
            status = TestStatus.PASS
            score = self.scorer.score_position(found_position)
            details = f"Found at position {found_position}"
        else:
            status = TestStatus.WARN
            score = self.scorer.score_position(found_position)
            details = f"Position {found_position}, expected top {max_position}"

        return TestResult(
            name=test.get("name", f"Coverage: {query[:30]}"),
            test_type="coverage",
            status=status,
            query=query,
            expected_url=expected_url,
            found_url=found_url,
            found_position=found_position,
            expected_position_range=(1, max_position),
            response_time_ms=response.response_time_ms,
            total_hits=response.total_hits,
            score=score,
            details=details,
            variant=variant,
            auto_generated=test.get("auto_generated", False),
        )

    def run_zero_result_test(
        self,
        query: str,
        variant: str,
        version: str = "v2",
    ) -> TestResult:
        """
        Run a zero-result test - verify query returns at least one result.

        Args:
            query: Search query
            variant: Variant to test
            version: Version to test

        Returns:
            TestResult
        """
        response = self.client.search(
            query=query,
            variant=variant,
            version=version,
        )

        if response.total_hits > 0:
            status = TestStatus.PASS
            details = f"Found {response.total_hits} results"
        else:
            status = TestStatus.FAIL
            details = "No results found"

        return TestResult(
            name=f"Zero-result: {query}",
            test_type="zero_result",
            status=status,
            query=query,
            response_time_ms=response.response_time_ms,
            total_hits=response.total_hits,
            score=1.0 if response.total_hits > 0 else 0.0,
            details=details,
            variant=variant,
        )

    def run_facet_test(
        self,
        variant: str,
        version: str = "v2",
    ) -> TestResult:
        """
        Run a facet test - verify variant filter returns only that variant's pages.

        Args:
            variant: Variant to test
            version: Version to test

        Returns:
            TestResult
        """
        # Search with variant filter
        response = self.client.search(
            query="",  # Empty query to get all results
            variant=variant,
            version=version,
            hits_per_page=50,
        )

        # Check that all results are from the expected variant
        wrong_variant_count = 0
        for hit in response.hits:
            # Check if URL contains the expected variant
            if f"/{variant}/" not in hit.url and f"/docs/{version}/{variant}" not in hit.url:
                wrong_variant_count += 1

        if wrong_variant_count == 0:
            status = TestStatus.PASS
            details = f"All {len(response.hits)} results from {variant}"
        else:
            status = TestStatus.FAIL
            details = f"{wrong_variant_count}/{len(response.hits)} results from wrong variant"

        return TestResult(
            name=f"Facet: {variant}",
            test_type="facet",
            status=status,
            query=f"variant:{variant}",
            response_time_ms=response.response_time_ms,
            total_hits=response.total_hits,
            score=1.0 - (wrong_variant_count / max(len(response.hits), 1)),
            details=details,
            variant=variant,
        )

    def run_performance_test(
        self,
        query: str,
        variant: str,
        version: str = "v2",
        max_time_ms: int = 500,
        warn_time_ms: int = 200,
    ) -> TestResult:
        """
        Run a performance test - verify search completes within time threshold.

        Args:
            query: Search query
            variant: Variant to test
            version: Version to test
            max_time_ms: Maximum acceptable response time
            warn_time_ms: Warning threshold

        Returns:
            TestResult
        """
        response = self.client.search(
            query=query,
            variant=variant,
            version=version,
        )

        if response.response_time_ms <= warn_time_ms:
            status = TestStatus.PASS
            details = f"Response time: {response.response_time_ms}ms"
        elif response.response_time_ms <= max_time_ms:
            status = TestStatus.WARN
            details = f"Slow response: {response.response_time_ms}ms (warn threshold: {warn_time_ms}ms)"
        else:
            status = TestStatus.FAIL
            details = f"Too slow: {response.response_time_ms}ms (max: {max_time_ms}ms)"

        return TestResult(
            name=f"Performance: {query}",
            test_type="performance",
            status=status,
            query=query,
            response_time_ms=response.response_time_ms,
            total_hits=response.total_hits,
            score=max(0.0, 1.0 - (response.response_time_ms / max_time_ms)),
            details=details,
            variant=variant,
        )
