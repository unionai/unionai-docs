# Visual QA Project Status

> Last updated: 2026-01-13
> Branch: `peeter/ai-visual-check`
> Last commit: `93173c3e` - Add visual QA system for automated docs rendering checks

## Project Goal

Build an automated visual QA system that:
1. Captures screenshots of rendered documentation pages using Playwright
2. Analyzes screenshots with Claude Vision API to detect rendering issues
3. Runs on each PR via GitHub Actions
4. Reports issues in GitHub Actions summary with severity levels

## Current State: MVP Complete, Needs Polish

### What's Working

- **Screenshot capture**: Fully working with Playwright
  - Tested on flyte variant: 24 pages captured successfully
  - Async with concurrency control (5 concurrent pages)
  - Full-page screenshots at 1920x1080

- **Claude Vision integration**: Code complete, not yet tested with API
  - Structured JSON response parsing
  - Retry logic with exponential backoff
  - Batch processing with rate limiting

- **Report generation**: Code complete
  - GitHub Actions summary (markdown)
  - JSON report for artifacts
  - Console output

- **CI integration**: Workflow file created
  - `.github/workflows/visual-qa.yml`
  - Triggers on PRs to main + manual dispatch
  - Uploads screenshots and report as artifacts

### What Still Needs Work

1. **Page paths for byoc/selfmanaged variants**
   - The `pages.yaml` has placeholder paths copied from flyte
   - These need to be verified/corrected (some paths differ between variants)
   - Run: `make dist && make visual-qa` to test each variant

2. **Claude Vision API testing**
   - Requires `ANTHROPIC_API_KEY` environment variable
   - Not yet tested end-to-end with real API calls
   - Run without `--skip-analysis` flag to test

3. **GitHub Actions secret**
   - Need to add `ANTHROPIC_API_KEY` as repository secret
   - Required for CI to work

4. **Prompt tuning**
   - The vision analysis prompt in `vision_analyzer.py` may need adjustment
   - Based on real-world results, may get false positives/negatives

## File Structure

```
tools/visual_qa/
├── __init__.py           # Package init
├── __main__.py           # Allows: python -m tools.visual_qa
├── cli.py                # CLI entry point (argparse)
├── pages.yaml            # Page configuration per variant
├── screenshot_capture.py # Playwright async screenshot capture
├── vision_analyzer.py    # Claude Vision API integration
└── report_generator.py   # GitHub summary + JSON reports

.github/workflows/
└── visual-qa.yml         # GitHub Actions workflow

Makefile                  # Added: visual-qa target
```

## Key Commands

```bash
# Install dependencies
uv pip install playwright pyyaml anthropic
uv run python -m playwright install chromium

# Build docs (required before visual QA)
make dist

# Run screenshot capture only (no API calls)
uv run python -m tools.visual_qa \
  --base-url http://localhost:9999 \
  --variant flyte \
  --skip-analysis

# Run full visual QA (requires ANTHROPIC_API_KEY)
export ANTHROPIC_API_KEY=sk-...
make visual-qa

# Run on specific variant
uv run python -m tools.visual_qa \
  --base-url http://localhost:9999 \
  --variant byoc \
  --output-dir /tmp/visual-qa-results
```

## Issues Encountered & Solutions

### 1. `main.py` ignored by gitignore
- **Problem**: `.gitignore` has `main.py` entry (line 36)
- **Solution**: Renamed to `cli.py`, added `__main__.py` for `-m` invocation

### 2. Blank screenshots for missing pages
- **Problem**: Some paths in `pages.yaml` don't exist in all variants
- **Solution**: Updated flyte paths after testing. byoc/selfmanaged still need verification
- **How to detect**: Look for screenshots < 10KB: `find /tmp/visual-qa-results/screenshots -size -10k`

### 3. Path differences between variants
- **Example**: Flyte uses `/user-guide/run-scaling/` but original config had `/user-guide/running-scaling/`
- **Solution**: Check actual paths with: `ls dist/docs/v2/{variant}/user-guide/`

## Next Steps (Priority Order)

1. **Verify byoc/selfmanaged paths in pages.yaml**
   ```bash
   # Check byoc structure
   ls dist/docs/v2/byoc/user-guide/
   ls dist/docs/v2/byoc/deployment/
   ```

2. **Test with Claude Vision API**
   ```bash
   export ANTHROPIC_API_KEY=sk-...
   uv run python -m tools.visual_qa \
     --base-url http://localhost:9999 \
     --variant flyte \
     --output-dir /tmp/visual-qa-results
   ```

3. **Add GitHub secret and test PR workflow**

4. **Tune prompt based on results** (if too many false positives/negatives)

## Design Decisions

- **Claude Sonnet** chosen over Opus for cost-effectiveness (vision analysis doesn't need Opus-level reasoning)
- **Desktop-only viewport** (1920x1080) to keep runtime reasonable (~20 min for all variants)
- **~25 pages per variant** balances coverage vs. API costs
- **Fail on critical only** by default (configurable with `--fail-on`)
- **Screenshots saved as artifacts** for manual review of flagged issues

## User Preferences (from planning)

- Use Claude Vision API (not pixel-diff regression)
- Detect all rendering issues (layout, images, styling, typography, etc.)
- Check key pages only (~20-30 per variant)
- Check all 3 variants (flyte, byoc, selfmanaged)
