---
title: Deploy the gateway
description: Place the Inference Gateway on a cluster, size it for your request rate, and choose who can reach it.
icon: rocket-takeoff
weight: 1
variants: -flyte +union
---

# Deploy the gateway

Deploy a gateway on the cluster where your LLM traffic originates. It runs as a Union app in your data plane, and every task, app, and laptop then calls its endpoint.

## Deploy from the console

1. Open **Settings → Inference Gateway** in the Union console and start a new gateway.
2. Fill in the gateway:

   | Field | Meaning |
   |---|---|
   | **Name** | Lowercase letters, digits, and dashes, for example `llm-gateway`. It also names the gateway's app and subdomain. |
   | **Cluster pool** | Where the gateway runs. |
   | **Cluster (optional)** | Pins the gateway to one named cluster, for organizations with several clusters. |
   | **Allow anonymous access** | Whether callers need Union sign-in. See [Choose who can reach the gateway](#choose-who-can-reach-the-gateway). |
   | **Providers** | Optional. Providers you add here are mounted on the first deploy. See [Providers](./providers). |

3. Deploy the gateway.

You can't change the placement after the gateway is created.

The console shows the gateway's endpoint when it is running. Callers use this URL, with `/v1` appended, as the base URL of any OpenAI-compatible client.

Self-hosted models and guardrail apps must run on the same cluster as the gateway, because the gateway reaches them over cluster-local addresses. Pick the placement with that in mind.

## Size the gateway

You size the gateway in requests per second, not replicas. Edit the gateway to set:

| Setting | Meaning | Default |
|---|---|---|
| **Min requests/sec** | Capacity that is always running. | 1,000 |
| **Max requests/sec** | The ceiling the gateway scales out to under load. Up to 10,000. | The minimum |

Union runs one replica per 1,000 rps and autoscales between the two bounds on the observed request rate. Redeploying without changing these values keeps the current sizing.

Each replica gets its share of a key's budget from the control plane, which never grants more in total than the key's budget. Two consequences follow:

- Running more than one replica doesn't let a key spend more than its budget.
- A replica restart doesn't reset a key's spend for the current budget window. The share the replica held before the restart stays counted against the budget.

The spend history in the console is computed separately, from usage records.

## Choose who can reach the gateway

| Access mode | Who reaches the endpoint | Use it when |
|---|---|---|
| **Allow anonymous access** checked (default) | Anyone with the URL. The virtual key is the only credential. | Callers outside Union need a plain API-key style endpoint, for example a third-party SaaS tool. |
| **Allow anonymous access** unchecked | Only callers with a Union identity. They still present a virtual key. | You want the endpoint closed to the internet. Developers reach it from laptops with `flyte proxy app`. |

With anonymous access, a leaked virtual key can be used by anyone until you revoke it, up to that key's budget and allowed models. Keep budgets tight on keys that leave your organization. See [Use from your laptop](./use-from-laptop) for how each mode works from a developer machine.

Redeploying without changing the access mode keeps the current setting.

## Permissions

| Action | Required permission |
|---|---|
| View the gateway, providers, keys, and guardrails | View LLM gateway |
| Deploy the gateway, add providers, set guardrails | Manage LLM gateway |
| Create, read, and revoke virtual keys; view usage | Manage LLM gateway keys |

## How changes reach the gateway

Every change you make, such as a new key, a revoked key, a budget, a provider, or a guardrail, is part of the gateway's *policy*. The gateway keeps a watch open on the control plane, which checks for policy changes every 15 seconds, so a change reaches the gateway within about 15 seconds. The control plane never connects in to the gateway.

Adding a hosted provider changes what is mounted on the gateway, so the gateway redeploys automatically. If that redeploy fails, the provider shows **Pending deploy** until you deploy the gateway again.

Updating the gateway's proxy image needs a redeploy. The console shows when a newer image is available.
