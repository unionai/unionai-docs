# Serving workflow output

In this section we use a Union app to display the output of a Union workflow.

## Example app

In a local directory, create the following files:

```{code-block} shell
├── app.py
├── main.py
└── wf.py
```

## App declaration

```{code-block} python
:caption: app.py

"""A Union app that serves the output of a Union workflow"""

from union import Artifact, Resources
from union.app import App, Input

# Declare an Artifact with the name "my_file".
# Note that this must be same Artifact name as declared in the workflow code in `wf.py`, below.
MyFile = Artifact(name="my_file")

app = App(
    name="streamlit-workflow-output",
    inputs=[
        Input(
            name="my_file",
            value=MyFile.query(),
            download=True,
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

"""A Streamlit app that displays the contents of a file"""

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

"""A Union workflow that creates an artifact from a file"""

from union import Artifact, Resources, FlyteFile, ImageSpec, current_context, task, workflow
from pathlib import Path
from typing_extensions import Annotated

# ImageSpec defining the container image that will run the task
# Replace YOUR-Registry with the actual name of your own registry!
image_spec = ImageSpec(
    registry="YOUR-REGISTRY",
    name="serving-example-image",
    base_image="ghcr.io/flyteorg/flytekit:py3.12-latest",
    packages=["union"],
)

# Declare an Artifact with the name "my_file"
# Note that this must be same Artifact name as declared in the App declaration code in `app.py`, above.
MyFile = Artifact(name="my_file")

# Define a task that creates an artifact from a file.
# Uses the artifact declared above.
@task(container_image=image_spec)
def t() -> Annotated[FlyteFile, MyFile]:
    working_dir = Path(current_context().working_directory)
    my_file = working_dir / "my_file.txt"

    with open(my_file, "w") as file:
        file.write("Some data")

    return MyFile.create_from(my_file)

# Define a workflow that executes the task.
@workflow
def wf() -> FlyteFile:
    return t()
```

## Run the workflow to create the artifact

To run this example you will need to register and run the workflow first:

```{code-block} bash
:caption: Run the workflow
$ union run --remote wf.py wf
```

This will create an `Artifact` called `my_file` from the file `my_file.txt` that contains the text `Some data`.
Obviously, this is just a toy example, but you can imagine the file containing useful data produced by your workflow that you want to display via your app.

To see that the artifact was successfully created, you can go to the Artifacts list in the Union UI and search for `my_file`:

![Artifacts list](/_static/images/user-guide/core-concepts/serving/serving-workflow-output/artifacts-list.png)

You can select the artifact to see more details:

![Artifact view](/_static/images/user-guide/core-concepts/serving/serving-workflow-output/artifact-view.png)

## Deploy the app

Now that you have confirmed that the artifact has been created, you can deploy your app:

```{code-block} bash
$ union deploy apps app.py streamlit-workflow-output
```

The URI of the artifact `my_file` is passed as the environment variable `MY_FILE` via the `input` parameter in the App constructor.
Within `main.py`, the file is retrieved using that environment variable and the contents are displayed in the Streamlit app.

You can confirm that the app is deployed by going to the Apps list in the Union UI:

![Apps list](/_static/images/user-guide/core-concepts/serving/serving-workflow-output/apps-list.png)

Select the app to see more details:

![App view](/_static/images/user-guide/core-concepts/serving/serving-workflow-output/app-view.png)

Click on the **Endpoint** to view the app itself in action:

![App in action](/_static/images/user-guide/core-concepts/serving/serving-workflow-output/app-in-action.png)

Note that the content of the file, "Some data" is successfully displayed in the app.
