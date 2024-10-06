# API

To get started, install `union`:

```
pip install -U union
```

This will install the `flytekit` and `union` SDKs, the `union` CLI, and `UnionRemote`.

::::{grid} 2

:::{grid-item-card} {octicon}`rocket` Flytekit SDK
:link: flytekit-sdk/index
:link-type: doc

Flytekit is the main Python SDK for building workflows.
:::

:::{grid-item-card} {octicon}`workflow` Union SDK
:link: union-sdk/index
:link-type: doc

The Union SDK adds additional features to Flytekit.
:::

:::{grid-item-card} {octicon}`terminal` Union CLI
:link: union-cli
:link-type: doc

The Union CLI is the command-line interface for interacting with your Union instance.
:::

:::{grid-item-card} {octicon}`terminal` uctl CLI
:link: uctl-cli/index
:link-type: doc

uctl is an alternative CLI for performing administrative tasks or use in CI/CD environments. It is a Golang binary that can be installed on any platform supported by Golang.
:::

:::{grid-item-card} {octicon}`globe` UnionRemote
:link: union-remote/index
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
