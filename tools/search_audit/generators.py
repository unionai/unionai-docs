"""Auto-generate test cases from documentation content."""

import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


@dataclass
class PageInfo:
    """Information about a documentation page."""

    url: str
    title: str
    variant: str
    version: str


class SitemapTestGenerator:
    """Generate coverage tests from sitemap.xml files."""

    def __init__(self, dist_path: Path, skip_patterns: list[str] | None = None):
        self.dist_path = dist_path
        self.skip_patterns = skip_patterns or []

    def extract_pages(self, variant: str, version: str = "v2") -> list[PageInfo]:
        """Extract all pages from a variant's sitemap."""
        sitemap_path = self.dist_path / "docs" / version / variant / "sitemap.xml"

        if not sitemap_path.exists():
            return []

        tree = ET.parse(sitemap_path)
        root = tree.getroot()

        # Handle XML namespace
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

        pages = []
        for url_elem in root.findall("sm:url", ns):
            loc = url_elem.find("sm:loc", ns)
            if loc is None or loc.text is None:
                continue

            full_url = loc.text

            # Skip patterns
            if any(re.search(pattern, full_url) for pattern in self.skip_patterns):
                continue

            # Extract path from full URL
            parsed = urlparse(full_url)
            url_path = parsed.path

            # Extract title from URL slug
            slug = url_path.rstrip("/").split("/")[-1]
            if not slug:
                slug = "home"
            title = slug.replace("-", " ").title()

            pages.append(
                PageInfo(
                    url=url_path,
                    title=title,
                    variant=variant,
                    version=version,
                )
            )

        return pages

    def generate_tests(
        self,
        variant: str,
        version: str = "v2",
        max_expected_position: int = 5,
        max_tests: int = 50,
    ) -> list[dict[str, Any]]:
        """
        Generate coverage tests for each page.

        Each test verifies that searching for the page title
        returns that page within the expected position range.
        """
        pages = self.extract_pages(variant, version)

        tests = []
        for page in pages[:max_tests]:
            tests.append(
                {
                    "name": f"Coverage: {page.title}",
                    "query": page.title,
                    "variant": variant,
                    "version": version,
                    "expected_url": page.url,
                    "max_position": max_expected_position,
                    "auto_generated": True,
                    "test_type": "coverage",
                }
            )

        return tests


class LLMsFullTestGenerator:
    """Generate tests from llms-full.txt content."""

    def __init__(self, dist_path: Path):
        self.dist_path = dist_path

    def parse_pages(
        self, variant: str, version: str = "v2"
    ) -> list[tuple[str, str, list[str]]]:
        """
        Parse llms-full.txt and extract pages with their headings.

        Returns:
            List of tuples: (page_url, page_title, [heading1, heading2, ...])
        """
        llms_path = self.dist_path / "docs" / version / variant / "llms-full.txt"

        if not llms_path.exists():
            return []

        content = llms_path.read_text(encoding="utf-8")

        pages = []
        current_url = None
        current_title = None
        current_headings: list[str] = []

        for line in content.split("\n"):
            # Check for page marker: === PAGE: https://... ===
            page_match = re.match(r"=== PAGE: (https?://[^\s]+) ===", line)
            if page_match:
                # Save previous page
                if current_url and current_title:
                    pages.append((current_url, current_title, current_headings))

                full_url = page_match.group(1)
                current_url = urlparse(full_url).path
                current_headings = []
                current_title = None
                continue

            # Check for main title (# heading)
            if current_url and not current_title:
                title_match = re.match(r"^# (.+)$", line)
                if title_match:
                    current_title = title_match.group(1).strip()
                    continue

            # Check for subheadings (## or ###)
            heading_match = re.match(r"^#{2,3}\s+(.+)$", line)
            if heading_match and current_url:
                heading_text = heading_match.group(1).strip()
                # Clean up heading (remove special chars)
                heading_text = re.sub(r"[^\w\s-]", "", heading_text).strip()
                if heading_text and len(heading_text) > 3:
                    current_headings.append(heading_text)

        # Don't forget last page
        if current_url and current_title:
            pages.append((current_url, current_title, current_headings))

        return pages

    def generate_tests(
        self,
        variant: str,
        version: str = "v2",
        max_headings_per_page: int = 2,
        max_tests: int = 50,
    ) -> list[dict[str, Any]]:
        """
        Generate tests that verify key headings lead to their pages.
        """
        pages = self.parse_pages(variant, version)

        tests = []
        for url, title, headings in pages:
            if len(tests) >= max_tests:
                break

            # Test page title
            if title:
                tests.append(
                    {
                        "name": f"Title: {title[:40]}",
                        "query": title,
                        "variant": variant,
                        "version": version,
                        "expected_url": url,
                        "max_position": 5,
                        "auto_generated": True,
                        "test_type": "coverage",
                    }
                )

            # Test top headings
            for heading in headings[:max_headings_per_page]:
                if len(tests) >= max_tests:
                    break
                tests.append(
                    {
                        "name": f"Heading: {heading[:40]}",
                        "query": heading,
                        "variant": variant,
                        "version": version,
                        "expected_url": url,
                        "max_position": 10,
                        "auto_generated": True,
                        "test_type": "coverage",
                    }
                )

        return tests
