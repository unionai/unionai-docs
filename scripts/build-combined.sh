#!/bin/bash

# Build script for GitHub Actions
# This script handles building both versions and combining them

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

usage() {
    cat << EOF
Usage: $0 [OPTIONS]

OPTIONS:
    -t, --type TYPE         Build type: production or preview (required)
    -b, --base-ref REF      Base branch reference (for PR builds)
    -h, --head-ref REF      Head branch reference (for PR builds)
    -o, --output DIR        Output directory (default: final_dist)
    --help                  Show this help message

Examples:
    # Production build (builds both v1 and v2)
    $0 --type production

    # PR preview build (builds PR branch + stable other version)
    $0 --type preview --base-ref main --head-ref feature-branch

EOF
}

log() {
    echo "[BUILD] $*" >&2
}

error() {
    echo "[ERROR] $*" >&2
    exit 1
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -t|--type)
            BUILD_TYPE="$2"
            shift 2
            ;;
        -b|--base-ref)
            BASE_REF="$2"
            shift 2
            ;;
        -h|--head-ref)
            HEAD_REF="$2"
            shift 2
            ;;
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        --help)
            usage
            exit 0
            ;;
        *)
            error "Unknown option: $1"
            ;;
    esac
done

# Validate required arguments
if [[ -z "$BUILD_TYPE" ]]; then
    error "Build type is required. Use --type production or --type preview"
fi

if [[ "$BUILD_TYPE" == "preview" && (-z "$BASE_REF" || -z "$HEAD_REF") ]]; then
    error "Preview builds require both --base-ref and --head-ref"
fi

# Set defaults
OUTPUT_DIR="${OUTPUT_DIR:-final_dist}"

cd "$REPO_ROOT"

# Ensure submodules are available
if [ ! -d "external/unionai-examples" ] || [ -z "$(ls -A external/unionai-examples 2>/dev/null)" ]; then
    log "Warning: unionai-examples submodule not available, creating placeholder"
    mkdir -p external/unionai-examples
    touch external/unionai-examples/.gitkeep
fi

# Clean up any previous builds
rm -rf dist current_dist pr_dist "$OUTPUT_DIR"

if [[ "$BUILD_TYPE" == "production" ]]; then
    log "Building production site (both versions)"
    
    # Get current branch
    CURRENT_BRANCH=$(git branch --show-current)
    log "Current branch: $CURRENT_BRANCH"
    
    # Determine versions
    if [[ "$CURRENT_BRANCH" == "main" ]]; then
        CURRENT_VERSION="v2"
        OTHER_VERSION="v1"
        OTHER_BRANCH="v1"
    elif [[ "$CURRENT_BRANCH" == "v1" ]]; then
        CURRENT_VERSION="v1"
        OTHER_VERSION="v2"
        OTHER_BRANCH="main"
    else
        error "Production builds are only supported from main or v1 branches"
    fi
    
    log "Building current version ($CURRENT_VERSION) from $CURRENT_BRANCH"
    make dist-ci
    mv dist current_dist
    
    log "Switching to $OTHER_BRANCH for $OTHER_VERSION"
    git checkout "$OTHER_BRANCH"
    
    log "Building other version ($OTHER_VERSION) from $OTHER_BRANCH"
    make dist-ci
    
    # Switch back to original branch
    git checkout "$CURRENT_BRANCH"
    
    # Combine builds
    log "Combining builds"
    mkdir -p "$OUTPUT_DIR/docs"
    
    if [[ "$CURRENT_VERSION" == "v2" ]]; then
        # Copy v2 (current) to docs/v2/
        cp -r current_dist/docs/* "$OUTPUT_DIR/docs/"
        # Copy v1 (other) to docs/v1/
        cp -r dist/docs/* "$OUTPUT_DIR/docs/v1/"
    else
        # Copy v1 (current) to docs/v1/
        cp -r current_dist/docs/* "$OUTPUT_DIR/docs/v1/"
        # Copy v2 (other) to docs/v2/
        cp -r dist/docs/* "$OUTPUT_DIR/docs/"
    fi
    
    # Copy root index.html from current version
    cp current_dist/index.html "$OUTPUT_DIR/"
    
elif [[ "$BUILD_TYPE" == "preview" ]]; then
    log "Building PR preview"
    
    # Determine version from base ref
    if [[ "$BASE_REF" == "main" ]]; then
        PR_VERSION="v2"
        OTHER_VERSION="v1"
        OTHER_BRANCH="v1"
    elif [[ "$BASE_REF" == "v1" ]]; then
        PR_VERSION="v1"
        OTHER_VERSION="v2"
        OTHER_BRANCH="main"
    else
        error "PR base ref must be main or v1"
    fi
    
    log "Building PR version ($PR_VERSION) from current HEAD"
    make dist-ci
    mv dist pr_dist
    
    log "Switching to $OTHER_BRANCH for $OTHER_VERSION"
    git checkout "$OTHER_BRANCH"
    
    log "Building other version ($OTHER_VERSION) from $OTHER_BRANCH"
    make dist-ci
    
    # Switch back to PR branch
    git checkout "$HEAD_REF" || git checkout -
    
    # Combine builds
    log "Combining builds for preview"
    mkdir -p "$OUTPUT_DIR/docs"
    
    if [[ "$PR_VERSION" == "v2" ]]; then
        # PR is for v2, copy PR build to docs/v2/ and other to docs/v1/
        cp -r pr_dist/docs/* "$OUTPUT_DIR/docs/"
        cp -r dist/docs/* "$OUTPUT_DIR/docs/v1/"
    else
        # PR is for v1, copy PR build to docs/v1/ and other to docs/v2/
        cp -r pr_dist/docs/* "$OUTPUT_DIR/docs/v1/"
        cp -r dist/docs/* "$OUTPUT_DIR/docs/"
    fi
    
    # Copy root index.html from PR version
    cp pr_dist/index.html "$OUTPUT_DIR/"
    
else
    error "Unknown build type: $BUILD_TYPE"
fi

log "Build complete! Output in $OUTPUT_DIR"
log "Structure:"
find "$OUTPUT_DIR" -type f | head -20