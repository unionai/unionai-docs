---
title: Architecture
weight: 1
variants: -flyte +union
sidebar_expanded: true
---

# Architecture

Union.ai's security is built on a foundational architectural principle: strict separation between the Union.ai-hosted control plane and the customer-hosted data plane. This separation ensures that all customer data remains within the customer's own cloud infrastructure while the control plane handles only orchestration metadata.

The network architecture reinforces this separation with an outbound-only connectivity model that eliminates the need for inbound firewall rules on the customer's network.

This section covers:

* [Two-plane separation](./two-plane-separation): The foundational security architecture.
* [Control plane](./control-plane): What the control plane stores, its infrastructure, and its components.
* [Data plane](./data-plane): Components, Kubernetes security, container security, IAM, and Apps & Serving.
* [Network architecture](./network): Outbound-only model, Cloudflare Tunnel, regional endpoints, and communication paths.
* [Private connectivity (BYOC)](./private-connectivity): PrivateLink and Private Service Connect for BYOC cluster management.
* [Deployment models](./deployment-models): Self-managed vs BYOC differences, availability, and resilience.
