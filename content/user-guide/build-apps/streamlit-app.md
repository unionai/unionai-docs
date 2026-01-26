---
title: Streamlit app
weight: 8
variants: +flyte +serverless +byoc +selfmanaged
---

# Streamlit app

Streamlit is a popular framework for building interactive web applications and dashboards. Flyte makes it easy to deploy Streamlit apps as long-running services.

## Basic Streamlit app

The simplest way to deploy a Streamlit app is to use the built-in Streamlit "hello" demo:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit/basic_streamlit.py" fragment=app-definition lang=python >}}

This just serves the built-in Streamlit "hello" demo.

## Single-file Streamlit app

For a single-file Streamlit app, you can wrap the app code in a function and use the `args` parameter to specify the command to run the app.
Note that the command is running the file itself, and uses the `--server` flag to start the server.

This is useful when you have a relatively small and simple app that you want to deploy as a single file.

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit/single_file_streamlit.py" fragment=streamlit-app lang=python >}}

Note that the `if __name__ == "__main__"` block is used to both serve the `AppEnvironment` *and* run the app code via
the `streamlit run` command using the `--server` flag.

## Multi-file Streamlit app

When your streamlit application grows more complex, you may want to split your app into multiple files.
For a multi-file Streamlit app, use the `include` parameter to bundle your app files:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit/multi_file_streamlit.py" fragment=app-env lang=python >}}

Where your project structure looks like this:

```
project/
├── main.py           # Main Streamlit app
├── utils.py          # Utility functions
└── components.py     # Reusable components
```

Your `main.py` file would contain your Streamlit app code:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit/main.py" fragment=streamlit-app lang=python >}}

## Example: Data visualization dashboard

Here's a complete example of a Streamlit dashboard, all in a single file.

Define the streamlit app in the `main` function:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit/data_visualization_dashboard.py" fragment=streamlit-app lang=python >}}

Define the `AppEnvironment` to serve the app:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit/data_visualization_dashboard.py" fragment=app-env lang=python >}}

And finally the app serving logic:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit/data_visualization_dashboard.py" fragment=serve lang=python >}}

## Best practices

1. **Use `include` for custom apps**: Always include your app files when deploying custom Streamlit code
2. **Set the port correctly**: Ensure your Streamlit app uses `--server.port 8080` (or match your `port` setting)
3. **Cache data**: Use `@st.cache_data` for expensive computations to improve performance
4. **Resource sizing**: Adjust resources based on your app's needs (data size, computations)
5. **Public vs private**: Set `requires_auth=False` for public dashboards, `True` for internal tools

## Troubleshooting

**App not loading:**
- Verify the port matches (use `--server.port 8080`)
- Check that all required files are included
- Review container logs for errors

**Missing dependencies:**
- Ensure all required packages are in your image's pip packages
- Check that file paths in `include` are correct

**Performance issues:**
- Increase CPU/memory resources
- Use Streamlit's caching features (`@st.cache_data`, `@st.cache_resource`)
- Optimize data processing
