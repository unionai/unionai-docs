# Declaring artifacts

In order to define a task or workflow that emits an artifact, you must first declare the artifact and the keys for any [partitions](./index.md#partitions) you wish for it to have. For the `Artifact` class parameters and methods, see the [Flytekit Artifact documentation](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.Artifact.html).

## Basic artifact

In the following example, an artifact called `BasicTaskData` is declared, along with a task that emits that artifact. Since it is a basic artifact, it doesn't have any partitions.

{@@ if byoc or byok or flyte @@}

:::{note}
To use the example code on this page, you will need to add your `registry` to the `pandas_image` ImageSpec block.
:::

{@@ endif @@}

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/artifacts/basic.py
:caption: basic.py
:language: python
```

## Time-partitioned artifact

By default, time partitioning is not enabled for artifacts. To enable it, declare the artifact with `time_partitioned` set to `True`. You can optionally set the granularity for the time partition to `MINUTE`, `HOUR`, `DAY`, or `MONTH`; the default is `DAY`.

You must also pass a value to `time_partition`, which you can do at runtime or by binding `time_partition` to an input.

### Passing a value to `time_partition` at runtime

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/artifacts/time_partition_runtime.py
:caption: time_partition_runtime.py
:language: python
:emphasize-lines: 1,5,14-15,21-23
```

### Passing a value to `time_partition` by input

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/artifacts/time_partition_input.py
:caption: time_partition_input.py
:language: python
:emphasize-lines: 20-21,28
```

## Artifact with custom partition keys

You can specify up to 10 custom partition keys when declaring an artifact. Custom partition keys can be set at runtime or be passed as inputs.

### Passing a value to a custom partition key at runtime

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/artifacts/partition_keys_runtime.py
:caption: partition_keys_runtime.py
:language: python
:emphasize-lines: 16,35-36
```

### Passing a value to a custom partition key by input

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/artifacts/partition_keys_input.py
:caption: partition_keys_input.py
:language: python
:emphasize-lines: 16,34
```

## Artifact with model card example

You can attach a model card with additional metadata to your artifact, formatted in Markdown:

```{rli} https://raw.githubusercontent.com/unionai/unionai-examples/main/user_guide/core_concepts/artifacts/model_card.py
:caption: model_card.py
:language: python
:emphasize-lines: 4,14-17,26
```
