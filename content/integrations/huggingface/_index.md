---
title: Hugging Face
description: Pass Hugging Face datasets.Dataset and IterableDataset values between tasks as typed inputs and outputs.
icon: emoji-smile
weight: 1
variants: +flyte +union
---

# Hugging Face

The Hugging Face plugin makes [`datasets.Dataset`](https://huggingface.co/docs/datasets/) and `datasets.IterableDataset` first-class task inputs and outputs, and adds `from_hf()`, which turns a dataset on the [Hub](https://huggingface.co/datasets) into a value you can pass around your workflow.

Both halves run on the same mechanism. `from_hf()` builds a `flyte.io.DataFrame` carrying an `hf://` URI, and the plugin's decoders resolve that URI into a real dataset object at the moment a task asks for one. Nothing downloads until then, which is what lets a Hub dataset behave like any other typed value: pass it between tasks, choose it at runtime, hand the same reference to several tasks at once.

## When to use this plugin

- Pulling training or evaluation data from the Hub without a `load_dataset()` call and a hand-written cache directory in every task
- Passing `datasets.Dataset` objects between tasks with no manual Parquet handling
- Sharing one download across every run in a project, via `cache_root`
- Streaming a split that doesn't fit in memory as a `datasets.IterableDataset`

## Installation

```bash
pip install flyteplugins-huggingface
```

Add the plugin to your task image. Flyte finds it through the `flyte.plugins.types` entry point and registers the type handlers on startup, so there is nothing to import and nothing to call:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/hf_datasets.py" fragment="setup" lang="python" >}}

## What the plugin registers

Six handlers against Flyte's dataframe transformer engine. All of them read and write Parquet; the `hf` ones differ only in that they resolve an `hf://` URI first.

| Python type                | Direction | URI scheme | Behavior                                                                         |
| -------------------------- | --------- | ---------- | -------------------------------------------------------------------------------- |
| `datasets.Dataset`         | output    | any        | Writes the in-memory table to a single `00000.parquet`                           |
| `datasets.Dataset`         | input     | storage    | Reads every Parquet file under the URI and concatenates them into one table      |
| `datasets.Dataset`         | input     | `hf`       | Materializes the Hub source first, then reads it as above                        |
| `datasets.IterableDataset` | output    | any        | Streams batches out to sharded Parquet, rotating every 100,000 rows              |
| `datasets.IterableDataset` | input     | storage    | Returns a generator-backed dataset that pulls row batches from Parquet on demand |
| `datasets.IterableDataset` | input     | `hf`       | Materializes the Hub source first, then streams it as above                      |

Parquet is the default format for both types, so you never annotate a format.

Because these register against the shared dataframe engine, a dataset this plugin writes reads back as a `pandas.DataFrame`, a `pl.DataFrame` or a `pyarrow.Table` in a downstream task; it's Parquet either way. That interchange runs one way only though: the encoder is chosen from the _declared_ type, so handing a `pandas.DataFrame` to a parameter annotated `datasets.Dataset` fails in the encoder with `'DataFrame' object has no attribute 'data'`. Going that direction, take the frame as its own type and convert inside the task with `datasets.Dataset.from_pandas(df)`.

## Referencing a dataset on the Hub

`from_hf()` names a dataset. It does not load one:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/hf_datasets.py" fragment="source" lang="python" >}}

What it returns is a `flyte.io.DataFrame` whose URI encodes the request:

```text
hf://stanfordnlp/imdb?name=plain_text&split=train
```

That URI is what Flyte stores and what the UI shows. The task body receives a hydrated `datasets.Dataset` because the parameter is annotated as one and the `hf` decoder ran on the way in.

Its arguments:

| Argument     | Meaning                                                                                                                 |
| ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `repo`       | The Hub dataset repo, such as `stanfordnlp/imdb` or `nyu-mll/glue`                                                      |
| `name`       | The config (subset) within that repo. Resolved automatically when omitted, with caveats below                           |
| `split`      | A single split such as `train`. Omitting it means _all_ splits                                                          |
| `revision`   | The Hub revision to read. Defaults to `refs/convert/parquet`                                                            |
| `cache_root` | A storage prefix for sharing materialized datasets across runs. See [Reusing downloads](#reusing-downloads-across-runs) |

### It is a value, not just a default

The examples above use `from_hf()` as a parameter default because that reads well, but it isn't a special form. The result is an ordinary `flyte.io.DataFrame`, so you can build one at runtime and pass it in:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/hf_datasets.py" fragment="runtime-arg" lang="python" >}}

This is the form to reach for when the dataset is a parameter of the pipeline rather than a property of the task: mapping one task over several configs, letting a caller choose a split, or reading the repo name from a config file.

A task can also accept or return the reference as a plain `flyte.io.DataFrame`. Typed that way, no decoder runs and nothing downloads. The reference is forwarded as-is:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/hf_datasets.py" fragment="passthrough" lang="python" >}}

**The annotation on the receiving parameter decides whether a download happens.** `datasets.Dataset` materializes the whole thing. `datasets.IterableDataset` materializes it and streams the rows. `flyte.io.DataFrame` does neither.

It also explains something you will notice on remote runs. Ask a completed run for its outputs from your laptop and a dataset comes back as a `DataFrame` reference rather than an opened `datasets.Dataset`. Nothing went wrong; the structured-dataset literal is the transport, and no one asked for a `datasets.Dataset` yet.

## Configs and splits

### Config resolution

Pass `name` and the plugin uses it. Omit it, and it resolves in this order:

1. Use the config literally named `default`, if the converted-Parquet branch has one.
2. Otherwise, if there is exactly one config, use it.
3. Otherwise, raise, listing what's available.

So `from_hf("stanfordnlp/imdb", split="train")` works, because IMDB has a single config (`plain_text`), while `from_hf("nyu-mll/glue", split="train")` fails with:

```text
Hugging Face dataset nyu-mll/glue has multiple parquet configs: ax, cola, mnli,
mnli_matched, mnli_mismatched, mrpc, qnli, qqp, rte, sst2, stsb, wnli.
Pass name=... to from_hf().
```

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/hf_datasets.py" fragment="config" lang="python" >}}

Name the config explicitly even when resolution would succeed. It puts the real config in the URI, which is what shows up in the UI and in the cache key, and it means a repo that gains a second config later doesn't turn your task into a runtime error.

### Omitting `split` concatenates everything

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/hf_datasets.py" fragment="splits" lang="python" >}}

Every converted Parquet split under the config is read and presented as one dataset. You do not get a `DatasetDict` and no column records which split a row came from.

The IMDB case is a good illustration of how surprising this is: `plain_text` has `train` (25,000), `test` (25,000), and `unsupervised` (50,000), so omitting `split` hands you 100,000 rows, half of them unlabeled. Specify the split unless you genuinely want the union.

## Reusing downloads across runs

Without `cache_root`, a Hub reference materializes into a throwaway path scoped to the current execution. Every run downloads again.

With `cache_root`, materialized Parquet lands in a shared registry that later runs check first:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/hf_datasets.py" fragment="cache" lang="python" >}}

Point it at a prefix your tasks can read and write. The layout underneath is:

```text
{cache_root}/huggingface/datasets/
  by-key/{key}.json                       # registry record
  blobs/{key}/_flyte_hf_manifest.json     # what this artifact contains
  blobs/{key}/0000.parquet                # the shards themselves
```

On a hit you'll see `Using cached Hugging Face dataset at ...` in the task logs; on a miss, `Materializing Hugging Face dataset ... to remote cache artifact ...`.

### Two caches, keyed differently

The plugin's artifact cache and Flyte's task cache do not key on the same thing.

|                                   | Keyed on                                                        | Decides                                      |
| --------------------------------- | --------------------------------------------------------------- | -------------------------------------------- |
| **Artifact cache** (`cache_root`) | repo, config, split, revision, **plus the resolved shard list** | Whether the Hub is contacted                 |
| **Task cache** (`DataFrame.hash`) | repo, config, split, revision                                   | Whether a downstream cached task re-executes |

`from_hf()` stamps a hash onto the `DataFrame` it returns, and Flyte uses a literal's hash, when present, in place of the serialized literal when computing an action's cache key. Two consequences follow:

- **`cache_root` is not part of the hash:** Switching cache roots or adding one to a reference that didn't have one, does not invalidate downstream cached tasks. This is deliberate: where the bytes are staged says nothing about what they are.
- **The shard list is not part of the hash either:** If a repo's Parquet conversion is regenerated, the artifact cache notices and re-downloads, but a downstream `cache="auto"` task still hits on its old result.

> [!WARNING] Pin `revision` when correctness depends on the exact bytes
> The default `refs/convert/parquet` is a moving branch that Hugging Face regenerates when the source dataset changes. Worse, the shard fingerprint the artifact cache computes is built from what `HfFileSystem.ls` reports, which in practice is the path and byte size — the `etag` and `last_modified` fields it also looks for come back empty. A revision that changes content without changing file sizes will not invalidate either cache.
>
> For reproducible training runs, pass an explicit `revision` (a commit SHA on the converted-Parquet branch) rather than relying on cache invalidation to notice a change for you.

## Reading only the columns you need

Annotate the parameter with an `OrderedDict` of the columns you want and the plugin pushes that down into the Parquet read:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/hf_datasets.py" fragment="projection" lang="python" >}}

Columns you don't name are never decoded. On a wide dataset, selecting just two columns out of forty can significantly reduce read overhead. This also works with `cache_root`: the cached artifact retains all columns, while each task reads only the subset it needs.

## `Dataset` or `IterableDataset`

Both types accept the same references. The difference is what happens on the way in.

`datasets.Dataset` reads every Parquet file under the URI and concatenates them into one in-memory Arrow table. Fast, random-access and bounded by your task's memory.

`datasets.IterableDataset` returns a generator-backed dataset that pulls row batches from Parquet as you consume them. Peak memory is one batch:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/hf_datasets.py" fragment="iterable" lang="python" >}}

Notes on the iterable form:

- Consume it with ordinary synchronous iteration (`for row in ds`, `ds.take(n)`), even inside an `async` task.
- `.map()` stays lazy, as it does in plain `datasets`. Nothing runs until rows are pulled.
- Returning one writes sharded Parquet, rotating to a new file every 100,000 rows. A returned `datasets.Dataset`, by contrast, always writes a single file.
- There is no random access, no `len()`, and no shuffle buffer beyond what `datasets` itself provides.

Rule of thumb: `Dataset` when the split fits in the task's memory and you want to index into it, `IterableDataset` when it doesn't or when you're making a single pass.

## Passing datasets between tasks

A task can return a `datasets.Dataset` it built or transformed and the next task just declares the type:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/hf_datasets.py" fragment="handoff" lang="python" >}}

Serialization to Parquet is automatic in both directions. This is independent of `from_hf()` (a dataset produced by task code is a materialized value, not a source reference), but the two compose exactly as you'd hope: pull from the Hub, transform, hand the result on and only the first task ever touches `huggingface.co`.

> [!WARNING] Call `flatten_indices()` before returning a filtered or shuffled dataset
> `filter()`, `shuffle()`, `train_test_split()` and non-contiguous `select()` do not copy rows. They record an index mapping over the original Arrow table. When the dataset is serialized, the encoder writes the underlying table but not that mapping. As a result, the next task receives the full original set of rows rather than the transformed subset, with no error or warning.
>
> ```python
> # Returns all 3 rows, including the two that were filtered out.
> return ds.filter(lambda row: row["label"] == 1)
>
> # Returns 1 row, as intended.
> return ds.filter(lambda row: row["label"] == 1).flatten_indices()
> ```
>
> A contiguous `select(range(n))` happens to work because datasets implements it as a slice rather than an index mapping. Don’t rely on that distinction. Call `flatten_indices()` on any dataset you didn’t construct row by row; when there is no index mapping, it is effectively a no-op.
>
> This applies to `datasets.Dataset` only. A returned `IterableDataset` is written by iterating it, so its transformations are already applied.

List-valued columns survive the round trip, which is what makes the tokenize-then-train split practical: a CPU task can emit `input_ids` and `attention_mask` and a GPU task consumes them without ever loading a tokenizer. They come back as an Arrow list feature, so expect the integer width to be whatever Parquet stored rather than exactly what you handed in.

## Private and gated datasets

Set `HF_TOKEN` in the task environment. The plugin passes it to `HfFileSystem` for both listing and download:

```python
env = flyte.TaskEnvironment(
    name="hf_env",
    image=image,
    secrets=[flyte.Secret(key="huggingface-token", as_env_var="HF_TOKEN")],
)
```

Without it the plugin falls back to anonymous access and logs:

```text
HF_TOKEN not set, using anonymous access. Private datasets will fail.
```

That's a warning, not an error, and it appears on _every_ materialization including public ones. A private repo then fails later, when the listing comes back empty. If a dataset you know exists reports no Parquet conversion, check the token before you check the dataset.

See [Secrets](../../user-guide/tasks/task-configuration/secrets) for how to store and mount one.

## End-to-end: fine-tuning on IMDB

The pipeline below sources IMDB from the Hub, tokenizes on CPU, fine-tunes DistilBERT on GPU, and scores held-out reviews by streaming them. Every dataset crossing a task boundary does so as a `datasets` object; no task writes a data file by hand.

The environments split by hardware, with one `cache_root` shared across the project:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/imdb_sentiment.py" fragment="env" lang="python" >}}

Subsampling comes first, and it is where the `flatten_indices()` rule above applies: a shuffled `select()` that skips it would hand all 25,000 rows to the trainer:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/imdb_sentiment.py" fragment="prepare" lang="python" >}}

Tokenizing is a cached CPU task. It returns a dataset whose `input_ids` and `attention_mask` are list columns, and those cross to the GPU task intact:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/imdb_sentiment.py" fragment="tokenize" lang="python" >}}

Training receives datasets, not paths, and hands `Trainer` exactly what it expects:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/imdb_sentiment.py" fragment="train" lang="python" >}}

Evaluation receives the very same value the tokenizer was given, a `datasets.Dataset`, but annotates it as an `IterableDataset`, so it arrives as a stream and gets scored a batch at a time instead of loaded:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/imdb_sentiment.py" fragment="evaluate" lang="python" >}}

Same bytes in storage, different view, decided entirely by the annotation.

The driver builds both references up front and fans the CPU work out across them:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/imdb_sentiment.py" fragment="main" lang="python" >}}

The first run downloads both splits into `cache_root`. Every run after that starts from Parquet already in storage, including runs from a colleague's laptop once `HF_CACHE_ROOT` points you both at the same bucket.

When you adapt this, keep one detail from `main`: evaluation scores the _shuffled_ subsample, not the head of the raw test split. IMDB's test split is ordered by label, 12,500 negatives followed by 12,500 positives, so streaming the first N rows would score a model against negatives only and report an accuracy that means nothing. Sorted splits are common enough on the Hub that you should check before taking a prefix of one.

It runs locally with no setup, because `CACHE_ROOT` falls back to a local directory when `HF_CACHE_ROOT` is unset:

```bash
flyte run --local imdb_sentiment.py main --train_rows 200 --eval_rows 100
```

Same code path either way. Only where the cache lives changes, so set `HF_CACHE_ROOT` to a bucket when you want the download shared.

## Running the examples

Both files are self-contained scripts. `hf_datasets.py` composes the individual features into one driver task:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/huggingface/hf_datasets.py" fragment="main" lang="python" >}}

Run either against a cluster with `python hf_datasets.py`, or against local disk with `flyte run --local hf_datasets.py main`. Both cache to a local directory unless `HF_CACHE_ROOT` names object storage, so neither needs setup to try.

## Common use cases

- **Training pipelines on public data**: source the dataset by reference, download it once per project rather than once per run, and keep the repo, config, split and revision visible in the run's inputs.
- **Tokenize once, train many**: a cached CPU task emits tokenized datasets; GPU tasks consume them directly, so hyperparameter sweeps never re-tokenize.
- **Evaluation over large splits**: stream a held-out split as an `IterableDataset` and score it in bounded memory.
- **Fan-out over configs**: map one task across the configs of a multi-config benchmark by building a `from_hf()` reference per config at runtime.
- **Mixed-backend workflows**: land Hub data as Parquet and read it downstream as pandas, Polars, or Arrow through the shared dataframe engine.

## API reference

See the [Hugging Face API reference](../../api-reference/integrations/huggingface/_index) for `from_hf()` and `HFSource`. The encode/decode handlers are internal; you never construct one yourself.
