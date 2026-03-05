#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCS_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
HELM_CHARTS_DIR="${1:-../helm-charts}"

# Resolve to absolute path
HELM_CHARTS_DIR="$(cd "$HELM_CHARTS_DIR" && pwd)"

CHARTS=(dataplane knative-operator)
DEST_DIR="$DOCS_ROOT/content/deployment/helm-chart-reference"
CLEANUP_FILES=()

# --- Validate prerequisites ---

if ! command -v helm-docs &>/dev/null; then
  echo "ERROR: helm-docs is not installed."
  echo "Install with: brew install norwoodj/tap/helm-docs"
  echo "Or see: https://github.com/norwoodj/helm-docs#installation"
  exit 1
fi

cleanup() {
  for f in "${CLEANUP_FILES[@]}"; do
    rm -f "$f"
  done
}
trap cleanup EXIT

mkdir -p "$DEST_DIR"

# --- Generate docs for each chart ---

for CHART in "${CHARTS[@]}"; do
  CHART_DIR="$HELM_CHARTS_DIR/charts/$CHART"

  if [[ ! -d "$CHART_DIR" ]]; then
    echo "ERROR: Chart directory not found: $CHART_DIR"
    echo "Usage: $0 [path-to-helm-charts-repo]"
    exit 1
  fi

  TEMPLATE_SRC="$DOCS_ROOT/scripts/helm-docs/$CHART.md.gotmpl"
  TEMPLATE_DST="$CHART_DIR/$CHART.md.gotmpl"
  OUTPUT="$CHART_DIR/README.md"
  DEST="$DEST_DIR/$CHART.md"

  # Copy template into chart directory (helm-docs expects it there)
  cp "$TEMPLATE_SRC" "$TEMPLATE_DST"
  CLEANUP_FILES+=("$TEMPLATE_DST")

  echo "Generating helm-docs for $CHART..."
  helm-docs \
    --chart-search-root "$CHART_DIR" \
    --template-files "$CHART.md.gotmpl" \
    --output-file README.md

  # Wrap angle-bracket placeholders (e.g. <ACCOUNT_ID>, <configmap-name>) in
  # backticks so Hugo's goldmark renderer doesn't treat them as raw HTML.
  # Pattern: < followed by a letter, then 1+ letters/digits/underscores/hyphens, then >
  # Minimum 2 chars inside brackets to avoid matching real HTML tags like <p>, <a>.
  sed -E 's/<([A-Za-z][A-Za-z0-9_-]+)>/`<\1>`/g' "$OUTPUT" > "$DEST"
  echo "Generated: $DEST"
done
