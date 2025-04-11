#!/bin/bash

declare -r mydir=$(dirname "$0")
declare -r myip=$(ifconfig en0 | grep inet | grep -v inet6 | awk '{print $2}')
declare -r output="link_checker_output.json"

sed -e "s/@@IP@@/${myip}/g" < config.yml.tmpl > config.yml

if ! command -v caddy 1>/dev/null; then
  echo "FATAL: Link checker requires caddy (Python HTTP server is weak!)"
  echo "       $ brew install caddy"
  exit 1
fi

echo "-----------------------------------"
cat "${mydir}/config.yml"
echo "-----------------------------------"

docker run -v "${mydir}/config.yml":/config.yml:ro,z jenswbe/dead-link-checker \
  --json > "${output}"

result=$(cat <<EOF

---------------------------------
Results in ${output} @ $(realpath "${output}")
Failures: $(grep -c AbsoluteURL < "${output}")
---------------------------------

EOF
)

echo "$result"

(
  echo "$result"
  cat "$output"
) | less
