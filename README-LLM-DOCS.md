# LLM-Optimized Documentation Generation

This repository includes a system for generating consolidated, LLM-optimized documentation files from the Hugo-based documentation source. The system produces single-file documentation that is perfect for use with Large Language Models, with all internal links converted to hierarchical references.

## Overview

The documentation pipeline works as follows:

1. **Hugo builds variant-specific markdown** from the source content
2. **LLM doc builder** consolidates all pages into single files with optimized link processing
3. **Result**: Clean, searchable, self-contained documentation files for each variant

## Architecture

### Source Content Structure
```
content/
├── user-guide/
│   ├── getting-started/
│   │   ├── index.md
│   │   ├── local-setup.md
│   │   └── ...
│   ├── task-configuration/
│   └── ...
├── tutorials/
├── integrations/
└── ...
```

### Hugo Processing
The Hugo build system processes the source content using:
- **Variants**: Different product versions (flyte, byoc, selfmanaged, serverless)
- **Shortcodes**: Dynamic content insertion based on variants
- **Templates**: Consistent page structure and navigation

### Generated Output Structure
```
dist/docs/v2/
├── flyte/
│   ├── md/           # Hugo-generated markdown
│   └── llms-full.txt # LLM-optimized consolidated doc
├── byoc/
│   ├── md/
│   └── llms-full.txt
└── ...
```

## LLM Documentation Builder (`build_llm_docs.py`)

### Core Features

1. **Depth-First Traversal**: Follows `## Subpages` links in proper hierarchical order
2. **Hierarchical Link Processing**: Converts all internal links to searchable hierarchical references
3. **Multi-Variant Support**: Generates separate files for each documentation variant
4. **Complete Heading Analysis**: Parses all headings to support anchor link resolution

### Processing Pipeline

#### 1. Documentation Regeneration
```bash
make dist  # Rebuilds all Hugo variants
```

#### 2. Variant Discovery
Automatically discovers available variants in `dist/docs/v2/`

#### 3. Page Traversal
Starting from `md/index.md`, follows subpage links depth-first:
```markdown
## Subpages
- [User Guide](user-guide/index.md)
- [Tutorials](tutorials/index.md)
```

#### 4. Hierarchy Building
Builds complete page hierarchy as it traverses:
- `index.md` → "Documentation"
- `user-guide/index.md` → "Documentation > User Guide"
- `user-guide/getting-started/local-setup.md` → "Documentation > User Guide > Getting Started > Local Setup"

#### 5. Heading Analysis
For each page, parses all markdown headings to build anchor lookup:
```markdown
# Local Setup                    → Page title (already in hierarchy)
## Setting up a configuration    → "Getting Started > Local Setup > Setting up a configuration file"
### Specify explicitly          → "Getting Started > Local Setup > Setting up a configuration file > Specify explicitly"
```

#### 6. Link Processing
Converts all internal links to hierarchical references:

**Cross-page links:**
- `[Local setup](local-setup.md)` → `**Getting started > Local setup**`
- `[Config](local-setup.md#setting-up-a-configuration-file)` → `**Getting started > Local setup > Setting up a configuration file**`

**Same-page anchor links:**
- `[Image building](#image-building)` → `**Task configuration > Container images > Image building**`

**Preserved links:**
- External: `[GitHub](https://github.com/...)` → unchanged
- Cross-variant: `[Union.ai](/docs/v2/byoc/)` → unchanged
- Static files: `[notebook.ipynb](/_static/...)` → unchanged

## Usage

### Generating LLM Documentation

Run the build script:
```bash
python build_llm_docs.py
```

This will:
1. Run `make dist` to regenerate all documentation variants
2. Process each variant (flyte, byoc, selfmanaged, serverless)
3. Generate `llms-full.txt` files in each variant directory

### Output Files

Generated files are located at each variant directory:
- `dist/docs/v2/flyte/llms-full.txt` + `llms.txt`
- `dist/docs/v2/byoc/llms-full.txt` + `llms.txt`
- `dist/docs/v2/selfmanaged/llms-full.txt` + `llms.txt`
- `dist/docs/v2/serverless/llms-full.txt` + `llms.txt`

**Two files per variant:**

1. **`llms-full.txt`** - The complete consolidated documentation:
   - **Complete documentation** for that variant in depth-first order
   - **Page delimiters**: `=== PAGE: path/to/file.md ===`
   - **Hierarchical internal links**: All `.md` and `#anchor` links converted to `**Page > Section**` format
   - **Preserved external links**: GitHub, cross-variant, and static file links unchanged

2. **`llms.txt`** - A redirect/discovery file:
   - Brief explanation of the LLM documentation system
   - Link to the corresponding `llms-full.txt` file
   - Variant and version information
   - Usage guidance for LLMs and RAG systems

## Key Implementation Details

### Lookup Table System
The builder maintains a comprehensive lookup table mapping:
```
# Pages
"user-guide/getting-started/local-setup.md" → "Getting Started > Local Setup"

# Anchors
"local-setup.md#using-the-configuration-file" → "Getting Started > Local Setup > Using the configuration file"
```

### Anchor Generation
Heading titles are converted to URL anchors using standard rules:
- Lowercase conversion
- Space to hyphen replacement
- Special character removal
- Example: "Setting up a Configuration File" → "setting-up-a-configuration-file"

### Hierarchy Optimization
The system automatically strips redundant prefixes:
- Raw: "Documentation > Flyte > Getting Started > Local Setup"
- Optimized: "Getting Started > Local Setup" (in flyte variant)

This keeps references concise while maintaining uniqueness within each variant.

### Error Handling
- **Missing files**: Warnings logged, processing continues
- **Broken links**: Fallback to link text with current context
- **Invalid anchors**: Graceful fallback to text-based reference

## Benefits for LLM Usage

### Perfect Internal References
- ✅ **No broken links**: All internal `.md` references point to content in the same file
- ✅ **Searchable**: LLMs can find any referenced content by searching hierarchical titles
- ✅ **Context-rich**: Every reference includes full page and section hierarchy
- ✅ **Consistent format**: All internal references follow `**Page > Section**` pattern

### Complete Content
- ✅ **Single file**: All documentation in one consolidated file per variant
- ✅ **Proper order**: Content follows logical depth-first navigation structure
- ✅ **No duplication**: Each page appears exactly once in the correct hierarchical position

### LLM-Friendly Format
- ✅ **Clear delimiters**: Easy to identify page boundaries
- ✅ **Hierarchical structure**: Matches how humans think about documentation organization
- ✅ **No file system dependencies**: All references are text-based within the same document

## Example Output

```markdown
=== PAGE: user-guide/getting-started/local-setup.md ===

# Local Setup

Before proceeding, make sure you have completed the steps in **Getting started**.

Use the **Getting started > `flyte create config`** command, making the following changes:

See **Getting started > Local setup > Setting up a configuration file** for details.

## Setting up a configuration file

You can also reference **Task configuration > Container images > Image building** for advanced setup.

=== PAGE: user-guide/getting-started/running.md ===

# Running Your First Task

...
```

## Maintenance

### Updating the System
The LLM documentation builder automatically regenerates content from the current Hugo source. To update:

1. **Content changes**: Modify files in `content/` directory
2. **Regenerate**: Run `python build_llm_docs.py`
3. **New files**: Added automatically if linked via `## Subpages`

### Adding New Variants
New Hugo variants are automatically detected and processed. No code changes required.

### Debugging
- Enable verbose output by checking the console during build
- Inspect generated `md/` directories to verify Hugo processing
- Check file sizes - significant changes may indicate processing issues

## Integration

The LLM documentation files can be used with:
- **Vector databases** for semantic search
- **RAG systems** for question answering
- **AI assistants** for documentation support
- **API documentation tools** that consume markdown
- **Training datasets** for domain-specific models

The hierarchical link structure ensures that LLMs can accurately reference and cross-reference content without confusion about file paths or broken links.