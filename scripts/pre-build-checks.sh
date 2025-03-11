#!/bin/bash

declare homepage
homepage=$(grep ^homepage ./themes/union/theme.toml \
               | cut -d= -f2 | tr -d '"' | tr -d " ")
readonly homepage

declare mentions_doc
mentions_doc=$(grep -r "${homepage}" content | grep -vi binary \
                   | cut -d: -f1 | sort | uniq)
readonly mentions_doc

if [[ ! -z $mentions_doc ]]; then
  cat <<EOF
FATAL: These files makes hardcoded URLs for docs pages.
       Instead, make them relative to the site:

$(for file in $mentions_doc; do echo "  - $file"; done)

EOF

  exit 1
fi

