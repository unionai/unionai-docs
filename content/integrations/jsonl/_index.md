---
title: JSONL
weight: 1
variants: +flyte +union
---

# JSONL

The JSONL plugin adds two typed I/O types for working with [JSON Lines](https://jsonlines.org/) data as task inputs and outputs: `flyteplugins.jsonl.JsonlFile` for a single JSONL file and `flyteplugins.jsonl.JsonlDir` for a directory of sharded JSONL files. Both are backed by [`orjson`](https://github.com/ijl/orjson) for fast serialization and stream records one at a time, so you can process datasets that don't fit in memory.

`JsonlFile` and `JsonlDir` extend the built-in `flyte.io.File` and `flyte.io.Dir` types, so they inherit remote-storage, upload/download, and caching behavior — they simply add JSONL-aware streaming readers and writers on top.

## When to use this plugin

- Passing line-delimited JSON datasets (LLM training/eval sets, event logs, model outputs) between tasks
- Streaming records without loading an entire file into memory
- Writing large outputs as automatically rotated, sharded directories
- Working with compressed JSONL (`.jsonl.zst`) transparently

## Installation

```bash
pip install flyteplugins-jsonl
```

Add the plugin to your task image. Installing it registers `JsonlFile` and `JsonlDir` with the Flyte type engine automatically — no explicit registration call is needed:

```python
import flyte

image = flyte.Image.from_debian_base(name="jsonl").with_pip_packages("flyteplugins-jsonl")

env = flyte.TaskEnvironment(name="jsonl_env", image=image)
```

## Working with `JsonlFile`

Create a writable file reference with `JsonlFile.new_remote()`, then stream records through the `writer()` context manager. On the read side, `iter_records()` yields one parsed `dict` per line.

```python
from flyteplugins.jsonl import JsonlFile


@env.task
async def write_dataset() -> JsonlFile:
    f = JsonlFile.new_remote("data.jsonl")
    async with f.writer() as w:
        for i in range(10_000):
            await w.write({"id": i, "text": f"record {i}"})
    return f


@env.task
async def count_records(f: JsonlFile) -> int:
    total = 0
    async for record in f.iter_records():
        total += 1
    return total
```

Chain the tasks from a parent task and run it:

```python
@env.task
async def main() -> int:
    dataset = await write_dataset()
    return await count_records(dataset)


if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(main)
    print(run.url)
```

### Synchronous tasks

Every method has a synchronous counterpart for non-`async` tasks — use `writer_sync()` and `iter_records_sync()`:

```python
@env.task
def write_dataset_sync() -> JsonlFile:
    f = JsonlFile.new_remote("data.jsonl")
    with f.writer_sync() as w:
        w.write({"key": "value"})
    return f
```

## Working with `JsonlDir`

`JsonlDir` writes a directory of shard files (`part-00000.jsonl`, `part-00001.jsonl`, …) and reads them back transparently in sorted order. Pass `max_records_per_shard` (or `max_bytes_per_shard`) to control shard rotation:

```python
from flyteplugins.jsonl import JsonlDir


@env.task
async def write_shards() -> JsonlDir:
    d = JsonlDir.new_remote("output_shards")
    async with d.writer(max_records_per_shard=1000) as w:
        for i in range(5000):
            await w.write({"id": i})
    return d


@env.task
async def read_shards(d: JsonlDir) -> int:
    count = 0
    async for record in d.iter_records():
        count += 1
    return count
```

`JsonlDir` also exposes `iter_batches()` to yield lists of records at a time, and inherits all `flyte.io.Dir` capabilities (`walk()`, `list_files()`, `download()`).

## Configuration and options

### Compression

Give the file a `.jsonl.zst` (or `.jsonl.zstd`) extension and records are zstd-compressed transparently on write and decompressed on read. Tune the level via the writer:

```python
f = JsonlFile.new_remote("data.jsonl.zst")
async with f.writer(compression_level=6) as w:  # higher = smaller, slower
    await w.write({"key": "value"})
```

For `JsonlDir`, set `shard_extension=".jsonl.zst"` on `writer()`. Mixed compressed and uncompressed shards within a directory are supported on read.

### Error handling on read

The record iterators accept an `on_error` argument — `"raise"` (default), `"skip"` to drop malformed lines, or a callable `(line_number, raw_line, exception) -> None` for custom handling:

```python
async for record in f.iter_records(on_error="skip"):
    ...
```

### Arrow batches

To hand JSONL data to columnar tooling, stream it as Arrow `RecordBatch`es with `iter_arrow_batches(batch_size=...)`. Memory usage stays bounded by the batch size.

## Common use cases

- **LLM dataset pipelines** — stream prompt/completion or eval records between preprocessing, generation, and scoring tasks.
- **Event and log processing** — read large line-delimited logs shard by shard without buffering the whole file.
- **Fan-out writes** — produce a `JsonlDir` of rotated shards from a task that emits millions of records, then consume it downstream.

## API reference

See the [JSONL API reference](../../api-reference/integrations/jsonl/_index) for the full `JsonlFile` and `JsonlDir` method listings.
