---
title: Subscribe and sign up
description: "Create your organization and choose how you pay: on AWS Marketplace or directly. Billing is separate from where your data plane runs."
icon: rocket-takeoff
weight: 1
variants: -flyte +union
---

# Subscribe and sign up

Every Union.ai deployment starts here. You create your organization in the Union.ai UI and try out a local workflow that you follow in the UI. When you are ready, you provision your cloud resources and connect your cluster. You don't have to wait on Union.ai to set anything up.

**How you pay is separate from where your data plane runs.** A subscription is a billing relationship, not infrastructure: you can subscribe on AWS Marketplace and run your data plane on GCP or Azure.

- **On AWS Marketplace.** Buy **Union Team** on AWS Marketplace, so the charges appear on your AWS bill. Start at [AWS Marketplace](./aws-marketplace), which hands you on to sign-up.
- **Directly.** Start at [Create your account and organization](./create-organization). There is no GCP or Azure Marketplace listing yet.

Either way, a new organization starts with a 30-day free trial. The trial covers Union.ai's charges, not your cloud provider's: the resources your data plane runs on are billed to your own cloud account during the trial too. See [What it costs](../selfmanaged/whats-installed#what-it-costs).

**You can try it before you set up a cluster.** Once your organization exists, a workflow you run on your own machine reports to it and appears in the Union.ai UI. That is enough to see how Union.ai works before you create any cloud resources.

## The path

1. **Subscribe**, if you pay on AWS Marketplace: [subscribe on AWS Marketplace](./aws-marketplace), then follow the handoff to Union.ai.
2. **[Create your account and organization](./create-organization).** Your organization is your team's workspace: it groups your team members, projects, tasks, apps and so on.
3. **[Run your first workflow locally](./run-locally).** Run a workflow on your own machine and follow it in the Union.ai UI, with no cluster. Optional, but the quickest way to see Union.ai working.

Then set up your [self-managed deployment](../selfmanaged/_index): provision your cloud resources on [AWS](../selfmanaged/aws/_index), [GCP](../selfmanaged/gcp/_index), or [Azure](../selfmanaged/azure/_index), and [connect your cluster](../selfmanaged/connect-a-cluster).

{{< subpage-cards >}}
