---
title: Logging and audit
weight: 7
variants: -flyte +union
---

# Logging and audit

## Task logging

Logs are collected and shipped to the customer's cloud-native log service: CloudWatch Logs (AWS), Cloud Logging (GCP), or Azure Monitor (Azure). Live logs are streamed directly from the Kubernetes API while a task is running. Persisted logs are read from the cloud log aggregator after a pod terminates.

Log data does not transit the control plane. Live and persisted logs alike are served from the data plane through the Direct-to-Data-Plane tunnel directly to the requesting client; no log byte ever passes through Union.ai infrastructure. There is no content filtering or redaction at any layer of the log pipeline. Log lines include structured metadata: timestamp, message content, and originator classification.

## Observability metrics

A per-cluster monitoring instance stores time-series observability metrics including resource utilization and cost data. Queries are served from the data plane through the Direct-to-Data-Plane tunnel. Metrics data never leaves the customer's infrastructure. In BYOC deployments, Union.ai deploys and manages the monitoring stack.

## Audit trail

Every API request is authenticated with the identity context captured. Run and action lifecycle events are recorded with timestamps, phases, and responsible identities. RBAC changes and user management operations are logged. Secret creation and management operations are tracked, though values are never logged. Cluster state changes and tunnel health events are recorded. Error information is preserved per attempt, enabling forensic analysis of failures.

## Verification

### Task logging

**Reviewer focus:** Confirm that task logs are stored in the customer's cloud log service and that the control plane does not persist log data.

**How to verify:**

1. Run a task that writes known log output.

2. Find the log in the customer's cloud log service:

   ```bash
   aws logs get-log-events --log-group <group> --log-stream <stream>
   ```

3. Open the Union.ai UI task logs panel and use browser developer tools (Network tab) to verify that log data comes through the tunnel.

4. Confirm Fluent Bit is running on every node:

   ```bash
   kubectl get ds -n union | grep fluent
   ```

This verification is fully self-service.

### Audit trail

**Reviewer focus:** Confirm that all operations are logged with identity, operation, and timestamp, and that the audit trail is complete and queryable.

**How to verify:**

Audit data is available from the following sources:

- Control plane execution and lifecycle events: `uctl get execution --all -o json`, filtered by time window.
- Authentication events: the configured identity provider's audit log (e.g., Okta).
- Cluster operations: the Kubernetes audit log on the data plane.
- Cloud IAM activity: CloudTrail (AWS), Cloud Audit Logs (GCP), or Azure Monitor activity logs.
