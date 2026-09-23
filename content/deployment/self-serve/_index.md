---
title: Self-serve setup
description: "The fastest way to deploy Union.ai: subscribe to Union.ai Teams on AWS Marketplace, create your organization, and connect your cluster, all from the Union.ai UI."
icon: rocket-takeoff
weight: 1
variants: -flyte +union
---

# Self-serve setup

This is the fastest way to deploy Union.ai, and it starts with a 30-day free trial. You subscribe to **Union.ai Teams** on AWS Marketplace, create your organization in the Union.ai UI, try out a local workflow (but visible through Union.ai), create the AWS resources the data plane runs on, and connect your cluster. You don't install the data plane manually or wait on Union.ai to set it up for you.

The result is a [self-managed deployment](../selfmanaged/_index): the data plane runs in your cluster, and you own the cluster and its upgrades. Self-serve setup is currently available on AWS. It is coming soon for GCP and Azure.

**You can try it before you set up a cluster.** Once your organization exists, a workflow you run on your own machine reports to it and appears in the Union.ai UI. That is enough to see how Union.ai works before you create any AWS resources.

**Nothing dials in.** You never open a port, expose an endpoint, or hand over cluster credentials. The agent you install connects outwards.

## The path

1. **[Start from AWS Marketplace](./from-aws-marketplace).** Subscribe to the [Union.ai Teams listing](https://aws.amazon.com/marketplace/pp/prodview-66k3cmidsgv5o) on AWS Marketplace, so the charges appear on your AWS bill, then follow the handoff to Union.ai.
2. **[Sign up and create your Union.ai organization](./sign-up).** Your organization is your team's workspace: it groups your team members, projects, tasks, apps and so on. Run a workflow on your own machine and see it in the console straight away, with no cluster.
3. **[Provision your AWS resources](./aws-infrastructure).** Create the EKS cluster, S3 bucket, ECR repository and IAM roles your data plane runs on, in your AWS account.
4. **[Connect your cluster](./connect-a-cluster).** Give Union.ai a Kubernetes cluster to run your workloads on, and it installs the data plane into it.

{{< subpage-cards >}}
