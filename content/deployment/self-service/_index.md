---
title: Self-service setup
description: "The fastest way to deploy Union.ai: subscribe to Union.ai Teams on AWS Marketplace, create your organization, and connect your cluster, all from the Union.ai UI."
icon: rocket-takeoff
weight: 1
variants: -flyte +union
---

# Self-service setup

This is the fastest way to deploy Union.ai. You subscribe to **Union.ai Teams** on AWS Marketplace, create your organization in the Union.ai UI, run something to see it work, then connect a Kubernetes cluster of your own. Everything happens from the Union.ai UI: you don't provision the data plane by hand or wait on Union.ai to set it up for you.

The result is a [self-managed deployment](../selfmanaged/_index): the data plane runs in your cluster, and you own the cluster and its upgrades. Self-service setup is currently available on AWS; GCP and Azure are coming soon.

**Nothing dials in.** You never open a port, expose an endpoint, or hand over cluster credentials. The agent you install connects outwards.

## The path

1. **[Start from AWS Marketplace](./from-aws-marketplace).** Subscribe through AWS Marketplace, so the charges appear on your AWS bill, then follow the handoff to Union.ai. Skip this step if you are not buying through AWS Marketplace.
2. **[Sign up and create your Union.ai organization](./sign-up).** Your organization is your workspace: it holds your projects, workflows and team. Once it exists you can run a workflow straight away, with no cluster.
3. **[Connect your cluster](./connect-a-cluster).** Give Union.ai a Kubernetes cluster to run your workloads on, and it installs the data plane into it.

You do not need a cluster to start. A run on your own machine reports itself to your organization and appears in the console, which is enough to see how Union.ai works before committing infrastructure to it.

{{< subpage-cards >}}
