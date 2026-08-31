---
title: Plugin setup
description: Cluster-side configuration for the few task plugins that need it.
icon: sliders
variants: +flyte -union
weight: 6
---

# Plugin setup

Flyte runs tasks through plugins, and a few of them need configuration on the cluster
before they work. This section collects that setup, one page per plugin.

Most plugins need nothing here. Reach for these pages when you are changing how a
plugin reaches something outside the cluster, an object store or a credential for
example, rather than when you are first installing Flyte.

- [Flyte copilot storage configuration](./copilot-storage): how copilot reaches your object
  store to move task inputs and outputs, including the Secret the chart creates for it
  and what to do when you manage the Flyte configuration yourself.

{{< subpage-cards >}}
