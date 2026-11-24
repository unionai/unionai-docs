---
title: Product tiers
description: Compare the Team and Enterprise plans for Union.ai, including pricing model, deployment options, limits, security, networking, and support.
icon: list-columns
weight: 1
variants: -flyte +union
---

# Product tiers

Union.ai has two plans, **Team** and **Enterprise**. Every self-service sign-up starts on Team.
To see your plan and what you've used against its limits, go to **Settings → Plan & usage**.

A feature is either in a plan or it isn't. There are no add-ons.
For rates per action, vCPU, memory, and GPU, see [Union.ai pricing](https://www.union.ai/pricing).

| | Team | Enterprise |
|---|---|---|
| **For** | Teams taking AI from experiment to production | Organizations running mission-critical AI, ML, and agents across teams, regions, and clouds |
| **Price** | $950 per month minimum, credited to usage | Annual commit, credited to usage |
| **Get started** | [Create your account and organization](./sign-up/create-organization). Your first $950 of usage is free, with no card required. | [Talk to sales](https://www.union.ai/get-a-quote) |

## Compare plans

In the tables below, ✓ means included and – means not included.

### Commercial

| Feature | Team | Enterprise |
|---|---|---|
| How you pay | $950 monthly minimum, charged on the 1st and issued back as a $950 usage credit. Unused credit expires at the end of the month. Renews automatically. | Annual commit, paid up front and fully credited. The rate card continues as overage after the commit is consumed. |
| Usage rates | The four published monthly ladders | One rate per meter (the bottom of each ladder), with no bands |
| Monthly action ceiling | None | None |
| Single-tenant control plane | – | ✓ |
| Guided Install (one-time) | Standard $5,000, Advanced from $15,000 | Standard $5,000, Advanced from $15,000 |

### Deployment

| Feature | Team | Enterprise |
|---|---|---|
| [Self-managed](./selfmanaged/_index): Union.ai runs the control plane, you run the data plane | ✓ | ✓ |
| [Union-managed (BYOC)](./byoc/_index): Union.ai runs the data plane in your cloud account | $500 per cluster per month | $500 per cluster per month, capped at $2,500 |
| Clouds | All regions, neoclouds, and hyperscalers | Any cloud |
| Marketplace commit drawdown | – | ✓ |

### Limits

| Feature | Team | Enterprise |
|---|---|---|
| Active clusters | 2 | Unlimited |
| Multi-region and multi-cloud on one control plane | – | ✓ |
| Concurrent actions | 10,000 | Custom |
| Fanout (actions per run) | 200,000 | Custom |
| Apps | ✓ | Custom |
| Named artifacts | Unlimited. Each version is billed as an action. | Unlimited. Each version is billed as an action. |
| Tracked runs | Unlimited. Each run is billed as an action. | Unlimited. Each run is billed as an action. |
| Retention | 30 days, with 90-day trends | Custom, contractual |
| Extended retention or deletion terms beyond 30 days | – | ✓ |

### Identity and security

| Feature | Team | Enterprise |
|---|---|---|
| Login | Federated login (Google and Microsoft) | Federated login (Google and Microsoft), SSO, SAML |
| HIPAA BAA | On request | On request |
| Zero-trust architecture | ✓ | ✓ |
| Managed secrets | ✓ | ✓ |
| Customer-owned secrets backend (Vault and similar) | – | ✓ |
| CMEK (customer-managed encryption keys) | – | ✓ |
| BYOK (bring your own key) | – | ✓ |

### Networking

| Feature | Team | Enterprise |
|---|---|---|
| Public endpoints | ✓ | ✓ |
| BYO-VPC | ✓ | ✓ |
| Private control-plane endpoint | – | ✓ |
| Proxy-only egress | – | ✓ |
| Private image mirror | – | ✓ |

### Platform

| Feature | Team | Enterprise |
|---|---|---|
| Pure-Python authoring | ✓ | ✓ |
| Reusable containers | ✓ | ✓ |
| Fast cold starts | ✓ | ✓ |
| Caching | ✓ | ✓ |
| Replay | ✓ | ✓ |
| Recover | ✓ | ✓ |
| Remote debugging | ✓ | ✓ |
| Remote image builds | ✓ | ✓ |
| Ray, Spark, and Dask plugins | ✓ | ✓ |
| Triggers | ✓ | ✓ |
| Queues | ✓ | ✓ |
| User management | ✓ | ✓ |
| Volumes | ✓ | ✓ |

### Enterprise only

| Feature | Team | Enterprise |
|---|---|---|
| Custom cloud configuration | – | ✓ |
| Custom RBAC and namespace topology | – | ✓ |

### Support

| Feature | Team | Enterprise |
|---|---|---|
| Support plan | Standard: 12×5, Sev 1 in 4 business hours | Premier: 24×7 for Sev 1 and Sev 2, Sev 1 in 1 hour, shared engineer |
| Mission Critical support | – | Paid upgrade. See [Union.ai support](https://www.union.ai/support). |
| Control-plane availability | 99.9% SLA | 99.9% SLA |

## Your first month

A new organization starts on Team with the $950 minimum waived.
If Union.ai runs your clusters, the $500 fee on your first cluster is also waived that month.
You don't need a payment method until the credit is used up or the month ends.

## Move to Enterprise

Talk to Union.ai when you scale past one team or past two clusters.
Also get in touch when security or procurement needs a private endpoint, CMEK, custom RBAC, retention beyond 30 days, or 24×7 support.
Select **Talk to us** in **Settings → Plan & usage**, or [contact sales](https://www.union.ai/get-a-quote).
