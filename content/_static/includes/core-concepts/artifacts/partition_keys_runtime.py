from datetime import datetime

import pandas as pd
from typing_extensions import Annotated
import union
from flytekit.core.artifact import Inputs, Granularity

pandas_image = union.ImageSpec(
    packages=["pandas==2.2.2"]
)

BasicArtifact = union.Artifact(
    name="my_basic_artifact",
    time_partitioned=True,
    time_partition_granularity=Granularity.HOUR,
    partition_keys=["key1"]
)


@union.task(container_image=pandas_image)
def t1(
    key1: str, date: datetime
) -> Annotated[pd.DataFrame, BasicArtifact(key1=Inputs.key1)]:
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    return BasicArtifact.create_from(
        df,
        time_partition=date
    )


@union.workflow
def wf():
    run_date = datetime.now()
    values = ["value1", "value2", "value3"]
    for value in values:
        t1(key1=value, date=run_date)
