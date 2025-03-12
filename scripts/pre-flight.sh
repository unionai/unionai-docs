#!/bin/bash

if ! command -v hugo 1>/dev/null; then
  cat <<EOF
---------------------------------------
FATAL: 'hugo' site builder required.

Install with:
  MacOS  : brew install hugo
  Ubuntu : apt  install hugo
---------------------------------------

EOF
  exit 1
fi
