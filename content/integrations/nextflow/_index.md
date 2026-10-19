---
title: Nextflow
description: Run Nextflow pipelines on Flyte, with every Nextflow task as a child action of the calling task.
icon: diagram-3
weight: 3
variants: +flyte +union
---

# Nextflow

The Nextflow plugin runs [Nextflow](https://www.nextflow.io/) pipelines on Flyte. The Nextflow head runs inside a Flyte task, and the [nf-flyte](https://github.com/unionai/nf-flyte) Nextflow plugin runs every Nextflow task as a child action of that task. A pipeline therefore shows up in Flyte as one run, with one action per Nextflow task:

- Each process runs in its own `container`, with its `cpus`, `memory`, `disk`, `accelerator`, and `time` directives. The image only needs `bash`: Flyte stages the task's files.
- Nextflow keeps its own retries (`errorStrategy`) and `-resume`. Flyte caches task results across runs.
- Aborting the Flyte run aborts the pipeline and its running tasks.

Use this plugin to run existing Nextflow pipelines, such as those from [nf-core](https://nf-co.re/), without rewriting them, and to chain them with Python tasks in the same Flyte run.

## Installation

```bash
pip install flyteplugins-nextflow
```

## Quick start

`nextflow_image()` builds the image for the task that runs the Nextflow head, with `flyteplugins-nextflow` installed. Call `run_nextflow` from an async task:

```python
import flyte
from flyte.io import Dir
from flyteplugins.nextflow import nextflow_image, run_nextflow

env = flyte.TaskEnvironment(
    name="nextflow",
    image=nextflow_image(),
    resources=flyte.Resources(cpu=2, memory="4Gi"),
)


@env.task
async def nf_core_demo(revision: str = "1.2.0") -> Dir:
    # The `test` profile brings its own small samplesheet and resource limits
    return await run_nextflow("nf-core/demo", revision=revision, profile="test", outdir="results")
```

```bash
flyte run nf_core_demo.py nf_core_demo
```

This runs the [nf-core/demo](https://nf-co.re/demo) pipeline (FastQC, seqtk trim, and MultiQC). Each process runs as a child action of `nf_core_demo`, in its own biocontainers image, and the results directory comes back as a `Dir`.

The resources on the task environment apply only to the Nextflow head. Pipeline processes get their resources from their own directives.

## `run_nextflow` arguments

| Argument     | Description |
|--------------|-------------|
| `pipeline`   | Repository (`nf-core/rnaseq`), URL or path to run. |
| `revision`   | Git tag, branch or commit (`-r`). |
| `profile`    | Comma-separated config profiles (`-profile`). |
| `params`     | Pipeline parameters as a mapping, passed as a params file. |
| `outdir`     | `--outdir`. A relative path goes under the task's raw data prefix. The directory is returned as a `Dir`; without `outdir`, `run_nextflow` returns `None`. |
| `work_dir`   | Work directory. Default: `nextflow-work` under the task's raw data prefix. |
| `config`     | Extra Nextflow config: config text, or an absolute path to a config file (a `Path`, or a string ending in `.config`). Relative paths don't resolve, because Nextflow runs in a temporary launch directory. |
| `resume`     | Resume the previous run that used the same `work_dir`. |
| `report`     | Render Nextflow's execution report, timeline, and DAG into the task's Flyte report. The task must be declared with `report=True`. |
| `extra_args` | Any other `nextflow run` arguments. |

`run_nextflow` must be called from inside a Flyte task.

For example, to pass pipeline parameters and add a config override:

```python
await run_nextflow(
    "nf-core/rnaseq",
    params={"input": "s3://my-bucket/samplesheet.csv", "genome": "GRCh38"},
    config="process.errorStrategy = 'retry'\nprocess.maxRetries = 2",
    outdir="results",
)
```

## Reports

With `report=True`, Nextflow's execution report, timeline, and DAG appear as tabs in the task's report in the Flyte UI. Declare the task with `report=True` as well:

```python
@env.task(report=True)
async def rnaseq() -> Dir:
    return await run_nextflow("nf-core/rnaseq", profile="test", outdir="results", report=True)
```

The reports are published even when the pipeline fails.

## Resume

Nextflow's resume state lives in the work directory, not in the task pod:

- the task cache (the cloud cache on object stores; `.nextflow-cache` in the work directory locally)
- a session ID derived from the work directory

This has two effects:

- **Retries resume automatically.** The default work directory is shared by all attempts of a task, so a retried task passes `-resume` and picks up where the failed attempt stopped.
- **Resuming across runs needs a fixed `work_dir`.** Pass the same `work_dir` to each run, and `resume=True` from the second run on:

  ```python
  await run_nextflow("nf-core/rnaseq", work_dir="s3://my-bucket/rnaseq-work", resume=True)
  ```

## Errors

If Nextflow exits with a non-zero status, `run_nextflow` raises a `NextflowError`. Its message contains the end of the Nextflow output and the end of `.nextflow.log`, and its `exit_code` attribute holds Nextflow's exit status.

## Local runs

When the task runs locally (`flyte run --local`), Nextflow uses its own executors instead of nf-flyte: `local` by default, or whatever `profile` or `config` selects, such as `docker`. This needs `nextflow` on the `PATH`.

## Image

`nextflow_image()` contains a JRE, Nextflow, and the nf-flyte plugin. Pipeline processes don't run in this image; each one runs in its own `container`.

| Argument           | Description |
|--------------------|-------------|
| `nextflow_version` | Nextflow release to install. Default: `25.10.6`. |
| `nf_flyte`         | nf-flyte plugin to install: a version from the Nextflow plugin registry, or the `Path` to a locally built plugin zip (`nf-flyte-<version>.zip`). |
| `base`             | Image to add Nextflow to. Default: the Flyte Debian base image. |
| `name`             | Image name. Default: `nextflow`. |

To use a locally built nf-flyte plugin, pass its zip:

```python
from pathlib import Path

image = nextflow_image(
    nf_flyte=Path("~/nf-flyte/build/distributions/nf-flyte-0.1.0.zip").expanduser(),
)
```

## Requirements

- `flyte` 2.12.0 or later, and `flyteplugins-nextflow` 2.12.0 or later.
- On a cluster, the work directory must be on an object store Flyte can read (S3, GCS, or Azure). The default, under the task's raw data prefix, always is.
- Every process container needs `bash`.
