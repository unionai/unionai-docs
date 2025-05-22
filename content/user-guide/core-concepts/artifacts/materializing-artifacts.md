---
title: Materializing artifacts
weight: 2
variants: -flyte +serverless +byoc +selfmanaged
---

# Materializing artifacts

You can materialize an artifact by executing the task or workflow that emits the artifact.

In the example below, to materialize the `BasicArtifact` artifact, the `t1` task must be executed. The `wf` workflow runs the `t1` task three times with different values for the `key1` partition each time.
Note that each time `t1` is executed, it emits a new version of the `BasicArtifact` artifact.

{{< variant byoc selfmanaged flyte >}}
{{< markdown >}}
> [!NOTE]
> To use the example code on this page, you will need to add your `registry` to the `pandas_image` ImageSpec block.
{{< /markdown >}}
{{< /variant >}}

```python
# partition_keys_runtime.py

from datetime import datetime

import pandas as pd
import {{< key kit_import >}}
from flytekit.core.artifact import Inputs, Granularity
from typing_extensions import Annotated


pandas_image = {{< key kit_as >}}.ImageSpec(
    packages=["pandas==2.2.2"]
)

BasicArtifact = {{< key kit_as >}}.Artifact(
    name="my_basic_artifact",
    time_partitioned=True,
    time_partition_granularity=Granularity.HOUR,
    partition_keys=["key1"]
)


@{{< key kit_as >}}.task(container_image=pandas_image)
def t1(
    key1: str, date: datetime
) -> Annotated[pd.DataFrame, BasicArtifact(key1=Inputs.key1)]:
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    return BasicArtifact.create_from(
        df,
        time_partition=date
    )


@{{< key kit_as >}}.workflow
def wf():
    run_date = datetime.now()
    values = ["value1", "value2", "value3"]
    for value in values:
        t1(key1=value, date=run_date)
```

> [!NOTE]
> You can also materialize an artifact by executing the `create_artifact` method of `{{< key kit_remote >}}`.
> For more information, see the [{{< key kit_remote >}} documentation](../../development-cycle/union-remote).
