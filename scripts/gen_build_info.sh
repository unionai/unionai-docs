#!/bin/bash

declare commit
commit=$(git rev-parse HEAD)
readonly commit

declare version
version=$(grep ^VERSION makefile.inc | awk '{print $3}')
if [[ -z "${version}" ]]; then
    version="main"
fi
readonly version

echo "[build info] Commit: ${commit}"
echo "[build info] Version: ${version}"

cat <<EOF > dist/build_info.json
{
    "commit": "${commit}",
    "version": "${version}"
}
EOF

# Save a copy in /docs/ so we can see in the original site
cp dist/build_info.json dist/docs/build_info.json
