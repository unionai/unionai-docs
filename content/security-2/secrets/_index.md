---
title: Secrets management
weight: 700
variants: -flyte +union
sidebar_expanded: true
---

# Secrets management

Union.ai provides enterprise-grade secrets management with a security-first design. Secret values are stored exclusively within the customer's infrastructure using configurable backends. The secrets API is **write-only by design** — secret values cannot be read back through the API, eliminating an entire class of exfiltration attacks.

This section covers:

* [Secrets backends](./secrets-backends): The four configurable backends and their storage locations.
* [Secret lifecycle and scoping](./secret-lifecycle-and-scoping): How secrets are created, consumed, and scoped, including the write-only API design.
