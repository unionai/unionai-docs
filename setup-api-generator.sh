#!/bin/bash

set -e  # Exit on any error

echo "🚀 Setting up API generator environment..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ Error: uv is not installed. Please install uv first:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Create virtual environment in repo root (clear existing if present)
echo "📦 Creating virtual environment..."
uv venv --clear

# Install flyte beta from PyPI into the virtual environment
echo "⬇️  Installing latest flyte beta release..."
uv pip install --pre flyte

# Install additional dependencies needed by the API generator
echo "📋 Installing API generator dependencies..."
uv pip install pyyaml prometheus-client

echo "✅ Setup complete!"
echo ""
echo "🎯 Next steps:"
echo "  1. Activate the virtual environment:"
echo "     source .venv/bin/activate"
echo "  2. Run the API generator:"
echo "     make -f Makefile.api.flyte-sdk"
echo ""
echo "📝 Quick command sequence:"
echo "     source .venv/bin/activate && make -f Makefile.api.flyte-sdk"