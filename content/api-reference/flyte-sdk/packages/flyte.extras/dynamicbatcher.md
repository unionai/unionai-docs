---
title: DynamicBatcher
version: 2.0.11
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# DynamicBatcher

**Package:** `flyte.extras`

Batches records from many concurrent producers and runs them through
    a single async processing function, maximizing resource utilization.

    The batcher runs two internal loops:

    1. **Aggregation loop** — drains the submission queue and assembles
       cost-budgeted batches, respecting `target_batch_cost`,
       `max_batch_size`, and `batch_timeout_s`.
    2. **Processing loop** — pulls assembled batches and calls
       `process_fn`, resolving each record's `asyncio.Future`.

    Type Parameters:
        RecordT: The input record type produced by your tasks.
        ResultT: The per-record output type returned by `process_fn`.

    Args:
        process_fn:
            `async def f(batch: list[RecordT]) -&gt; list[ResultT]`
            Must return results in the **same order** as the input batch.

        cost_estimator:
            Optional `(RecordT) -&gt; int` function.  When provided, it is
            called to estimate the cost of each submitted record.
            Falls back to `record.estimate_cost()` if the record
            implements `CostEstimator`, then to `default_cost`.

        target_batch_cost:
            Cost budget per batch.  The aggregator fills batches up to
            this limit before dispatching.

        max_batch_size:
            Hard cap on records per batch regardless of cost budget.

        min_batch_size:
            Minimum records before dispatching.  Ignored when the timeout
            fires or shutdown is in progress.

        batch_timeout_s:
            Maximum seconds to wait for a full batch.  Lower values reduce
            idle time but may produce smaller batches.

        max_queue_size:
            Bounded queue size.  When full, `submit` awaits
            (backpressure).

        prefetch_batches:
            Number of pre-assembled batches to buffer between the
            aggregation and processing loops.

        default_cost:
            Fallback cost when no estimator is available.

    Example::

        async def process(batch: list[dict]) -&gt; list[str]:
            ...

        async with DynamicBatcher(process_fn=process) as batcher:
            futures = []
            for record in my_records:
                f = await batcher.submit(record)
                futures.append(f)
            results = await asyncio.gather(*futures)
    


## Parameters

```python
class DynamicBatcher(
    process_fn: ProcessFn[RecordT, ResultT],
    cost_estimator: CostEstimatorFn[RecordT] | None,
    target_batch_cost: int,
    max_batch_size: int,
    min_batch_size: int,
    batch_timeout_s: float,
    max_queue_size: int,
    prefetch_batches: int,
    default_cost: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `process_fn` | `ProcessFn[RecordT, ResultT]` | |
| `cost_estimator` | `CostEstimatorFn[RecordT] \| None` | |
| `target_batch_cost` | `int` | |
| `max_batch_size` | `int` | |
| `min_batch_size` | `int` | |
| `batch_timeout_s` | `float` | |
| `max_queue_size` | `int` | |
| `prefetch_batches` | `int` | |
| `default_cost` | `int` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_running` | `None` | Whether the aggregation and processing loops are active. |
| `stats` | `None` | Current `BatchStats` snapshot. |

## Methods

| Method | Description |
|-|-|
| [`start()`](#start) | Start the aggregation and processing loops. |
| [`stop()`](#stop) | Graceful shutdown: process all enqueued work, then stop. |
| [`submit()`](#submit) | Submit a single record for batched processing. |
| [`submit_batch()`](#submit_batch) | Convenience: submit multiple records and return their futures. |


### start()

```python
def start()
```
Start the aggregation and processing loops.



**Raises**

| Exception | Description |
|-|-|
| `RuntimeError` | If the batcher is already running. |

### stop()

```python
def stop()
```
Graceful shutdown: process all enqueued work, then stop.

Blocks until every pending future is resolved.


### submit()

```python
def submit(
    record: RecordT,
    estimated_cost: int | None,
) -> asyncio.Future[ResultT]
```
Submit a single record for batched processing.

Returns an `asyncio.Future` that resolves once the batch
containing this record has been processed.

Example::

    future = await batcher.submit(my_record, estimated_cost=128)
    result = await future


| Parameter | Type | Description |
|-|-|-|
| `record` | `RecordT` | The input record. |
| `estimated_cost` | `int \| None` | Optional explicit cost.  When omitted the batcher tries `cost_estimator`, then `record.estimate_cost()`, then `default_cost`. |

**Returns**

A future whose result is the corresponding entry from the list
returned by `process_fn`.


**Raises**

| Exception | Description |
|-|-|
| `RuntimeError` | If the batcher is not running. |

> [!NOTE]
> If the internal queue is full this coroutine awaits until space
> is available, providing natural backpressure to fast producers.

### submit_batch()

```python
def submit_batch(
    records: Sequence[RecordT],
    estimated_cost: Sequence[int] | None,
) -> list[asyncio.Future[ResultT]]
```
Convenience: submit multiple records and return their futures.



| Parameter | Type | Description |
|-|-|-|
| `records` | `Sequence[RecordT]` | Iterable of input records. |
| `estimated_cost` | `Sequence[int] \| None` | Optional per-record cost estimates.  Length must match *records* when provided. |

**Returns:** List of futures, one per record.

