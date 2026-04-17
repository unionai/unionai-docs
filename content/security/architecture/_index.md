---
title: Security architecture
weight: 300
variants: -flyte +union
sidebar_expanded: true
---

# Security architecture

Union.ai's security is built on a foundational architectural principle: strict separation between the Union-hosted **control plane** and the customer-hosted **data plane**. This separation ensures that all customer data remains within the customer's own cloud infrastructure while the control plane handles only orchestration metadata.

This section covers:

* [Control plane and data plane separation](./control-plane-data-plane): What each plane stores, how they interact, and the security implications.
* [Network architecture overview](./network-architecture): The outbound-only connectivity model and communication paths between planes.
* [Data flow architecture](./data-flow-and-presigned-urls): How data moves through the system using presigned URLs and streaming relays.
* [Compute and control plane components](./components): Detailed architecture of each service component and its security properties.
* [Deployment models and BYOC differences](./deployment-models): How Self-Managed and BYOC deployments differ in terms of access, management, and responsibility.
