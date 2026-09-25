---
title: Self-serve setup
description: "The fastest way to deploy Union.ai: subscribe to Union Team on AWS Marketplace, create your organization, and connect your cluster, all from the Union.ai UI."
icon: rocket-takeoff
weight: 1
variants: -flyte +union
---

# Self-serve setup

This is the fastest way to deploy Union.ai, and it starts with a 30-day free trial. You subscribe to **Union Team** on AWS Marketplace, create your organization in the Union.ai UI, and try out a local workflow that you follow in the UI. When you are ready, you create the AWS resources the data plane runs on and connect your cluster, and the data plane is installed for you. You don't have to wait on Union.ai to set anything up.

The result is a [self-managed deployment](../selfmanaged/_index): the data plane runs in your cluster, and you own the cluster and its upgrades. Self-serve setup is currently available on AWS. Google Cloud and Azure are coming soon.

**You can try it before you set up a cluster.** Once your organization exists, a workflow you run on your own machine reports to it and appears in the Union.ai UI. That is enough to see how Union.ai works before you create any AWS resources.

**Nothing dials in.** You never open a port, expose an endpoint, or hand over cluster credentials. The agent you install connects outwards.

## The path

1. **[Start from AWS Marketplace](./aws-marketplace).** Subscribe to the [Union Team listing](https://aws.amazon.com/marketplace/pp/prodview-66k3cmidsgv5o) on AWS Marketplace, so the charges appear on your AWS bill, then follow the handoff to Union.ai.
2. **[Sign up for Union.ai](./sign-up).** Your organization is your team's workspace: it groups your team members, projects, tasks, apps and so on.
3. **[Run your first workflow locally](./run-locally).** Run a workflow on your own machine and follow it in the Union.ai UI, with no cluster. Optional, but the quickest way to see Union.ai working.
4. **[Provision your AWS resources](./aws-infrastructure).** Create the EKS cluster, S3 bucket, ECR repository and IAM roles your data plane runs on, in your AWS account.
5. **[Connect your cluster](./connect-a-cluster).** Give Union.ai a Kubernetes cluster to run your workloads on, and it installs the data plane into it.

{{< subpage-cards >}}
