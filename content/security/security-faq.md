---
title: Security FAQ
weight: 14
variants: -flyte +byoc +selfmanaged
---

# Security FAQ

### Does Union.ai store any of my data?

No. Union.ai’s control plane stores only orchestration metadata (task definitions, run status, user records).
All customer data—including task inputs/outputs, code, logs, secrets, container images, and reports—resides exclusively in your own cloud infrastructure.

### Can Union.ai access my data?

Union.ai has no access to your compute plane at all. The Cloudflare tunnel is the only connection, and it is outbound-only from your cluster.

> [!NOTE]
> In BYOC deployments, Union.ai has K8s cluster management access but cannot access your data. See [BYOC deployment differences: Human access](./byoc-differences#human-access-to-customer-environments).

### What happens if the Union.ai control plane is compromised?

Because the control plane stores only orchestration metadata and never persists customer data, a control plane compromise would not expose your task inputs, outputs, code, secrets, or logs.
The attacker would gain access only to workflow metadata (task names, run status, scheduling configuration).

### Do I need to open inbound firewall rules?

No.
The Cloudflare Tunnel is outbound-only from your compute plane.
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

Union.ai enforces tenant isolation at multiple layers. In the control plane database, every record uses org as part of its primary key or unique index; all queries are gated by the authenticated org context before SQL execution, and cross-org access is explicitly denied at the service layer. Each customer’s compute plane runs in a physically separate Kubernetes cluster within the customer’s own cloud account, with no shared compute infrastructure between tenants. Within an organization, RBAC controls access at the project and domain level, and Kubernetes namespaces enforce resource-level isolation. These controls are within scope of the SOC 2 Type II audit.

### What compliance certifications does Union.ai hold?

Union.ai is SOC 2 Type II certified for Security, Availability, and Integrity.
The audit was conducted by Sansiba San Filippo LLP.
The SOC 2 report is available upon request.
Union.ai’s architecture also supports GDPR compliance through EU-region compute plane deployment.
