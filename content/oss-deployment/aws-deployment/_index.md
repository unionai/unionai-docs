---
title: AWS deployment
description: Install Flyte on AWS with either the flyte-binary or the flyte-core Helm chart.
icon: cloud
variants: +flyte -union
weight: 3
---

# AWS deployment

Flyte ships two charts that deploy the same platform to a real cluster. Both assume
you have already provisioned the [external dependencies](../overview) — a Kubernetes
cluster, a PostgreSQL database, and an object-store bucket — and that you have `helm`
and `kubectl` configured against your cluster.

Pick one:

| Chart | What it deploys | Use it when |
|---|---|---|
| [`flyte-binary`](./flyte-binary) | One Deployment running every Flyte component | Most installs. Fewest moving parts, one pod to watch, one config to reason about. |
| [`flyte-core`](./flyte-core) | The same components split into one Deployment each — runs, actions, events, cache, dataproxy, secret, executor | You need to scale, schedule, or roll out components independently: a hot control plane, a large event volume, per-component node pools or resource limits. |

Both charts read the same underlying Flyte configuration and expose the same API, so
the choice is about operations, not features. The `flyte-core` guide is written to
mirror the `flyte-binary` one step for step, so you can compare them side by side.

> [!NOTE] The values schemas are not interchangeable
> The two charts organize their values differently — `flyte-binary` nests service
> settings under `flyte-core-components`, `flyte-core` under `configuration` and
> `components`. A `values.yaml` written for one chart will not install the other.
> The [`flyte-core` page](./flyte-core#values-differences-from-flyte-binary) lists
> the differences.

Once Flyte is running, secure it with [Authentication and SSO](../authentication).
