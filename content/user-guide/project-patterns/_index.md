---
title: Project patterns
description: Patterns for BYO images, monorepos with uv, CI/CD, and multi-team resource management.
icon: folder
weight: 9
variants: +flyte +union
---

# Project patterns

The rest of the user guide explains what Flyte can do.
This section explains how we recommend you structure real projects.

These are opinionated guides. They represent patterns we've seen work well across many teams and production deployments. If you're starting a new project or scaling an existing one, start here.

{{< grid >}}

{{< link-card target="bring-your-own-image" icon="box-seam" title="Bring your own image (BYOI)" >}}
Two patterns for teams that own their Docker images and want Flyte for orchestration without handing over their build pipeline.
{{< /link-card >}}

{{< link-card target="monorepo-with-uv" icon="folder2-open" title="Monorepo with uv" >}}
How to structure Flyte projects with uv, from single-package setups to multi-team monorepos with shared and independent lockfiles.
{{< /link-card >}}

{{< link-card target="cicd" icon="arrow-repeat" title="CI/CD deployments" >}}
How to deploy a Flyte project from CI. Uses GitHub Actions as the reference, but the building blocks (API key, `flyte deploy`, commit-pinned versions) translate to any runner.
{{< /link-card >}}

{{< variant union >}}
{{< link-card target="resource-management" icon="people" title="Resource management and multi-team scaling" >}}
Projects, domains, quotas, RBAC, and secrets: the primitives to set up before you have ten teams and a noisy-neighbor problem.
{{< /link-card >}}
{{< /variant >}}

{{< /grid >}}
