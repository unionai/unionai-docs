---
title: Multimodal retrieval evaluation
weight: 2
variants: +flyte +union
---

# Multimodal retrieval evaluation

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/multimodal-retrieval-evaluation).

This tutorial builds an experiment framework for benchmarking **visual document retrieval** on the [ViDoRe benchmark](https://huggingface.co/vidore). The corpus is a set of PDF page *images* and the queries are plain-text questions — each retrieval method must find the page that answers a question from the raw image alone.

Three approaches are compared:

- **ColPali-v1.2** — patch-level multi-vector embeddings from a vision-language model (PaliGemma), scored with MaxSim late interaction. No OCR.
- **SigLIP-SO400M** — a single global embedding per page from Google's CLIP successor.
- **OCR + BM25** — a text-only baseline that OCRs each page with [docTR](https://github.com/mindee/doctr) on GPU and ranks with BM25.

Each experiment is one `ExperimentConfig`; the pipeline fans them out as concurrent Flyte tasks and returns a ranked comparison table with an interactive HTML report. It's a strong showcase of several Flyte features working together:

- **`ReusePolicy`** keeps warm GPU containers (with the ~7 GB ColPali weights already in VRAM) alive across task calls.
- A process-level **`DynamicBatcher`** aggregates queries from all concurrent search tasks into single GPU batches.
- **`cache="auto"`** so a model's index is built at most once per corpus and shared across experiments.
- **Typed Pydantic inputs/outputs** so every metric is stored alongside the exact config that produced it.

## Define the container image

One image serves every task. `unionai-reuse` provides the actor bridge required by `ReusePolicy`.

{{< code file="/unionai-examples/v2/tutorials/multimodal-retrieval-evaluation/retrieval_eval.py" fragment=image lang=python >}}

The Python dependencies (ColPali, transformers, docTR, etc.) are declared in the `uv` script header at the top of the file.

## Define the task environments

Each model gets its own GPU environment so their warm-container pools scale independently. The ColPali and SigLIP environments use `ReusePolicy` to keep model weights resident; the driver coordinates orchestration, BM25, evaluation, and reporting.

{{< code file="/unionai-examples/v2/tutorials/multimodal-retrieval-evaluation/retrieval_eval.py" fragment=envs lang=python >}}

## Configuration and data types

An experiment is fully described by an `ExperimentConfig`. Because it's a Pydantic model, Flyte serializes it alongside every output.

{{< code file="/unionai-examples/v2/tutorials/multimodal-retrieval-evaluation/retrieval_eval.py" fragment=config_types lang=python >}}

The corpus, queries, retrieval results, and metrics are likewise typed. Page images are stored as `flyte.io.File` handles in blob storage, so tasks read images directly rather than re-fetching over HTTP.

{{< code file="/unionai-examples/v2/tutorials/multimodal-retrieval-evaluation/retrieval_eval.py" fragment=data_types lang=python >}}

## Loading, indexing, and search

`load_vidore_pages` downloads a ViDoRe subset and uploads each page image to blob storage (cached, with retries). Indexing tasks (`index_colpali`, `index_siglip`) encode every page into a `.npz` index, and the OCR task (`extract_page_texts`) produces the text baseline. These run on the GPU environments and are cached per corpus.

Search uses the `DynamicBatcher` so queries from all concurrent search-task invocations on a warm container are merged into a single GPU batch:

{{< code file="/unionai-examples/v2/tutorials/multimodal-retrieval-evaluation/retrieval_eval.py" fragment=search_colpali lang=python >}}

> [!NOTE]
> The `DynamicBatcher` implementation lives in the `extras/` package next to the example. Run the script from the example directory so the import resolves.

## Run one experiment

`run_experiment` selects the right index/search path based on the runtime value of `config.model` — Flyte v2's dynamic execution means there's no static DAG to wire up. `flyte.group` wraps each experiment in a named span in the UI.

{{< code file="/unionai-examples/v2/tutorials/multimodal-retrieval-evaluation/retrieval_eval.py" fragment=run_experiment lang=python >}}

## Compare experiments

The driver loads the dataset once, fans out across all configs with `asyncio.gather`, and emits an interactive Chart.js report in the Flyte UI. Experiments sharing a model reuse the cached index, so you only pay GPU time for new work.

{{< code file="/unionai-examples/v2/tutorials/multimodal-retrieval-evaluation/retrieval_eval.py" fragment=compare_experiments lang=python >}}

## Run the evaluation

This example has no secrets — datasets and model weights are pulled from public Hugging Face repositories. It does require GPUs, so run it remotely.

The experiment grid is defined in the entry point; adding a model or varying `top_k` is a one-line change:

{{< code file="/unionai-examples/v2/tutorials/multimodal-retrieval-evaluation/retrieval_eval.py" fragment=grid lang=python >}}

From the [example directory](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/multimodal-retrieval-evaluation):

```
cd v2/tutorials/multimodal-retrieval-evaluation
python retrieval_eval.py
```

When the run completes, open the `generate_report` task in the UI to see the summary cards, the grouped Recall@K / NDCG@K / MRR bar chart, and the ranked results table.
