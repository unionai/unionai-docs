---
title: NVIDIA Nsight Systems
description: "Flyte NVIDIA Nsight Systems plugin."
icon: book
version: 2.11.1.dev3+g825fdbe57
variants: +flyte +union
layout: py_api
---

# NVIDIA Nsight Systems



## Directory

### Functions

| Function | Description |
|-|-|
| [`flyteplugins.nsight.capture_report_file()`](flyteplugins.nsight/_index#capture_report_file) | Upload the .nsys-rep and surface it as a trace output. |
| [`flyteplugins.nsight.nsys_available()`](flyteplugins.nsight/_index#nsys_available) | True if the `nsys` binary is on PATH in this container. |
| [`flyteplugins.nsight.nsys_profile()`](flyteplugins.nsight/_index#nsys_profile) | Profile a Flyte task with Nsight Systems. |
| [`flyteplugins.nsight.session_name()`](flyteplugins.nsight/_index#session_name) |  |
| [`flyteplugins.nsight.under_nsys()`](flyteplugins.nsight/_index#under_nsys) | True only when the runtime actually re-exec'd this process under `nsys launch`. |
| [`flyteplugins.nsight.nsys.profile()`](flyteplugins.nsight.nsys/_index#profile) | Profile the wrapped block as a named region. |
| [`flyteplugins.nsight.nsys.range()`](flyteplugins.nsight.nsys/_index#range) | Profile the wrapped block as a named region. |
| [`flyteplugins.nsight.nvtx.mark()`](flyteplugins.nsight.nvtx/_index#mark) | Drop a single NVTX marker at this instant. |
| [`flyteplugins.nsight.nvtx.range()`](flyteplugins.nsight.nvtx/_index#range) | Push an NVTX range on enter and pop it on exit. |

### Packages

| Package | Description |
|-|-|
| [`flyteplugins.nsight`](flyteplugins.nsight/_index) | Flyte NVIDIA Nsight Systems plugin. |
| [`flyteplugins.nsight.nsys`](flyteplugins.nsight.nsys/_index) | Region profiling: collect only part of a task. |
| [`flyteplugins.nsight.nvtx`](flyteplugins.nsight.nvtx/_index) | NVTX annotation helpers. |

