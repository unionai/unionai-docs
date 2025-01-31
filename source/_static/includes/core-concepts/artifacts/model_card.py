import pandas as pd
from typing_extensions import Annotated
import union
from union.artifacts import ModelCard

pandas_image = union.ImageSpec(
    packages=["pandas==2.2.2"]
)

BasicArtifact = union.Artifact(name="my_basic_artifact")


def generate_md_contents(df: pd.DataFrame) -> str:
    contents = "# Dataset Card\n" "\n" "## Tabular Data\n"
    contents = contents + df.to_markdown()
    return contents


@union.task(container_image=pandas_image)
def t1() -> Annotated[pd.DataFrame, BasicArtifact]:
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})

    return BasicArtifact.create_from(
        df,
        ModelCard(generate_md_contents(df))
    )


@union.workflow
def wf():
    t1()
