---
title: CostEstimator
version: 2.2.0
variants: +flyte +union
layout: py_api
---

# CostEstimator

**Package:** `flyte.extras`

Protocol for records that can estimate their own processing cost.

Implement this on your record type and the batcher will call it
automatically when no explicit `estimated_cost` is passed to
`DynamicBatcher.submit`.



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
