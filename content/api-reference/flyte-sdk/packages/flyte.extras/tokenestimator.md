---
title: TokenEstimator
version: 2.0.11
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# TokenEstimator

**Package:** `flyte.extras`

Protocol for records that can estimate their own token count.

Implement this on your record type and the `TokenBatcher` will
call it automatically when no explicit `estimated_tokens` is passed
to `TokenBatcher.submit`.



```python
protocol TokenEstimator()
```
## Methods

| Method | Description |
|-|-|
| [`estimate_tokens()`](#estimate_tokens) |  |


### estimate_tokens()

```python
def estimate_tokens()
```
