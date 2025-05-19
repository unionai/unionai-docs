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
FATAL: The following files contain an absolute external URL pointing to the docs pages.
       Make it a relative instead:

$(for file in $mentions_doc; do echo "  - $file"; done)

EOF

  exit 1
fi

declare mentions_docs_home
mentions_docs_home=$(grep -r "(/docs/" content | grep -vi binary \
                   | cut -d: -f1 | sort | uniq)
readonly mentions_docs_home

if [[ ! -z $mentions_docs_home ]]; then
  cat <<EOF
FATAL: The following files contain an absilute external URL pointing to docs pages.
       Instead, use {{< docs_home {variant} }} to mention a specific doc root.

$(for file in $mentions_docs_home; do echo "  - $file"; done)

EOF

  exit 1
fi