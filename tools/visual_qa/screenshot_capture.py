"""Screenshot capture using Playwright for visual QA."""

import asyncio
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class ScreenshotResult:
    """Result of a screenshot capture operation."""

    variant: str
    page_path: str
    viewport_name: str
    screenshot_path: Optional[Path]
    error: Optional[str] = None

    @property
    def full_url(self) -> str:
        """Return the full URL path for this screenshot."""
        return f"/docs/v2/{self.variant}{self.page_path}"

    @property
    def success(self) -> bool:
        """Return True if screenshot was captured successfully."""
        return self.screenshot_path is not None and self.error is None


class ScreenshotCapture:
    """Capture screenshots of documentation pages using Playwright."""

    def __init__(self, base_url: str, output_dir: Path, max_concurrent: int = 5):
        """
        Initialize screenshot capture.

        Args:
            base_url: Base URL of the documentation server (e.g., http://localhost:9000)
            output_dir: Directory to save screenshots
            max_concurrent: Maximum concurrent browser pages
        """
        self.base_url = base_url.rstrip("/")
        self.output_dir = output_dir
        self.max_concurrent = max_concurrent
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _generate_filename(self, variant: str, page_path: str, viewport: dict) -> str:
        """Generate a safe filename for the screenshot."""
        safe_path = page_path.strip("/").replace("/", "_") or "index"
        return f"{variant}_{safe_path}_{viewport['width']}x{viewport['height']}.png"

    async def _capture_single(
        self,
        browser,
        semaphore: asyncio.Semaphore,
        variant: str,
        page_path: str,
        viewport: dict,
        viewport_name: str,
    ) -> ScreenshotResult:
        """Capture a single page screenshot with semaphore control."""
        async with semaphore:
            page = None
            try:
                page = await browser.new_page()
                await page.set_viewport_size(
                    {"width": viewport["width"], "height": viewport["height"]}
                )

                full_url = f"{self.base_url}/docs/v2/{variant}{page_path}"
                await page.goto(full_url, wait_until="networkidle", timeout=30000)

                # Wait for any lazy-loaded content or animations
                await page.wait_for_timeout(1500)

                # Generate output path
                filename = self._generate_filename(variant, page_path, viewport)
                output_path = self.output_dir / filename

                # Capture full-page screenshot
                await page.screenshot(path=str(output_path), full_page=True)

                return ScreenshotResult(
                    variant=variant,
                    page_path=page_path,
                    viewport_name=viewport_name,
                    screenshot_path=output_path,
                )

            except Exception as e:
                return ScreenshotResult(
                    variant=variant,
                    page_path=page_path,
                    viewport_name=viewport_name,
                    screenshot_path=None,
                    error=str(e),
                )
            finally:
                if page:
                    await page.close()

    async def capture_all(self, config: dict) -> list[ScreenshotResult]:
        """
        Capture screenshots for all configured pages.

        Args:
            config: Configuration dict with 'variants' and 'viewports' keys

        Returns:
            List of ScreenshotResult objects
        """
        try:
            from playwright.async_api import async_playwright
        except ImportError:
            raise ImportError(
                "Playwright is required for screenshot capture. "
                "Install with: pip install playwright && playwright install chromium"
            )

        async with async_playwright() as p:
            browser = await p.chromium.launch()
            semaphore = asyncio.Semaphore(self.max_concurrent)

            tasks = []
            for variant, variant_config in config.get("variants", {}).items():
                for page_path in variant_config.get("key_pages", []):
                    for viewport_name, viewport in config.get("viewports", {}).items():
                        tasks.append(
                            self._capture_single(
                                browser,
                                semaphore,
                                variant,
                                page_path,
                                viewport,
                                viewport_name,
                            )
                        )

            results = await asyncio.gather(*tasks)
            await browser.close()

            return list(results)

    async def capture_variant(
        self, config: dict, variant: str
    ) -> list[ScreenshotResult]:
        """
        Capture screenshots for a single variant.

        Args:
            config: Configuration dict with 'variants' and 'viewports' keys
            variant: Variant name to capture

        Returns:
            List of ScreenshotResult objects
        """
        filtered_config = {
            "variants": {variant: config["variants"].get(variant, {"key_pages": []})},
            "viewports": config.get("viewports", {}),
        }
        return await self.capture_all(filtered_config)
