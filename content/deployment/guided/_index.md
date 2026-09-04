---
title: Guided deployment
description: "Set up Union yourself from the console, instead of sending your configuration to Union and waiting for it to be set up for you."
icon: rocket-takeoff
weight: 0
variants: -flyte +union
---

# Guided deployment

Set up {{< key product_name >}} yourself, from the console: create an organization, then connect a Kubernetes cluster of your own. Your data plane runs in your infrastructure, and {{< key product_name >}} manages it for you.

**Nothing dials in.** You never open a port, expose an endpoint, or hand over cluster credentials. The agent you install connects outwards.

## Choosing between the deployment paths

| Path | How you get set up | Who manages the data plane |
|------|--------------------|----------------------------|
| **Guided deployment** (this section) | You set it up yourself in the console. An agent you install does the work. | {{< key product_name >}} |
| [BYOC](../byoc/_index) | You send {{< key product_name >}} your cloud account details and configuration. {{< key product_name >}} sets the data plane up and hands back your endpoints. | {{< key product_name >}} |
| [Self-managed](../selfmanaged/_index) | You provision and install the data plane yourself, then register the cluster. | You |

Guided deployment and BYOC end in the same place. Choose guided deployment to set it up yourself; choose BYOC to have {{< key product_name >}} set it up with you. Choose self-managed if you need to keep operational responsibility for the data plane, and {{< key product_name >}} to have no access to your cluster.

## The path, in order

1. **[Sign up and run your first workflow](./sign-up)** — create an account and an organization, then run something and see it in the console. No cluster needed.
2. **[Connect your own cluster](./connect-a-cluster)** — give {{< key product_name >}} a Kubernetes cluster to run workloads on.

You do not need a cluster to start. A run on your own machine reports itself to your organization and appears in the console, which is enough to see how {{< key product_name >}} works before committing infrastructure to it.

{{< subpage-cards >}}
