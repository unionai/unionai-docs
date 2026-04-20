---
title: Project patterns
weight: 13
variants: +flyte +union
sidebar_expanded: false
---

# Project patterns

The rest of the user guide explains what Flyte can do.
This section explains how we recommend you structure real projects.

These are opinionated guides. They represent patterns we've seen work well across many teams and production deployments. If you're starting a new project or scaling an existing one, start here.

{{< grid >}}

{{< link-card target="bring-your-own-image" title="Bring your own image (BYOI)" >}}
Two patterns for teams that own their Docker images and want Flyte for orchestration without handing over their build pipeline.
{{< /link-card >}}

{{< link-card target="monorepo-with-uv" title="Monorepo with uv" >}}
How to structure Flyte projects with uv, from single-package setups to multi-team monorepos with shared and independent lockfiles.
{{< /link-card >}}

{{< /grid >}}
