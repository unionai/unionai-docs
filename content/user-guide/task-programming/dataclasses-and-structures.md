---
title: Data classes and structures
weight: 2
variants: +flyte +union
---

# Data classes and structures

Dataclasses and Pydantic models are fully supported in Flyte as **materialized data types**:
Structured data where the full content is serialized and passed between tasks.
Use these as you would normally, passing them as inputs and outputs of tasks.

Unlike **offloaded types** like [`DataFrame`s](./dataframes), [`File`s and `Dir`s](./files-and-directories), data class and Pydantic model data is fully serialized, stored, and deserialized between tasks.
This makes them ideal for configuration objects, metadata, and smaller structured data where all fields should be serializable.

> [!TIP]
> For third-party types that don't have built-in Flyte support (e.g. `geopandas.GeoDataFrame`),
> you can make them work inside dataclasses by implementing mashumaro's
> [`SerializableType`](https://github.com/Fatal1ty/mashumaro?tab=readme-ov-file#serializabletype-interface)
> interface (`_serialize` / `_deserialize`). This tells mashumaro's `MessagePackEncoder` how to
> convert your type to and from a msgpack-friendly representation.
> See the [geopandas in dataclass example](https://github.com/unionai/flyte-sdk/tree/main/examples/type_transformers/test_geopandas_in_dataclass.py) for a working pattern.

## Example: Combining Dataclasses and Pydantic Models

This example demonstrates how data classes and Pydantic models work together as materialized data types, showing nested structures and batch processing patterns:

{{< code file="/unionai-examples/v2/user-guide/task-programming/dataclasses-and-structures/example.py" lang="python" >}}

