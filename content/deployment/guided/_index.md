---
title: Guided deployment
description: "Set up Union yourself from the console, instead of sending your configuration to Union and waiting for it to be set up for you."
icon: rocket-takeoff
weight: 0
variants: -flyte +union
---

# Guided deployment

This section is one continuous path: create a {{< key product_name >}} account, get an organization, and connect a Kubernetes cluster of your own, without talking to anyone at {{< key product_name >}}.

Today it covers a Kubernetes cluster you bring yourself. Over time it is intended to become the way any {{< key product_name >}} deployment is set up, rather than a separate kind of deployment.

It is deliberately self-contained. Everything you need is here in order, so you should not have to jump between sections to get running. Some of it repeats material covered elsewhere in more depth, and where it does, each page links on to the reference version.

## How this differs from the other deployment paths

Guided deployment and [BYOC](../byoc/_index) end in the same place: your data plane runs in your infrastructure, and {{< key product_name >}} manages it for you. What differs is how you get there.

| Path | How you get set up | Who manages the data plane afterwards |
|------|--------------------|---------------------------------------|
| [BYOC](../byoc/_index) | You send {{< key product_name >}} your cloud account details and configuration. {{< key product_name >}} sets the data plane up and hands back your endpoints. | {{< key product_name >}} |
| **Guided deployment** (this section) | You do that setup yourself in the console. An agent you install does the work. | {{< key product_name >}} |
| [Self-managed](../selfmanaged/_index) | You provision and install the data plane yourself, then register the cluster. | You |

So guided deployment is not a different destination from BYOC, it is a different route to it: the part that used to be an exchange of configuration with {{< key product_name >}} is now something you do yourself, in minutes, without waiting on anyone.

Self-managed is the genuinely different one. There you keep operational responsibility, and {{< key product_name >}} has no access to your cluster.

**Nothing dials in.** On this path you never open a port, expose an endpoint, or hand over cluster credentials. The agent you install connects outwards.

## You can start without a cluster at all

You do not need any infrastructure to see {{< key product_name >}} work. A run on your own machine can report itself to your organization and appear in the console, which is enough to understand the model before you commit a cluster to it.

Start there if you are evaluating, and come back to [Connect your own cluster](./connect-a-cluster) when you want workloads to run on real infrastructure.

{{< subpage-cards >}}

<!-- When #1573 (user-guide/get-started/sign-up.md) settles, decide whether that page moves here or
     stays and is linked. Peeter's instruction was a self-contained flow in this section; a signup
     page living under user-guide/get-started breaks that. Raised with him 2026-09-04. -->
