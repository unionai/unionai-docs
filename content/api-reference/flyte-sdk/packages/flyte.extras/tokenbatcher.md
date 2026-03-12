---
title: TokenBatcher
version: 2.0.6
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# TokenBatcher

**Package:** `flyte.extras`

Token-aware batcher for LLM inference workloads.

A thin convenience wrapper around :class:`DynamicBatcher` that accepts
token-specific parameter names (``inference_fn``, ``token_estimator``,
``target_batch_tokens``, etc.) and maps them to the base class.

Also checks the :class:`TokenEstimator` protocol (``estimate_tokens()``)
in addition to :class:`CostEstimator` (``estimate_cost()``).

Example::

    async def inference(batch: list[Prompt]) -&gt; list[str]:
        ...

    async with TokenBatcher(inference_fn=inference) as batcher:
        future = await batcher.submit(Prompt(text="Hello"))
        result = await future



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

## Methods

| Method | Description |
|-|-|
| [`submit()`](#submit) | Submit a single record for batched inference. |


### submit()

```python
def submit(
    record: RecordT,
    estimated_tokens: int | None,
    estimated_cost: int | None,
) -> asyncio.Future[ResultT]
```
Submit a single record for batched inference.

Accepts either ``estimated_tokens`` or ``estimated_cost``.



| Parameter | Type | Description |
|-|-|-|
| `record` | `RecordT` | The input record. |
| `estimated_tokens` | `int \| None` | Optional explicit token count. |
| `estimated_cost` | `int \| None` | Optional explicit cost (base class parameter). |

