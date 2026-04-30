---
title: Two-plane separation
weight: 1
variants: -flyte +union
---

# Two-plane separation

Union.ai's architecture is divided into two distinct planes: a **control plane** hosted by Union.ai on AWS, and a **data plane** that runs on the customer's own Kubernetes cluster within their cloud account.

## Control plane

The control plane handles workflow orchestration, user management, and the web interface. It stores only the metadata required for these functions; bulk customer data payloads are stored as URI references rather than inline. See [Control plane](./control-plane) for components and infrastructure.

## Data plane

The data plane is where all computation and data handling occurs. It runs entirely within the customer's cloud account, on infrastructure the customer controls (or, in the BYOC model, infrastructure that Union.ai manages on the customer's behalf within the customer's account). It is protected by the customer's IAM policies. See [Data plane](./data-plane) for components, Kubernetes security, and IAM.

## Blast radius

This separation limits the blast radius of a control plane security incident. A compromised control plane would only expose what is stored or proxied through it: task metadata in its databases, inline data transiting memory during active requests, and log stream content. It could not expose bulk customer data, which is signed and accessed directly on the data plane.

For the full classification of what data lives in each plane, what transits control plane memory, and how each pathway is protected, see [Data classification and residency](../data-protection/classification-and-residency). For network paths between the planes, see [Network architecture](./network).

