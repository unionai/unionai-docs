# Serving workflow output

In this section we will demonstrate how to use a Union app to display the output of a Union workflow.

## Example app

Your project directory should now look like this:

```{code-block}bash
├── app.py
├── main.py
├── wf.py
```

## App declaration

```{code-block} python
:caption: app.py

from union import Artifact, Resources
from union.app import App, Input

MyFile = Artifact(name="my_file")

app = App(
    name="streamlit-workflow-output",
    inputs=[
        Input(
            name="my_file",
            value=MyFile.query(),
            auto_download=True,
            env_name="MY_FILE",
        ),
    ],
    container_image="ghcr.io/thomasjpfan/streamlit-app-image-seg:0.1.30",
    command=[
        "streamlit",
        "run",
        "main.py",
        "--server.port",
        "8080",
    ],
    port=8080,
    include=["./main.py"],
    limits=Resources(cpu="2", mem="6Gi", ephemeral_storage="4Gi"),
    min_replicas=1,
    max_replicas=1,
)

```

## main.py

```{code-block} python
:caption: main.py

import os
import streamlit as st

my_file = os.getenv("MY_FILE")
with open(my_file, "r") as file:
    my_file_content = file.read()

st.title("Display workflow output")
st.write(my_file_content)

```

## wf.py

```{code-block} python
:caption: wf.py

from union import Artifact, Resources, FlyteFile, current_context, task, workflow
from pathlib import Path
from typing_extensions import Annotated

MyFile = Artifact(name="my_file")

@task
def t() -> Annotated[FlyteFile, SegModel]:
    working_dir = Path(current_context().working_directory)
    my_file = working_dir / "my_file.txt"

    with open(my_file, "w") as file:
        file.write("Some data")

    return MyFile.create_from(my_file)

@workflow
def wf() -> FlyteFile:
    return t()
```

## Run the example

To run this example you will need to register and run the workflow first:

```{code-block} bash
:caption: Run the workflow
$ union run --remote wf.py wf
```

This will create an `Artifact` called `my_file` from the file `my_file.txt` that contains the text `Some data`.

Now you can deploy your app:

```{code-block} bash
$ union deploy apps app.py streamlit-demo-wf-data
```

The URI of the artifact `my_file` is passed as the environment variable `MY_FILE` via the `input` parameter in the App constructor.
Within `main.py`, the file is retrieved using that environment variable and the contents are displayed in the Streamlit app.
