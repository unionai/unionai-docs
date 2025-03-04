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
EOF
