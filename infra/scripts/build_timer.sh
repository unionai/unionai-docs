#!/bin/bash
# Build timer — records step durations to a temp file and prints a summary.
#
# Usage:
#   export BUILD_TIMER_FILE=$(mktemp)
#   source scripts/build_timer.sh
#
#   build_step_start "Step name"
#   ... do work ...
#   build_step_end
#
#   build_summary   # prints timing table

: "${BUILD_TIMER_FILE:=/tmp/build_timer_$$}"

_build_step_name=""
_build_step_start=0

build_step_start() {
    _build_step_name="$1"
    _build_step_start=$(date +%s)
    printf "\n\033[1;36m==>\033[0m \033[1m%s\033[0m\n" "$_build_step_name"
}

build_step_end() {
    local end=$(date +%s)
    local elapsed=$(( end - _build_step_start ))
    local mins=$(( elapsed / 60 ))
    local secs=$(( elapsed % 60 ))
    if [ "$mins" -gt 0 ]; then
        printf "\033[1;36m    done\033[0m (%dm %ds)\n" "$mins" "$secs"
    else
        printf "\033[1;36m    done\033[0m (%ds)\n" "$secs"
    fi
    echo "${elapsed} ${_build_step_name}" >> "$BUILD_TIMER_FILE"
}

build_summary() {
    local total=0
    printf "\n\033[1;36m%s\033[0m\n" "================================================"
    printf "\033[1m  Build timing summary\033[0m\n"
    printf "\033[1;36m%s\033[0m\n" "================================================"
    while IFS=' ' read -r secs name; do
        local mins=$(( secs / 60 ))
        local s=$(( secs % 60 ))
        if [ "$mins" -gt 0 ]; then
            printf "  %-35s %4dm %02ds\n" "$name" "$mins" "$s"
        else
            printf "  %-35s %7ds\n" "$name" "$s"
        fi
        total=$(( total + secs ))
    done < "$BUILD_TIMER_FILE"
    printf "\033[1;36m%s\033[0m\n" "------------------------------------------------"
    local tmins=$(( total / 60 ))
    local tsecs=$(( total % 60 ))
    if [ "$tmins" -gt 0 ]; then
        printf "  \033[1m%-35s %4dm %02ds\033[0m\n" "TOTAL" "$tmins" "$tsecs"
    else
        printf "  \033[1m%-35s %7ds\033[0m\n" "TOTAL" "$total"
    fi
    printf "\033[1;36m%s\033[0m\n" "================================================"
    rm -f "$BUILD_TIMER_FILE"
}
