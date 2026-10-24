---
title: Nextflow
description: "Run Nextflow pipelines on Flyte."
icon: book
version: 2.12.1
variants: +flyte +union
layout: py_api
---

# Nextflow



Run Nextflow pipelines on Flyte.

The Nextflow head runs inside a Flyte task, and the `nf-flyte` Nextflow plugin turns every
Nextflow task into a child action of that task, so a whole pipeline is a single Flyte run.

```python
import flyte
from flyteplugins.nextflow import nextflow_image, run_nextflow

env = flyte.TaskEnvironment(name="nextflow", image=nextflow_image())

@env.task
async def demo() -> flyte.io.Dir:
    return await run_nextflow("nf-core/demo", revision="1.2.0", profile="test", outdir="results")
```
## Directory

### Errors

| Exception | Description |
|-|-|
| [`NextflowError`](./nextflowerror) | Raised when `nextflow run` exits with a non-zero status. |

### Methods

| Method | Description |
|-|-|
| [`nextflow_image()`](#nextflow_image) | Image for the task that runs the Nextflow head: a JRE, Nextflow, the nf-flyte plugin and this package. |
| [`run_nextflow()`](#run_nextflow) | Run a Nextflow pipeline from inside a Flyte task. |


### Variables

| Property | Type | Description |
|-|-|-|
| `DEFAULT_NEXTFLOW_VERSION` | `str` |  |
| `DEFAULT_NF_FLYTE_VERSION` | `str` |  |

## Methods

#### nextflow_image()

```python
def nextflow_image(
    nextflow_version: str = '25.10.6',
    nf_flyte: str | Path = '0.1.0',
    base: flyte.Image | None = None,
    name: str = 'nextflow',
) -> flyte.Image
```
Image for the task that runs the Nextflow head: a JRE, Nextflow, the nf-flyte plugin and
this package.

Pipeline processes don't run in this image; each one runs in its own `container`.



| Parameter | Type | Description |
|-|-|-|
| `nextflow_version` | `str` | Nextflow release to install. |
| `nf_flyte` | `str \| Path` | nf-flyte plugin to install, either a version from the Nextflow plugin registry or the path to a locally built plugin zip (`nf-flyte-<version>.zip`). |
| `base` | `flyte.Image \| None` | Image to add Nextflow to (default: the Flyte debian base image). |
| `name` | `str` | Image name. |

#### run_nextflow()

```python
def run_nextflow(
    pipeline: str,
    revision: str | None = None,
    profile: str | None = None,
    params: Mapping[str, Any] | None = None,
    outdir: str | None = None,
    work_dir: str | None = None,
    config: str | Path | None = None,
    resume: bool = False,
    report: bool = False,
    extra_args: Sequence[str] = (),
) -> Dir | None
```
Run a Nextflow pipeline from inside a Flyte task. On a Flyte cluster, every Nextflow task
runs as a child action of the calling task, through the nf-flyte executor; the calling task
must use `nextflow_image()`. In a local run, Nextflow uses its own executors instead
(`local` unless `config` or `profile` selects another, e.g. `docker`).



| Parameter | Type | Description |
|-|-|-|
| `pipeline` | `str` | Pipeline to run: a repository (e.g. `nf-core/rnaseq`), URL or local path. |
| `revision` | `str \| None` | Pipeline revision (git tag, branch or commit). |
| `profile` | `str \| None` | Comma separated Nextflow config profiles, e.g. `test`. |
| `params` | `Mapping[str, Any] \| None` | Pipeline parameters, passed through a params file. |
| `outdir` | `str \| None` | Output directory, passed as `--outdir`. A relative path is placed under this task's raw data prefix. The directory is returned as a `Dir`. |
| `work_dir` | `str \| None` | Work directory; on a cluster, an object store location Flyte can read. Defaults to a `nextflow-work` prefix under this task's raw data prefix, which is shared by all attempts of the task, so a retried task resumes where the failed attempt stopped. Set a fixed location to resume across runs. |
| `config` | `str \| Path \| None` | Extra Nextflow config: a path to a config file, or config text. |
| `resume` | `bool` | Resume a previous run that used the same `work_dir`. Always on when the task is being retried. |
| `report` | `bool` | Render Nextflow's execution report, timeline and DAG into the task's Flyte report. The task must be declared with `report=True`. |
| `extra_args` | `Sequence[str]` | Extra arguments for `nextflow run`. |

**Returns:** The `outdir` as a `Dir`, or None when no `outdir` is given.

