---
title: ResourceMeta
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ResourceMeta

**Package:** `flytekit.extend.backend.base_connector`

This is the metadata for the job. For example, the id of the job.


```python
def ResourceMeta()
```
## Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | Decode the resource meta from bytes. |
| [`encode()`](#encode) | Encode the resource meta to bytes. |


### decode()

```python
def decode(
    data: bytes,
) -> ResourceMeta
```
Decode the resource meta from bytes.


| Parameter | Type | Description |
|-|-|-|
| `data` | `bytes` | |

### encode()

```python
def encode()
```
Encode the resource meta to bytes.


