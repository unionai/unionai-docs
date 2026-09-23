---
title: Self-service setup
description: "The fastest way to deploy Union.ai: subscribe to Union.ai Teams on AWS Marketplace, create your organization, and connect your cluster, all from the Union.ai UI."
icon: rocket-takeoff
weight: 1
variants: -flyte +union
---

# Self-service setup

This is the fastest way to deploy Union.ai. You subscribe to **Union.ai Teams** on AWS Marketplace, create your organization in the Union.ai UI, connect a Kubernetes cluster of your own. You create the AWS resources the data plane runs on; everything after that happens from the Union.ai UI. You don't install the data plane by hand or wait on Union.ai to set it up for you.

The result is a [self-managed deployment](../selfmanaged/_index): the data plane runs in your cluster, and you own the cluster and its upgrades. Self-service setup is currently available on AWS.

**Nothing dials in.** You never open a port, expose an endpoint, or hand over cluster credentials. The agent you install connects outwards.

## The path

1. **[Start from AWS Marketplace](./from-aws-marketplace).** Subscribe through AWS Marketplace, so the charges appear on your AWS bill, then follow the handoff to Union.ai. Skip this step if you are not buying through AWS Marketplace.
2. **[Sign up and create your Union.ai organization](./sign-up).** Your organization is your workspace: it holds your projects, tasks, apps and so on. Once it exists you can confirm by running a workflow on your local machine and see it in in the Union UI (straight away, with no cluster).
3. **[Provision your AWS resources](./aws-infrastructure).** Create the EKS cluster, S3 bucket, ECR repository and IAM roles your data plane runs on, in your AWS account.
4. **[Connect your cluster](./connect-a-cluster).** Give Union.ai a Kubernetes cluster to run your workloads on, and it installs the data plane into it.

You do not need a cluster to start. A run on your own machine reports itself to your organization and appears in the console, which is enough to see how Union.ai works before committing infrastructure to it.

{{< subpage-cards >}}
