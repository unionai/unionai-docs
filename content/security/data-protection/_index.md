---
title: Data protection
weight: 2
variants: -flyte +union
sidebar_expanded: true
---

# Data protection

Union.ai protects customer data through a classification framework, residency guarantees, and cloud-native encryption. All customer data is encrypted both at rest and in transit.

The platform uses three data access patterns:

- **Presigned URLs** for bulk data (files, DataFrames, code bundles), which bypass the control plane entirely.
- **Inline proxy** for structured task I/O and secret values, which transits control plane memory encrypted in transit, exists as plaintext in memory only during request handling, and is not persisted.
- **Streaming relays** for logs and metrics, which transit control plane memory and are not persisted.

This section covers:

* [Classification and residency](./classification-and-residency): How data is classified, where it resides, and multi-cloud region support.
* [Data flow](./data-flow): Presigned URL and streaming relay patterns, and what data appears in the UI.
* [Encryption](./encryption): Encryption at rest and in transit across all storage and communication paths.
* [Secrets management](./secrets): Write-only API design, backends, and secret lifecycle.
* [Workflow data flow](./workflow-data-flow): Security controls at each stage of the workflow lifecycle.
* [Multi-cloud support](./multi-cloud): Supported cloud providers and consistent security guarantees.
* [Logging and audit](./logging-and-audit): Task logging, observability metrics, and audit trails.
