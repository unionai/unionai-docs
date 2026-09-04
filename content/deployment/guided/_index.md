---
title: Guided deployment
description: "Set up Union yourself from the console, instead of sending your configuration to Union and waiting for it to be set up for you."
icon: rocket-takeoff
weight: 1
variants: -flyte +union
---

# Guided deployment

Set up {{< key product_name >}} yourself, from the console: create an organization, run something to see it work, then connect a Kubernetes cluster of your own when you need one. Your data plane runs in your infrastructure, and {{< key product_name >}} manages it for you.

**Nothing dials in.** You never open a port, expose an endpoint, or hand over cluster credentials. The agent you install connects outwards.

## Choosing between the deployment paths

| Path | How you get set up | Who manages the data plane |
|------|--------------------|----------------------------|
| **Guided deployment** (this section) | You set it up yourself in the console. An agent you install does the work. | {{< key product_name >}} |
| [BYOC](../byoc/_index) | You send {{< key product_name >}} your cloud account details and configuration. {{< key product_name >}} sets the data plane up and hands back your endpoints. | {{< key product_name >}} |
| [Self-managed](../selfmanaged/_index) | You provision and install the data plane yourself, then register the cluster. | You |

Guided deployment and BYOC end in the same place. Choose guided deployment to set it up yourself; choose BYOC to have {{< key product_name >}} set it up with you. Choose self-managed if you need to keep operational responsibility for the data plane, and {{< key product_name >}} to have no access to your cluster.

## Where to start

There are two ways in, and they meet at the same place.

- **Buying through AWS Marketplace?** Start at [Start from AWS Marketplace](./from-aws-marketplace). It covers the purchase and the handoff to {{< key product_name >}} that follows it, then sends you to the sign-up page below.
- **Everyone else** starts at [Sign up and create your Union.ai organization](./sign-up).

## The path

1. **[Sign up and create your Union.ai organization](./sign-up).** Your organization is your workspace: it holds your projects, workflows and team. Once it exists you can run a workflow straight away, with no cluster.
2. **[Connect your cluster](./connect-a-cluster).** Give {{< key product_name >}} a Kubernetes cluster to run your workloads on.

You do not need a cluster to start. A run on your own machine reports itself to your organization and appears in the console, which is enough to see how {{< key product_name >}} works before committing infrastructure to it.

{{< subpage-cards >}}
