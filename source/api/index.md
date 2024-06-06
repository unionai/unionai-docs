# API reference

You can interact with your Union deployment in the following ways:

* Use the [`flytekit`](https://docs.flyte.org/en/latest/api/flytekit/docs_index.html) and [`unionai`](sdk/index) Python SDKs in your workflow code.
* Use the [`unionai` CLI](unionai-cli) to register, run, and retrieve workflows and other entities, and more, via the command line.
* Use [`UnionRemote`](unionremote) in a Python runtime environment to programmatically access your Union deployment.

To get started, install `unionai`:

```
pip install -U unionai
```
This will install the `flytekit` and `unionai` SDKs, the `unionai` CLI, and `UnionRemote`.
