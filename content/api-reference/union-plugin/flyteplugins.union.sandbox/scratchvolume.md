---
title: ScratchVolume
description: "A session's disk that stays on the node and ends with the session: ``env.session(name, volume=ScratchVolume())``."
icon: braces
version: 0.26.2
variants: -flyte +union
layout: py_api
---

# ScratchVolume

**Package:** `flyteplugins.union.sandbox`

A session's disk that stays on the node and ends with the session:
``env.session(name, volume=ScratchVolume())``. Its session can't be committed
or forked. Sessions get a new SandboxVolume by default.


## Parameters

```python
def ScratchVolume()
```
