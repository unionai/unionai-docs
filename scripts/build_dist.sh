#!/bin/bash
# Full dist build with progress reporting and timing instrumentation.
# Called by: make dist

export BUILD_TIMER_FILE=$(mktemp)
source scripts/build_timer.sh

# Always print summary, even on failure
trap 'build_summary' EXIT

MAKE_CMD="make"
EXIT_CODE=0

run_step() {
    local name="$1"
    shift
    build_step_start "$name"
    if "$@"; then
        build_step_end
    else
        local rc=$?
        build_step_end
        return $rc
    fi
}

run_step "Pre-build checks & setup" $MAKE_CMD base || exit 1

run_step "Update redirects"    $MAKE_CMD update-redirects || exit 1
run_step "Check deleted pages" $MAKE_CMD check-deleted-pages || true
run_step "Update API docs"     $MAKE_CMD update-api-docs || exit 1
run_step "Check internal links" $MAKE_CMD check-links || true

for variant in flyte byoc selfmanaged; do
    run_step "Hugo build: $variant" $MAKE_CMD variant VARIANT=$variant || exit 1
done

run_step "Generate LLM docs" $MAKE_CMD llm-docs || exit 1
