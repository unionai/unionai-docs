---
title: AWS Marketplace
description: Subscribe to Union through AWS Marketplace and associate the subscription with your organization, so the charges appear on your AWS bill.
icon: cart
weight: 1
variants: -flyte +union
---

# AWS Marketplace

You can subscribe to Union.ai through AWS Marketplace, so the charges appear on your AWS bill alongside everything else you buy there. New subscriptions start with a 30-day free trial; see the [listing](https://aws.amazon.com/marketplace/pp/prodview-66k3cmidsgv5o) for the current terms.

This page covers the purchase itself, and the handoff to Union.ai that follows it. Buying a subscription sets up the billing relationship. It does not create your Union.ai account, so once you have subscribed you carry on to [Sign up and create your Union.ai organization](./sign-up).

## What you'll need

An AWS account that is allowed to subscribe on AWS Marketplace. Many organizations restrict this to a billing or procurement account.

You don't need a cluster or any other AWS resources yet. You create those later, in [Provision your AWS resources](./aws-infrastructure).

## 1. Subscribe on AWS Marketplace

Open the [Union Team listing](https://aws.amazon.com/marketplace/pp/prodview-66k3cmidsgv5o) on AWS Marketplace and subscribe with the AWS account you want the charges to appear on.

> [!NOTE] Choose Union Team, not Union Enterprise
> If you search for Union.ai under **Discover products** in AWS Marketplace instead of following the link above, you see two listings: **Union Team** and **Union Enterprise**. Self-serve setup is Union Team. Union Enterprise is a separate offering.

The account you buy from doesn't have to be the one Union.ai runs in. You can run the data plane in the same AWS account or in a different one.

## 2. Continue to Union.ai

Once you make the purchase, click **Set up your account** to be taken to the the Union.ai sign-up page.

> [!NOTE] One subscription, one organization
> A marketplace subscription can only be associated with a single Union.ai organization. If you try to associate the same subscription with a second organization, Union.ai refuses rather than splitting your entitlement across two workspaces.

## Next steps

The next steps are:

1. **[Sign up and create your Union.ai organization](./sign-up).** Name your organization and choose a region.
2. **[Run your first workflow locally](./run-locally).** Optional: see Union.ai working before you set up a cluster.
3. **[Provision your AWS resources](./aws-infrastructure).** Create the EKS cluster, S3 bucket, ECR repository and IAM roles your data plane runs on.
4. **[Connect your cluster](./connect-a-cluster).** Enter the details of the resources you created, and Union.ai installs the data plane on them.
