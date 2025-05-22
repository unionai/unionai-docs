---
title: flytekit.interfaces.random
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interfaces.random

## Directory

### Methods

| Method | Description |
|-|-|
| [`seed_flyte_random()`](#seed_flyte_random) | If one wants to influence the pseudo-random behavior of flytekit, this function can be used to seed the flytekit. |


## Methods

#### seed_flyte_random()

```python
def seed_flyte_random(
    seed,
)
```
If one wants to influence the pseudo-random behavior of flytekit, this function can be used to seed the flytekit
generator. It is not recommended that this be done as lack of entropy between jobs can result in overwriting data
created at random locations.

Currently, this is used by flytekit to create entropy in low entropy situations (such as Array Jobs) where the job
index can be used as a seed to ensure sibling jobs do not have random collisions.


| Parameter | Type |
|-|-|
| `seed` |  |

