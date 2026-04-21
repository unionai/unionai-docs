---
title: Identity and access
weight: 3
variants: -flyte +union
sidebar_expanded: true
---

# Identity and access

Union.ai provides a layered identity and access management system that controls how users and applications authenticate, what resources they can access, and how tenant isolation is enforced. Access control spans two distinct domains: in-product authentication and authorization (RBAC, SSO, API keys) and infrastructure-level access to the customer's cloud environment.

This section covers:

* [Authentication](./authentication): OIDC, API keys, service accounts, and SSO configuration.
* [Role-based access control](./rbac): Built-in roles, custom policies, enforcement, and the least-privilege principle.
* [Tenant isolation](./tenant-isolation): Database-layer, data plane, and service-level isolation between customers.
* [Human access controls](./human-access): How Union.ai personnel access customer environments in self-managed and BYOC deployments.
