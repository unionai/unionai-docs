# API reference

You can interact with your Union deployment in the following ways:

* Use the [`flytekit`](https://docs.flyte.org/en/latest/api/flytekit/docs_index.html) and [`unionai`](sdk/index) Python SDKs in your workflow code.
* Use the [`unionai` CLI](unionai-cli) to access your Union deployment via the command line.
* Use [`UnionRemote`](unionremote) to access your Union deployment from a Python script or runtime environment.

To get started, install `unionai`:

{@@ if serverless @@}

```
pip install -U unionai
```

{@@ elif byoc @@}

::::{tab-set}

:::{tab-item} Unix/macOS

```{code-block} shell
pip install -U 'unionai[byoc]'
```

:::


:::{tab-item} Windows

```{code-block} shell
pip install -U "unionai[byoc]"
```

:::
::::

{@@ endif @@}

This will install the `flytekit` and `unionai` SDKs, the `unionai` CLI, and `UnionRemote`.
