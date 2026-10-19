---
title: Set up from the Union.ai UI
description: "The fastest way to deploy Union.ai: create your organization, provision your cloud resources, and connect your cluster, all from the Union.ai UI."
icon: rocket-takeoff
weight: 1
variants: -flyte +union
---

# Set up from the Union.ai UI

This is the fastest way to deploy Union.ai. You create your organization in the Union.ai UI and try out a local workflow that you follow in the UI. When you are ready, you create the cloud resources the data plane runs on and connect your cluster, and the data plane is installed for you. You don't have to wait on Union.ai to set anything up.

The result is a [self-managed deployment](../selfmanaged/_index): the data plane runs in your cluster, and you own the cluster and its upgrades. Your cluster can run on AWS, GCP, or Azure.

How you subscribe depends on where your data plane runs:

- **AWS: subscribe on AWS Marketplace.** Buy **Union Team** on AWS Marketplace, so the charges appear on your AWS bill. New subscriptions start with a 30-day free trial. Start at [AWS Marketplace](./aws-marketplace).
- **GCP or Azure: subscribe through Union.ai.** There is no GCP or Azure marketplace listing yet, so contact Union.ai for a subscription. Then start at [Sign up for Union.ai](./sign-up).

**You can try it before you set up a cluster.** Once your organization exists, a workflow you run on your own machine reports to it and appears in the Union.ai UI. That is enough to see how Union.ai works before you create any cloud resources.

**Nothing dials in.** You never open a port, expose an endpoint, or hand over cluster credentials. The agent you install connects outwards.

## The path

1. **Subscribe.** On AWS, [subscribe on AWS Marketplace](./aws-marketplace), so the charges appear on your AWS bill, then follow the handoff to Union.ai. On GCP or Azure, contact Union.ai for a subscription.
2. **[Sign up for Union.ai](./sign-up).** Your organization is your team's workspace: it groups your team members, projects, tasks, apps and so on.
3. **[Run your first workflow locally](./run-locally).** Run a workflow on your own machine and follow it in the Union.ai UI, with no cluster. Optional, but the quickest way to see Union.ai working.
4. **Provision your cloud resources on [AWS](./aws-infrastructure), [GCP](./gcp-infrastructure), or [Azure](./azure-infrastructure).** Create the Kubernetes cluster, object store, image registry, and identities your data plane runs on, in your own cloud account. Optional if you already have resources that meet the requirements.
5. **[Connect your cluster](./connect-a-cluster).** Give Union.ai a Kubernetes cluster to run your workloads on, and it installs the data plane into it.

{{< subpage-cards >}}
