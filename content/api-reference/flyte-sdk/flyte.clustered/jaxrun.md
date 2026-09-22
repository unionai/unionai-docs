---
title: JaxRun
description: "JAX multi-process runtime for a ClusteredTaskEnvironment."
icon: braces
version: 2.10.0
variants: +flyte +union
layout: py_api
---

# JaxRun

**Package:** `flyte.clustered`

JAX multi-process runtime for a ClusteredTaskEnvironment.

Each pod runs exactly one Python process (`nproc_per_node` must be 1) that owns every local
accelerator — JAX's recommended multi-host layout. The pod-0 process hosts the `jax.distributed`
coordinator on `MASTER_ADDR:MASTER_PORT`; every process must call `flyte.clustered.jax_initialize`
before any JAX computation. No launcher binary is involved: the `clustered` entrypoint exports the
process topology and execs `a0` directly.


## Parameters

```python
def JaxRun()
```
