#!/bin/bash

declare run_log
run_log=$(mktemp)
readonly run_log

trap 'rm -f "$run_log"' EXIT

if [[ -z $VARIANT ]]; then
    echo "VARIANT is not set"
    exit 1
fi

hugo --config hugo.toml,config.${VARIANT}.toml --destination dist/${VARIANT} \
    --panicOnWarning 1> "$run_log" 2>&1
if [[ $? -ne 0 ]]; then
    echo '--------------------------'
    sed 's/WARN/\x1b[33mWARN\x1b[0m/g; s/ERROR/\x1b[31mERROR\x1b[0m/g' "$run_log" \
        | grep -v "suppress this warning" | grep -v "ignoreLogs ="
    echo '--------------------------'
    echo "FATAL: Hugo failed"
    exit 1
fi