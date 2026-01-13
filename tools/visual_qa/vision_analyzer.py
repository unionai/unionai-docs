"""Vision analysis using Claude API for visual QA."""

import asyncio
import base64
import json
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

ANALYSIS_PROMPT = """You are a documentation QA specialist reviewing a rendered documentation page screenshot.

Analyze this screenshot for ANY rendering or visual issues. Report problems in these categories:

1. **Layout Issues**: Overlapping elements, misaligned content, broken grid/flexbox layouts, elements outside viewport
2. **Typography Issues**: Truncated text, text overflow, unreadable font sizes, broken text wrapping
3. **Image Issues**: Missing images (broken image icons), improperly sized images, images that don't load
4. **Navigation Issues**: Broken menus, sidebar problems, breadcrumb issues, missing navigation elements
5. **Code Block Issues**: Syntax highlighting problems, horizontal scroll issues, truncated code
6. **Component Issues**: Broken tabs, accordions, tooltips, or other UI components not rendering correctly
7. **Responsive Issues**: Content not adapting properly to viewport size
8. **Styling Issues**: Missing CSS (unstyled elements), wrong colors, missing icons

For each issue found, provide:
- severity: "critical" (blocks usage), "major" (significant visual problem), "minor" (cosmetic)
- category: one of the categories above
- description: clear description of what's wrong
- location: approximate location on page (top/middle/bottom, left/center/right)

If the page renders correctly with no issues, respond with an empty issues array.

Respond in this exact JSON format:
{
  "page_url": "<the page URL>",
  "overall_status": "pass" | "fail",
  "issues": [
    {
      "severity": "critical" | "major" | "minor",
      "category": "<category>",
      "description": "<description>",
      "location": "<location>"
    }
  ],
  "summary": "<one sentence summary>"
}"""


@dataclass
class AnalysisIssue:
    """A single issue found during visual analysis."""

    severity: str  # critical, major, minor
    category: str
    description: str
    location: str


@dataclass
class AnalysisResult:
    """Result of analyzing a single screenshot."""

    page_url: str
    screenshot_path: Path
    overall_status: str  # pass, fail
    issues: list[AnalysisIssue] = field(default_factory=list)
    summary: str = ""
    error: Optional[str] = None

    @property
    def has_critical(self) -> bool:
        """Return True if any critical issues were found."""
        return any(i.severity == "critical" for i in self.issues)

    @property
    def has_major(self) -> bool:
        """Return True if any major issues were found."""
        return any(i.severity == "major" for i in self.issues)


class VisionAnalyzer:
    """Analyze screenshots using Claude Vision API."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-sonnet-4-20250514",
        batch_size: int = 10,
        batch_delay: float = 5.0,
        max_retries: int = 3,
    ):
        """
        Initialize the vision analyzer.

        Args:
            api_key: Anthropic API key (defaults to ANTHROPIC_API_KEY env var)
            model: Claude model to use for vision analysis
            batch_size: Number of images to process per batch
            batch_delay: Delay in seconds between batches
            max_retries: Maximum retries for failed API calls
        """
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY environment variable or api_key parameter required"
            )

        self.model = model
        self.batch_size = batch_size
        self.batch_delay = batch_delay
        self.max_retries = max_retries

        try:
            import anthropic

            self.client = anthropic.Anthropic(api_key=self.api_key)
        except ImportError:
            raise ImportError(
                "anthropic package is required. Install with: pip install anthropic"
            )

    def _encode_image(self, image_path: Path) -> str:
        """Encode image to base64."""
        with open(image_path, "rb") as f:
            return base64.standard_b64encode(f.read()).decode("utf-8")

    def _parse_response(self, response_text: str, page_url: str) -> dict:
        """Parse JSON response from Claude, handling markdown code blocks."""
        text = response_text.strip()

        # Handle markdown code block wrapping
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0]
        elif "```" in text:
            text = text.split("```")[1].split("```")[0]

        try:
            return json.loads(text.strip())
        except json.JSONDecodeError as e:
            return {
                "page_url": page_url,
                "overall_status": "fail",
                "issues": [
                    {
                        "severity": "critical",
                        "category": "Analysis Error",
                        "description": f"Failed to parse Claude response: {e}",
                        "location": "N/A",
                    }
                ],
                "summary": "Analysis failed due to response parsing error",
            }

    def analyze_screenshot(
        self, screenshot_path: Path, page_url: str
    ) -> AnalysisResult:
        """
        Analyze a single screenshot for visual issues.

        Args:
            screenshot_path: Path to the screenshot image
            page_url: URL of the page (for context)

        Returns:
            AnalysisResult with findings
        """
        for attempt in range(self.max_retries):
            try:
                image_data = self._encode_image(screenshot_path)

                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=2000,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "image",
                                    "source": {
                                        "type": "base64",
                                        "media_type": "image/png",
                                        "data": image_data,
                                    },
                                },
                                {
                                    "type": "text",
                                    "text": f"Page URL: {page_url}\n\n{ANALYSIS_PROMPT}",
                                },
                            ],
                        }
                    ],
                )

                response_text = response.content[0].text
                parsed = self._parse_response(response_text, page_url)

                issues = [
                    AnalysisIssue(
                        severity=i.get("severity", "minor"),
                        category=i.get("category", "Unknown"),
                        description=i.get("description", ""),
                        location=i.get("location", ""),
                    )
                    for i in parsed.get("issues", [])
                ]

                return AnalysisResult(
                    page_url=page_url,
                    screenshot_path=screenshot_path,
                    overall_status=parsed.get("overall_status", "fail"),
                    issues=issues,
                    summary=parsed.get("summary", ""),
                )

            except Exception as e:
                if attempt == self.max_retries - 1:
                    return AnalysisResult(
                        page_url=page_url,
                        screenshot_path=screenshot_path,
                        overall_status="fail",
                        error=str(e),
                        summary=f"Analysis failed: {e}",
                    )
                # Exponential backoff
                time.sleep(2**attempt)

        # Should not reach here, but just in case
        return AnalysisResult(
            page_url=page_url,
            screenshot_path=screenshot_path,
            overall_status="fail",
            error="Max retries exceeded",
            summary="Analysis failed after max retries",
        )

    async def analyze_batch(
        self, screenshots: list[tuple[Path, str]]
    ) -> list[AnalysisResult]:
        """
        Analyze multiple screenshots with rate limiting.

        Args:
            screenshots: List of (screenshot_path, page_url) tuples

        Returns:
            List of AnalysisResult objects
        """
        results = []

        for i in range(0, len(screenshots), self.batch_size):
            batch = screenshots[i : i + self.batch_size]

            # Process batch (sync calls wrapped in executor for async context)
            loop = asyncio.get_event_loop()
            batch_results = await asyncio.gather(
                *[
                    loop.run_in_executor(
                        None, self.analyze_screenshot, screenshot_path, page_url
                    )
                    for screenshot_path, page_url in batch
                ]
            )

            results.extend(batch_results)

            # Rate limit: delay between batches
            if i + self.batch_size < len(screenshots):
                await asyncio.sleep(self.batch_delay)

        return results
