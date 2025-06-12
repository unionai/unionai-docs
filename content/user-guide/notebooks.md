---
title: Notebooks
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
---

# Notebooks

Flyte is designed to work seamlessly with Jupyter notebooks, allowing you to write and execute workflows directly within a notebook environment.

## Iterating on and running a workflow

Download the following notebook file and open it in your favorite Jupyter environment: {{< download "/_static/public/interactive.ipynb" "interactive.ipynb" >}}

In this example we have a simple workflow defined in our notebook.
You can iterate on the code in the notebook while running each cell in turn.

Note that the `flyte.init()` call at the top of the notebook looks like this:

```python
flyte.init(
    endpoint="https://union.example.com",
    org="example_org",
    project="example_project",
    domain="development",
)
```

You will have to adjust it to match your Union server endpoint, organization, project, and domain.

## Accessing runs and downloading logs

Similarly, you can download the following notebook file and open it in your favorite Jupyter environment: {{< download "/_static/public/remote.ipynb" "remote.ipynb" >}}

In this example we use [`flyte.remote`](../api-reference/flyte-sdk/packages/flyte.remote) to list existing runs, access them, and download their details and logs


