---
title: ResourceMeta
version: 2.0.0b50
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ResourceMeta

**Package:** `flyte.connectors`

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


