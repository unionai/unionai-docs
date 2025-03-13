---
title: Pydantic BaseModel
weight: 10
variants: +flyte +serverless +byoc +byok
---

# Pydantic BaseModel

{{< if-variant flyte >}}
`flytekit` version >=1.14 supports natively the `JSON` format that Pydantic `BaseModel` produces,  enhancing the
interoperability of Pydantic BaseModels with the Flyte type system.

{{< note >}}
Pydantic BaseModel V2 only works when you are using flytekit version >= v1.14.0.
{{< /note >}}

With the 1.14 release, `flytekit` adopted `MessagePack` as the serialization format for Pydantic `BaseModel`,
overcoming a major limitation of serialization into a JSON string within a Protobuf `struct` datatype like the previous versions do:

to store `int` types, Protobuf's `struct` converts them to `float`, forcing users to write boilerplate code to work around this issue.

{{< note >}}
By default, `flytekit >= 1.14` will produce `msgpack` bytes literals when serializing, preserving the types defined in your `BaseModel` class.
If you're serializing `BaseModel` using `flytekit` version >= v1.14.0 and you want to produce Protobuf `struct` literal instead, you can set environment variable `FLYTE_USE_OLD_DC_FORMAT` to `true`.

For more details, you can refer the MESSAGEPACK IDL RFC: [https://github.com/flyteorg/flyte/blob/master/rfc/system/5741-binary-idl-with-message-pack.md](https://github.com/flyteorg/flyte/blob/master/rfc/system/5741-binary-idl-with-message-pack.md)
{{< /note >}}

{{< note >}}
To clone and run the example code on this page, see the [Flytesnacks repo](https://github.com/flyteorg/flytesnacks/tree/master/examples/data_types_and_io/).
{{< /note >}}

{{< note >}}
You can put Dataclass and FlyteTypes (FlyteFile, FlyteDirectory, FlyteSchema, and StructuredDataset) in a pydantic BaseModel.
{{< /note >}}

{{< /if-variant >}}
{{< if-variant byoc byok serverless >}}

{{< note >}}
You can put Dataclass and UnionTypes (FlyteFile, FlyteDirectory, FlyteSchema, and StructuredDataset) in a pydantic BaseModel.
{{< /note >}}

{{< /if-variant >}}

To begin, import the necessary dependencies:

```python
import os
import tempfile
import pandas as pd
from union
from flytekit.types.structured import StructuredDataset
from pydantic import BaseModel
```

Build your custom image with ImageSpec:
```python
image_spec = union.ImageSpec(
    registry="ghcr.io/flyteorg",
    packages=["pandas", "pyarrow", "pydantic"],
)
```

## Python types
We define a `pydantic basemodel` with `int`, `str` and `dict` as the data types.

```python
class Datum(BaseModel):
    x: int
    y: str
    z: dict[int, str]
```

You can send a `pydantic basemodel` between different tasks written in various languages, and input it through the {@= Product =@} console as raw JSON.

{{< note >}}
All variables in a data class should be **annotated with their type**. Failure to do will result in an error.
{{< /note >}}

Once declared, a dataclass can be returned as an output or accepted as an input.

```python
@union.task(container_image=image_spec)
def stringify(s: int) -> Datum:
    """
    A Pydantic model return will be treated as a single complex JSON return.
    """
    return Datum(x=s, y=str(s), z={s: str(s)})


@union.task(container_image=image_spec)
def add(x: Datum, y: Datum) -> Datum:
    x.z.update(y.z)
    return Datum(x=x.x + y.x, y=x.y + y.y, z=x.z)
```

## {@= Product =@} types
We also define a data class that accepts `StructuredDataset`, `FlyteFile` and `FlyteDirectory`.

{{< if-variant byoc byok serverless >}}

```python
class FlyteTypes(BaseModel):
    dataframe: StructuredDataset
    file: union.FlyteFile
    directory: union.FlyteDirectory


@union.task(container_image=image_spec)
def upload_data() -> FlyteTypes:
    df = pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [20, 22]})

    temp_dir = tempfile.mkdtemp(prefix="flyte-")
    df.to_parquet(os.path.join(temp_dir, "df.parquet"))

    file_path = tempfile.NamedTemporaryFile(delete=False)
    file_path.write(b"Hello, World!")
    file_path.close()

    fs = FlyteTypes(
        dataframe=StructuredDataset(dataframe=df),
        file=union.FlyteFile(file_path.name),
        directory=union.FlyteDirectory(temp_dir),
    )
    return fs


@union.task(container_image=image_spec)
def download_data(res: FlyteTypes):
    expected_df = pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [20, 22]})
    actual_df = res.dataframe.open(pd.DataFrame).all()
    assert expected_df.equals(actual_df), "DataFrames do not match!"

    with open(res.file, "r") as f:
        assert f.read() == "Hello, World!", "File contents do not match!"

    assert os.listdir(res.directory) == ["df.parquet"], "Directory contents do not match!"
```

A data class supports the usage of data associated with Python types, data classes,
FlyteFile, FlyteDirectory and StructuredDataset.

We define a workflow that calls the tasks created above.

```python
@union.workflow
def basemodel_wf(x: int, y: int) -> (Datum, FlyteTypes):
    o1 = add(x=stringify(s=x), y=stringify(s=y))
    o2 = upload_data()
    download_data(res=o2)
    return o1, o2
```

{{< /if-variant >}}
{{< if-variant byoc byok serverless >}}

```python
class UnionTypes(BaseModel):
    dataframe: StructuredDataset
    file: union.FlyteFile
    directory: union.FlyteDirectory


@union.task(container_image=image_spec)
def upload_data() -> UnionTypes:
    df = pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [20, 22]})

    temp_dir = tempfile.mkdtemp(prefix="union-")
    df.to_parquet(os.path.join(temp_dir, "df.parquet"))

    file_path = tempfile.NamedTemporaryFile(delete=False)
    file_path.write(b"Hello, World!")
    file_path.close()

    fs = FlyteTypes(
        dataframe=StructuredDataset(dataframe=df),
        file=union.FlyteFile(file_path.name),
        directory=union.FlyteDirectory(temp_dir),
    )
    return fs


@union.task(container_image=image_spec)
def download_data(res: UnionTypes):
    expected_df = pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [20, 22]})
    actual_df = res.dataframe.open(pd.DataFrame).all()
    assert expected_df.equals(actual_df), "DataFrames do not match!"

    with open(res.file, "r") as f:
        assert f.read() == "Hello, World!", "File contents do not match!"

    assert os.listdir(res.directory) == ["df.parquet"], "Directory contents do not match!"
```

A data class supports the usage of data associated with Python types, data classes,
FlyteFile, FlyteDirectory and StructuredDataset.

We define a workflow that calls the tasks created above.

```python
@union.workflow
def basemodel_wf(x: int, y: int) -> (Datum, UnionTypes):
    o1 = add(x=stringify(s=x), y=stringify(s=y))
    o2 = upload_data()
    download_data(res=o2)
    return o1, o2
```

{{< /if-variant >}}

To trigger a task that accepts a dataclass as an input with `{{< var cli_lower >}} run`, you can provide a JSON file as an input:

```
$ {{< var cli_lower >}} run dataclass.py basemodel_wf --x 1 --y 2
```

{{< if-variant flyte >}}

To trigger a task that accepts a dataclass as an input with `pyflyte run`, you can provide a JSON file as an input:
```
pyflyte run \
  https://raw.githubusercontent.com/flyteorg/flytesnacks/b71e01d45037cea883883f33d8d93f258b9a5023/examples/data_types_and_io/data_types_and_io/pydantic_basemodel.py \
  basemodel_wf --x 1 --y 2
```

{{< /if-variant >}}
{{< if-variant byoc byok serverless >}}

To trigger a task that accepts a dataclass as an input with `union run`, you can provide a JSON file as an input:
```
union run \
  https://raw.githubusercontent.com/flyteorg/flytesnacks/b71e01d45037cea883883f33d8d93f258b9a5023/examples/data_types_and_io/data_types_and_io/pydantic_basemodel.py \
  basemodel_wf --x 1 --y 2
```

{{< /if-variant >}}
