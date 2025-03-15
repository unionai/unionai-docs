#!/bin/bash

if [[ ! -e hugo.local.toml ]]; then
  echo
  echo -e "\033[0;41m+----------------------------------------------------------------------+\033[0m"
  echo -e "\033[0;41m| FATAL: You need to have a 'hugo.local.toml' for development mode.    |\033[0m"
  echo -e "\033[0;41m|        (please copy it from 'hugo.local.toml~sample' to get started) |\033[0m"
  echo -e "\033[0;41m+----------------------------------------------------------------------+\033[0m"
  echo
  exit 1
fi

legacy=0
if grep -q -c variant_hide_in_development "hugo.local.toml"; then
  legacy=1
fi
if grep -q -c variant_identify_variant_in_development "hugo.local.toml"; then
  legacy=1
fi

if [[ $legacy -eq 1 ]]; then
  echo -e "\033[0;41m+----------------------------------------------------------------------+\033[0m"
  echo -e "\033[0;41m| FATAL: You have legacy settings in 'hugo.local.toml'.                |\033[0m"
  echo -e "\033[0;41m|        (please copy settings from 'hugo.local.toml~sample')          |\033[0m"
  echo -e "\033[0;41m+----------------------------------------------------------------------+\033[0m"
  echo
  exit 1
fi
