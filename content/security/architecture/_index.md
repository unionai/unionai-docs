---
title: Architecture
weight: 1
variants: -flyte +union
sidebar_expanded: true
---

# Architecture

Union.ai's security is built on a foundational architectural principle: Separation between the Union.ai-hosted control plane and the customer-hosted data plane.

* Bulk customer data items such as files, directories, DataFrames, code bundles, container images, and inter-task artifacts are stored exclusively in the customer's infrastructure and never enter the control plane.

* Smaller inline data items such as structured task inputs/outputs, secret values during creation, and execution log streams transit control plane memory as plaintext but are not persisted there.

* The control plane databases store orchestration and task metadata, which may include fields such as environment variables and default input values. This information is encrypted at rest.

* The network architecture reinforces this separation with an outbound-only connectivity model that eliminates the need for inbound firewall rules on the customer's network.

The following table summarizes how these architectural decisions translate into concrete security benefits:

| Decision | Benefit |
| --- | --- |
| Bulk customer data never enters control plane | Minimizes blast radius of control plane compromise |
| Inline data passes through control plane memory only transiently | Not persisted, cached, or logged |
| Outbound-only connections | No inbound attack surface on customer network |
| Presigned URLs for data access | No persistent data access credentials |
| Write-only secrets API | Cannot exfiltrate secrets via API |
| Workload identity federation | No static credentials on data plane |
| Cloud-native encryption | Leverages provider-managed encryption |

This section covers:

* [Two-plane separation](./two-plane-separation): The foundational security architecture.
* [Control plane](./control-plane): What the control plane stores, its infrastructure, and its components.
* [Data plane](./data-plane): Components, Kubernetes security, container security, IAM, and Apps & Serving.
* [Network architecture](./network): Outbound-only model, Cloudflare Tunnel, regional endpoints, and communication paths.
* [Private connectivity (BYOC)](./private-connectivity): PrivateLink and Private Service Connect for BYOC cluster management.
* [Deployment models](./deployment-models): Self-managed vs BYOC differences, availability, and resilience.
