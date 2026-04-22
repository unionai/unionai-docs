---
title: Run a Python script
weight: 11
variants: +flyte +union
---

# Run a Python script

`flyte run python-script` executes an arbitrary `.py` file on a remote
Flyte cluster without wrapping it in a workflow or `@env.task`. Point it
at a script, request resources, and the SDK builds an image, bundles
the code, and runs it.

## When to use it

Reach for `python-script` when:

- You have a working script and want to run it on real cluster hardware
  (GPUs, big memory, long jobs) without rewriting it as a `@env.task`.
- You're prototyping, benchmarking, or reproducing a one-off job and
  don't need typed I/O, caching, or DAG semantics.
- You want to give a collaborator something they can run themselves
  with a single CLI command.

Reach for a normal `@env.task` workflow instead when you need typed
inputs and outputs, cross-task dependencies, caching, retries, or
parameterized re-runs from the UI.

## Quickstart

```bash
flyte run python-script hello.py
```

This uses the default Debian base image, 1 CPU, and 2 GiB of memory —
enough for "hello world". Add flags to request more.

```bash
flyte run python-script train.py \
    --gpu 1 --gpu-type A100 --memory 64Gi \
    --packages torch,transformers \
    --output-dir output
```

Run-level options (`--follow`, `--name`, `--project`, `--domain`) go
on the `flyte run` command, before `python-script`:

```bash
flyte run --project my-proj --domain development python-script ...
```

## What you can specify

| Flag | Default | Purpose |
|---|---|---|
| `--cpu` | `1` | CPU cores to request. |
| `--memory` | `2Gi` | Memory to request. |
| `--gpu` | `0` | Number of GPUs (omit for CPU-only). |
| `--gpu-type` | `T4` | Accelerator class: `T4`, `A100`, `H100`, `L4`, `A10G`, etc. Only used when `--gpu > 0`. |
| `--image` | *(auto)* | Container image URI or a named image from your config. Mutually exclusive with `--packages`. |
| `--packages` | *(none)* | Comma-separated pip packages layered onto the default base image, e.g. `torch,transformers`. Mutually exclusive with `--image`. |
| `--timeout` | `3600` | Task timeout in seconds. The subprocess is killed 60 s before this. |
| `--extra-args` | *(none)* | Comma-separated values passed to the script as `sys.argv`. |
| `--output-dir` | *(none)* | Directory path *inside the container* to upload as the task's output after the script finishes. |
| `--include-files` | *(none)* | Path or glob (relative to the script's directory) to bundle alongside the script. Repeat the flag to pass multiple entries. |
| `--queue` | *(config)* | Flyte queue / cluster override. |

## Handling dependencies

Three modes, in order of increasing control:

### 1. Standard library only

No flag needed. The default image is a plain Debian with Python;
anything in the stdlib (`json`, `os`, `subprocess`, `csv`, `datetime`,
…) works without further setup.

```bash
flyte run python-script hello.py
```

### 2. Pip packages on top of the default image

```bash
flyte run python-script analyze.py --packages numpy,pandas,matplotlib
```

The SDK layers a `pip install` step onto the default image and caches
the result. Re-runs with the same package set skip the build. Changing
the set invalidates the cache and rebuilds.

### 3. Bring your own image

When you need a specific Python version, system packages, or a
pre-baked environment, pass a full image URI:

```bash
flyte run python-script job.py \
    --image 1234.dkr.ecr.us-east-2.amazonaws.com/my-org/job:v1.2.3
```

Your image **must have `flyte` installed** so the Flyte runtime inside
the pod can launch the script. A Dockerfile starting from
`python:3.12-slim-bookworm` with `pip install flyte` works.

If your image is registered in your Flyte config under a short name,
pass the short name instead of a URI and the SDK looks it up in the
image map.

## Handling inputs and outputs

`python-script` does **not** use Flyte's typed I/O. Your script is a
regular Python program: it reads `sys.argv` and writes to a directory
on disk.

### Passing inputs

Use `--extra-args` for positional arguments. The comma-separated values
become `sys.argv[1:]` inside the container:

```bash
flyte run python-script job.py --extra-args "alice,42,--verbose"
```

```python
# job.py
import sys
name, count, *flags = sys.argv[1:]
```

For structured inputs (JSON payloads, files), either inline the data
as a single `--extra-args` value that your script parses, or have the
script download from an S3 path it knows about.

### Capturing outputs

Use `--output-dir` to point at a directory the script writes to. After
the script exits with code 0, the SDK uploads the entire directory
recursively (including subdirectories and binary files) as a
`flyte.io.Dir` on the task's output:

```bash
flyte run python-script job.py --output-dir output
```

```python
# job.py
import os
os.makedirs("output", exist_ok=True)
with open("output/result.csv", "w") as f:
    f.write("col1,col2\n1,2\n")
```

The uploaded directory appears in the run's outputs panel as an S3
URI. Browse or download it from the UI.

`stdout` (with `stderr` merged) is also available on the task output
as a ~80-line tail, so you can peek at the end-of-run output without
reopening the log stream.

## Bundling: what gets uploaded

By default the CLI only bundles the script you pointed at. If your
script imports sibling modules or reads local config/data files, list
them with `--include-files` (repeat the flag for multiple entries):

```bash
flyte run python-script train.py \
    --include-files "*.py" \
    --include-files "configs/settings.yaml"
```

Entries are paths or globs resolved relative to the script's directory;
absolute paths are passed through unchanged. Given:

```
my_job/
  train.py       # flyte run python-script my_job/train.py --include-files "*.py"
  data_utils.py  # importable as: from data_utils import ...
  model.py       # importable as: from model import ...
```

the glob `"*.py"` picks up both sibling modules and makes them
importable inside the container.

For anything more elaborate (transitive package trees, large data
assets, system dependencies), bake the files into a custom image with
`--image`, or switch to a regular `@env.task` workflow.

## Python API

The same feature is available as `flyte.run_python_script()` for
programmatic use:

```python
from pathlib import Path
import flyte

flyte.init_from_config("config.yaml")

run = flyte.run_python_script(
    Path("train.py"),
    gpu=1,
    gpu_type="A100",
    memory="64Gi",
    image=["torch", "transformers"],  # list = pip packages on base image
    output_dir="output",
    extra_args=["--epochs", "10"],
    include_files=["*.py", "configs/settings.yaml"],
)
print(run.url)
```
