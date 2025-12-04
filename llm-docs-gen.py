# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "beautifulsoup4>=4.12.0",
#     "markdownify>=0.11.0",
# ]
# ///

import os
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import re

# CONFIGURATION
# ---------------------------------------------------------
# The local path where your build output sits
BUILD_DIR = "dist"
DOCS_ROOT = "docs/v2" # Hugo builds into dist/docs/v2/{variant}/

# The public domain where this will be hosted (for absolute links)
BASE_URL = "https://www.union.ai"

# HTML Selectors to IGNORE (Remove navs, footers, sidebars)
# Adjust these based on your specific Docusaurus/Sphinx/Hugo class names
EXCLUDE_SELECTORS = [
    "nav",
    "footer",
    "script",
    "style",
    ".sidebar",
    ".menu",
    ".table-of-contents",
    ".pagination-nav"
]

# HTML Selectors to KEEP (The main content)
# If None, it processes <body> but removes exclusions.
# If set (e.g., "main" or "article"), it narrows down strictly to that tag.
MAIN_CONTENT_SELECTOR = "main"
# ---------------------------------------------------------

def clean_html(html_content, file_path):
    """
    Parses HTML, removes noise, and extracts the main content.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # 1. Remove unwanted elements
    for selector in EXCLUDE_SELECTORS:
        for tag in soup.select(selector):
            tag.decompose()

    # 2. Focus on main content if selector is defined
    content = soup
    if MAIN_CONTENT_SELECTOR:
        found = soup.select_one(MAIN_CONTENT_SELECTOR)
        if found:
            content = found

    # 3. Fix Relative Links to Absolute
    # We need to calculate what the URL would be based on the file path
    # relative_path = dist/docs/v2/byoc/index.html -> docs/v2/byoc/index.html
    rel_path = os.path.relpath(file_path, BUILD_DIR)
    parent_url = f"{BASE_URL}/{os.path.dirname(rel_path)}"

    # Fix images
    for img in content.find_all('img', src=True):
        if not img['src'].startswith(('http', '//')):
            # Simple join; for production, might need robust urljoin handling
            img['src'] = f"{parent_url}/{img['src']}".replace("/./", "/")

    # Fix links
    for a in content.find_all('a', href=True):
        if not a['href'].startswith(('http', '//', '#', 'mailto:')):
            a['href'] = f"{parent_url}/{a['href']}".replace("/./", "/")

    return content

def process_page_hierarchically(page_data, variant_dir, base_heading_level=1):
    """
    Process a single page and its children hierarchically.
    Returns formatted content with proper heading levels.
    """
    content_parts = []
    
    # Determine HTML file path
    html_file_path = Path(BUILD_DIR) / page_data["html_file"]
    
    if not html_file_path.exists():
        print(f"Warning: HTML file not found: {html_file_path}")
        return ""
    
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            cleaned_soup = clean_html(f.read(), html_file_path)
            
            # Extract title
            title = page_data.get("title", "Untitled Page")
            
            # Get web URL 
            web_path = page_data["path"]
            web_url = f"{BASE_URL}{web_path}"
            
            # Get relative path for source reference
            rel_path = os.path.relpath(html_file_path, BUILD_DIR)
            
            # Convert to Markdown
            markdown = md(str(cleaned_soup), heading_style="atx")
            
            # Remove excessive newlines
            markdown = re.sub(r'\n\s*\n', '\n\n', markdown)
            
            # Adjust heading levels in the markdown content
            # We need to shift all headings down to make room for our hierarchy
            lines = markdown.split('\n')
            adjusted_lines = []
            for line in lines:
                if line.startswith('#'):
                    # Count existing heading level
                    existing_level = 0
                    for char in line:
                        if char == '#':
                            existing_level += 1
                        else:
                            break
                    
                    # Add base heading level offset (but cap at 6)
                    new_level = min(existing_level + base_heading_level + 1, 6)
                    new_heading = '#' * new_level + line[existing_level:]
                    adjusted_lines.append(new_heading)
                else:
                    adjusted_lines.append(line)
            
            adjusted_markdown = '\n'.join(adjusted_lines)
            
            # Create the section header with proper heading level
            section_heading = '#' * base_heading_level + f" {title}"
            
            section = f"""
{section_heading}

> **Source**: {rel_path}  
> **Web URL**: {web_url}  
> **Level**: {page_data.get('level', 0)} | **Weight**: {page_data.get('weight', 999999)}

{adjusted_markdown}

"""
            content_parts.append(section)
            
    except Exception as e:
        print(f"Warning: Could not process {html_file_path}: {e}")
        return ""
    
    # Process children recursively
    children = page_data.get("children", [])
    for child in children:
        child_content = process_page_hierarchically(child, variant_dir, base_heading_level + 1)
        content_parts.append(child_content)
    
    return "".join(content_parts)

def generate_scoped_files():
    """
    Generates llms-full.txt files using site-metadata.json for structure and ordering.
    Returns a list of generated files for the master router.
    """
    import json
    generated_contexts = []

    docs_path = Path(BUILD_DIR) / DOCS_ROOT

    if not docs_path.exists():
        print(f"Error: Directory {docs_path} not found.")
        return []

    # Known variant directories based on Makefile
    variants = ["flyte", "byoc", "selfmanaged"]  # serverless commented out in Makefile

    # Iterate over variant directories (flyte, byoc, selfmanaged)
    for variant in variants:
        variant_dir = docs_path / variant
        if variant_dir.exists() and variant_dir.is_dir():
            print(f"Processing variant: {variant}...")

            # Load site metadata
            metadata_file = variant_dir / "site-metadata.json"
            if not metadata_file.exists():
                print(f"Warning: No site-metadata.json found for {variant}. Skipping.")
                continue
            
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
            except Exception as e:
                print(f"Error reading metadata for {variant}: {e}")
                continue
            
            full_text_content = []
            
            # Add main header
            variant_header = f"# Union.ai Documentation: {variant.upper()}\n\n"
            variant_header += f"> **Context**: {variant} deployment model  \n"
            variant_header += f"> **Generated**: {metadata.get('generated_at', 'unknown')}  \n"
            variant_header += f"> **Total Pages**: {metadata.get('total_pages', 'unknown')}  \n\n"
            full_text_content.append(variant_header)

            # Process pages according to metadata hierarchy
            pages = metadata.get("pages", [])
            for page in pages:
                page_content = process_page_hierarchically(page, variant_dir, base_heading_level=1)
                full_text_content.append(page_content)

            # Write the llms-full.txt inside the variant directory
            output_filename = "llms-full.txt"
            output_path = variant_dir / output_filename

            with open(output_path, 'w', encoding='utf-8') as out_f:
                out_f.write("".join(full_text_content))

            print(f"Generated: {output_path}")

            # Store metadata for the router
            generated_contexts.append({
                "variant": variant,
                "path": f"{DOCS_ROOT}/{variant}/{output_filename}"
            })

    return generated_contexts

def generate_master_router(contexts):
    """
    Generates the root llms.txt acting as a menu.
    """
    router_content = "# Union and Flyte Documentation Index\n\n"
    router_content += "> Flyte is the leading open source platform for orchestrating mission-critical workflows.\n\n"
    router_content += "> Union is a commercial product based on Flyte that offers greatly enhanced performance and scaling capabilities.\n\n"
    router_content += "## Select documentation by product variant\n\n"

    for ctx in sorted(contexts, key=lambda x: x['variant']):
        url = f"{BASE_URL}/{ctx['path']}"
        variant_name = ctx['variant'].upper()

        # Add description based on variant
        descriptions = {
            "flyte": "Flyte OSS",
            "byoc": "Union BYOC (Bring Your Own Cloud)",
            "selfmanaged": "Union Self-managed",
            "serverless": "Union Serverless"
        }
        desc = descriptions.get(ctx['variant'], f"{ctx['variant']} deployment")

        router_content += f"- [{variant_name} Documentation]({url}): Full context for {desc}.\n"

    router_content += "\n"
    router_content += "## About\n\n"
    router_content += "These files contain the complete Union.ai documentation converted to LLM-friendly format. "
    router_content += "Each product variant has its own consolidated documentation file.\n"

    # Write to BUILD root
    root_path = Path(BUILD_DIR) / "llms.txt"
    with open(root_path, 'w', encoding='utf-8') as f:
        f.write(router_content)

    print(f"Generated Root Router at: {root_path}")

if __name__ == "__main__":
    try:
        print("Starting LLM documentation generation...")
        contexts = generate_scoped_files()

        if not contexts:
            print("No documentation contexts found. Make sure the build completed successfully.")
            exit(1)

        generate_master_router(contexts)
        print(f"Successfully generated LLM documentation files for {len(contexts)} variants.")

    except ImportError as e:
        print(f"Missing required Python packages: {e}")
        print("Please install: pip install beautifulsoup4 markdownify")
        exit(1)
    except Exception as e:
        print(f"Error generating LLM documentation: {e}")
        exit(1)