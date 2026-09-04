---
title: Start from AWS Marketplace
description: Subscribe to Union through AWS Marketplace and claim your subscription, so the charges appear on your AWS bill.
icon: cart
weight: 1
variants: -flyte +union
---

<!-- ⚠️ UNVERIFIED, AND NOT READY TO PUBLISH. DOC-1538, target 14 Sep (listing live), 1 Oct
     (announcement).

     Nobody has run the buyer journey. Neither Peeter nor this run has AWS Marketplace purchasing
     credentials, so every step below is written from the shipped source rather than from watching
     it happen:
       cloud origin/main:idl/signup/payload.proto           (MarketplaceCheckout, handoff_token)
       cloud origin/main:idl/signup/marketplace_service.proto (ClaimMarketplaceBuyer,
                                                              LinkContractToOrganization)
       cloud origin/main:.union/selfserve/provision_org_split_v2.py
                                                            (/fleet/marketplace/handoff/redeem)
     ENG26-1151 is running the journey from the test buyer account, timed and recorded. THAT
     RECORDING IS THE AUTHORITY. Reconcile this page against it before publishing, and expect the
     screen names and button labels to need correcting: none of them are asserted here, precisely
     because they have not been seen.

     TWO THINGS THIS PAGE DELIBERATELY DOES NOT SAY.
     1. It does not call the flow one-click, or count the steps as fewer than they are. The project's
        standing instruction is "Plan for B. Test for A. Announce whichever is real", and nobody
        describes this as one-click externally until Tier A is demonstrated in the test buyer
        account. The steps below are written as the discrete steps they are.
     2. It does not describe a CloudFormation stack or an AWS Quick Launch. DOC-1538's Tier A and
        Tier B both assume the buyer deploys a CFT into their own account. There is no
        CloudFormation anywhere in the signup or marketplace path on origin/main. If that is wrong,
        it is wrong in a way worth knowing before launch, so check it rather than quietly adding a
        stack step back.

     SCOPE: this page is the PURCHASE and the handoff, nothing else. It stops at the sign-up form
     and sends the reader to sign-up.md, which is where creating an organization and running
     something already live. It briefly did more than that and the intro was left claiming to cover
     "the steps between subscribing and running something", which it did not; Peeter caught it.
     If you add to this page, check the intro still describes what is actually below it.

     OPEN QUESTION, unresolved and NOT visible on the page: provisioning calls Omnistrate's
     /fleet/user to create a "consumption user". It is not clear whether that gives a marketplace
     buyer compute an ordinary self-serve signup does not get. Nothing here depends on the answer,
     because the page hands off before compute is discussed. But if marketplace buyers DO get
     managed compute, then sign-up.md and connect-a-cluster.md are the wrong onward path for them
     and this page should say so instead. Worth asking Ryan or Jeev. -->

# Start from AWS Marketplace

You can subscribe to {{< key product_name >}} through AWS Marketplace, so the charges appear on your AWS bill alongside everything else you buy there.

This page covers the purchase itself, and the handoff to {{< key product_name >}} that follows it. Buying a subscription sets up the billing relationship. It does not create the workspace you work in, so once you have subscribed you carry on to [Sign up and create your Union.ai organization](./sign-up), which is the same path everyone else follows.

If you already have a {{< key product_name >}} organization, you do not need this page.

## What you'll need

An AWS account that is allowed to subscribe on AWS Marketplace. Many organizations restrict this to a billing or procurement account.

You do not deploy anything into your own AWS account to buy a subscription, and you do not need a Kubernetes cluster.

## 1. Subscribe on AWS Marketplace

Find the {{< key product_name >}} listing on AWS Marketplace and subscribe with the AWS account you want the charges to appear on.

Your subscription is tied to the AWS account that buys it, so buy it from the account whose bill you want it on. Moving a subscription between AWS accounts later is an AWS-side change, not something you can do from {{< key product_name >}}.

## 2. Continue to {{< key product_name >}}

After the subscription is confirmed, AWS hands you off to {{< key product_name >}}.

Follow that handoff when you see it. It carries a short-lived token that ties your new organization to the subscription you just bought, and it expires, so if you leave it too long you may need to return to your AWS Marketplace subscriptions and start the handoff again.

> [!NOTE] One subscription, one organization
> A marketplace subscription can only be claimed by a single {{< key product_name >}} organization. If you try to claim the same subscription from a second organization, {{< key product_name >}} refuses rather than splitting your entitlement across two workspaces.

## Next steps

The handoff lands you on the {{< key product_name >}} sign-up form. From there your path is the same as anyone else's: continue with **[Sign up and create your Union.ai organization](./sign-up)**.
