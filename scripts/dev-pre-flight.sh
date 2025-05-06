#!/bin/bash

fatal() {
  declare -r msg="$1"
  declare -r action="$2"
  echo
  echo -e "\033[0;41m+-------------------------------------------------------------------------------+\033[0m"
  printf "\033[0;41m| FATAL: %-70s |\033[0m\n" "$msg"
  printf "\033[0;41m|        %-70s |\033[0m\n" "${action}"
  echo -e "\033[0;41m+-------------------------------------------------------------------------------+\033[0m"
  echo
  exit 1
}

if [[ ! -e hugo.local.toml ]]; then
  fatal \
    "You need to have a 'hugo.local.toml' for development mode" \
    "(please copy it from 'hugo.local.toml~sample' to get started)"
fi

if grep -q -c variant_hide_in_development "hugo.local.toml"; then
  fatal \
    "You have legacy settings in 'hugo.local.toml'" \
    "(please copy settings from 'hugo.local.toml~sample')"
fi
if grep -q -c variant_identify_variant_in_development "hugo.local.toml"; then
  fatal \
    "You have legacy settings in 'hugo.local.toml'" \
    "(please copy settings from 'hugo.local.toml~sample')"
fi

# Check if we have all the settings described in the sample file
known_settings=$(
  tr -d ' ' <"hugo.local.toml~sample" |
    tr -d ' ' | cut -d= -f1 | grep -v '^#' | grep -v '\[params]' | sort |
    cut -d= -f1 | grep -v '^#' | grep -v '\[params]' | sort
)
for sett in $known_settings; do
  if ! tr -d ' ' <"hugo.local.toml" | grep -q -c "^$sett="; then
    fatal \
      "You are missing the '$sett' setting in 'hugo.local.toml'" \
      "(please copy it from 'hugo.local.toml~sample')"
  fi
done
