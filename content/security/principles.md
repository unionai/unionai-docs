---
title: Principles
variants: -flyte -serverless +byoc -selfmanaged
weight: 1
---

# Security Principles

Union was designed with security in mind, and provides a number of features to help you secure your data and applications. It adheres to the following principles:

1. Least privilege
2. Union does not access customer data
3. No requirement to open public endpoints

## Least Privilege

Although we are the defacto DevOps for the customer and maintain both the Control Plane and the Data Plane, we tailor the privileges to the minimum required to manage the system effectively. No more, no less.

## Union does not access customer data

The best way to avoid losing the customer data is not possess it in the first place! Both BYOC and Self-Manage drive a strong edge between the Control Plane and Data Plane. All customer data lives in the Data Plane (which is always setup in the customer cloud accounts) and Union stores the minimum amount of metadata in the control plane (only sufficient to schedule and coordinate the workflow executions)

## No requirement to open public endpoints

To protect all customer information we do not open public endpoints for the bi-directional communication. We leverage Cloudflare Tunnels for that, protecting both the Data Plane and Control Plane from attacks and threat of exposure.
