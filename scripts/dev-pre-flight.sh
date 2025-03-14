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
