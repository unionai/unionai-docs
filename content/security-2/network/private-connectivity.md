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

## Standards compliance

This private connectivity architecture satisfies:

* **ISO 27001 A.5.15** -- access control: restricts access to network services and management interfaces
* **CIS v8 4.4** -- restrict administrative access: administrative interfaces not exposed to Internet
* **CIS v8 12.11** -- segment administration interfaces: separation of administrative interfaces from public access

## Self-managed comparison

In self-managed deployments, this private management connection does not exist. Union.ai has zero access to the customer's data plane infrastructure -- the Cloudflare Tunnel is the only connection between the control plane and data plane.
