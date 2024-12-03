# Serving workflow output

In the previous example we defined and deployed a simple Streamlit app unconnected to any Union workflow.

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

from union import App, Input, Resources

app = App(
    name="streamlit-demo-wf-data",
    inputs=[
        Input(
            name="DATA_FILE_PATH",
            value=<MY-DATA-URI>,
            auto_download=True,
        ),
    ],
    container_image="ghcr.io/thomasjpfan/streamlit-app:0.1.20",
    command=["streamlit", "run", "main.py", "--server.port", "8080"],
    port=8080,
    include=["./main.py"]
)
```

## main.py

```{code-block} python
:caption: main.py

import os
import streamlit as st
from pathlib import Path

data_file_path = Path(os.environ["DATA_FILE_PATH"])
data = data_file_path.read_text()
st.header("I want to update the header of my file")
st.subheader(data)
```

## wf.py

```{code-block} python
:caption: wf.py

from pathlib import Path
from union import current_context, task, workflow, FlyteFile

@task
def my_task() -> FlyteFile:
    working_dir = Path(current_context().working_directory)
    new_file = working_dir / "data.txt"
    new_file.write_text("This is some workflow data")
    return new_file


@workflow
def wf() -> FlyteFile:
    return my_task()
```

## Run the example

To run this example you will need to register and run the workflow first:

```{code-block} bash
:caption: Run the workflow
$ union run --remote wf.py wf
```

This will write the data file to the Union object store.

Once the workflow is completed, you need to get the URI of the file in the object store.
It can be copied from the task output in the UI:

![Copy output URI](/_static/images/user-guide/core-concepts/serving/serving-workflow-outputa/copy-output-uri.png)

Paste this URI into `<MY-DATA-URI>` in the `input` parameter of the App declaration above.

Now you deploy your app:

```{code-block} bash
$ union deploy apps app.py streamlit-demo-wf-data
```

When the app runs, inside `main.py` the URI of the file will be retrieved as the environment variable `DATA_FILE_PATH` and displayed in the Streamlit app.
