---
title: Streamlit app
weight: 8
variants: +flyte +serverless +byoc +selfmanaged
---

# Streamlit app

Streamlit is a popular framework for building interactive web applications and dashboards. Flyte makes it easy to deploy Streamlit apps as long-running services.

## Basic Streamlit app

The simplest way to deploy a Streamlit app is to use the built-in Streamlit "hello" demo:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit/basic_streamlit.py" lang=python >}}

## Custom Streamlit app

For a custom Streamlit app, use the `include` parameter to bundle your app files:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit/custom_streamlit.py" lang=python >}}

Your `main.py` file would contain your Streamlit app code:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/streamlit/main.py" fragment=streamlit-app lang=python >}}

## Multi-file Streamlit app

For apps with multiple files, include all necessary files:

```python
app_env = flyte.app.AppEnvironment(
    name="streamlit-multi-file",
    image=image,
    args="streamlit run main.py --server.port 8080",
    port=8080,
    include=["main.py", "utils.py", "components.py"],  # Include all files
    resources=flyte.Resources(cpu="1", memory="1Gi"),
)
```

Structure your project like this:

```
project/
├── main.py           # Main Streamlit app
├── utils.py          # Utility functions
└── components.py     # Reusable components
```

## Example: Data visualization dashboard

Here's a complete example of a Streamlit dashboard:

```python
# main.py
import streamlit as st
import pandas as pd
import numpy as np

st.title("Sales Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=100, freq="D"),
        "sales": np.random.randint(1000, 5000, 100),
    })

data = load_data()

# Sidebar filters
st.sidebar.header("Filters")
start_date = st.sidebar.date_input("Start date", value=data["date"].min())
end_date = st.sidebar.date_input("End date", value=data["date"].max())

# Filter data
filtered_data = data[
    (data["date"] >= pd.Timestamp(start_date)) &
    (data["date"] <= pd.Timestamp(end_date))
]

# Display metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Sales", f"${filtered_data['sales'].sum():,.0f}")
with col2:
    st.metric("Average Sales", f"${filtered_data['sales'].mean():,.0f}")
with col3:
    st.metric("Days", len(filtered_data))

# Chart
st.line_chart(filtered_data.set_index("date")["sales"])
```

Deploy with:

```python
import flyte
import flyte.app

image = flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages(
    "streamlit==1.41.1",
    "pandas==2.2.3",
    "numpy==2.2.3",
)

app_env = flyte.app.AppEnvironment(
    name="sales-dashboard",
    image=image,
    args="streamlit run main.py --server.port 8080",
    port=8080,
    include=["main.py"],
    resources=flyte.Resources(cpu="2", memory="2Gi"),
    requires_auth=False,
)

if __name__ == "__main__":
    flyte.init_from_config()
    app = flyte.deploy(app_env)
    print(f"Dashboard URL: {app[0].url}")
```

## Custom domain

You can use a custom subdomain for your Streamlit app:

```python
app_env = flyte.app.AppEnvironment(
    name="streamlit-app",
    image=image,
    command="streamlit hello --server.port 8080",
    port=8080,
    domain=flyte.app.Domain(subdomain="dashboard"),  # Custom subdomain
    resources=flyte.Resources(cpu="1", memory="1Gi"),
)
```

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

