---
title: JSONL
weight: 1
variants: +flyte +union
---

# JSONL

The JSONL plugin adds two typed I/O types for working with [JSON Lines](https://jsonlines.org/) data as task inputs and outputs: `flyteplugins.jsonl.JsonlFile` for a single JSONL file and `flyteplugins.jsonl.JsonlDir` for a directory of sharded JSONL files. Both are backed by [`orjson`](https://github.com/ijl/orjson) for fast serialization and stream records one at a time, so you can process datasets that don't fit in memory.

`JsonlFile` and `JsonlDir` extend the built-in `flyte.io.File` and `flyte.io.Dir` types, so they inherit remote-storage, upload/download, and caching behavior. They simply add JSONL-aware streaming readers and writers on top. Every read/write method has a synchronous `_sync` counterpart (`writer_sync()`, `iter_records_sync()`) for use in non-`async` tasks.

## When to use this plugin

- Passing line-delimited JSON datasets (LLM training/eval sets, event logs, model outputs) between tasks
- Streaming records without loading an entire file into memory
- Writing large outputs as automatically rotated, sharded directories
- Working with compressed JSONL (`.jsonl.zst`) transparently

## Installation

```bash
pip install flyteplugins-jsonl
```

Add the plugin to your task image. Installing it registers `JsonlFile` and `JsonlDir` with the Flyte type engine automatically. No explicit registration call is needed:

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="setup" lang="python" >}}

## Working with `JsonlFile`

Create a writable file reference with `JsonlFile.new_remote()`, then stream records through the `writer()` context manager without holding the whole dataset in memory:

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="write-jsonl-file" lang="python" >}}

Reading is equally streaming. `iter_records()` yields one parsed `dict` per line:

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="read-jsonl-file" lang="python" >}}

## Working with `JsonlDir`

`JsonlDir` writes a directory of shard files (`part-00000.jsonl`, `part-00001.jsonl`, …) and reads them back transparently in sorted order. Pass `max_records_per_shard` (or `max_bytes_per_shard`) to control shard rotation:

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="write-jsonl-dir" lang="python" >}}

Reading iterates across all shards transparently, prefetching the next shard in the background to overlap network I/O with processing:

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="read-jsonl-dir" lang="python" >}}

For bulk processing, `iter_batches()` yields lists of records at a time; `JsonlDir` also inherits all `flyte.io.Dir` capabilities (`walk()`, `list_files()`, `download()`):

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="batch-iteration" lang="python" >}}

## Configuration and options

### Compression

Give the file a `.jsonl.zst` (or `.jsonl.zstd`) extension and records are zstd-compressed transparently on write and decompressed on read. Tune the level via the writer:

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="write-compressed-file" lang="python" >}}

For `JsonlDir`, set `shard_extension=".jsonl.zst"` on `writer()`. Mixed compressed and uncompressed shards within a directory are supported on read:

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="write-compressed-dir" lang="python" >}}

### Error handling on read

The record iterators accept an `on_error` argument: `"raise"` (default), `"skip"` to drop malformed lines, or a callable `(line_number, raw_line, exception) -> None` for custom handling:

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="error-handling" lang="python" >}}

### Arrow batches

To hand JSONL data to columnar tooling, stream it as Arrow `RecordBatch`es with `iter_arrow_batches(batch_size=...)`. Memory usage stays bounded by the batch size. Arrow iteration requires the optional `pyarrow` dependency. Install it with `pip install 'flyteplugins-jsonl[arrow]'`:

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="arrow-batches" lang="python" >}}

## Common use cases

- **LLM dataset pipelines**: stream prompt/completion or eval records between preprocessing, generation, and scoring tasks.
- **Event and log processing**: read large line-delimited logs shard by shard without buffering the whole file.
- **Fan-out writes**: produce a `JsonlDir` of rotated shards from a task that emits millions of records, then consume it downstream.

## API reference

See the [JSONL API reference](../../api-reference/integrations/jsonl/_index) for the full `JsonlFile` and `JsonlDir` method listings.
