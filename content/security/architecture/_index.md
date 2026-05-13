---
title: Architecture
weight: 1
variants: -flyte +union
sidebar_expanded: true
---

# Architecture

Union.ai's security architecture rests on a foundational division between the Union.ai-hosted control plane, which orchestrates execution, and the customer-hosted data plane, where all computation occurs and all customer data resides. The two planes are connected by an outbound-only route that requires no inbound firewall rules on the customer side.

In the BYOC model, Union.ai manages the data plane over a private connection. In the self-managed model, the customer manages the data plane themselves. In both cases, the same security controls apply, and the same [data residency guarantees](../data-protection/classification-and-residency) hold.

This section covers:

* **[Two-plane separation](./two-plane-separation)**: The division between between the Union.ai-hosted control plane and the customer-hosted data plane is the foundation of the security architecture.

* **[Control plane](./control-plane)**: The control plane is the Union.ai-hosted orchestration component. It stores only orchestration and task metadata, which is encrypted at rest. Bulk data is referenced via signed URIs only, the actual bulk data never touches the control plane.

* **[Data plane](./data-plane)**: The data plane runs entirely within the customer's cloud account. All computation occurs here and all customer data resides here. It uses workload identity federation (IRSA / Workload Identity / Azure Workload Identity) instead of static credentials, so no long-lived access keys are stored on the data plane.

* **[Network architecture](./network)**: The data plane initiates all connections to the control plane via two outbound-only routes. There is no inbound attack surface on the customer's network and therefore no firewall rules are required.

* **[Private connectivity (BYOC)](./private-connectivity)**: In the BYOC model, Union.ai manages the customer's Kubernetes cluster via PrivateLink, Private Service Connect, or Azure Private Link. The Kubernetes API is never exposed to the public internet.

* **[Deployment models](./deployment-models)**: Self-managed and BYOC share the same two-plane architecture and security controls, differing only in who operates the data plane's Kubernetes cluster.
