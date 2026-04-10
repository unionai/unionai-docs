---
title: Security comparison
weight: 100
variants: -flyte +union
sidebar_expanded: false
---

# Security Documentation Comparison Report: Union vs Databricks

**Date:** 2026-04-09
**Union docs reviewed:** `/content/security-2/` (43 files, 8 sections)
**Databricks docs reviewed:** `/task-tracker/databricks-security/` (71 files, 5 sections)

## Executive Summary

The Union security-2 docs are structurally modeled on Databricks' thematic organization but differ significantly in approach. Union emphasizes **architectural transparency** -- explaining *why* the system is secure through design decisions like control plane/data plane separation, write-only secrets API, and outbound-only tunnels. Databricks emphasizes **operational completeness** -- providing step-by-step configuration guides with CLI examples, UI paths, and per-provider setup instructions.

Both approaches are valid for different reasons. However, Union's security docs currently have gaps that would matter to enterprise security reviewers completing vendor assessments. This report identifies those gaps and recommends targeted improvements.

**Important context:** Many operational topics flagged as "missing" in the raw comparison are already covered in Union's user guide and deployment docs (see Section 4). The security section should cross-reference these, not duplicate them.

---

## 1. Where Union Is Stronger Than Databricks

These are genuine advantages worth preserving and emphasizing:

### Data residency and architectural transparency
Union's CP/DP separation documentation is significantly more detailed and transparent than anything in Databricks' security docs. The `architecture/control-plane-data-plane.md` page (985 words) clearly maps every data type to its residency, access pattern, and whether it transits the control plane. Databricks' equivalent (`network/concepts/architecture.md`, 217 words) is vague by comparison.

### Write-only secrets API
Union's secrets architecture is genuinely superior from a security standpoint. The write-only API design (no read-back of secret values) eliminates an entire class of exfiltration attacks. Databricks explicitly notes that workspace admins can read any secret -- a weaker posture. The docs explain this well.

### Presigned URL model
The presigned URL security model (time-limited, single-object, operation-specific) is well documented with clear controls. This is a strong story.

### Workload identity federation
Union documents modern credential management (IRSA, GCP Workload Identity, Azure Workload Identity) with no static credentials. Databricks doesn't surface this level of detail.

### Threat modeling
The `operations/vulnerability-management.md` page includes explicit threat model scenarios (control plane compromise, tunnel interception, presigned URL leakage). Databricks has no equivalent. This is valuable for security reviewers.

---

## 2. Where Union Is Thinner Than Databricks

These are areas where the security docs need more depth, not necessarily more operational how-to content, but more security-focused detail.

### 2a. Compliance pages lack depth for audit use

**HIPAA:** Union's page is 206 words. Databricks' is 828 words. The critical gaps are:

- **No BAA (Business Associate Agreement) discussion.** Healthcare customers need to know whether Union offers a BAA, how to request one, and what it covers. This is table-stakes for HIPAA.
- **No shared responsibility breakdown specific to HIPAA.** Databricks lists what AWS does, what Databricks does, and what the customer must do. Union's general shared responsibility model exists but isn't mapped to HIPAA controls.
- **No customer obligations checklist.** What must a customer do to run HIPAA-compliant workloads on Union? (e.g., enable CMK, restrict PHI to data plane, configure audit logging)

**SOC 2:** The page lists the 70+ controls from the Trust Center but doesn't explain what's covered in the audit scope in terms a security reviewer can map to their questionnaire. The current content is more of a marketing summary than an audit-ready reference.

**GDPR:** At 140 words, this is too thin. It should address data subject rights (access, deletion, portability), data processing agreements, and sub-processor disclosure.

### 2b. Encryption section lacks enterprise depth

Union's `encryption-at-rest.md` is a single 6-row table (120 words). For enterprise security questionnaires, reviewers need:

- **CMK/BYOK options:** The table says "CMK supported" for object stores but provides no detail. Is there a guide? What KMS services are supported? What's the key rotation policy?
- **Encryption algorithms:** Which AES mode? What key lengths? The table says "cloud-provider default" but doesn't specify.
- **Key lifecycle:** Rotation, revocation, destruction procedures.

Databricks devotes 446 words to CMK alone, with a 13-row comparison table mapping data types to encryption features.

### 2c. Audit logging architecture not surfaced for compliance

The `operations/logging-monitoring-audit.md` page covers task logging and observability but doesn't explicitly connect to compliance requirements. Security reviewers want to know:

- What events are logged (auth attempts, RBAC changes, secret operations, data access)?
- How long are logs retained?
- Can logs be exported for SIEM integration?
- Are logs tamper-proof?

The current audit trail section (6 bullet points) covers the right topics at a high level but needs more specificity for audit use.

### 2d. MFA not addressed

MFA is entirely absent from the docs. Since Union delegates MFA to the customer's IdP, this should be stated explicitly: "MFA enforcement is managed by your identity provider. Union.ai does not implement a separate MFA layer." One sentence in `auth/sso-configuration.md` would close this gap.

---

## 3. Structural Observations

### Databricks puts operational and security content together; Union separates them

Databricks' secrets page (1,488 words) is both a security reference and an operational guide with CLI examples. Union separates these: security properties in `security-2/secrets/`, operational usage in `user-guide/task-configuration/secrets.md`. This is a reasonable architecture -- the security section explains the security posture, the user guide explains how to use the feature.

However, the security section currently **doesn't link to the operational guides**. A security reviewer reading the secrets page has no path to the operational details. This is an easy fix.

### Index pages are appropriately brief

Union's `_index.md` files are short (80-110 words) with links to child pages. This matches Hugo conventions and is fine. Databricks' index pages are similar.

### Component architecture is a unique strength

The `architecture/components.md` page with its Mermaid diagram has no Databricks equivalent. It's the kind of thing a security architect would appreciate during a deep-dive review.

---

## 4. Operational Content Already in Other Docs

The raw Databricks comparison flagged several "missing" operational topics. These are already covered elsewhere in Union's docs:

| Topic | Existing location | Security-2 should... |
|---|---|---|
| SSO/OIDC setup (Google, Okta, SAML) | `deployment/byoc/single-sign-on-setup/` | Link from `auth/sso-configuration.md` (already done) |
| RBAC custom policies (CLI/SDK examples) | `user-guide/user-management.md` | Add link from `auth/rbac.md` |
| Secrets creation, listing, scoping | `user-guide/task-configuration/secrets.md` | Add link from `secrets/secret-lifecycle-and-scoping.md` |
| API key create/manage/rotate | `user-guide/authenticating.md` | Add link from `auth/authentication.md` |
| Service account setup | `user-guide/authenticating.md` | Add link from `auth/authentication.md` |
| Authentication overview | `user-guide/authenticating.md` | Add link from `auth/authentication.md` |

**Not documented anywhere:**
- MFA enforcement (delegated to IdP -- needs a one-line statement)

---

## 5. Recommendations

### Priority 1: Fix accuracy issues (from accuracy audit)

These are factual errors that should be corrected regardless of depth considerations.

| File | Issue | Fix |
|---|---|---|
| Multiple files referencing mTLS | Code shows TLS with token auth, not mutual TLS client certificates | Change "mutual TLS (mTLS)" to "TLS-encrypted authenticated tunnel" throughout, or verify with infra team whether Cloudflare's protocol constitutes mTLS and add a clarifying note |
| `auth/rbac.md`, `auth/authentication.md` | Only 3 user-facing roles mentioned; 7 internal system roles undisclosed | Add note: "In addition to these three user-assignable roles, Union.ai uses internal system roles for platform operations. These are not user-visible or user-assignable." |

### Priority 2: Add cross-reference links to operational docs

These are quick edits (one line each) that close the "where do I learn how to do this?" gap without duplicating content.

| File | Add link to |
|---|---|
| `auth/authentication.md` | `user-guide/authenticating.md` for API key and service account setup |
| `auth/rbac.md` | `user-guide/user-management.md` for custom policy configuration |
| `secrets/secret-lifecycle-and-scoping.md` | `user-guide/task-configuration/secrets.md` for creating and using secrets |
| `auth/sso-configuration.md` | Already links to `deployment/byoc/single-sign-on-setup/` (no change needed) |

### Priority 3: Expand compliance pages for audit readiness

These are the pages most likely to be read by enterprise security and compliance teams during vendor evaluation. They need more substance.

**`compliance/hipaa.md`** -- expand from 206 to ~500 words:
- Add BAA availability statement (whether Union offers BAAs, how to request)
- Add HIPAA-specific shared responsibility breakdown (what Union does vs what customer must do)
- Add customer checklist for HIPAA-compliant deployments
- Reference specific HIPAA safeguard categories (administrative, technical, physical) and how Union addresses each

**`compliance/gdpr.md`** -- expand from 140 to ~300 words:
- Add data subject rights (how customers can fulfill access/deletion/portability requests given the architecture)
- Add data processing agreement availability
- Add sub-processor disclosure reference

**`compliance/soc2.md`** -- minor expansion:
- Add what the audit scope covers in terms reviewers can map to their questionnaires (systems, processes, controls tested)
- Currently reads more as Trust Center summary; needs to be more audit-specific

### Priority 4: Add encryption depth

**`keys/encryption-at-rest.md`** -- expand from 120 to ~300 words:
- Add CMK/BYOK section: which cloud KMS services are supported, how to enable, link to deployment docs if a setup guide exists
- Add encryption algorithm specifics (AES-256-GCM for RDS, SSE-S3 uses AES-256, etc.)
- Add key rotation statement (cloud provider managed rotation or customer-managed)

### Priority 5: Strengthen audit logging for compliance

**`operations/logging-monitoring-audit.md`** -- expand the audit trail section:
- List specific event types that are logged (authentication events, RBAC changes, secret operations, run lifecycle, cluster state changes)
- State log retention policy or that it's customer-configurable
- Mention SIEM integration capability (if logs can be exported)
- Connect audit logging to compliance requirements (SOC 2, HIPAA)

### Priority 6: Add MFA statement

**`auth/sso-configuration.md`** -- add one paragraph:
- State that MFA enforcement is delegated to the customer's identity provider
- Union.ai does not implement a separate MFA layer
- Customer's existing MFA policies apply to Union.ai access automatically through SSO

---

## 6. What NOT to Change

- **Don't add operational how-to content** to the security section. The user guide already covers this. Add cross-reference links instead.
- **Don't expand the architecture section.** It's already Union's strongest area and appropriately detailed.
- **Don't add per-provider SSO guides** (Databricks has 8+ of these). Union's deployment docs cover this.
- **Don't try to match Databricks' page count.** Databricks has 71 files because they cover many features Union doesn't have (IP access lists, VPC peering, FedRAMP, GovCloud, etc.). Union's 43 files cover the right topics.
- **Don't add operational secrets management CLI examples.** These belong in `user-guide/task-configuration/secrets.md`.

---

## Summary of Recommended Changes

| Priority | Effort | Files affected | Description |
|---|---|---|---|
| P1 | Small | ~6 files | Fix mTLS wording, add system roles note |
| P2 | Small | 3 files | Add cross-reference links to operational docs |
| P3 | Medium | 3 files | Expand HIPAA, GDPR, SOC 2 for audit readiness |
| P4 | Small | 1 file | Add encryption depth (CMK, algorithms, rotation) |
| P5 | Small | 1 file | Expand audit logging section |
| P6 | Trivial | 1 file | Add MFA delegation statement |
