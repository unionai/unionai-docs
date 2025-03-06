#!/bin/bash

cat <<EOF
Usage: make [target] [options]

Targets:

  dist

    Build the distribution (all variants)

  variant VARIANT=<variant>

    Build a specific variant (byoc, serverless, etc)

  dev

    Runs the interactive development environment

  serve PORT=<port>

    Launches a web server on the built site for local browsing
EOF

echo
