---
title: Logging, monitoring, and audit
weight: 7
variants: -flyte +byoc +selfmanaged
---

# Logging, monitoring, and audit

## Task logging

Logs are collected by Fluentbit (deployed as a DaemonSet on the data plane) and shipped to the customer’s cloud-native log service:

| Cloud Provider | Log Service | Integration |
| --- | --- | --- |
| AWS | CloudWatch Logs | Fluentbit → CloudWatch |
| GCP | Cloud Logging (Stackdriver) | Fluentbit → Cloud Logging |
| Azure | Azure Monitor / Log Analytics | Fluentbit → Azure Monitor |

The data plane log provider serves logs from two sources: live logs streamed directly from the Kubernetes API while a task is running, and persisted logs read from the cloud log aggregator after a pod terminates.
Log data is never stored in the control plane—it is streamed from the customer’s data plane through the Cloudflare tunnel and relayed to the client as a stateless pass-through.

## Observability metrics

A per-cluster ClickHouse instance stores time-series observability metrics including resource utilization and cost data.
Queries are proxied through the DataProxy service to the customer’s ClickHouse instance.
Metrics data never leaves the customer’s infrastructure.

## Audit trail

Union.ai maintains comprehensive audit capabilities:

* Every API request is authenticated and the identity context is captured
* Run and action lifecycle events are recorded with timestamps, phases, and responsible identities
* RBAC changes and user management operations are logged
* Secret creation and management operations are tracked (values are never logged)
* Cluster state changes and tunnel health events are recorded
* Error information is preserved per attempt, enabling forensic analysis of failures

## Incident response

Union.ai maintains documented incident response procedures aligned with SOC 2 Type II requirements.
These include defined escalation paths, communication protocols, containment procedures, and post-incident review processes.
The control plane’s stateless handling of customer data limits the potential impact of any control plane incident.
