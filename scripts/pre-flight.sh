#!/bin/bash

declare -r hugo_min_version=0.145.0

ver_from_string() {
  echo "$@" | awk -F. '{ printf("%d%03d%03d%03d\n", $1,$2,$3,$4); }';
}

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

hugo_ver=$(hugo version | grep -o 'v[0-9]\+\.[0-9]\+\.[0-9]\+' | sed 's/v//')
version_number=$(ver_from_string $hugo_ver)
min_version_number=$(ver_from_string $hugo_min_version)


if [[ $version_number -lt $min_version_number ]]; then
  cat <<EOF
---------------------------------------
FATAL: 'hugo' version ${hugo_min_version} or greater required.

Install with:
  MacOS  : brew install hugo
  Ubuntu : apt  install hugo
---------------------------------------
EOF
  exit 1
fi