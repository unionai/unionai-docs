---
title: Including extra files
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Including extra files

When your app needs additional files beyond the main script (like utility modules, configuration files, or data files), you can use the `include` parameter to specify which files to bundle with your app.

## How include works

The `include` parameter takes a list of file paths (relative to the directory containing your app definition). These files are bundled together and made available in the app container at runtime.

```python
include=["main.py", "utils.py", "config.yaml"]
```

## When to use include

Use `include` when:

- Your app spans multiple Python files (modules)
- You have configuration files that your app needs
- You have data files or templates your app uses
- You want to ensure specific files are available in the container

> [!NOTE]
> If you're using specialized app environments like `FastAPIAppEnvironment`, Flyte automatically detects and includes the necessary files, so you may not need to specify `include` explicitly.

## Examples

### Multi-file Streamlit app

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit/custom_streamlit.py" lang=python >}}

In this example:
- `main.py` is your main Streamlit app file
- `utils.py` contains helper functions used by `main.py`
- Both files are included in the app bundle

### Multi-file FastAPI app

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/multi_file/app.py" lang=python >}}

### App with configuration files

```python
include=["app.py", "config.yaml", "templates/"]
```

## File discovery

When using specialized app environments like `FastAPIAppEnvironment`, Flyte uses code introspection to automatically discover and include the necessary files. This means you often don't need to manually specify `include`.

However, if you have files that aren't automatically detected (like configuration files, data files, or templates), you should explicitly list them in `include`.

## Path resolution

Files in `include` are resolved relative to the directory containing your app definition file. For example:

```
project/
├── apps/
│   ├── app.py          # Your app definition
│   ├── utils.py        # Included file
│   └── config.yaml     # Included file
```

In `app.py`:

```python
include=["utils.py", "config.yaml"]  # Relative to apps/ directory
```

## Best practices

1. **Only include what you need**: Don't include unnecessary files as it increases bundle size
2. **Use relative paths**: Always use paths relative to your app definition file
3. **Include directories**: You can include entire directories, but be mindful of size
4. **Test locally**: Verify your includes work by testing locally before deploying
5. **Check automatic discovery**: Specialized app environments may already include files automatically

## Limitations

- Large files or directories can slow down deployment
- Binary files are supported but consider using data storage (S3, etc.) for very large files
- The bundle size is limited by your Flyte cluster configuration

