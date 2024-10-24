# Serving workflow output

In the previous example we defined and deployed a simple Streamlit app unconnected to any Union workflow.

In this section we will demonstrate how to use a Union app to display the out of a Union workflow.

## Example

Your project directory should now look like this:

```bash
├── app.py
├── main.py
├── wf.py
```

[TODO: add link to full example in GH]()

### app.py

```{code-block} python
:caption: app.py

from union import App, Input, Resources

app = App(
    name="streamlit-demo-wf-data",
    inputs=[
        Input(
            name="DATA_FILE_PATH",
            value="s3://opencompute-staging-sample-tenant/yw/akvrr49wc4qdhbl62nlq-n0-0/099d1a5b222e611a6c440f2a307dd256/data.txt",
            auto_download=True,
        ),
    ],
    container_image="ghcr.io/thomasjpfan/streamlit-app:0.1.20",
    command=["streamlit", "run", "main.py", "--server.port", "8080"],
    port=8080,
    include=["./main.py"]
)
```

### main.py

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

### wf.py

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
This will write the data file to the Union object store.
You then need to get the URI of the file in the object store and paste it into the App definition as an input and deploy the app.
When the app runs, inside `main.py` the URI of the file will be retrieved as the environment variable `DATA_FILE_PATH` and displayed in the Streamlit app.
