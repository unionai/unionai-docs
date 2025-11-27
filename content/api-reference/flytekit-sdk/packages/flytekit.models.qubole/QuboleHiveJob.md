---
title: QuboleHiveJob
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# QuboleHiveJob

**Package:** `flytekit.models.qubole`

```python
class QuboleHiveJob(
    query,
    cluster_label,
    tags,
    query_collection,
)
```
Initializes a HiveJob.



| Parameter | Type | Description |
|-|-|-|
| `query` |  | |
| `cluster_label` |  | |
| `tags` |  | |
| `query_collection` |  | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: _qubole. |


### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: _qubole.QuboleHiveJob


## Properties

| Property | Type | Description |
|-|-|-|
| `cluster_label` |  | {{< multiline >}}The cluster label where the query should be executed
:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `query` |  | {{< multiline >}}The query to be executed
:rtype: HiveQuery
{{< /multiline >}} |
| `query_collection` |  | {{< multiline >}}The queries to be executed
:rtype: HiveQueryCollection
{{< /multiline >}} |
| `tags` |  | {{< multiline >}}User tags for the queries
:rtype: list[Text]
{{< /multiline >}} |

