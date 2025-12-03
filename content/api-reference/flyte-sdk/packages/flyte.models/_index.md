---
title: flyte.models
version: 2.0.0b34
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.models

## Directory

### Classes

| Class | Description |
|-|-|
| [`ActionID`](../flyte.models/actionid) | A class representing the ID of an Action, nested within a Run. |
| [`Checkpoints`](../flyte.models/checkpoints) | A class representing the checkpoints for a task. |
| [`CodeBundle`](../flyte.models/codebundle) | A class representing a code bundle for a task. |
| [`GroupData`](../flyte.models/groupdata) |  |
| [`NativeInterface`](../flyte.models/nativeinterface) | A class representing the native interface for a task. |
| [`PathRewrite`](../flyte.models/pathrewrite) | Configuration for rewriting paths during input loading. |
| [`RawDataPath`](../flyte.models/rawdatapath) | A class representing the raw data path for a task. |
| [`SerializationContext`](../flyte.models/serializationcontext) | This object holds serialization time contextual information, that can be used when serializing the task and. |
| [`TaskContext`](../flyte.models/taskcontext) | A context class to hold the current task executions context. |

### Methods

| Method | Description |
|-|-|
| [`generate_random_name()`](#generate_random_name) | Generate a random name for the task. |


### Variables

| Property | Type | Description |
|-|-|-|
| `MAX_INLINE_IO_BYTES` | `int` |  |
| `TYPE_CHECKING` | `bool` |  |

## Methods

#### generate_random_name()

```python
def generate_random_name()
```
Generate a random name for the task. This is used to create unique names for tasks.
TODO we can use unique-namer in the future, for now its just guids


