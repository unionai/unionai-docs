#!/bin/bash

declare content
content=$(find content -name "*.md" -exec sh -c 'head -n 10 "$1" | grep -l "^jupyter_notebook:" "$1"' sh {} \;)
readonly content

# Go through each file and:
# 1. Read the jupyuter_notebook field
# 2. Calculate the hash of the notebook
# 3. Compare the hash with the content_hash field
# 4. Calculate the hash of the copy @ content/_static/notebooks
# 5. Compare the hash with the content_hash field
# 6. If the hash is different, print message about it
# 7. If any notebook hash is different, exit with 1

exit_code=0

for file in $content; do
    notebook=$(head -n 10 "$file" | grep "^jupyter_notebook:" | sed 's/^jupyter_notebook: //')
    content_hash=$(head -n 10 "$file" | grep "^content_hash:" | sed 's/^content_hash: //' | awk '{print $1}')
    
    if [ -z "$content_hash" ]; then
        echo "ERROR: $file is missing content_hash field"
        exit_code=1
        continue
    fi
    
    # Calculate hash of the original notebook
    if [ -f ".$notebook" ]; then
        original_hash=$(shasum -a 256 ".$notebook" | cut -d ' ' -f 1)
        
        if [ "$original_hash" != "$content_hash" ]; then
            echo "ERROR: $file has different hash than original notebook (.$notebook)"
            echo "  Expected: $content_hash"
            echo "  Got:      $original_hash"
            exit_code=1
        fi
    else
        echo "ERROR: Original notebook not found: .$notebook"
        exit_code=1
    fi   
done

if [[ $exit_code -eq 0 ]]; then
    echo "[ OK ] All notebooks are up to date"
fi

exit $exit_code

