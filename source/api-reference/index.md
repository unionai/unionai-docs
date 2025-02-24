{@@ if flyte @@}

# Flyte API reference

```{admonition} Flyte
These docs are for [**Flyte**](./about-union.md#flyte).
Switch to another variant with the version selector above.
```

{@@ elif serverless @@}

# Union Serverless API reference

```{admonition} Union Serverless
These docs are for [**Union Serverless**](./about-union.md#union-serverless).
Switch to another variant with the version selector above.
```

{@@ elif byoc @@}

# Union BYOC API reference

```{admonition} Union BYOC
These docs are for [**Union BYOC**](./about-union.md#union-byoc).
Switch to another variant with the version selector above.
```

{@@ elif byok @@}

# Union BYOK API reference

```{admonition} Union BYOK
These docs are for [**Union BYOK**](./about-union.md#union-byok).
Switch to another variant with the version selector above.
```

{@@ endif @@}


This section provides the reference material for all Union APIs, SDKs and CLIs.

To get started, install `union`:

```
pip install -U union
```

This will install the Union SDK and the `union` CLI.

::::{grid}

:::{grid-item-card} {octicon}`workflow` Union SDK
:link: union-sdk/index
:link-type: doc
:columns: 12

The Union SDK provides the Python API for building Union workflows.
:::

:::{grid-item-card} {octicon}`terminal` Union CLI
:link: union-cli
:link-type: doc
:columns: 6

The Union CLI is the command-line interface for interacting with your Union instance.
:::

:::{grid-item-card} {octicon}`terminal` Uctl CLI
:link: uctl-cli/index
:link-type: doc
:columns: 6

`uctl` is an alternative CLI for performing administrative tasks and for use in CI/CD environments.
:::

::::
