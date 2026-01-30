#!/bin/bash

# Cloudflare Pages build script
# This script ensures Python dependencies are available and runs the full build process

set -e

echo "=== Cloudflare Pages Build Script ==="
echo "Current directory: $(pwd)"
echo "Python version: $(python3 --version)"
echo "Node version: $(node --version)"

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install toml

# Verify dependencies
echo "Verifying Python dependencies..."
python3 -c "import toml; print('toml version:', toml.__version__)"

# Run the build process
echo "Running make dist..."
make dist

echo "Build completed successfully!"
echo "Generated files:"
ls -la dist/

# Copy dist directory to Cloudflare Pages output
echo "Preparing output for Cloudflare Pages..."
# Cloudflare Pages expects output in the root directory or a specific output directory
# The dist/ directory contains our built site