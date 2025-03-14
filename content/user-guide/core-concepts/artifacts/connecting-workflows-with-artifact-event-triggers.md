---
title: Connecting workflows with artifact event triggers
weight: 5
variants: +flyte +serverless +byoc +byok
---

# Connecting workflows with artifact event triggers

In the following example, we define an upstream workflow and a downstream workflow, and define a [trigger](../launch-plans/reactive-workflows.md) in a launch plan to connect the two workflows via an [artifact event](../launch-plans/reactive-workflows.md#artifact-events).

## Imports

{{< variant byoc byok flyte >}}
{{< note >}}
To use the example code on this page, you will need to add your `registry` to the `pandas_image` ImageSpec block.
{{< /note >}}
{{< /variant >}}

First we import the required packages:

```python
# trigger_on_artifact.py

from datetime import datetime

import pandas as pd
from flytekit import ImageSpec, task, workflow, LaunchPlan
from flytekit.core.artifact import Artifact, Inputs
from typing_extensions import Annotated
from union.artifacts import OnArtifact

pandas_image = ImageSpec(
    packages=["pandas==2.2.2"]
)

UpstreamArtifact = Artifact(
    name="my_upstream_artifact",
    time_partitioned=True,
    partition_keys=["key1"],
)


@task(container_image=pandas_image)
def upstream_t1(key1: str) -> Annotated[pd.DataFrame,
                                        UpstreamArtifact(key1=Inputs.key1)]:
    dt = datetime.now()
    my_df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    return UpstreamArtifact.create_from(my_df, key1=key1,
                                        time_partition=dt)


@workflow
def upstream_wf() -> pd.DataFrame:
    return upstream_t1(key1="value1")


on_upstream_artifact = OnArtifact(
    trigger_on=UpstreamArtifact,
)


@task
def downstream_t1():
    print("Downstream task triggered")


@workflow
def downstream_wf():
    downstream_t1()


downstream_triggered = LaunchPlan.create(
    "downstream_with_trigger_lp",
    downstream_wf,
    trigger=on_upstream_artifact
)
```
{{/* lines: 1-7 */}}


## Upstream artifact and workflow definition

Then we define an upstream artifact and a workflow that emits a new version of `UpstreamArtifact` when executed:

```python
# trigger_on_artifact.py

from datetime import datetime

import pandas as pd
from flytekit import ImageSpec, task, workflow, LaunchPlan
from flytekit.core.artifact import Artifact, Inputs
from typing_extensions import Annotated
from union.artifacts import OnArtifact

pandas_image = ImageSpec(
    packages=["pandas==2.2.2"]
)

UpstreamArtifact = Artifact(
    name="my_upstream_artifact",
    time_partitioned=True,
    partition_keys=["key1"],
)


@task(container_image=pandas_image)
def upstream_t1(key1: str) -> Annotated[pd.DataFrame,
                                        UpstreamArtifact(key1=Inputs.key1)]:
    dt = datetime.now()
    my_df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    return UpstreamArtifact.create_from(my_df, key1=key1,
                                        time_partition=dt)


@workflow
def upstream_wf() -> pd.DataFrame:
    return upstream_t1(key1="value1")


on_upstream_artifact = OnArtifact(
    trigger_on=UpstreamArtifact,
)

@task
def downstream_t1():
    print("Downstream task triggered")

@workflow
def downstream_wf():
    downstream_t1()

downstream_triggered = LaunchPlan.create(
    "downstream_with_trigger_lp",
    downstream_wf,
    trigger=on_upstream_artifact
)
```
{{/* lines: 13-31 */}}

## Artifact event definition

Next we define the artifact event that will link the upstream and downstream workflows together:

```python
# trigger_on_artifact.py

from datetime import datetime

import pandas as pd
from flytekit import ImageSpec, task, workflow, LaunchPlan
from flytekit.core.artifact import Artifact, Inputs
from typing_extensions import Annotated
from union.artifacts import OnArtifact

pandas_image = ImageSpec(
    packages=["pandas==2.2.2"]
)

UpstreamArtifact = Artifact(
    name="my_upstream_artifact",
    time_partitioned=True,
    partition_keys=["key1"],
)


@task(container_image=pandas_image)
def upstream_t1(key1: str) -> Annotated[pd.DataFrame,
                                        UpstreamArtifact(key1=Inputs.key1)]:
    dt = datetime.now()
    my_df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    return UpstreamArtifact.create_from(my_df, key1=key1,
                                        time_partition=dt)


@workflow
def upstream_wf() -> pd.DataFrame:
    return upstream_t1(key1="value1")


on_upstream_artifact = OnArtifact(
    trigger_on=UpstreamArtifact,
)


@task
def downstream_t1():
    print("Downstream task triggered")


@workflow
def downstream_wf():
    downstream_t1()


downstream_triggered = LaunchPlan.create(
    "downstream_with_trigger_lp",
    downstream_wf,
    trigger=on_upstream_artifact
)
```
{{/* :lines: 34-36 */}}

## Downstream workflow definition

Then we define the downstream task and workflow that will be triggered when the upstream artifact is created:

```python
# trigger_on_artifact.py

from datetime import datetime

import pandas as pd
from flytekit import ImageSpec, task, workflow, LaunchPlan
from flytekit.core.artifact import Artifact, Inputs
from typing_extensions import Annotated
from union.artifacts import OnArtifact

pandas_image = ImageSpec(
    packages=["pandas==2.2.2"]
)

UpstreamArtifact = Artifact(
    name="my_upstream_artifact",
    time_partitioned=True,
    partition_keys=["key1"],
)


@task(container_image=pandas_image)
def upstream_t1(key1: str) -> Annotated[pd.DataFrame,
                                        UpstreamArtifact(key1=Inputs.key1)]:
    dt = datetime.now()
    my_df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    return UpstreamArtifact.create_from(my_df, key1=key1,
                                        time_partition=dt)


@workflow
def upstream_wf() -> pd.DataFrame:
    return upstream_t1(key1="value1")


on_upstream_artifact = OnArtifact(
    trigger_on=UpstreamArtifact,
)


@task
def downstream_t1():
    print("Downstream task triggered")


@workflow
def downstream_wf():
    downstream_t1()


downstream_triggered = LaunchPlan.create(
    "downstream_with_trigger_lp",
    downstream_wf,
    trigger=on_upstream_artifact
)
```
{{/* :lines: 34-36 :lines: 39-46 */}}

## Launch plan with trigger definition

Finally we create a launch plan with a trigger set to an `OnArtifact` object to link the two workflows via the `Upstream` artifact. The trigger will initiate an execution of the downstream `downstream_wf` workflow upon the creation of a new version of the `Upstream` artifact.

```python
# trigger_on_artifact.py

from datetime import datetime

import pandas as pd
from flytekit import ImageSpec, task, workflow, LaunchPlan
from flytekit.core.artifact import Artifact, Inputs
from typing_extensions import Annotated
from union.artifacts import OnArtifact

pandas_image = ImageSpec(
    packages=["pandas==2.2.2"]
)

UpstreamArtifact = Artifact(
    name="my_upstream_artifact",
    time_partitioned=True,
    partition_keys=["key1"],
)


@task(container_image=pandas_image)
def upstream_t1(key1: str) -> Annotated[pd.DataFrame,
                                        UpstreamArtifact(key1=Inputs.key1)]:
    dt = datetime.now()
    my_df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    return UpstreamArtifact.create_from(my_df, key1=key1,
                                        time_partition=dt)


@workflow
def upstream_wf() -> pd.DataFrame:
    return upstream_t1(key1="value1")


on_upstream_artifact = OnArtifact(
    trigger_on=UpstreamArtifact,
)


@task
def downstream_t1():
    print("Downstream task triggered")


@workflow
def downstream_wf():
    downstream_t1()


downstream_triggered = LaunchPlan.create(
    "downstream_with_trigger_lp",
    downstream_wf,
    trigger=on_upstream_artifact
)
```
{{/* :lines: 49-53 */}}

> [!NOTE]
> The `OnArtifact` object must be attached to a launch plan in order for the launch plan to be triggered by the creation of a new version of the artifact.

## Full example code

Here is the full example code file:

```python
# trigger_on_artifact.py

from datetime import datetime

import pandas as pd
from flytekit import ImageSpec, task, workflow, LaunchPlan
from flytekit.core.artifact import Artifact, Inputs
from typing_extensions import Annotated
from union.artifacts import OnArtifact

pandas_image = ImageSpec(
    packages=["pandas==2.2.2"]
)

UpstreamArtifact = Artifact(
    name="my_upstream_artifact",
    time_partitioned=True,
    partition_keys=["key1"],
)


@task(container_image=pandas_image)
def upstream_t1(key1: str) -> Annotated[pd.DataFrame,
                                        UpstreamArtifact(key1=Inputs.key1)]:
    dt = datetime.now()
    my_df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    return UpstreamArtifact.create_from(my_df, key1=key1,
                                        time_partition=dt)


@workflow
def upstream_wf() -> pd.DataFrame:
    return upstream_t1(key1="value1")


on_upstream_artifact = OnArtifact(
    trigger_on=UpstreamArtifact,
)


@task
def downstream_t1():
    print("Downstream task triggered")


@workflow
def downstream_wf():
    downstream_t1()


downstream_triggered = LaunchPlan.create(
    "downstream_with_trigger_lp",
    downstream_wf,
    trigger=on_upstream_artifact
)
```