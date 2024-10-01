# API

To get started, install `union`:

```
pip install -U union
```

This will install the `flytekit` and `union` SDKs, the `union` CLI, and `UnionRemote`.
See [Quick start](../index.md#quick-start) for more details.


::::{grid} 2

:::{grid-item-card} {octicon}`rocket` Flytekit SDK
:link: flytekit-sdk
:link-type: doc

Flytekit is the main Python SDK for building workflows.
:::

:::{grid-item-card} {octicon}`workflow` Union SDK
:link: union-sdk
:link-type: doc

The Union SDK adds additional features to Flytekit.
:::

:::{grid-item-card} {octicon}`terminal` Union CLI
:link: union-cli
:link-type: doc

The Union CLI is the command-line interface for interacting with your Union instance.
:::

:::{grid-item-card} {octicon}`globe` UnionRemote
:link: union-remote
:link-type: doc

The UnionRemote Python API lets you manage Union workflows with Python code.
:::

{@@ if byoc @@}
:::{grid-item-card} {octicon}`gear` Config
:link: config
:link-type: doc

The Config Python API is used to connect to your Union BYOC instance.
:::
{@@ endif @@}

::::
