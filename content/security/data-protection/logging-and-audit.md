---
title: Logging and audit
weight: 1
variants: -flyte +union
---

# Logging and audit

## Task logging

Logs are collected by Fluent Bit (deployed as a DaemonSet on the data plane) and shipped to the customer's cloud-native log service: CloudWatch Logs (AWS), Cloud Logging (GCP), or Azure Monitor (Azure). Live logs are streamed directly from the Kubernetes API while a task is running. Persisted logs are read from the cloud log aggregator after a pod terminates.

Log data is not persisted in the control plane. It is streamed as a stateless pass-through relay, encrypted in transit on both network hops (client-to-CP and DP-to-CP), and exists as plaintext in control plane memory only during each streaming request. Persisted logs (fetched from CloudWatch, Stackdriver, or Azure Monitor for completed executions) also transit the control plane via the same streaming proxy path. There is no content filtering or redaction at any layer of the log pipeline. Any sensitive data (secrets, PII, stack traces) that user code writes to stdout/stderr flows through control plane memory unmodified. Log lines include structured metadata: timestamp, message content, and originator classification. For details on how log data flows through the system, see [Two-plane separation](../architecture/two-plane-separation).

## Observability metrics

A per-cluster instance (Prometheus and/or ClickHouse) stores time-series observability metrics including resource utilization and cost data. Queries are proxied through the DataProxy service to the customer's instance. Metrics data never leaves the customer's infrastructure. In BYOC deployments, Union.ai deploys and manages the monitoring stack.

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

3. Open the Union UI task logs panel and use browser developer tools (Network tab) to verify that log data comes through the tunnel.

4. Confirm Fluent Bit is running on every node:

   ```bash
   kubectl get ds -n union | grep fluent
   ```

Self-service verification using existing features.

### Audit trail

**Reviewer focus:** Confirm that all operations are logged with identity, operation, and timestamp, and that the audit trail is complete and queryable.

**How to verify:**

Ideal: a unified audit command that captures all operations:

```bash
union security audit --window 1h --output audit-report.json
```

Available today using existing tools:

- `uctl get execution --all -o json` filtered by time
- IdP audit log (Okta) for authentication events
- Kubernetes audit log on the data plane for cluster operations
- CloudTrail for IAM activity

A unified audit command aggregating control plane API logs, Kubernetes audit logs, and cloud audit trails would be a high-value addition.
