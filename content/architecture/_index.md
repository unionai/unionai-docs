---
title: Architecture
weight: 6
variants: +flyte -serverless -byoc +selfmanaged
top_menu: true
sidebar_expanded: true
---

# Architecture

This section covers the architecture of the {{< key product_name >}} system.

{{< variant selfmanaged >}}
{{< markdown >}}

Union’s modular architecture allows for great flexibility and control. The customer can decide how many clusters to have, their shape, and who has access to what. All communication is encrypted.

![Architecture](/_static/images/deployment/architecture.svg)

## Control plane

The control plane is responsible for coordinating work across one or more Data Planes.

## Data plane

All your workflow and task executions are performed in the data plane, which runs within your public, private, or hybrid clouds. The data plane’s clusters are provisioned and managed by the control plane through a resident Union operator with minimal required permissions.

### Worker nodes

Worker nodes are responsible for executing your workloads. You have full control over the configuration of your worker nodes.

When worker nodes are not in use, they automatically scale down to the configured minimum. (we scale to zero.)

{{< /markdown >}}
{{< /variant >}}