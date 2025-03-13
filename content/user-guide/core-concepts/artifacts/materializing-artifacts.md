---
title: Materializing artifacts
weight: 3
variants: +flyte +serverless +byoc +byok
---

# Materializing artifacts

You can materialize an artifact by executing the task or workflow that emits the artifact.

In the example below, to materialize the `BasicArtifact` artifact, the `t1` task must be executed. The `wf` workflow runs the `t1` task three times with different values for the `key1` partition each time.
Note that each time `t1` is executed, it emits a new version of the `BasicArtifact` artifact.

{{< if-variant byoc byok flyte >}}

{{< note >}}
To use the example code on this page, you will need to add your `registry` to the `pandas_image` ImageSpec block.
{{< /note >}}

{{< /if-variant >}}

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

{{< note >}}
You can also materialize an artifact by executing the `create_artifact` method of `UnionRemote`.
For more information, see the [UnionRemote documentation](../../../api-reference/union-sdk/union-remote/index.md).
{{< /note >}}
