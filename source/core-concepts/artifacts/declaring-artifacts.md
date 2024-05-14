# Declaring artifacts

In order to define a task or workflow that emits an artifact, you must first declare the artifact and the keys for any [partitions](index.md#partitions) you wish for it to have. For the `Artifact` class parameters and methods, see the [Flytekit Artifact documentation](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.Artifact.html).

## Basic artifact

In the following example, an artifact called `BasicTaskData` is declared, along with a task that emits that artifact. Since it is a basic artifact, it doesn't have any partitions:

```{literalinclude} ../../_static/includes/artifacts/basic.py
:language: python
```

## Time-partitioned artifact

By default, time partitioning is not enabled for artifacts. To enable it, declare the artifact with `time_partitioned` set to `True`. You can optionally set the granularity for the time partition to `MINUTE`, `HOUR`, `DAY`, or `MONTH`; the default is `DAY`.

You must also pass a value to `time_partition`, which you can do at runtime or by binding `time_partition` to an input.

### Passing a value to `time_partition` at runtime

```{literalinclude} ../../_static/includes/artifacts/time_partition_runtime.py
:language: python
:emphasize-lines: 1,5,10-11,17-19
```

### Passing a value to `time_partition` by input

```{literalinclude} ../../_static/includes/artifacts/time_partition_input.py
:language: python
:emphasize-lines: 16-17,24
```

## Artifact with custom partition keys

You can specify up to 10 custom partition keys when declaring an artifact. Custom partition keys can be set at runtime or be passed as inputs.

### Passing a value to a custom partition key at runtime

```{literalinclude} ../../_static/includes/artifacts/partition_keys_runtime.py
:language: python
:emphasize-lines: 13,32-33
```

### Passing a value to a custom partition key by input

```{literalinclude} ../../_static/includes/artifacts/partition_keys_input.py
:language: python
:emphasize-lines: 13,31
```

## Artifact with model card example

You can attach a model card with additional metadata to your artifact, formatted in Markdown:

```{literalinclude} ../../_static/includes/artifacts/model_card.py
:language: python
:emphasize-lines: 4,10-13,22
```
