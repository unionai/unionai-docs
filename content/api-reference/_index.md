---
title: API reference
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
top_menu: true
sidebar_expanded: true
---

# API reference

This section provides the reference material for all {{< key product_name >}} APIs, SDKs and CLIs.

{{< variant serverless byoc selfmanaged >}}
{{< markdown >}}

To get started, add `union` to your project

```shell
$ uv add union
```

This will install the Union and Flytekit SDKs and the `union` CLI.
{{< /markdown >}}
{{< grid >}}

{{< link-card target="flytekit-sdk" icon="workflow" title="Flytekit SDK" >}}
The Flytekit SDK provides the core Python API for building Union.ai workflows and apps.
{{< /link-card >}}

{{< link-card target="union-sdk" icon="workflow" title="Union SDK" >}}
The Union SDK provides additional Union.ai-specific capabilities, on top of the core Flytekit SDK.
{{< /link-card >}}

{{< link-card target="union-cli" icon="terminal" title="Union CLI" >}}
The Union CLI is the command-line interface for interacting with your Union instance.
{{< /link-card >}}

{{< link-card target="uctl-cli" icon="terminal" title="Uctl CLI" >}}
The Uctl CLI is an alternative CLI for performing administrative tasks and for use in CI/CD environments.
{{< /link-card >}}

{{< /grid >}}
{{< /variant >}}

{{< variant flyte>}}
{{< markdown >}}

To get started, add `flytekit` to your project

```shell
$ uv add flytekit
```

This will install the Flytekit SDKs and the `pyflyte` CLI.
{{< /markdown >}}
{{< grid >}}

{{< link-card target="flytekit-sdk" icon="workflow" title="Flytekit SDK" >}}
The Flytekit SDK provides the core Python API for building Flyte workflows.
{{< /link-card >}}

{{< link-card target="pyflyte-cli" icon="terminal" title="Pyflyte CLI" >}}
The Pyflyte CLI is the command-line interface for interacting with your Flyte instance.
{{< /link-card >}}

{{< link-card target="flytectl-cli" icon="terminal" title="Flytectl CLI" >}}
The Flytectl CLI is an alternative CLI for performing administrative tasks and for use in CI/CD environments.
{{< /link-card >}}

{{< link-card target="flyteidl" icon="terminal" title="Flyteidl" >}}
Flyteidl is the specification for the Flyte language in protobuf.
{{< /link-card >}}

{{< /grid >}}
{{< /variant >}}
