---
title: Security FAQ
weight: 14
variants: -flyte +byoc +selfmanaged
---

# Security FAQ

### Does Union.ai store any of my data?

No.
Union.ai’s control plane stores only orchestration metadata (task definitions, run status, user records).
All customer data—including task inputs/outputs, code, logs, secrets, container images, and reports—resides exclusively in your own cloud infrastructure.

### Can Union.ai access my data?

Union.ai does not have persistent access to your data.
The control plane does not possess your cloud IAM credentials.
Data access is mediated through presigned URLs (generated on your data plane using your IAM credentials) or through the Cloudflare tunnel as a stateless relay.

### What happens if the Union.ai control plane is compromised?

Because the control plane stores only orchestration metadata and never persists customer data, a control plane compromise would not expose your task inputs, outputs, code, secrets, or logs.
The attacker would gain access only to workflow metadata (task names, run status, scheduling configuration).

### Do I need to open inbound firewall rules?

No.
The Cloudflare Tunnel is outbound-only from your data plane.
Your network requires no inbound firewall rules, reducing your attack surface.

### Can I use my own encryption keys?

Yes.
Because your data resides in your own cloud infrastructure, you can configure customer-managed keys (CMK) on your object stores, databases, and secrets managers according to your organization’s key management policies.

### Is there an API to read secret values?

No.
The Secrets API is write-only for values.
The GetSecret RPC returns only metadata (name, scope, creation time).
Secret values are consumable only by task pods at runtime, eliminating API-based secret exfiltration.

### How does Union.ai handle multi-tenancy?

Every database record is scoped by organization.
Cross-organization access is denied at the service layer.
Each customer’s data plane is completely isolated in their own cloud account.
Within an organization, RBAC controls access at the project and role level.

### What compliance certifications does Union.ai hold?

Union.ai is SOC 2 Type II certified for Security, Availability, and Integrity.
The audit was conducted by Sansiba San Filippo LLP.
The SOC 2 report is available upon request.
Union.ai’s architecture also supports GDPR compliance through EU-region data plane deployment.

### Why do some AWS permissions use wildcard (`*`) resource scopes?

Some permissions use `*` instead of a more restricted scope because either AWS does not provide a mechanism to restrict them further, or they are required to perform actions across multiple services or resources.
For example, a VPC resource ID is a randomly generated identifier assigned at creation time (e.g., `vpc-01654a5601c67647f`).
Due to the random nature of the identifier, it is not possible to create a predictive policy like `arn:aws:ec2:*:*:vpc/???????`.
In contrast, some APIs like EKS allow a customer-chosen identifier, enabling restrictions like `arn:aws:eks:*:*:cluster/union-*`.
See [Appendix G](./appendix#g-aws-union-admin-iam-policy) and [Appendix H](./appendix#h-aws-private-link-iam-policy) for the full permission listings with resource scopes.
