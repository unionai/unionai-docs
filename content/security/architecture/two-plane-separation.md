---
title: Two-plane separation
weight: 1
variants: -flyte +union
---

# Two-plane separation

Union.ai's architecture is divided into two distinct planes: a **control plane** hosted by Union.ai on AWS, and a **data plane** that runs on the customer's own Kubernetes cluster within their cloud account.

## Control plane

The control plane handles workflow orchestration, user management, and the web interface. It stores only the metadata required for these functions; bulk customer data payloads are stored as URI references rather than inline. See [Control plane](./control-plane) for components and infrastructure.

> **No customer data, metadata, code, or logs ever touch Union.ai's control plane. Not in flight. Not at rest. Not ever.**

## Data plane

The data plane is where all computation and data handling occurs. It runs entirely within the customer's cloud account, on infrastructure the customer controls (or, in the BYOC model, infrastructure that Union.ai manages on the customer's behalf within the customer's account). It is protected by the customer's IAM policies. See [Data plane](./data-plane) for components, Kubernetes security, and IAM.

## Blast radius

This separation limits the blast radius of a control plane security incident. A compromised control plane would expose only metadata: task definitions, run IDs, schedules, phase transitions, error messages, and the RBAC graph. It could not expose customer data of any kind -- workflow inputs and outputs, code bundles, log streams, secrets, and auxiliary UI traffic are all served directly from the data plane through the Direct-to-DataPlane tunnel and never enter the control plane in any form.

For the full classification of what data lives in each plane and how each pathway is protected, see [Data classification and residency](../data-protection/classification-and-residency). For network paths between the planes, see [Network architecture](./network).

