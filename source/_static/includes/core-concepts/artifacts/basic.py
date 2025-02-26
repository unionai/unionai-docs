import pandas as pd
from typing_extensions import Annotated
import union

pandas_image = union.ImageSpec(
    packages=["pandas==2.2.2"]
)

BasicTaskData = union.Artifact(
    name="my_basic_artifact"
)


@union.task(container_image=pandas_image)
def t1() -> Annotated[pd.DataFrame, BasicTaskData]:
    my_df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})
    return BasicTaskData.create_from(my_df)


@union.workflow
def wf() -> pd.DataFrame:
    return t1()
