---
title: Security best practices
weight: 15
variants: -flyte +union
---

# Security best practices

> [!TIP] New in zero-trust architecture
> This page was introduced as part of the zero-trust security architecture.

This page provides recommendations for hardening your Union.ai deployment beyond the platform defaults.

## Recommended security configuration

* **Choose Enterprise 1 for maximum data isolation** — The [Enterprise 1 security tier](./deployment-models#enterprise-1-enhanced-security) restricts all data visualization to users connected to your corporate VPN, ensuring no external access to customer data.
* **Configure the shortest practical presigned URL TTL** — Presigned URLs default to a 1-hour expiration. Organizations with stricter requirements should configure shorter TTLs to minimize the exposure window.
* **Use cloud-native secrets backends** — AWS Secrets Manager, GCP Secret Manager, or Azure Key Vault provide stronger isolation than the default Kubernetes Secrets backend.

> [!NOTE] Information needed
> Specific recommended TTL values and CMK (Customer Managed Key) configuration steps per cloud provider are not yet documented.

## Network hardening

* **Restrict egress to Cloudflare CIDR blocks** — In locked-down environments, limit outbound traffic to published Cloudflare CIDR blocks for both the control plane tunnel and the Direct-to-DataPlane tunnel.
* **Configure VPN for Enterprise 1** — Deploy a VPN-routable load balancer within your VPC to restrict data access to corporate network users only.
* **Apply Kubernetes network policies** — Use network policies to restrict pod-to-pod communication and limit egress from task pods.

> [!NOTE] Information needed
> Specific network policy templates, recommended firewall rules, and Cloudflare CIDR block details should be obtained from the Union.ai networking team.

## IAM hardening

* **Review IAM role permissions regularly** — Audit the admin and user IAM roles provisioned per data plane to ensure they follow least-privilege principles.
* **Use workload identity federation** — Avoid static credentials on the data plane. Use cloud-native workload identity (IAM Roles for Service Accounts on AWS, Workload Identity on GCP, Azure Workload Identity on Azure).
* **Scope secrets narrowly** — Use project and domain scoping to limit secret access to the workloads that need them.

## Monitoring and detection

* **Enable audit logging** — Ensure all API requests, RBAC changes, and secret operations are logged.
* **Monitor tunnel health** — Set up alerts for tunnel connectivity issues, which may indicate network changes or potential interference.
* **Set up alerts for anomalous access patterns** — Monitor for unusual API request volumes, unexpected user access, or failed authentication attempts.

> [!NOTE] Information needed
> Specific monitoring recommendations, alert templates, and integration guidance with customer SIEM systems are not yet documented.

## Supply chain security

* **Implement container image scanning** — Apply scanning policies to all container images before deployment to the customer registry.
* **Use approved base image registries** — Configure Image Builder to pull base images only from customer-approved registries.
* **Review third-party dependencies** — Union.ai's vendor management program is covered under the SOC 2 Type II audit. See [Third-party dependency risk](./vulnerability-and-risk-management#third-party-dependency-risk) for details.

> [!NOTE] Information needed
> Specific scanning tool recommendations, SBOM (Software Bill of Materials) availability, signed build verification, and Union.ai's own supply chain security practices for data plane components are not yet documented.
