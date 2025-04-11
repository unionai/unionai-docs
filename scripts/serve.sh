#!/bin/bash

declare port=${PORT:-9000}
decalre launch=${LAUNCH:-1}


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

cd dist

if command -v caddy 1>/dev/null; then
  echo "Using Caddy HTTP server"
  caddy file-server --listen=:${port}
else
  echo "Using Python HTTP server"
  python3 -m http.server ${PORT}
fi

cd ..
