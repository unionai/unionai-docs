#!/bin/bash

files=$(find source -name '*.md')
if grep -c . <<< "${files}" 1>/dev/null; then
  echo 'FATAL: "source" folder cannot have Markdown files'
  echo "$files" | sed -e 's/^/  - /'
  exit 1
fi

files=$(
  find source -name '*.png';
  find source -name '*.gif';
)
if grep -c . <<< "${files}" 1>/dev/null; then
  echo 'FATAL: "source" folder cannot have images.'
  echo "$files" | sed -e 's/^/  - /'
  exit 1
fi

files=$(find 'content' -type f \
	| grep -v md$ \
	| grep -v png$ | grep -v gif$ | grep -v svg$ \
	| grep -v "/_static/includes/")
if grep -c . <<< "${files}" 1>/dev/null; then
  echo 'FATAL: "content" can only contain content (md, png, gif)'
  echo "$files" | sed -e 's/^/  - /'
  exit 1
fi

echo 'SUCCESS: Content and builder are separated.'
exit 0
