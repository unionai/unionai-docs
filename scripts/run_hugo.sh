#!/bin/bash

declare run_log
run_log=$(mktemp)
readonly run_log

declare -r hugo_build_toml=".hugo.build.toml"

trap 'rm -f "$run_log" "$hugo_build_toml"' EXIT

if [[ -z $VARIANT ]]; then
    echo "VARIANT is not set"
    exit 1
fi

declare target
declare baseURL

rm -f ".hugo.build.toml"

if [[ -z $VERSION ]]; then
    echo "Version LATEST"
    target="dist/docs/${VARIANT}"
    baseURL="/docs/${VARIANT}/"
    touch "hugo.build.toml"
else
    echo "Version $VERSION"
    target="dist/docs/${VERSION}/${VARIANT}"
    baseURL="/docs/${VERSION}/${VARIANT}/"
    cat << EOF > ".hugo.build.toml"
[params]
current_version = "${VERSION}"
EOF
fi

readonly target

echo "Target: $target"

# --panicOnWarning makes all warnf calls fatal (not just errorf).
# This is intentional: content issues should block deployment.
hugo --config hugo.toml,hugo.site.toml,hugo.ver.toml,config.${VARIANT}.toml,.hugo.build.toml \
    --destination "${target}" --baseURL "${baseURL}" \
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
    echo "FATAL: Hugo build failed for variant=${VARIANT}"
    exit 1
fi
