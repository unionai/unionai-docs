#!/bin/bash

declare -r mydir=$(dirname "$0")
declare -r myip=$(ifconfig en0 | grep inet | grep -v inet6 | awk '{print $2}')

sed -e "s/@@IP@@/${myip}/g" < config.yml.tmpl > config.yml

cat config.yml

docker run -v ${mydir}/config.yml:/config.yml:ro,z jenswbe/dead-link-checker \
  --json
