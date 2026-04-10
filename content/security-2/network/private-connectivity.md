---
title: Private connectivity (BYOC)
weight: 3
variants: -flyte +union
---

# Private connectivity (BYOC)

In BYOC deployments, Union.ai maintains a **private management connection** to the customer's Kubernetes cluster in addition to the Cloudflare Tunnel. This connection uses cloud-native private connectivity:

| Cloud Provider | Technology |
| --- | --- |
| AWS | AWS PrivateLink |
| GCP | GCP Private Service Connect |
| Azure | Azure Private Link |

## Purpose

This connection is used exclusively for cluster management operations:

* Cluster upgrades
* Node pool provisioning
* Helm chart updates
* Health monitoring and troubleshooting

It does **not** carry customer data. The Kubernetes API endpoint is never exposed to the public Internet.

## Additional communication path

BYOC has an additional communication path not present in self-managed deployments:

| Communication Path | Protocol | Encryption |
| --- | --- | --- |
| Union.ai -> Customer K8s API | PrivateLink / PSC | TLS (private connectivity) |

This architecture satisfies ISO 27001 and CIS controls for restricting administrative access. See [Standards compliance](../compliance/standards-compliance).

## Self-managed comparison

In self-managed deployments, this private management connection does not exist. The Cloudflare Tunnel is the only connection between the control plane and data plane.
