---
title: Multi-script apps
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Multi-script apps

Real-world applications often span multiple files. This page shows how to build FastAPI and Streamlit apps with multiple Python files.

## FastAPI multi-script app

### Project structure

```
project/
├── app.py          # Main FastAPI app file
└── module.py       # Helper module
```

### Example: Multi-file FastAPI app

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/multi_file/app.py" lang=python >}}

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/multi_file/module.py" lang=python >}}

### Automatic file discovery

`FastAPIAppEnvironment` automatically discovers and includes the necessary files by analyzing your imports. However, if you have files that aren't automatically detected (like configuration files or data files), you can explicitly include them:

```python
app_env = FastAPIAppEnvironment(
    name="fastapi-with-config",
    app=app,
    include=["app.py", "module.py", "config.yaml"],  # Explicit includes
    # ...
)
```

## Streamlit multi-script app

### Project structure

```
project/
├── main.py         # Main Streamlit app
├── utils.py        # Utility functions
└── components.py   # Reusable components
```

### Example: Multi-file Streamlit app

```python
# main.py
import streamlit as st
from utils import process_data
from components import render_chart

st.title("Multi-file Streamlit App")

data = st.file_uploader("Upload data file")

if data:
    processed = process_data(data)
    render_chart(processed)
```

```python
# utils.py
import pandas as pd

def process_data(data_file):
    """Process uploaded data file."""
    df = pd.read_csv(data_file)
    # ... processing logic ...
    return df
```

```python
# components.py
import streamlit as st

def render_chart(data):
    """Render a chart component."""
    st.line_chart(data)
```

### Deploying multi-file Streamlit app

```python
import flyte
import flyte.app

image = flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages(
    "streamlit==1.41.1",
    "pandas==2.2.3",
)

app_env = flyte.app.AppEnvironment(
    name="streamlit-multi-file",
    image=image,
    args="streamlit run main.py --server.port 8080",
    port=8080,
    include=["main.py", "utils.py", "components.py"],  # Include all files
    resources=flyte.Resources(cpu="1", memory="1Gi"),
    requires_auth=False,
)

if __name__ == "__main__":
    flyte.init_from_config()
    app = flyte.deploy(app_env)
    print(f"App URL: {app[0].url}")
```

## Complex multi-file example

Here's a more complex example with multiple modules:

### Project structure

```
project/
├── app.py
├── models/
│   ├── __init__.py
│   └── user.py
├── services/
│   ├── __init__.py
│   └── auth.py
└── utils/
    ├── __init__.py
    └── helpers.py
```

### Example code

```python
# app.py
from fastapi import FastAPI
from models.user import User
from services.auth import authenticate
from utils.helpers import format_response

app = FastAPI(title="Complex Multi-file App")

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = User(id=user_id, name="John Doe")
    return format_response(user)
```

```python
# models/user.py
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
```

```python
# services/auth.py
def authenticate(token: str) -> bool:
    # ... authentication logic ...
    return True
```

```python
# utils/helpers.py
def format_response(data):
    return {"data": data, "status": "success"}
```

### Deploying complex app

```python
from flyte.app.extras import FastAPIAppEnvironment
import flyte

app_env = FastAPIAppEnvironment(
    name="complex-app",
    app=app,
    image=flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages(
        "fastapi",
        "uvicorn",
        "pydantic",
    ),
    # Include all necessary files
    include=[
        "app.py",
        "models/",
        "services/",
        "utils/",
    ],
    resources=flyte.Resources(cpu=1, memory="512Mi"),
)
```

## Best practices

1. **Use explicit includes**: For Streamlit apps, explicitly list all files in `include`
2. **Automatic discovery**: For FastAPI apps, `FastAPIAppEnvironment` handles most cases automatically
3. **Organize modules**: Use proper Python package structure with `__init__.py` files
4. **Test locally**: Test your multi-file app locally before deploying
5. **Include all dependencies**: Include all files that your app imports

## Troubleshooting

**Import errors:**
- Verify all files are included in the `include` parameter
- Check that file paths are correct (relative to app definition file)
- Ensure `__init__.py` files are included for packages

**Module not found:**
- Add missing files to the `include` list
- Check that import paths match the file structure
- Verify that the image includes all necessary packages

**File not found at runtime:**
- Ensure all referenced files are included
- Check mount paths for file/directory inputs
- Verify file paths are relative to the app root directory
