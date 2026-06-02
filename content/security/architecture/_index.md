---
title: Architecture
weight: 1
variants: -flyte +union
sidebar_expanded: true
---

# Architecture

Union.ai's security architecture rests on a foundational division between the Union.ai-hosted control plane, which orchestrates execution, and the customer-hosted data plane, where all computation occurs and all customer data resides. The data plane initiates all communication with the control plane over an outbound-only channel, requiring no inbound firewall rules on the customer side.

In the BYOC model, Union.ai manages the data plane over a private connection. In the self-managed model, the customer manages the data plane themselves. In both cases, the same security controls apply, and the same [data residency guarantees](../data-protection/classification-and-residency) hold.

This section covers:

* **[Two-plane separation](./two-plane-separation)**: The division between the Union.ai-hosted control plane and the customer-hosted data plane is the foundation of the security architecture.

* **[Control plane](./control-plane)**: The control plane is the Union.ai-hosted orchestration component. It stores only orchestration metadata (run IDs, schedules, phase transitions, task definitions, error messages, and the RBAC graph), encrypted at rest. Bulk data is referenced via signed URIs only; the actual bulk data never touches the control plane.

* **[Data plane](./data-plane)**: The data plane runs entirely within the customer's cloud account. All computation occurs here and all customer data resides here. It uses workload identity federation (IRSA / Workload Identity / Azure Workload Identity) instead of static credentials, so no long-lived access keys are stored on the data plane.

* **[Network architecture](./network)**: The data plane initiates all communication with Union.ai over an outbound-only direct gRPC connection. Customer-data requests flow client-to-data-plane through the Direct-to-DataPlane tunnel, terminating at an Envoy router inside the customer's cluster. There is no inbound attack surface on the customer's external network and therefore no firewall rules are required at the perimeter.

* **[Sovereign Data Plane](./sovereign-data-plane)**: An Enterprise-tier option that replaces the Direct-to-DataPlane tunnel with a customer-managed load balancer inside the customer's VPC, reachable only from the corporate VPN. No third-party network can reach the data plane; Union.ai employees cannot reach customer data even with full Union.ai credentials.

* **[Private connectivity (BYOC)](./private-connectivity)**: In the BYOC model, Union.ai manages the customer's Kubernetes cluster via PrivateLink, Private Service Connect, or Azure Private Link. The Kubernetes API is never exposed to the public internet.
