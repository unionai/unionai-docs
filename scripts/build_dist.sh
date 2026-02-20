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

if [ -z "$VARIANTS" ]; then
    echo "ERROR: VARIANTS is not set" >&2
    exit 1
fi

# Run Hugo variant builds in parallel — each writes to its own dist/ subdirectory.
printf "\n\033[1;36m==>\033[0m \033[1mHugo builds (parallel: $VARIANTS)\033[0m\n"
parallel_start=$(date +%s)
pids=()
variant_logs=()
variant_list=($VARIANTS)

for variant in "${variant_list[@]}"; do
    log=$(mktemp)
    variant_logs+=("$log")
    (
        vstart=$(date +%s)
        $MAKE_CMD variant VARIANT=$variant > "$log" 2>&1
        rc=$?
        echo "$(( $(date +%s) - vstart )) Hugo build: $variant" >> "$BUILD_TIMER_FILE"
        exit $rc
    ) &
    pids+=($!)
done

# Wait for all, collect failures
failed_variants=()
for i in "${!pids[@]}"; do
    if ! wait "${pids[$i]}"; then
        failed_variants+=("${variant_list[$i]}")
    fi
done

# Print logs (always, so Hugo output is visible)
for i in "${!variant_list[@]}"; do
    printf "\n\033[1;36m--- %s ---\033[0m\n" "${variant_list[$i]}"
    cat "${variant_logs[$i]}"
    rm -f "${variant_logs[$i]}"
done

# Record wall-clock time for the parallel group
parallel_elapsed=$(( $(date +%s) - parallel_start ))
echo "${parallel_elapsed} Hugo builds (wall clock)" >> "$BUILD_TIMER_FILE"

if [ ${#failed_variants[@]} -ne 0 ]; then
    echo "FAILED variants: ${failed_variants[*]}"
    exit 1
fi


run_step "Generate LLM docs" $MAKE_CMD llm-docs || exit 1
