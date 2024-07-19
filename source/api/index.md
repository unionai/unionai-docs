# API reference

You can interact with your Union deployment in the following ways:

* Use the [`flytekit`](https://docs.flyte.org/en/latest/api/flytekit/docs_index.html) and [`union`](./sdk/index) Python SDKs in your workflow code.
* Use the [`union` CLI](./union-cli) to access your Union deployment via the command line.
* Use [`UnionRemote`](./union-remote/index) to access your Union deployment from a Python script or runtime environment.

To get started, install `union`:

{@@ if serverless @@}

```
pip install -U union
```

{@@ elif byoc @@}

::::{tab-set}

:::{tab-item} Unix/macOS

```{code-block} shell
pip install -U 'union[byoc]'
```

:::


:::{tab-item} Windows

```{code-block} shell
pip install -U "union[byoc]"
```

:::
::::

{@@ endif @@}

This will install the `flytekit` and `union` SDKs, the `union` CLI, and `UnionRemote`.
