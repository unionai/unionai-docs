import re
import os
import json

def extract_meta_description(html_content):
    # Pattern to match meta description tags, handling multi-line content
    pattern = r'<meta[^>]*name="description"[^>]*content="([^"]*)"[^>]*>'
    match = re.search(pattern, html_content, re.IGNORECASE | re.DOTALL)
    if match:
        # Preserve all newlines and whitespace exactly as they appear
        return match.group(1)
    return ""

# Collect all meta descriptions
meta_descriptions = []

# Find all index.html files
for root, dirs, files in os.walk('dist/docs'):
    for file in files:
        if file == 'index.html':
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    description = extract_meta_description(content)
                    meta_descriptions.append({
                        "file_path": filepath,
                        "meta_description": description
                    })
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
                meta_descriptions.append({
                    "file_path": filepath,
                    "meta_description": "",
                    "error": str(e)
                })

# Write to JSON file
with open('meta_descriptions.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(meta_descriptions, jsonfile, indent=2, ensure_ascii=False)

print(f"Meta descriptions extracted successfully! {len(meta_descriptions)} files processed.")
