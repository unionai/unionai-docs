---
title: TokenBatcher
version: 2.0.11
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# TokenBatcher

**Package:** `flyte.extras`

Token-aware batcher for LLM inference workloads.

A thin convenience wrapper around `DynamicBatcher` that accepts
token-specific parameter names (`inference_fn`, `token_estimator`,
`target_batch_tokens`, etc.) and maps them to the base class.

Also checks the `TokenEstimator` protocol (`estimate_tokens()`)
in addition to `CostEstimator` (`estimate_cost()`).



## Parameters

```python
class TokenBatcher(
    inference_fn: ProcessFn[RecordT, ResultT] | None,
    process_fn: ProcessFn[RecordT, ResultT] | None,
    token_estimator: CostEstimatorFn[RecordT] | None,
    cost_estimator: CostEstimatorFn[RecordT] | None,
    target_batch_tokens: int | None,
    target_batch_cost: int,
    default_token_estimate: int | None,
    default_cost: int,
    max_batch_size: int,
    min_batch_size: int,
    batch_timeout_s: float,
    max_queue_size: int,
    prefetch_batches: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `inference_fn` | `ProcessFn[RecordT, ResultT] \| None` | |
| `process_fn` | `ProcessFn[RecordT, ResultT] \| None` | |
| `token_estimator` | `CostEstimatorFn[RecordT] \| None` | |
| `cost_estimator` | `CostEstimatorFn[RecordT] \| None` | |
| `target_batch_tokens` | `int \| None` | |
| `target_batch_cost` | `int` | |
| `default_token_estimate` | `int \| None` | |
| `default_cost` | `int` | |
| `max_batch_size` | `int` | |
| `min_batch_size` | `int` | |
| `batch_timeout_s` | `float` | |
| `max_queue_size` | `int` | |
| `prefetch_batches` | `int` | |

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
| [`submit()`](#submit) | Submit a single record for batched inference. |
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
    estimated_tokens: int | None,
    estimated_cost: int | None,
) -> asyncio.Future[ResultT]
```
Submit a single record for batched inference.

Accepts either `estimated_tokens` or `estimated_cost`.



| Parameter | Type | Description |
|-|-|-|
| `record` | `RecordT` | The input record. |
| `estimated_tokens` | `int \| None` | Optional explicit token count. |
| `estimated_cost` | `int \| None` | Optional explicit cost (base class parameter). |

**Returns**

A future whose result is the corresponding entry from the list
returned by the inference function.

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

