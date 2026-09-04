---
title: ProviderFactory
description: "What a plugin's exported provider class must look like."
icon: diagram-3
version: 2.7.0
variants: +flyte +union
layout: py_api
---

# ProviderFactory

**Package:** `flyte.extras.webhooks.testing`

What a plugin's exported provider class must look like.

Constructible with no arguments — the defaults are pre-wired — and
accepting `secret_env` for anyone storing the secret under another name.


```python
protocol ProviderFactory()
```
