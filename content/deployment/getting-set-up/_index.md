---
title: Getting set up
description: Create an organization, then connect a Kubernetes cluster of your own, entirely from the console.
icon: rocket-takeoff
weight: 0
variants: -flyte +union
---

# Getting set up

This section is one continuous path: create a {{< key product_name >}} account, get an organization, and connect a Kubernetes cluster you own, without talking to anyone at {{< key product_name >}}.

It is deliberately self-contained. Everything you need is here in order, so you should not have to jump between sections to get running. Some of it repeats material covered elsewhere in more depth, and where it does, each page links on to the reference version.

## How this differs from the other deployment paths

| Path | Who runs the data plane | How it gets installed |
|------|-------------------------|-----------------------|
| [BYOC](../byoc/_index) | {{< key product_name >}}, in your cloud account | {{< key product_name >}} provisions and operates it |
| [Self-managed](../selfmanaged/_index) | You | You provision and install it, then register the cluster |
| **Getting set up** (this section) | You | You register the cluster first, then install an agent that pulls the data plane down |

The order is the thing to notice. On the self-managed path you install the data plane and then tell {{< key product_name >}} about it. Here you register first, and an agent you install into the cluster connects outwards and installs the rest for you.

**Nothing dials in.** You never open a port, expose an endpoint, or hand over cluster credentials.

## You can start without a cluster at all

You do not need any infrastructure to see {{< key product_name >}} work. A run on your own machine can report itself to your organization and appear in the console, which is enough to understand the model before you commit a cluster to it.

Start there if you are evaluating, and come back to [Connect your own cluster](./connect-a-cluster) when you want workloads to run on real infrastructure.

{{< subpage-cards >}}

<!-- When #1573 (user-guide/get-started/sign-up.md) settles, decide whether that page moves here or
     stays and is linked. Peeter's instruction was a self-contained flow in this section; a signup
     page living under user-guide/get-started breaks that. Raised with him 2026-09-04. -->
