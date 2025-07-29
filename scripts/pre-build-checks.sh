#!/bin/bash

check_mentions_docs() {
  local -r homepage=$1

  declare mentions_doc
  mentions_doc=$(grep -r "${homepage}" content \
                     | grep -vi binary \
                     | grep -v content/community/contributing-docs/redirects.md \
                     | grep -v content/api-reference/flyte-cli.md \
                     | cut -d: -f1 | sort | uniq)
  readonly mentions_doc

  if [[ ! -z $mentions_doc ]]; then
    cat <<EOF
FATAL: The following files contain an absolute external URL pointing to the docs pages.
       (mentions: ${homepage})

Make them relative instead:

$(for file in $mentions_doc; do echo "  - $file"; done)

EOF

    exit 1
  fi
}

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

check_mentions_docs "https://docs.union.ai"
check_mentions_docs "https://union.ai/docs"
check_mentions_docs "https://www.union.ai/docs"
