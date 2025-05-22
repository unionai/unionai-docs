---
title: StructuredDataset
weight: 11
variants: +flyte +serverless +byoc +selfmanaged
---

# StructuredDataset

As with most type systems, Python has primitives, container types like maps and tuples, and support for user-defined structures. However, while there’s a rich variety of DataFrame classes (Pandas, Spark, Pandera, etc.), there’s no native Python type that represents a DataFrame in the abstract. This is the gap that the `StructuredDataset` type is meant to fill. It offers the following benefits:

- Eliminate boilerplate code you would otherwise need to write to serialize/deserialize from file objects into DataFrame instances,
- Eliminate additional inputs/outputs that convey metadata around the format of the tabular data held in those files,
- Add flexibility around how DataFrame files are loaded,
- Offer a range of DataFrame specific functionality - enforce compatibility of different schemas
  (not only at compile time, but also runtime since type information is carried along in the literal),
   store third-party schema definitions, and potentially in the future, render sample data, provide summary statistics, etc.

## Usage

To use the `StructuredDataset` type, import `pandas` and define a task that returns a Pandas Dataframe.
{{< key kit_name >}} will detect the Pandas DataFrame return signature and convert the interface for the task to
the `StructuredDataset` type.

## Example

This example demonstrates how to work with a structured dataset using {{< key product_name >}} entities.

> [!NOTE]
> To use the `StructuredDataset` type, you only need to import `pandas`. The other imports specified below are only necessary for this specific example.

{{< variant flyte >}}
{{< markdown >}}

<!-- TODO: Remove mention of Flytesnacks repos below -->

> [!NOTE]
> To clone and run the example code on this page, see the [Flytesnacks repo](https://github.com/flyteorg/flytesnacks/tree/master/examples/data_types_and_io/).

{{< /markdown >}}
{{< /variant >}}

To begin, import the dependencies for the example:

```python
import typing
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import {{< key kit_import >}}
from flytekit.models import literals
from flytekit.models.literals import StructuredDatasetMetadata
from flytekit.types.structured.structured_dataset import (
    PARQUET,
    StructuredDataset,
    StructuredDatasetDecoder,
    StructuredDatasetEncoder,
    StructuredDatasetTransformerEngine,
)
from typing_extensions import Annotated
```

Define a task that returns a Pandas DataFrame.

```python
@{{< key kit_as >}}.task(container_image=image_spec)
def generate_pandas_df(a: int) -> pd.DataFrame:
    return pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [a, 22], "Height": [160, 178]})
```

Using this simplest form, however, the user is not able to set the additional DataFrame information alluded to above,

- Column type information
- Serialized byte format
- Storage driver and location
- Additional third party schema information

This is by design as we wanted the default case to suffice for the majority of use-cases, and to require
as few changes to existing code as possible. Specifying these is simple, however, and relies on Python variable annotations,
which is designed explicitly to supplement types with arbitrary metadata.

## Column type information
If you want to extract a subset of actual columns of the DataFrame and specify their types for type validation,
you can just specify the column names and their types in the structured dataset type annotation.

First, initialize column types you want to extract from the `StructuredDataset`.

```python
all_cols = {{< key kit_as >}}.kwtypes(Name=str, Age=int, Height=int)
col = {{< key kit_as >}}.kwtypes(Age=int)
```

Define a task that opens a structured dataset by calling `all()`.
When you invoke `all()` with ``pandas.DataFrame``, the {{< key product_name >}} engine downloads the parquet file on S3, and deserializes it to `pandas.DataFrame`.
Keep in mind that you can invoke ``open()`` with any DataFrame type that's supported or added to structured dataset.
For instance, you can use ``pa.Table`` to convert the Pandas DataFrame to a PyArrow table.

```python
@{{< key kit_as >}}.task(container_image=image_spec)
def get_subset_pandas_df(df: Annotated[StructuredDataset, all_cols]) -> Annotated[StructuredDataset, col]:
    df = df.open(pd.DataFrame).all()
    df = pd.concat([df, pd.DataFrame([[30]], columns=["Age"])])
    return StructuredDataset(dataframe=df)


@{{< key kit_as >}}.workflow
def simple_sd_wf(a: int = 19) -> Annotated[StructuredDataset, col]:
    pandas_df = generate_pandas_df(a=a)
    return get_subset_pandas_df(df=pandas_df)
```

The code may result in runtime failures if the columns do not match.
The input ``df`` has ``Name``, ``Age`` and ``Height`` columns, whereas the output structured dataset will only have the ``Age`` column.

## Serialized byte format
You can use a custom serialization format to serialize your DataFrames.
Here's how you can register the Pandas to CSV handler, which is already available,
and enable the CSV serialization by annotating the structured dataset with the CSV format:

```python
from flytekit.types.structured import register_csv_handlers
from flytekit.types.structured.structured_dataset import CSV

register_csv_handlers()


@{{< key kit_as >}}.task(container_image=image_spec)
def pandas_to_csv(df: pd.DataFrame) -> Annotated[StructuredDataset, CSV]:
    return StructuredDataset(dataframe=df)


@{{< key kit_as >}}.workflow
def pandas_to_csv_wf() -> Annotated[StructuredDataset, CSV]:
    pandas_df = generate_pandas_df(a=19)
    return pandas_to_csv(df=pandas_df)
```

## Storage driver and location

By default, the data will be written to the same place that all other pointer-types (FlyteFile, FlyteDirectory, etc.) are written to.
This is controlled by the output data prefix option in {{< key product_name >}} which is configurable on multiple levels.

That is to say, in the simple default case, {{< key kit_name >}} will,

- Look up the default format for say, Pandas DataFrames,
- Look up the default storage location based on the raw output prefix setting,
- Use these two settings to select an encoder and invoke it.

So what's an encoder? To understand that, let's look into how the structured dataset plugin works.

## Inner workings of a structured dataset plugin

Two things need to happen with any DataFrame instance when interacting with {{< key product_name >}}:

- Serialization/deserialization from/to the Python instance to bytes (in the format specified above).
- Transmission/retrieval of those bits to/from somewhere.

Each structured dataset plugin (called encoder or decoder) needs to perform both of these steps.
{{< key kit_name >}} decides which of the loaded plugins to invoke based on three attributes:

- The byte format
- The storage location
- The Python type in the task or workflow signature.

These three keys uniquely identify which encoder (used when converting a DataFrame in Python memory to a {{< key product_name >}} value,
e.g. when a task finishes and returns a DataFrame) or decoder (used when hydrating a DataFrame in memory from a {{< key product_name >}} value,
e.g. when a task starts and has a DataFrame input) to invoke.

However, it is awkward to require users to use `typing.Annotated` on every signature.
Therefore, {{< key kit_name >}} has a default byte-format for every registered Python DataFrame type.

## The `uri` argument

BigQuery `uri` allows you to load and retrieve data from cloud using the `uri` argument.
The `uri` comprises of the bucket name and the filename prefixed with `gs://`.
If you specify BigQuery `uri` for structured dataset, BigQuery creates a table in the location specified by the `uri`.
The `uri` in structured dataset reads from or writes to S3, GCP, BigQuery or any storage.

Before writing DataFrame to a BigQuery table,

1. Create a [GCP account](https://cloud.google.com/docs/authentication/getting-started) and create a service account.
2. Create a project and add the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to your `.bashrc` file.
3. Create a dataset in your project.

Here's how you can define a task that converts a pandas DataFrame to a BigQuery table:

```python
@{{< key kit_as >}}.task
def pandas_to_bq() -> StructuredDataset:
    df = pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [20, 22]})
    return StructuredDataset(dataframe=df, uri="gs://<BUCKET_NAME>/<FILE_NAME>")
```

Replace `BUCKET_NAME` with the name of your GCS bucket and `FILE_NAME` with the name of the file the DataFrame should be copied to.

### Note that no format was specified in the structured dataset constructor, or in the signature. So how did the BigQuery encoder get invoked?
This is because the stock BigQuery encoder is loaded into {{< key kit_name >}} with an empty format.
The {{< key kit_name >}} `StructuredDatasetTransformerEngine` interprets that to mean that it is a generic encoder
(or decoder) and can work across formats, if a more specific format is not found.

And here's how you can define a task that converts the BigQuery table to a pandas DataFrame:

```python
@{{< key kit_as >}}.task
def bq_to_pandas(sd: StructuredDataset) -> pd.DataFrame:
   return sd.open(pd.DataFrame).all()
```

> [!NOTE]
> {{< key product_name >}} creates a table inside the dataset in the project upon BigQuery query execution.

## How to return multiple DataFrames from a task?
For instance, how would a task return say two DataFrames:
- The first DataFrame be written to BigQuery and serialized by one of their libraries,
- The second needs to be serialized to CSV and written at a specific location in GCS different from the generic pointer-data bucket

If you want the default behavior (which is itself configurable based on which plugins are loaded),
you can work just with your current raw DataFrame classes.

```python
@{{< key kit_as >}}.task
def t1() -> typing.Tuple[StructuredDataset, StructuredDataset]:
   ...
   return StructuredDataset(df1, uri="bq://project:flyte.table"), \
          StructuredDataset(df2, uri="gs://auxiliary-bucket/data")
```

If you want to customize the {{< key product_name >}} interaction behavior, you'll need to wrap your DataFrame in a `StructuredDataset` wrapper object.

## How to define a custom structured dataset plugin?

`StructuredDataset` ships with an encoder and a decoder that handles the conversion of a
Python value to a {{< key product_name >}} literal and vice-versa, respectively.
Here is a quick demo showcasing how one might build a NumPy encoder and decoder,
enabling the use of a 2D NumPy array as a valid type within structured datasets.

### NumPy encoder

Extend `StructuredDatasetEncoder` and implement the `encode` function.
The `encode` function converts NumPy array to an intermediate format (parquet file format in this case).

```python
class NumpyEncodingHandler(StructuredDatasetEncoder):
    def encode(
        self,
        ctx: {{< key kit_as >}}.FlyteContext,
        structured_dataset: StructuredDataset,
        structured_dataset_type: union.StructuredDatasetType,
    ) -> literals.StructuredDataset:
        df = typing.cast(np.ndarray, structured_dataset.dataframe)
        name = ["col" + str(i) for i in range(len(df))]
        table = pa.Table.from_arrays(df, name)
        path = ctx.file_access.get_random_remote_directory()
        local_dir = ctx.file_access.get_random_local_directory()
        local_path = Path(local_dir) / f"{0:05}"
        pq.write_table(table, str(local_path))
        ctx.file_access.upload_directory(local_dir, path)
        return literals.StructuredDataset(
            uri=path,
            metadata=StructuredDatasetMetadata(structured_dataset_type=union.StructuredDatasetType(format=PARQUET)),
        )
```

<!-- TODO: clean up code -->
### NumPy decoder

Extend `StructuredDatasetDecoder` and implement the `StructuredDatasetDecoder.decode` function.
The `StructuredDatasetDecoder.decode` function converts the parquet file to a `numpy.ndarray`.

```python
class NumpyDecodingHandler(StructuredDatasetDecoder):
    def decode(
        self,
        ctx: {{< key kit_as >}}.FlyteContext,
        flyte_value: literals.StructuredDataset,
        current_task_metadata: StructuredDatasetMetadata,
    ) -> np.ndarray:
        local_dir = ctx.file_access.get_random_local_directory()
        ctx.file_access.get_data(flyte_value.uri, local_dir, is_multipart=True)
        table = pq.read_table(local_dir)
        return table.to_pandas().to_numpy()
```

### NumPy renderer

Create a default renderer for numpy array, then {{< key kit_name >}} will use this renderer to
display schema of NumPy array on the Deck.

```python
class NumpyRenderer:
    def to_html(self, df: np.ndarray) -> str:
        assert isinstance(df, np.ndarray)
        name = ["col" + str(i) for i in range(len(df))]
        table = pa.Table.from_arrays(df, name)
        return pd.DataFrame(table.schema).to_html(index=False)
```

In the end, register the encoder, decoder and renderer with the `StructuredDatasetTransformerEngine`.
Specify the Python type you want to register this encoder with (`np.ndarray`),
the storage engine to register this against (if not specified, it is assumed to work for all the storage backends),
and the byte format, which in this case is `PARQUET`.

```python
StructuredDatasetTransformerEngine.register(NumpyEncodingHandler(np.ndarray, None, PARQUET))
StructuredDatasetTransformerEngine.register(NumpyDecodingHandler(np.ndarray, None, PARQUET))
StructuredDatasetTransformerEngine.register_renderer(np.ndarray, NumpyRenderer())
```

You can now use `numpy.ndarray` to deserialize the parquet file to NumPy and serialize a task's output (NumPy array) to a parquet file.

```python
@{{< key kit_as >}}.task(container_image=image_spec)
def generate_pd_df_with_str() -> pd.DataFrame:
    return pd.DataFrame({"Name": ["Tom", "Joseph"]})


@{{< key kit_as >}}.task(container_image=image_spec)
def to_numpy(sd: StructuredDataset) -> Annotated[StructuredDataset, None, PARQUET]:
    numpy_array = sd.open(np.ndarray).all()
    return StructuredDataset(dataframe=numpy_array)


@{{< key kit_as >}}.workflow
def numpy_wf() -> Annotated[StructuredDataset, None, PARQUET]:
    return to_numpy(sd=generate_pd_df_with_str())
```

> [!NOTE]
> `pyarrow` raises an `Expected bytes, got a 'int' object` error when the DataFrame contains integers.

You can run the code locally as follows:

```python
if __name__ == "__main__":
    sd = simple_sd_wf()
    print(f"A simple Pandas DataFrame workflow: {sd.open(pd.DataFrame).all()}")
    print(f"Using CSV as the serializer: {pandas_to_csv_wf().open(pd.DataFrame).all()}")
    print(f"NumPy encoder and decoder: {numpy_wf().open(np.ndarray).all()}")
```

### The nested typed columns

Like most storage formats (e.g. Avro, Parquet, and BigQuery), StructuredDataset support nested field structures.

{{< variant flyte >}}
{{< markdown >}}

> [!NOTE]
> Nested field StructuredDataset should be run when flytekit version > 1.11.0.

{{< /markdown >}}
{{< /variant >}}

```python
data = [
    {
        "company": "XYZ pvt ltd",
        "location": "London",
        "info": {"president": "Rakesh Kapoor", "contacts": {"email": "contact@xyz.com", "tel": "9876543210"}},
    },
    {
        "company": "ABC pvt ltd",
        "location": "USA",
        "info": {"president": "Kapoor Rakesh", "contacts": {"email": "contact@abc.com", "tel": "0123456789"}},
    },
]


@dataclass
class ContactsField:
    email: str
    tel: str


@dataclass
class InfoField:
    president: str
    contacts: ContactsField


@dataclass
class CompanyField:
    location: str
    info: InfoField
    company: str


MyArgDataset = Annotated[StructuredDataset, union.kwtypes(company=str)]
MyTopDataClassDataset = Annotated[StructuredDataset, CompanyField]
MyTopDictDataset = Annotated[StructuredDataset, {"company": str, "location": str}]

MyDictDataset = Annotated[StructuredDataset, union.kwtypes(info={"contacts": {"tel": str}})]
MyDictListDataset = Annotated[StructuredDataset, union.kwtypes(info={"contacts": {"tel": str, "email": str}})]
MySecondDataClassDataset = Annotated[StructuredDataset, union.kwtypes(info=InfoField)]
MyNestedDataClassDataset = Annotated[StructuredDataset, union.kwtypes(info=union.kwtypes(contacts=ContactsField))]

image = union.ImageSpec(packages=["pandas", "pyarrow", "pandas", "tabulate"], registry="ghcr.io/flyteorg")


@{{< key kit_as >}}.task(container_image=image)
def create_parquet_file() -> StructuredDataset:
    from tabulate import tabulate

    df = pd.json_normalize(data, max_level=0)
    print("original DataFrame: \n", tabulate(df, headers="keys", tablefmt="psql"))

    return StructuredDataset(dataframe=df)


@{{< key kit_as >}}.task(container_image=image)
def print_table_by_arg(sd: MyArgDataset) -> pd.DataFrame:
    from tabulate import tabulate

    t = sd.open(pd.DataFrame).all()
    print("MyArgDataset DataFrame: \n", tabulate(t, headers="keys", tablefmt="psql"))
    return t


@{{< key kit_as >}}.task(container_image=image)
def print_table_by_dict(sd: MyDictDataset) -> pd.DataFrame:
    from tabulate import tabulate

    t = sd.open(pd.DataFrame).all()
    print("MyDictDataset DataFrame: \n", tabulate(t, headers="keys", tablefmt="psql"))
    return t


@{{< key kit_as >}}.task(container_image=image)
def print_table_by_list_dict(sd: MyDictListDataset) -> pd.DataFrame:
    from tabulate import tabulate

    t = sd.open(pd.DataFrame).all()
    print("MyDictListDataset DataFrame: \n", tabulate(t, headers="keys", tablefmt="psql"))
    return t


@{{< key kit_as >}}.task(container_image=image)
def print_table_by_top_dataclass(sd: MyTopDataClassDataset) -> pd.DataFrame:
    from tabulate import tabulate

    t = sd.open(pd.DataFrame).all()
    print("MyTopDataClassDataset DataFrame: \n", tabulate(t, headers="keys", tablefmt="psql"))
    return t


@{{< key kit_as >}}.task(container_image=image)
def print_table_by_top_dict(sd: MyTopDictDataset) -> pd.DataFrame:
    from tabulate import tabulate

    t = sd.open(pd.DataFrame).all()
    print("MyTopDictDataset DataFrame: \n", tabulate(t, headers="keys", tablefmt="psql"))
    return t


@{{< key kit_as >}}.task(container_image=image)
def print_table_by_second_dataclass(sd: MySecondDataClassDataset) -> pd.DataFrame:
    from tabulate import tabulate

    t = sd.open(pd.DataFrame).all()
    print("MySecondDataClassDataset DataFrame: \n", tabulate(t, headers="keys", tablefmt="psql"))
    return t


@{{< key kit_as >}}.task(container_image=image)
def print_table_by_nested_dataclass(sd: MyNestedDataClassDataset) -> pd.DataFrame:
    from tabulate import tabulate

    t = sd.open(pd.DataFrame).all()
    print("MyNestedDataClassDataset DataFrame: \n", tabulate(t, headers="keys", tablefmt="psql"))
    return t


@{{< key kit_as >}}.workflow
def contacts_wf():
    sd = create_parquet_file()
    print_table_by_arg(sd=sd)
    print_table_by_dict(sd=sd)
    print_table_by_list_dict(sd=sd)
    print_table_by_top_dataclass(sd=sd)
    print_table_by_top_dict(sd=sd)
    print_table_by_second_dataclass(sd=sd)
    print_table_by_nested_dataclass(sd=sd)
```
