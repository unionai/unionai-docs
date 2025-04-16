#!/bin/bash

declare port=${PORT:-9000}
declare launch=${LAUNCH:-1}


if [[ $launch -eq 1 ]]; then
  cat <<EOF
------------------
Opening browser @ http://localhost:${port}
------------------
EOF
  open "http://localhost:${port}"
else
  cat <<EOF
------------------
Open browser @ http://localhost:${port}
------------------
EOF
fi


if command -v caddy 1>/dev/null; then
  echo "Using Caddy HTTP server"
  caddy run --config scripts/Caddyfile --watch
else
  echo "Using Python HTTP server"
  cd dist
  python3 -m http.server ${PORT}
  cd ..
fi