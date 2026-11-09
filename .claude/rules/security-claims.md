---
paths:
  - "content/security/**"
  - "content/deployment/**"
---

# Security claims: customer data and the control plane

The security pages say that customer data never transits Union.ai's control plane, for example "Not in
flight. Not at rest. Not ever." and, on the HIPAA page, "No PHI ever transits". Keep that wording. Don't
qualify it for the cases below.

- **Describe zero trust.** Every customer runs with zero trust on: the organization's zero-trust setting
  is enabled and its data planes serve customer-data requests directly. Describe that configuration.
  Don't document behavior that exists only without it as an exception to these claims.
- **"Customer data" is the data the customer's workloads process:** task inputs and outputs, files,
  directories and dataframes, code bundles, logs, reports, and secret values.
- **Orchestration metadata is not customer data.** That covers task definitions and their default
  values, run and action state, error messages, condition prompts, descriptions and signaled values,
  trigger specs and their inputs, metrics, and authorization checks (the caller's identity and the
  requested action). A path that carries only metadata is not a reason to hedge a page.

Practical advice about what developers write into metadata still belongs on the pages. For example,
whatever goes into an error message or a condition's prompt is stored in the control plane, so it
shouldn't carry sensitive data.

Decided by Peeter Piegaze, Head of Documentation, on 2026-11-09. Ask him before changing it.
