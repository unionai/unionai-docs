---
title: Encryption at rest
weight: 1
variants: -flyte +union
---

# Encryption at rest

All data at rest is encrypted using cloud-provider native encryption:

| Storage | Encryption Standard | Key Management |
| --- | --- | --- |
| Object Store (S3/GCS/Azure Blob) | Cloud-provider default (SSE-S3, Google-managed, Azure SSE) | Cloud provider managed; CMK supported |
| Container Registry | Cloud-provider encryption | Cloud provider managed |
| Secrets Backend (cloud) | Cloud-provider encryption | Cloud secrets manager |
| Secrets Backend (K8s) | `etcd` encryption | K8s cluster-level encryption |
| ClickHouse | Encrypted EBS/persistent disk | Cloud provider managed |
| Control Plane PostgreSQL | AWS RDS encryption | AES-256; AWS KMS managed |
