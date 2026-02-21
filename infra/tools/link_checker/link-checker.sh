#!/bin/bash

declare -r mydir=$(dirname "$0")
declare -r myip=$(ifconfig en0 | grep inet | grep -v inet6 | awk '{print $2}')
declare -r output="link_checker_output.json"

if ! command -v caddy 1>/dev/null; then
  echo "FATAL: Link checker requires caddy (Python HTTP server is weak!)"
  echo "       $ brew install caddy"
  exit 1
fi

target=""

while [ 1 ]; do
  if [[ -z $1 ]]; then
    break
  fi

  case "$1" in
    --local)
      target="http://${myip}:9000"
      ;;
    --official)
      target='https://www.union.ai/docs'
      ;;
    --staging)
      target='https://staging.union.ai/docs'
      ;;
    --branch)
      if [[ -z $2 ]]; then
        echo "FATAL: --branch <branch> is required"
        exit 1
      fi
      shift
      branch="$1"
      # Replace all slashes with hyphens in the branch name for URL compatibility
      branch_url=${branch//\//-}
      target="https://${branch_url}.docs-dog.pages.dev/docs"
      ;;
  esac

  shift
done

if [[ -z $target ]]; then
  echo "FATAL: $0 --local | --official | --staging | --branch <branch>"
  exit 1
fi

echo "Target: ${target}"

sed -e "s#@@TARGET@@#${target}#g" < "${mydir}/config.yml.tmpl" \
  > "${mydir}/config.yml"

echo "-----------------------------------"
cat "${mydir}/config.yml"
echo "-----------------------------------"

docker run -v "${mydir}/config.yml":/config.yml:ro,z jenswbe/dead-link-checker \
  --json > "${output}"

result=$(cat <<EOF

---------------------------------
Results in ${output} @ $(realpath "${output}")
Failures: $(grep -c AbsoluteURL < "${output}")
404: $(grep -c 404 < "${output}")
---------------------------------

EOF
)

echo "$result"

(
  echo "$result"
  cat "$output"
) | less
