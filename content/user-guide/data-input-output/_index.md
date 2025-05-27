---
title: Data input/output
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Data input/output

<!-- TODO: Double check this seciton for variant acccuracy -->
{{< variant flyte >}}
{{< markdown >}}

{{< key product_name >}} being a data-aware orchestration platform, types play a vital role within it.
This section provides an introduction to the wide range of data types that {{< key product_name >}} supports.
These types serve a dual-purpose by not only validating the data but also enabling seamless
transfer of data between local and cloud storage.
They enable:

- Data lineage
- Memoization
- Auto parallelization
- Simplifying access to data
- Auto generated CLI and launch UI

For a more comprehensive understanding of how Flyte manages data, refer to [Understand How Flyte Handles Data](https://docs.flyte.org/en/latest/user_guide/concepts/main_concepts/data_management.html#divedeep-data-management).

## Mapping Python to Flyte types

{{< key kit_name >}} automatically translates most Python types into Flyte types.
Here's a breakdown of these mappings:

| Python Type | Flyte Type | Conversion | Comment |
|-------------|------------|------------|---------|
| `int` | `Integer` | Automatic | Use Python 3 type hints. |
| `float` | `Float` | Automatic | Use Python 3 type hints. |
| `str` | `String` | Automatic | Use Python 3 type hints. |
| `bool` | `Boolean` | Automatic | Use Python 3 type hints. |
| `bytes`/`bytearray` | `Binary` | Not Supported | You have the option to employ your own custom typetransformer. |
| `complex` | NA | Not Supported | You have the option to employ your own custom type transformer. |
| `datetime.timedelta` | `Duration` | Automatic | Use Python 3 type hints. |
| `datetime.datetime` | `Datetime` | Automatic | Use Python 3 type hints. |
| `datetime.date` | `Datetime` | Automatic | Use Python 3 type hints. |
| `typing.List[T]` / `list[T]` | `Collection [T]` | Automatic | Use `typing.List[T]` or `list[T]`, where `T` canrepresent one of the other supported types listed in the table. |
| `typing.Iterator[T]` | `Collection [T]` | Automatic | Use `typing.Iterator[T]`, where `T` can represent one of the other supported types listed in the table. |
| File / file-like / `os.PathLike` | `FlyteFile` | Automatic | If you're using `file` or `os.PathLike` objects,Flyte will default to the binary protocol for the file. When using `FlyteFile["protocol"]`, it is assumedthat the file is in the specified protocol, such as 'jpg', 'png', 'hdf5', etc. |
| Directory | `FlyteDirectory` | Automatic | When using `FlyteDirectory["protocol"]`, it is assumed that all thefiles belong to the specified protocol. |
| `typing.Dict[str, V]` / `dict[str, V]` | `Map[str, V]` | Automatic | Use `typing.Dict[str, V]` or `dict[str, V`, where `V` can be one of the other supported types in the table, including a nested dictionary. |
| `dict` | JSON (`struct.pb`) | Automatic | Use `dict`. It's assumed that the untyped dictionary can beconverted to JSON. However, this may not always be possible and could result in a `RuntimeError`. |
| `@dataclass` | `Struct` | Automatic | The class should be a pure value class annotated with the `@dataclass`decorator. |
| `np.ndarray` | File | Automatic | Use `np.ndarray` as a type hint. |
| `pandas.DataFrame` | Structured Dataset | Automatic | Use `pandas.DataFrame` as a type hint. Pandas columntypes aren't preserved. |
| `polars.DataFrame` | Structured Dataset | Automatic | Use `polars.DataFrame` as a type hint. Polars columntypes aren't preserved. |
| `polars.LazyFrame` | Structured Dataset | Automatic | Use `polars.LazyFrame` as a type hint. Polars columntypes aren't preserved. |
| `pyspark.DataFrame` | Structured Dataset | To utilize the type, install the `flytekitplugins-spark` plugin. |Use `pyspark.DataFrame` as a type hint. |
| `pydantic.BaseModel` | `Map` | To utilize the type, install the `pydantic` module. | Use `pydantic.BaseModel`as a type hint. |
| `torch.Tensor` / `torch.nn.Module` | File | To utilize the type, install the `torch` library. | Use `torchTensor` or `torch.nn.Module` as a type hint, and you can use their derived types. |
| `tf.keras.Model` | File | To utilize the type, install the `tensorflow` library. | Use `tf.keras.Model` andits derived types. |
| `sklearn.base.BaseEstimator` | File | To utilize the type, install the `scikit-learn` library. | Use `sklearnbase.BaseEstimator` and its derived types. |
| User defined types | Any | Custom transformers | The `FlytePickle` transformer is the default option, but youcan also define custom transformers. For instructions on building custom type transformers, please refer to [this section](../../architecture/extending-flyte/custom-types). |

{{< /markdown >}}
{{< /variant >}}
{{< variant serverless >}}
{{< markdown >}}

This section covers how to manage data input and output in {{< key product_name >}}.
{{< key product_name >}} also supports all the [Data input/output features of Flyte](https://docs-builder.pages.dev/docs/flyte/user-guide/data-input-output/).


| Section | Description |
|----------------------------------------------------|----------------------------------------------------|
| [`FlyteFile`](./flyte-file-and-flyte-directory) | Use `FlyteFile` to easily pass files across tasks. |
| [`FlyteDirectory`](./flyte-file-and-flyte-directory) | Use `FlyteDirectory` to easily pass directories across tasks. |
| [`Downloading with FlyteFile and FlyteDirectory`](./downloading-with-ff-and-fd) | Details on how files and directories or downloaded with `FlyteFile` and `FlyteDirectory`. |
| [`StructuredDataset`](./structured-dataset) | Details on how `StructuredDataset`is used as a general dataframe type. |
| [`Dataclass`](./dataclass) | Details on how to uses dataclasses across tasks. |
| [`Pydantic BaseModel`](./pydantic) | Details on how to use pydantic models across tasks. |
| [`Accessing Attributes`](./accessing-attributes) | Details on how to directly access attributes on output promises for lists, dictionaries, dataclasses, and more. |
| [`Enums`](./enum) | Details on how use Enums across tasks. |
| [`Pickle`](./pickle) | Details on how use pickled objects across tasks for generalized typing of complex objects. |
| [`Pytorch`](./pytorch) | Details on how use torch tensors and models across tasks. |
| [`Tensorflow`](./tensorflow) | Details on how use tensorflow tensors and models across tasks. |

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged >}}
{{< markdown >}}

This section covers how to manage data input and output in {{< key product_name >}}.
{{< key product_name >}} also supports all the [Data input/output features of Flyte](https://docs-builder.pages.dev/docs/flyte/user-guide/data-input-output/).

| Section | Description |
|---------------------------------------------------|----------------------------------------------------|
| [`FlyteFile`](./flyte-file-and-flyte-directory) | Use `FlyteFile` to easily pass files across tasks. |
| [`FlyteDirectory`](./flyte-file-and-flyte-directory) | Use `FlyteDirectory` to easily pass directories across tasks. |
| [`Downloading with FlyteFile and FlyteDirectory`](./downloading-with-ff-and-fd) | Details on how files and directories or downloaded with `FlyteFile`. |
| [`StructuredDataset`](./structured-dataset) | Details on how `StructuredDataset`is used as a general dataframe type. |
| [`Dataclass`](./dataclass) | Details on how to uses dataclasses across tasks. |
| [`Pydantic BaseModel`](./pydantic) | Details on how to use pydantic models across tasks. |
| [`Accessing Attributes`](./accessing-attributes) | Details on how to directly access attributes on output promises for |
| [`Enums`](./enum) | Details on how use Enums across tasks. |
| [`Pickle`](./pickle) | Details on how use pickled objects across tasks for generalized typ |
| [`Pytorch`](./pytorch) | Details on how use torch tensors and models across tasks. |
| [`Tensorflow`](./tensorflow) | Details on how use tensorflow tensors and models across tasks. |
| [`Accelerated datasets`](./accelerated-datasets) | Upload your data once and access it from any task. |

{{< /markdown >}}
{{< /variant >}}
