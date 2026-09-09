---
title: Guided deployment
description: "Set up Union yourself from the console, instead of sending your configuration to Union and waiting for it to be set up for you."
icon: rocket-takeoff
weight: 1
variants: -flyte +union
---

# Guided deployment

A guided deployment is a [BYOC deployment](../byoc/_index) that you can buy and set up yourself. Subscribe, create your organization in the console, then connect a Kubernetes cluster of your own. Your data plane runs in your infrastructure, and {{< key product_name >}} manages it for you.

**Nothing dials in.** You never open a port, expose an endpoint, or hand over cluster credentials. The agent you install connects outwards.

## The path

1. **[Start from AWS Marketplace](./from-aws-marketplace).** Subscribe through AWS Marketplace, so the charges appear on your AWS bill, then follow the handoff to {{< key product_name >}}. Skip this step if you are not buying through AWS Marketplace.
2. **[Sign up and create your Union.ai organization](./sign-up).** Your organization is your workspace: it holds your projects, workflows and team.
3. **[Connect your cluster](./connect-a-cluster).** Give {{< key product_name >}} a Kubernetes cluster to run your workloads on, and it installs the data plane into it.

Waiting on permission to create a cluster? You do not have to wait to start. A run on your own machine reports itself to your organization and appears in the console, so you can get going and connect a cluster when you are ready.

{{< subpage-cards >}}
