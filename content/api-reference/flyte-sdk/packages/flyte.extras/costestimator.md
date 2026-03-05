---
title: CostEstimator
version: 2.0.3
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# CostEstimator

**Package:** `flyte.extras`

Protocol for records that can estimate their own processing cost.

Implement this on your record type and the batcher will call it
automatically when no explicit ``estimated_cost`` is passed to
:meth:`DynamicBatcher.submit`.

Example::

    @dataclass
    class ApiRequest:
        payload: str

        def estimate_cost(self) -&gt; int:
            return len(self.payload)



```python
protocol CostEstimator()
```
## Methods

| Method | Description |
|-|-|
| [`estimate_cost()`](#estimate_cost) |  |


### estimate_cost()

```python
def estimate_cost()
```
