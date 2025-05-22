---
title: flytekit.utils.pbhash
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.utils.pbhash

## Directory

### Methods

| Method | Description |
|-|-|
| [`compute_hash()`](#compute_hash) | Computes a deterministic hash in bytes for the Protobuf object. |
| [`compute_hash_string()`](#compute_hash_string) | Computes a deterministic hash in base64 encoded string for the Protobuf object. |


## Methods

#### compute_hash()

```python
def compute_hash(
    pb: google.protobuf.message.Message,
) -> bytes
```
Computes a deterministic hash in bytes for the Protobuf object.


| Parameter | Type |
|-|-|
| `pb` | `google.protobuf.message.Message` |

#### compute_hash_string()

```python
def compute_hash_string(
    pb: google.protobuf.message.Message,
) -> str
```
Computes a deterministic hash in base64 encoded string for the Protobuf object


| Parameter | Type |
|-|-|
| `pb` | `google.protobuf.message.Message` |

