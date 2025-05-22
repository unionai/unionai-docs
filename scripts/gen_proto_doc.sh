#!/bin/bash

declare -r source=${1:-"../../flyteorg/flyte/flyteidl/protos/flyteidl"}
declare -r output=${2:-"content/api-reference/flyteidl.md"}
declare    name=${3}

if [[ -z "${name}" ]]; then
  name=$(basename "${source}")
fi

declare protos
protos=$(find "${source}" -name "*.proto")
readonly protos

protoc -I../../flyteorg/flyte/flyteidl/protos \
    -I../../ext/googleapis \
    -I../../../go/pkg/mod/github.com/grpc-ecosystem/grpc-gateway/v2@v2.21.0 \
    --doc_out="." --doc_opt=themes/union/markdown/markdown.tmpl,"out.md" \
    ${protos}

if [[ ! -e "out.md" ]]; then
  echo -e "\033[0;31mFATAL:\033[0m Cannot generate documentation."
  exit 1
fi

cat <<EOF > "${output}"
---
title: "${name}"
variants: +byoc +selfmanaged +serverless +flyte
---

# ${name}
EOF

sed -e 's#<#&lt;#g' -e 's#>#&gt;#g' < out.md >> "${output}"

rm -f out.md
