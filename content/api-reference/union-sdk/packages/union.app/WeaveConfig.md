---
title: WeaveConfig
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# WeaveConfig

**Package:** `union.app`

```python
class WeaveConfig(
    project: str,
    entity: str,
    api_host: str,
    host: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | |
| `entity` | `str` | |
| `api_host` | `str` | |
| `host` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`before_to_union_idl()`](#before_to_union_idl) | Modify app in place at the beginning of `App. |


### before_to_union_idl()

```python
def before_to_union_idl(
    app: App,
    settings: union.app._models.AppSerializationSettings,
)
```
Modify app in place at the beginning of `App._to_union_idl`.


| Parameter | Type | Description |
|-|-|-|
| `app` | `App` | |
| `settings` | `union.app._models.AppSerializationSettings` | |

