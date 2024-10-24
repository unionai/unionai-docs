# Serving models

TODO: Clean up based on more recent examples from Thomas

```bash
streamlit_app.py
utils.py
app_def.py
my_union_app.py
```

* `streamlit_app.py` is...
* `utils.py` is imported from `streamlit_app.py`
* `app_def.py` is a Union specific configuration file
* `my_union_app.py` is the main file that defines the app and its dependencies

Here is an example of a Streamlit app in my_union_app.py:

```python
# my_union_app.py
from union.app_spec import AppSpec
from flytekit import Artifact
from union.serve import File

model = Artifact(name="model")

my_streamlit_app = AppSpec(
    name="my-streamlit-app",

    # Can also be a s3://
    inputs={"model_file": "s3://..."},

    # Artifact input
    # inputs={"MODEL_FILE": model.query()}

    container_image=ImageSpec(
        name="streamlit_app",
        requirements="requirements.txt",
    ),
    secret_requests=[Secret(...)],
    request=Resources(cpu="2", mem="4Gi"),
    includes=[
        "streamlit_app.py",
        "utils.py"
    ],
    entrypoint="streamlit run streamlit_app.py",
)
```

Small runtime library for downloading files and manage serving runtime


Here is streamlit_app.py:

```python
# streamlit_app.py
import os
from utils import load_model
from union.serve import File

file = File(input_name="model_file")
path = file.download()
model = load_model(path)
```
