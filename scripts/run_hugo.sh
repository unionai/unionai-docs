#!/bin/bash

declare run_log
run_log=$(mktemp)
readonly run_log

trap 'rm -f "$run_log"' EXIT

if [[ -z $VARIANT ]]; then
    echo "VARIANT is not set"
    exit 1
fi

hugo --config hugo.toml,hugo.site.toml,config.${VARIANT}.toml \
    --destination dist/docs/${VARIANT} \
    --panicOnWarning 1> "$run_log" 2>&1

err=$?
echo '--------------------------'
sed '
     s/failed:/\nfailed:/g;
     s/: failed/:\nfailed/g;
     s/: error/:\nerror/g;
     s/; see /;\n     see /g;
     s/WARN/----\nWARN/; s/WARN/\x1b[33mWARN\x1b[0m/g;
     s/ERROR/----\nERROR/; s/ERROR/\x1b[31mERROR\x1b[0m/g;
     s/^Error:/----\nError:/;
     s/Error:\n/\x1b[31mERROR \x1b[0m/g;
     s/\(render of "[^"]*" failed\)/\x1b[31m\1\x1b[0m/g;
     s/error calling \(Content: "[^"]*"\):/error calling \n     \x1b[36m\1\x1b[0m/g;
     ' "$run_log" \
    | grep -v "suppress this warning" | grep -v "ignoreLogs ="
echo '--------------------------'
if [[ $err -ne 0 ]]; then
    echo "FATAL: Hugo failed"
    exit 1
fi
