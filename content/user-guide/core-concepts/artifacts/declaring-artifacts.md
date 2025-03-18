---
title: Declaring artifacts
weight: 1
variants: +flyte +serverless +byoc +byok
---

# Declaring artifacts

In order to define a task or workflow that emits an artifact, you must first declare the artifact and the keys for any [partitions](./_index.md#partitions) you wish for it to have. For the `Artifact` class parameters and methods, see the [Flytekit Artifact documentation](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.Artifact.html).

## Basic artifact

In the following example, an artifact called `BasicTaskData` is declared, along with a task that emits that artifact. Since it is a basic artifact, it doesn't have any partitions.

{{< variant byoc byok flyte >}}
{{< markdown >}}

> [!NOTE]
> To use the example code on this page, you will need to add your `registry`
> to the `pandas_image` ImageSpec block.

{{< /markdown >}}
{{< /variant >}}

```python
# basic.py

import pandas as pd
from flytekit import ImageSpec, task, workflow
from flytekit.core.artifact import Artifact
from typing_extensions import Annotated

pandas_image = ImageSpec(
    packages=["pandas==2.2.2"]
)

BasicTaskData = Artifact(
    name="my_basic_artifact"
)


@task(container_image=pandas_image)
def t1() -> Annotated[pd.DataFrame, BasicTaskData]:
    my_df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    return BasicTaskData.create_from(my_df)


@workflow
def wf() -> pd.DataFrame:
    return t1()
```

## Time-partitioned artifact

By default, time partitioning is not enabled for artifacts. To enable it, declare the artifact with `time_partitioned` set to `True`. You can optionally set the granularity for the time partition to `MINUTE`, `HOUR`, `DAY`, or `MONTH`; the default is `DAY`.

You must also pass a value to `time_partition`, which you can do at runtime or by binding `time_partition` to an input.

### Passing a value to `time_partition` at runtime

```python
# time_partition_runtime.py

from datetime import datetime

import pandas as pd
from flytekit import ImageSpec, task, workflow
from flytekit.core.artifact import Artifact, Granularity
from typing_extensions import Annotated

pandas_image = ImageSpec(
    packages=["pandas==2.2.2"]
)

BasicArtifact = Artifact(
    name="my_basic_artifact",
    time_partitioned=True,
    time_partition_granularity=Granularity.HOUR
)


@task(container_image=pandas_image)
def t1() -> Annotated[pd.DataFrame, BasicArtifact]:
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    dt = datetime.now()
    return BasicArtifact.create_from(df, time_partition=dt)


@workflow
def wf() -> pd.DataFrame:
    return t1()
```
<!-- :emphasize-lines: 1,5,14-15,21-23 -->

### Passing a value to `time_partition` by input

```python
# time_partition_input.py

from datetime import datetime

import pandas as pd
from flytekit import ImageSpec, task, workflow
from flytekit.core.artifact import Artifact, Granularity
from typing_extensions import Annotated

pandas_image = ImageSpec(
    packages=["pandas==2.2.2"]
)

BasicArtifact = Artifact(
    name="my_basic_artifact",
    time_partitioned=True,
    time_partition_granularity=Granularity.HOUR
)


@task(container_image=pandas_image)
def t1(date: datetime) -> Annotated[pd.DataFrame, BasicArtifact]:
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    return BasicArtifact.create_from(df, time_partition=date)


@workflow
def wf(run_date: datetime):
    return t1(date=run_date)
```
<!-- :emphasize-lines: 20-21,28 -->

## Artifact with custom partition keys

You can specify up to 10 custom partition keys when declaring an artifact. Custom partition keys can be set at runtime or be passed as inputs.

### Passing a value to a custom partition key at runtime

```python
# partition_keys_runtime.py

from datetime import datetime

import pandas as pd
from flytekit import ImageSpec, task, workflow
from flytekit.core.artifact import Artifact, Inputs, Granularity
from typing_extensions import Annotated

pandas_image = ImageSpec(
    packages=["pandas==2.2.2"]
)

BasicArtifact = Artifact(
    name="my_basic_artifact",
    time_partitioned=True,
    time_partition_granularity=Granularity.HOUR,
    partition_keys=["key1"]
)


@task(container_image=pandas_image)
def t1(
    key1: str, date: datetime
) -> Annotated[pd.DataFrame, BasicArtifact(key1=Inputs.key1)]:
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    return BasicArtifact.create_from(
        df,
        time_partition=date
    )


@workflow
def wf():
    run_date = datetime.now()
    values = ["value1", "value2", "value3"]
    for value in values:
        t1(key1=value, date=run_date)
```
<!-- :emphasize-lines: 16,35-36 -->


### Passing a value to a custom partition key by input

```python
# partition_keys_input.py

from datetime import datetime

import pandas as pd
from flytekit import ImageSpec, task, workflow
from flytekit.core.artifact import Artifact, Inputs, Granularity
from typing_extensions import Annotated

pandas_image = ImageSpec(
    packages=["pandas==2.2.2"]
)

BasicArtifact = Artifact(
    name="my_basic_artifact",
    time_partitioned=True,
    time_partition_granularity=Granularity.HOUR,
    partition_keys=["key1"]
)


@task(container_image=pandas_image)
def t1(
    key1: str, dt: datetime
) -> Annotated[pd.DataFrame, BasicArtifact(key1=Inputs.key1)]:
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    return BasicArtifact.create_from(
        df,
        time_partition=dt,
        key1=key1
    )


@workflow
def wf(dt: datetime, val: str):
    t1(key1=val, dt=dt)
```
<!-- :emphasize-lines: 16,34 -->

## Artifact with model card example

You can attach a model card with additional metadata to your artifact, formatted in Markdown:

```python
# model_card.py

import pandas as pd
from flytekit import ImageSpec, task, workflow
from flytekit.core.artifact import Artifact
from union.artifacts import ModelCard
from typing_extensions import Annotated

pandas_image = ImageSpec(
    packages=["pandas==2.2.2"]
)

BasicArtifact = Artifact(name="my_basic_artifact")


def generate_md_contents(df: pd.DataFrame) -> str:
    contents = "# Dataset Card\n" "\n" "## Tabular Data\n"
    contents = contents + df.to_markdown()
    return contents


@task(container_image=pandas_image)
def t1() -> Annotated[pd.DataFrame, BasicArtifact]:
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})

    return BasicArtifact.create_from(
        df,
        ModelCard(generate_md_contents(df))
    )


@workflow
def wf():
    t1()
```
<!-- :emphasize-lines: 4,14-17,26 -->

