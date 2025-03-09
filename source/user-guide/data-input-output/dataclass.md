# Dataclass

When you've multiple values that you want to send across {@= Product =@} entities, you can use a `dataclass`.

{@@ if flyte @@}

Flytekit uses the [Mashumaro library](https://github.com/Fatal1ty/mashumaro)
to serialize and deserialize dataclasses.

With the 1.14 release, `flytekit` adopted `MessagePack` as the serialization format for dataclasses, addressing a major limitation of previous versions that serialized data into a JSON string within a Protobuf `struct`.

In earlier versions, Protobuf’s `struct` converted integer types to floats, requiring users to write boilerplate code to work around this issue.

:::{important}
If you're using Flytekit version < v1.11.1, you will need to add `from dataclasses_json import dataclass_json` to your imports and decorate your dataclass with `@dataclass_json`.
:::

:::{important}
Flytekit version < v1.14.0 will produce protobuf `struct` literal for dataclasses.

Flytekit version >= v1.14.0 will produce msgpack bytes literal for dataclasses.

If you're using Flytekit version >= v1.14.0 and you want to produce protobuf `struct` literal for dataclasses, you can 
set environment variable  `FLYTE_USE_OLD_DC_FORMAT` to `true`.

For more details, you can refer the MSGPACK IDL RFC: https://github.com/flyteorg/flyte/blob/master/rfc/system/5741-binary-idl-with-message-pack.md
:::

```{note}
To clone and run the example code on this page, see the [Flytesnacks repo](https://github.com/flyteorg/flytesnacks/tree/master/examples/data_types_and_io/).
```

{@@ endif @@}

To begin, import the necessary dependencies:

```python
import os
import tempfile
from dataclasses import dataclass

import pandas as pd
import union
from flytekit.types.structured import StructuredDataset
```

Build your custom image with ImageSpec:
```python
image_spec = union.ImageSpec(
    registry="ghcr.io/flyteorg",
    packages=["pandas", "pyarrow"],
)
```

## Python types
We define a `dataclass` with `int`, `str` and `dict` as the data types.

```python
@dataclass
class Datum:
    x: int
    y: str
    z: dict[int, str]
```

You can send a `dataclass` between different tasks written in various languages, and input it through the {@= Product =@} UI as raw JSON.

:::{note}
All variables in a data class should be **annotated with their type**. Failure to do will result in an error.
:::

Once declared, a dataclass can be returned as an output or accepted as an input.

```python
@union.task(container_image=image_spec)
def stringify(s: int) -> Datum:
    """
    A dataclass return will be treated as a single complex JSON return.
    """
    return Datum(x=s, y=str(s), z={s: str(s)})


@union.task(container_image=image_spec)
def add(x: Datum, y: Datum) -> Datum:
    x.z.update(y.z)
    return Datum(x=x.x + y.x, y=x.y + y.y, z=x.z)
```

## {@= Product =@} types
We also define a data class that accepts `StructuredDataset`, `FlyteFile` and `FlyteDirectory`.

{@@ if flyte @@}
```python
@dataclass
class FlyteTypes:
    dataframe: StructuredDataset
    file: union.FlyteFile
    directory: union.FlyteDirectory


@union.task(container_image=image_spec)
def upload_data() -> FlyteTypes:
    df = pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [20, 22]})

    temp_dir = tempfile.mkdtemp(prefix="flyte-")
    df.to_parquet(temp_dir + "/df.parquet")

    file_path = tempfile.NamedTemporaryFile(delete=False)
    file_path.write(b"Hello, World!")

    fs = FlyteTypes(
        dataframe=StructuredDataset(dataframe=df),
        file=union.FlyteFile(file_path.name),
        directory=union.FlyteDirectory(temp_dir),
    )
    return fs


@union.task(container_image=image_spec)
def download_data(res: FlyteTypes):
    assert pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [20, 22]}).equals(res.dataframe.open(pd.DataFrame).all())
    f = open(res.file, "r")
    assert f.read() == "Hello, World!"
    assert os.listdir(res.directory) == ["df.parquet"]
```

A data class supports the usage of data associated with Python types, data classes,
FlyteFile, FlyteDirectory and structured dataset.

We define a workflow that calls the tasks created above.

```python
@union.workflow
def dataclass_wf(x: int, y: int) -> (Datum, FlyteTypes):
    o1 = add(x=stringify(s=x), y=stringify(s=y))
    o2 = upload_data()
    download_data(res=o2)
    return o1, o2
```

{@@ elif byoc or byok or serverless @@}

```python
@dataclass
class UnionTypes:
    dataframe: StructuredDataset
    file: union.FlyteFile
    directory: union.FlyteDirectory


@union.task(container_image=image_spec)
def upload_data() -> UnionTypes:
    df = pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [20, 22]})

    temp_dir = tempfile.mkdtemp(prefix="union-")
    df.to_parquet(temp_dir + "/df.parquet")

    file_path = tempfile.NamedTemporaryFile(delete=False)
    file_path.write(b"Hello, World!")

    fs = UnionTypes(
        dataframe=StructuredDataset(dataframe=df),
        file=union.FlyteFile(file_path.name),
        directory=union.FlyteDirectory(temp_dir),
    )
    return fs


@union.task(container_image=image_spec)
def download_data(res: UnionTypes):
    assert pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [20, 22]}).equals(res.dataframe.open(pd.DataFrame).all())
    f = open(res.file, "r")
    assert f.read() == "Hello, World!"
    assert os.listdir(res.directory) == ["df.parquet"]
```

A data class supports the usage of data associated with Python types, data classes,
FlyteFile, FlyteDirectory and structured dataset.

We define a workflow that calls the tasks created above.

```python
@union.workflow
def dataclass_wf(x: int, y: int) -> (Datum, FlyteTypes):
    o1 = add(x=stringify(s=x), y=stringify(s=y))
    o2 = upload_data()
    download_data(res=o2)
    return o1, o2
```

{@@ endif @@}

You can run the workflow locally as follows:

```python
if __name__ == "__main__":
    dataclass_wf(x=10, y=20)
```

{@@ if flyte @@}

To trigger a task that accepts a dataclass as an input with `pyflyte run`, you can provide a JSON file as an input:
```
pyflyte run \
  https://raw.githubusercontent.com/flyteorg/flytesnacks/69dbe4840031a85d79d9ded25f80397c6834752d/examples/data_types_and_io/data_types_and_io/dataclass.py \
  add --x dataclass_input.json --y dataclass_input.json
```

{@@ elif byoc or byok or serverless @@}

To trigger a task that accepts a dataclass as an input with `union run`, you can provide a JSON file as an input:
```
union run \
  https://raw.githubusercontent.com/flyteorg/flytesnacks/69dbe4840031a85d79d9ded25f80397c6834752d/examples/data_types_and_io/data_types_and_io/dataclass.py \
  add --x dataclass_input.json --y dataclass_input.json
```

{@@ endif @@}