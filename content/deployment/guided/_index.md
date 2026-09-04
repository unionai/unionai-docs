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

## Where to start

There are two ways in, and they meet at the same place.

- **Buying through AWS Marketplace?** Start at [Start from AWS Marketplace](./from-aws-marketplace). It covers the purchase and the handoff to {{< key product_name >}} that follows it, then sends you to the sign-up page below.
- **Everyone else** starts at [Sign up and create your Union.ai organization](./sign-up).

## The path

1. **[Sign up and create your Union.ai organization](./sign-up).** Your organization is your workspace: it holds your projects, workflows and team. Once it exists you can run a workflow straight away, with no cluster.
2. **[Connect your cluster](./connect-a-cluster).** Give {{< key product_name >}} a Kubernetes cluster to run your workloads on.

You do not need a cluster to start. A run on your own machine reports itself to your organization and appears in the console, which is enough to see how {{< key product_name >}} works before committing infrastructure to it.

{{< subpage-cards >}}
