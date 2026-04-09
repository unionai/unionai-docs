---
title: Logging, monitoring, and audit
weight: 6
variants: -flyte +union
---

# Logging, monitoring, and audit

## Task logging

Logs are collected by `fluentbit` (deployed as a `DaemonSet` on the data plane) and shipped to the customer’s cloud-native log service:

| Cloud Provider | Log Service | Integration |
| --- | --- | --- |
| AWS | CloudWatch Logs | Fluent Bit → CloudWatch |
| GCP | Cloud Logging (Stackdriver) | Fluent Bit → Cloud Logging |
| Azure | Azure Monitor / Log Analytics | Fluent Bit → Azure Monitor |

The data plane log provider serves logs from two sources: live logs streamed directly from the Kubernetes API while a task is running, and persisted logs read from the cloud log aggregator after a pod terminates.
Log data is never stored in the control plane—it is streamed from the customer’s data plane through the Cloudflare tunnel and relayed to the client as a stateless pass-through.

## Observability metrics

A per-cluster instance (Prometheus and/or ClickHouse) stores time-series observability metrics including resource utilization and cost data.
Queries are proxied through the DataProxy service to the customer’s instance.
Metrics data never leaves the customer’s infrastructure. In BYOC deployments, Union.ai [deploys and manages the monitoring stack](./byoc-differences#infrastructure-management).

## Audit trail

Union.ai maintains comprehensive audit capabilities:

* Every API request is authenticated, and the identity context is captured
* Run and action lifecycle events are recorded with timestamps, phases, and responsible identities
* RBAC changes and user management operations are logged
* Secret creation and management operations are tracked (values are never logged)
* Cluster state changes and tunnel health events are recorded
* Error information is preserved per attempt, enabling forensic analysis of failures

## Incident response

Union.ai maintains documented incident response procedures aligned with SOC 2 Type II requirements.
These include defined escalation paths, communication protocols, containment procedures, and post-incident review processes.
The control plane’s stateless handling of customer data limits the potential impact of any control plane incident.
