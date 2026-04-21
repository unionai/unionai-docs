---
title: Architecture
weight: 1
variants: -flyte +union
sidebar_expanded: true
---

# Architecture

Union.ai's security is built on a foundational architectural principle: strict separation between the Union.ai-hosted control plane and the customer-hosted data plane. This separation ensures that all customer data remains within the customer's own cloud infrastructure while the control plane handles only orchestration metadata.

> [!WARNING]
> **Audit finding (ref #3, #4, #5, #7):** The claim that "all customer data remains within the customer's own cloud infrastructure" and that the control plane handles "only orchestration metadata" needs qualification. The audit found that structured task inputs/outputs (up to 10 MB per submission, 20 MiB per retrieval), secret values during Create/Update operations, and execution log streams all transit control plane memory transiently. Additionally, task definition closures stored in the control plane database contain environment variables, default input values, SQL statements, and K8s pod specs -- which go beyond pure orchestration metadata.

The network architecture reinforces this separation with an outbound-only connectivity model that eliminates the need for inbound firewall rules on the customer's network.

This section covers:

* [Two-plane separation](./two-plane-separation): The foundational security architecture.
* [Control plane](./control-plane): What the control plane stores, its infrastructure, and its components.
* [Data plane](./data-plane): Components, Kubernetes security, container security, IAM, and Apps & Serving.
* [Network architecture](./network): Outbound-only model, Cloudflare Tunnel, regional endpoints, and communication paths.
* [Private connectivity (BYOC)](./private-connectivity): PrivateLink and Private Service Connect for BYOC cluster management.
* [Deployment models](./deployment-models): Self-managed vs BYOC differences, availability, and resilience.
