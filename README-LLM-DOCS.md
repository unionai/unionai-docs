# LLM Documentation Generation

This system generates LLM-optimized documentation from the Hugo site builds.

## Overview

The LLM documentation generator processes the built Hugo site and creates:
1. **Markdown versions** of all pages (via Hugo templates)
2. **LLM-optimized directories** with clean markdown files
3. **Consolidated files** for each variant combining all content

## Usage

### Build all variants with LLM docs
```bash
make dist
```

### Build only LLM docs (after site is already built)
```bash
make llm-docs
```

## Architecture

### Version Detection
The system automatically detects whether it's running on v1 or v2:
- **v1**: Has `config.serverless.toml` and generates docs at `dist/docs/v1/{variant}`
- **v2**: Generates docs at `dist/docs/v2/{variant}`

### Variants
The system processes all available variants:
- **v1**: flyte, serverless, byoc, selfmanaged
- **v2**: flyte, byoc, selfmanaged

### Output Structure
For each variant, the system creates:
```
dist/docs/{version}/{variant}/
├── md/                    # Markdown versions of all pages (Hugo-generated)
└── llm/                   # LLM-optimized documentation
    ├── {variant}-complete.md  # All content in one file
    └── [individual files]     # Clean markdown files
```

## Dependencies

- Python 3.8+
- `toml>=0.10.2` (installed via uv or pip)

The system uses `uv` if available, falling back to `python3` + pip.

## Templates

The system requires these Hugo templates in `layouts/_default/`:
- `list.md` - For section/index pages
- `single.md` - For individual content pages

These templates generate markdown versions of pages alongside the HTML versions.

## Files

- `build_llm_docs.py` - Main script
- `pyproject.toml` - Python project configuration
- `requirements.txt` - Fallback dependencies
- `Makefile` - Integration with build system