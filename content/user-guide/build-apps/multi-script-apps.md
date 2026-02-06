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

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit/main.py" fragment=streamlit-app lang=python >}}

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit/utils.py" lang=python >}}

### Deploying multi-file Streamlit app

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit/multi_file_streamlit.py" fragment=app-env lang=python >}}

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

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/complex_multi_file/app.py" fragment=complex-app lang=python >}}

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/complex_multi_file/models/user.py" fragment=user-model lang=python >}}

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/complex_multi_file/services/auth.py" fragment=auth-service lang=python >}}

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/complex_multi_file/utils/helpers.py" fragment=helpers lang=python >}}

### Deploying complex app

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/complex_multi_file/app.py" fragment=complex-env lang=python >}}

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
