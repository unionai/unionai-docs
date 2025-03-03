#!/bin/bash

if [[ ! -e hugo.local.toml ]]; then
  echo -e "\033[0;41m"
  cat <<EOF

+----------------------------------------------------------------------+
| FATAL: You need to have a 'hugo.local.toml' for development mode.    |
|        (please copy it from 'hugo.local.toml~sample' to get started) |
+----------------------------------------------------------------------+

EOF
  echo -e "\033[0m"
  exit 1
fi
