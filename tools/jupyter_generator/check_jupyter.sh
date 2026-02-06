#!/bin/bash

# Check that generated jupyter notebook files are in sync with source notebooks
# This script only compares hashes - it doesn't require jupyter to be installed

set -e

errors=0

# Find all markdown files with jupyter_notebook in frontmatter
for file in $(find content -name "*.md" -exec sh -c 'head -n 10 "$1" | grep -q "^jupyter_notebook:" && echo "$1"' sh {} \;); do
    notebook=$(head -n 10 "$file" | grep "^jupyter_notebook:" | sed 's/^jupyter_notebook: //')
    stored_hash=$(head -n 10 "$file" | grep "^content_hash:" | sed 's/^content_hash: //')

    if [[ -z "$stored_hash" ]]; then
        echo "ERROR: $file is missing content_hash field"
        echo "  Run 'make -f Makefile.jupyter' to regenerate"
        errors=1
        continue
    fi

    if [[ ! -f ".$notebook" ]]; then
        echo "ERROR: Notebook not found: .$notebook (referenced by $file)"
        errors=1
        continue
    fi

    current_hash=$(shasum -a 256 ".$notebook" | cut -d ' ' -f 1)

    if [[ "$stored_hash" != "$current_hash" ]]; then
        echo "ERROR: $file is out of sync with source notebook"
        echo "  Source: .$notebook"
        echo "  Expected hash: $current_hash"
        echo "  Stored hash:   $stored_hash"
        echo "  Run 'make -f Makefile.jupyter' to regenerate"
        errors=1
    fi
done

if [[ $errors -eq 1 ]]; then
    exit 1
fi

echo "All jupyter notebooks are in sync"
