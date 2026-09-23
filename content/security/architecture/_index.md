---
title: Architecture
description: How the Union-hosted control plane and the customer-hosted data plane divide the work, and what that division protects.
icon: diagram-2
weight: 1
variants: -flyte +union
sidebar_expanded: true
---

# Architecture

Union.ai's **Zero Trust security** architecture rests on a foundational division between the Union.ai-hosted control plane, which orchestrates execution, and the customer-hosted data plane, where all computation occurs and all customer data resides. Under this model nothing is trusted implicitly: the data plane initiates all communication with the control plane over an outbound-only channel, requiring no inbound firewall rules on the customer side, and every customer-data request is authenticated and authorized inside the customer's cluster.

In the BYOC model, Union.ai manages the data plane over a private connection. In the self-managed model, the customer manages the data plane themselves. In both cases, the same security controls apply, and the same [data residency guarantees](../data-protection/classification-and-residency) hold.

The control plane stores only orchestration metadata: run IDs, schedules, phase transitions, task
definitions, error messages, and the RBAC graph, all encrypted at rest. Bulk data is referenced by
signed URI only and never touches it. The data plane runs entirely in the customer's cloud account,
holds all computation and all customer data, and uses workload identity federation (IRSA, Workload
Identity, Azure Workload Identity) rather than static credentials, so no long-lived access keys are
stored there.

All communication runs outbound-only over direct gRPC. Customer-data requests reach the data plane
through the Direct-to-Data-Plane tunnel and terminate at an Envoy router inside the customer's
cluster, so there is no inbound attack surface and no perimeter firewall rules are required. Two
options change that path: the Enterprise-tier **Sovereign Data Plane** replaces the tunnel with a
customer-managed load balancer inside the customer's VPC, reachable only from the corporate network;
and in **BYOC**, Union.ai manages the cluster over PrivateLink, Private Service Connect, or Azure
Private Link, so the Kubernetes API is never exposed to the public internet.

{{< subpage-cards >}}
