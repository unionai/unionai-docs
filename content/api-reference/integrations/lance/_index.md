---
title: Lance
icon: book
version: 2.11.0
variants: +flyte +union
layout: py_api
---

# Lance



## Directory

### Methods

| Method | Description |
|-|-|
| [`register_lance_df_transformers()`](#register_lance_df_transformers) | Register Lance DataFrame encoders and decoders with the DataFrameTransformerEngine. |


## Methods

#### register_lance_df_transformers()

```python
def register_lance_df_transformers()
```
Register Lance DataFrame encoders and decoders with the DataFrameTransformerEngine.

This function is called automatically via the flyte.plugins.types entry point
when flyte.init() is called with load_plugin_type_transformers=True (the default).


