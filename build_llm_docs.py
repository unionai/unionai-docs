#!/usr/bin/env python3

"""
Generate LLM-friendly documentation from Hugo site builds.

This script processes the dist directory after Hugo builds to create
LLM-ready documentation in markdown format for each variant.
"""

import os
import sys
import shutil
import argparse
from pathlib import Path


def detect_version():
    """Detect if we're in a v1 or v2 repository structure."""
    # Check for v1 indicators
    if Path("config.serverless.toml").exists():
        return "v1"
    
    # Check for v2 indicators
    dist_path = Path("dist/docs")
    if dist_path.exists():
        # Look for version-specific subdirectories
        v1_path = dist_path / "v1"
        v2_path = dist_path / "v2"
        if v2_path.exists():
            return "v2"
        elif v1_path.exists():
            return "v1"
    
    # Default assumption
    return "v1"


def find_variants():
    """Find all available documentation variants."""
    version = detect_version()
    
    if version == "v1":
        # v1 has variants at dist/docs/v1/{variant}
        base_path = Path("dist/docs/v1")
        if not base_path.exists():
            print(f"Error: {base_path} not found. Run 'make dist' first.")
            sys.exit(1)
    else:
        # v2 has variants at dist/docs/v2/{variant}
        base_path = Path("dist/docs/v2")
        if not base_path.exists():
            print(f"Error: {base_path} not found. Run 'make dist' first.")
            sys.exit(1)
    
    variants = []
    for item in base_path.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            variants.append(item.name)
    
    return sorted(variants), version


def process_variant(variant_name, version):
    """Process a single variant to create LLM documentation."""
    if version == "v1":
        variant_path = Path(f"dist/docs/v1/{variant_name}")
        tmp_md_path = Path(f"dist/docs/v1/{variant_name}/tmp-md")
        output_path = Path(f"dist/docs/v1/{variant_name}/md")
    else:
        variant_path = Path(f"dist/docs/v2/{variant_name}")
        tmp_md_path = Path(f"dist/docs/v2/{variant_name}/tmp-md")
        output_path = Path(f"dist/docs/v2/{variant_name}/md")
    
    print(f"\nProcessing {variant_name} variant...")
    
    # Check if tmp-md directory exists (created by Hugo with our templates)
    if not tmp_md_path.exists():
        print(f"  Warning: {tmp_md_path} not found. Skipping {variant_name}.")
        print(f"  Make sure Hugo generated the markdown files.")
        return False
    
    # Create LLM-specific directories
    llm_base = variant_path / "llm"
    if llm_base.exists():
        shutil.rmtree(llm_base)
    
    llm_base.mkdir(parents=True, exist_ok=True)
    
    # Copy and process files from tmp-md to llm directory
    md_files_copied = 0
    
    def copy_and_process_files(src_dir, dst_dir):
        nonlocal md_files_copied
        dst_dir.mkdir(parents=True, exist_ok=True)
        
        for item in src_dir.iterdir():
            if item.is_file() and item.suffix == '.txt':
                # Convert .txt files to .md files in the LLM directory
                dst_file = dst_dir / (item.stem + '.md')
                shutil.copy2(item, dst_file)
                md_files_copied += 1
            elif item.is_file():
                # Copy other files as-is
                dst_file = dst_dir / item.name
                shutil.copy2(item, dst_file)
                md_files_copied += 1
            elif item.is_dir():
                copy_and_process_files(item, dst_dir / item.name)
    
    copy_and_process_files(tmp_md_path, llm_base)
    
    print(f"  ✓ Copied {md_files_copied} markdown files to {llm_base}")
    
    # Create a consolidated file for the entire variant
    consolidated_file = llm_base / f"{variant_name}-complete.md"
    
    with open(consolidated_file, 'w', encoding='utf-8') as outf:
        outf.write(f"# {variant_name.title()} Documentation\n\n")
        outf.write("This is a consolidated view of all documentation for LLM processing.\n\n")
        
        def append_md_content(src_dir, prefix=""):
            for item in sorted(src_dir.iterdir()):
                if item.is_file() and item.suffix == '.md':
                    try:
                        with open(item, 'r', encoding='utf-8') as inf:
                            content = inf.read()
                            if content.strip():
                                outf.write(f"\n{'='*60}\n")
                                outf.write(f"FILE: {prefix}{item.name}\n")
                                outf.write(f"{'='*60}\n\n")
                                outf.write(content)
                                outf.write("\n\n")
                    except Exception as e:
                        print(f"  Warning: Could not read {item}: {e}")
                elif item.is_dir():
                    append_md_content(item, f"{prefix}{item.name}/")
        
        append_md_content(llm_base)
    
    print(f"  ✓ Created consolidated file: {consolidated_file}")
    return True


def main():
    parser = argparse.ArgumentParser(description='Generate LLM documentation')
    parser.add_argument('--no-make-dist', action='store_true',
                       help='Skip running make dist (assumes dist already exists)')
    args = parser.parse_args()
    
    print("🤖 Generating LLM Documentation...")
    
    # Build the site first unless --no-make-dist is specified
    if not args.no_make_dist:
        print("\n📦 Building site...")
        result = os.system("make dist")
        if result != 0:
            print("Error: Failed to build site with 'make dist'")
            sys.exit(1)
    
    # Find and process variants
    variants, version = find_variants()
    print(f"\n🔍 Detected {version} structure")
    print(f"Found variants: {', '.join(variants)}")
    
    successful_variants = 0
    for variant in variants:
        if process_variant(variant, version):
            successful_variants += 1
    
    print(f"\n✅ Successfully processed {successful_variants}/{len(variants)} variants")
    
    if successful_variants == 0:
        print("\n❌ No variants were successfully processed.")
        print("Make sure the markdown templates are properly configured.")
        sys.exit(1)
    else:
        print(f"\n🎉 LLM documentation ready in dist/docs/{version}/{{variant}}/llm/")


if __name__ == "__main__":
    main()