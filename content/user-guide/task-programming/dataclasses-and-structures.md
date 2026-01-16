---
title: Data classes and structures
weight: 70
variants: +flyte +serverless +byoc +selfmanaged
---

# Data classes and structures

Dataclasses and Pydantic models are fully supported in Flyte as **materialized data types**:
Structured data where the full content is serialized and passed between tasks.
Use these as you would normally, passing them as inputs and outputs of tasks.

Unlike **offloaded types** like [`DataFrame`s](./dataframes), [`File`s and `Dir`s](./files-and-directories), data class and Pydantic model data is fully serialized, stored, and deserialized between tasks.
This makes them ideal for configuration objects, metadata, and smaller structured data where all fields should be serializable.

## Example: Combining Dataclasses and Pydantic Models

This example demonstrates how data classes and Pydantic models work together as materialized data types, showing nested structures and batch processing patterns:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/dataclasses-and-structures/example.py" lang="python" >}}

