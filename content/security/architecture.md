---
title: Architecture
variants: -flyte -serverless +byoc +selfmanaged
weight: 1
---

# Architecture

## Private Dataplanes

### Amazon AWS

![AWS Architecture](../_static/images/security/aws_privatelink_simple.png)

Union leverages AWS Private Link to provide a private, secure connection to EKS management nodes.

References:

- [How Union makes it work?](providers/aws/permissions.md)
- [AWS Private Link](https://aws.amazon.com/privatelink/)

### Google Cloud Platform (GCP)

![GCP Architecture](../_static/images/security/gcp_privatelink_simple.png)

Union leverages GCP Private Service Connect to provide a private, secure connection to GKE management nodes.

References:

- [How Union makes it work?](providers/gcp/permissions.md)
- [GCP Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect)
