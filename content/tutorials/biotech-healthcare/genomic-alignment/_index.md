---
title: Genomic alignment
weight: 1
variants: +flyte +union
---

# Genomic alignment

> [!NOTE]
> Code available [on GitHub](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/genomic_alignment).

This tutorial builds a bioinformatics pipeline that aligns raw sequencing reads to a reference genome. The workflow downloads a reference genome and paired-end sequencing data, performs quality filtering, builds a reference index, and aligns the filtered reads with the [Bowtie 2](https://bowtie-bio.sourceforge.net/bowtie2/index.shtml) aligner, running each sample in parallel.

It's a good showcase of how Flyte handles real bioinformatics workloads:

- **Per-task resources** so quality filtering, indexing, and alignment each request exactly the CPU and memory they need.
- **`cache="auto"`** on the download and indexing steps, so re-runs skip work that hasn't changed.
- **Fan-out parallelism** across samples with `asyncio.gather`.
- **System dependencies** (`fastp`, `bowtie2`) installed into the container image with `apt`.

## Define the container image

Because the pipeline shells out to bioinformatics tools, we build a custom image with `flyte.Image.from_uv_script` and install `fastp` (quality filtering) and `bowtie2` (alignment) via `apt`.

{{< code file="/unionai-examples/v2/tutorials/genomic_alignment/genomic_alignment.py" fragment=image lang=python >}}

The Python dependencies are declared at the top of the file using the `uv` script style:

```
# /// script
# requires-python = "3.12"
# dependencies = [
#    "flyte",
#    "requests",
# ]
# main = "alignment_wf"
# ///
```

## Define the task environments

Each stage runs in its own `TaskEnvironment` with tailored resources. The top-level `base_env` declares the others as `depends_on` so the tasks it calls are available at run time.

{{< code file="/unionai-examples/v2/tutorials/genomic_alignment/genomic_alignment.py" fragment=envs lang=python >}}

## Define the data classes

We model the reference genome, sequencing reads, and alignment results as dataclasses. `flyte.io.File` and `flyte.io.Dir` reference offloaded data in blob storage, so large genomic files are passed between tasks by reference rather than copied through the orchestrator.

{{< code file="/unionai-examples/v2/tutorials/genomic_alignment/genomic_alignment.py" fragment=dataclasses lang=python >}}

## Fetch assets

The first task downloads the reference genome and paired-end reads from remote URLs and materializes them as `File`/`Dir` objects. It's cached, so repeat runs skip the download.

{{< code file="/unionai-examples/v2/tutorials/genomic_alignment/genomic_alignment.py" fragment=fetch_assets lang=python >}}

## Quality filtering with fastp

`pyfastp` removes duplicate and low-quality reads. It requests extra memory so it can process larger read files efficiently.

{{< code file="/unionai-examples/v2/tutorials/genomic_alignment/genomic_alignment.py" fragment=pyfastp lang=python >}}

## Build the Bowtie 2 index

A reference index rarely changes, so this task is cached.

{{< code file="/unionai-examples/v2/tutorials/genomic_alignment/genomic_alignment.py" fragment=bowtie2_index lang=python >}}

## Align reads

Each sample is aligned to the indexed reference with Bowtie 2, producing a SAM file.

{{< code file="/unionai-examples/v2/tutorials/genomic_alignment/genomic_alignment.py" fragment=bowtie2_align lang=python >}}

## Orchestrate the workflow

The top-level task fetches the assets, filters every sample in parallel, builds the index, and aligns all samples. Parallelism across samples is achieved with `asyncio.gather` rather than a separate `@dynamic` decorator.

{{< code file="/unionai-examples/v2/tutorials/genomic_alignment/genomic_alignment.py" fragment=workflow lang=python >}}

## Run the workflow

This example has no secrets or external API keys; it pulls public test data from GitHub.

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/genomic_alignment), run it as a `uv` script:

```
cd v2/tutorials/genomic_alignment
uv run --script genomic_alignment.py
```

Or submit it with the Flyte CLI:

```
flyte run genomic_alignment.py alignment_wf
```

When the run completes, each returned `Alignment` points to a SAM file in blob storage that you can download from the run's outputs in the UI.
