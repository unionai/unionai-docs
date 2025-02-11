from datetime import datetime

import pandas as pd
from typing_extensions import Annotated
import union
from flytekit.core.artifact import Granularity

pandas_image = union.ImageSpec(
    packages=["pandas==2.2.2"]
)

BasicArtifact = union.Artifact(
    name="my_basic_artifact",
    time_partitioned=True,
    time_partition_granularity=Granularity.HOUR
)


@union.task(container_image=pandas_image)
def t1() -> Annotated[pd.DataFrame, BasicArtifact]:
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    dt = datetime.now()
    return BasicArtifact.create_from(df, time_partition=dt)


@union.workflow
def wf() -> pd.DataFrame:
    return t1()
