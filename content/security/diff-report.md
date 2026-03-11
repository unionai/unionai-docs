# Diff report: old files vs new `_1.md` files

## Recurring changes across all files

These appear in nearly every file and are intentional systematic changes:

| Change | Significance |
|---|---|
| "data plane" → "compute plane" | Terminology update. The raw.md source uses "compute plane" consistently. The old files used "data plane". This is a deliberate terminology shift. |
| `Fluentbit`/`FluentBit` → `Fluent Bit` | Spelling fix. Official project name is two words. |
| `etcd` → `` `etcd` `` | Formatting. Backticked as a code identifier. |
| `adminflyterole` → `` `adminflyterole` `` | Formatting. Backticked as a code identifier. |
| Comma-separated K8s lists → backticked space-separated | Formatting. RBAC tables now use code spans for Resources, API Groups, and Verbs columns. |
| Role names backticked in RBAC tables | Formatting. K8s role names now in code spans. |

## Per-file significant differences

### `_index.md` → `_index_1.md`

- Bullet points are now single long lines instead of wrapped with 2-space continuation indents — formatting style change (one-sentence-per-line was applied to paragraphs but not bullets)
- "Auth / SSO" detail added to outbound connectivity bullet — content addition from raw source
- "without customer authorization" added to human isolation bullet — content addition from raw
- Closing paragraph wrapped in `> [!NOTE]` — formatting change (Hugo admonition)
- Trust portal URL trailing slash removed — trivial

### `company-overview.md` → `company-overview_1.md`

- `**originally developed at Lyft**` bold removed — formatting: raw source didn't bold this
- Deployment models table: old had 5 rows (BYOC, Self-Managed, Self-Managed+Support, Air-gapped, Air-gapped+Support) with 6 columns (including Union Admin Permissions, Private Link Permissions). New has 2 rows (BYOC, Self-Managed) with 4 columns. — **Significant content reduction.** The raw source only had 2 deployment models. The old file had more detailed/expanded table. **Needs review: were those extra rows intentional additions?**

### `security-architecture.md` → `security-architecture_1.md`

- Cross-references changed from `./appendix#...` to `#...` — link format change (intra-page vs cross-page). Since this will be a separate page, the `#` anchors won't work — **needs fixing to use relative links when pages are split.**
- Removed `<!-- TODO: Add architecture diagram -->` and similar HTML comments — old had author notes, new doesn't (raw didn't have them)
- Old had "The control plane cannot independently initiate connections to the data plane" bullet — removed in new. Minor content reduction.
- Old had Cloudflare CIDR link `[published Cloudflare CIDR blocks](https://developers...)` — new has plain text. **Lost hyperlink.**
- Old had "Union → Customer EKS/GKE | AWS PrivateLink / GCP Private Service Connect" row in Communication Paths table — removed in new. Content reduction from raw source.
- Old had "The code bundle is directly uploaded to object store using signed URLs" paragraph — removed in new, replaced by TODO stubs. Content change.
- New adds image reference and TODO stubs for "Data in the UI" / "Data in the API / CLI" — from raw source.

### `data-protection.md` → `data-protection_1.md`

- Task inputs/outputs transit column changed from "No — direct via presigned URL" to "Relayed in-memory (not stored)" — **Content change from raw source.** This is substantively different — the raw claims inputs/outputs are relayed, while the old file said they go direct. **Needs fact-checking with engineering.**
- "Control plane PostgreSQL" capitalization change — trivial formatting
- Data residency section: old used bold labels `**Data plane:**`, new uses `###` subheadings — structural change
- Cross-reference changed from "See section 4.1" to markdown link — improvement

### `identity-and-access-management.md` → `identity-and-access-management_1.md`

- Added sentence: "Users have the ability to create custom policies to further refine access control." — Content addition (was truncated in raw, we completed it)
- Minor only otherwise.

### `secrets-management.md` → `secrets-management_1.md`

- Write-only API section: old had 4 separate sentences on separate lines. New wraps them in a `> [!NOTE]` block as a single paragraph. — Formatting change (admonition)

### `infrastructure-security.md` → `infrastructure-security_1.md`

- Only terminology and backtick formatting changes. No content differences.

### `logging-monitoring-and-audit.md` → `logging-monitoring-and-audit_1.md`

- Old: "A per-cluster ClickHouse instance" → New: "A per-cluster instance (Prometheus and/or ClickHouse)" — Content change from raw. Broader/more accurate description.
- Added comma after "authenticated" in audit trail bullet — grammar fix

### `compliance-and-certifications.md` → `compliance-and-certifications_1.md`

- Standards compliance table: old had 4 columns (Framework, Control, Domain, Description) with 10 rows including CIS EKS-specific entries. New has 3 columns (Framework, Control, Description) with 8 rows, dropping CIS 1.5/3.x EKS-specific entries. — **Content reduction.** The raw source had a simpler table. **Needs review: were the extra CIS EKS rows intentional additions?**
- "HIPAA-certified" → "HIPAA certified" — minor style

### `workflow-execution-security.md` → `workflow-execution-security_1.md`

- Data flow summary section: old had 3 separate sentences, new wraps in `> [!NOTE]` — formatting change

### `multi-cloud-and-region-support.md` → `multi-cloud-and-region-support_1.md`

- Only terminology changes. No content differences.

### `organizational-security-practices.md` → `organizational-security-practices_1.md`

- Title: "Organizational security practices" → "Organizational & physical security practices" — title expanded per raw source
- Old intro was 1 sentence, new is 2 — content addition from raw
- Fixed broken italics: `**Verified controls*** (source...)*` → `**Verified controls** (source...)` — formatting fix
- "Governance and" → "Governance &" — style from raw
- Business continuity row: old had extra text about BYOC architecture resilience — content reduction from raw
- Closing note: old used italics `*...*`, new uses `> [!NOTE]` — formatting change

### `security-faq.md` → `security-faq_1.md`

- Title: "Security FAQ" → "Security FAQ for enterprise evaluators" — title expanded per raw
- "No." answer now on same line as first sentence — formatting
- Old had extra FAQ about AWS wildcard permissions with links to Appendix G/H — **content removed** (not in raw source)

### `appendix.md` → `appendix_1.md`

- Heading labels changed from `A.` → `A:` — formatting consistency
- `ClusterRole` no longer backticked in prose — per our convention
- First role name: old had `flyteadmin-clusterrole`, new has `[TODO]` — role name unknown in raw source
- Old Section D had category rows as bold table rows (`**Union Core Services**`), new splits into `###` subheadings — structural improvement
- Old had bold+backtick plane labels (`**Data plane**`), new uses plain text — formatting simplification
- Section E: old had backticked `union` namespace, new doesn't — minor
- **Sections G, H, I entirely removed** — old appendix had AWS Union Admin IAM policy (~600 lines of JSON), AWS Private Link IAM policy, and Required AWS VPC endpoints. These are not in the raw source. **Significant content loss — these were likely added separately. Need to decide whether to preserve them.**
- Contact section: old had email `security@unionai.ai` and links, new has plain text — formatting reduction

### `compute-plane-components-reference.md` → `compute-plane-components-reference_1.md`

- Title/heading: "Data plane" → "Compute plane" — terminology
- Old had `## Image Builder` (Title Case), new has `## Image builder` (sentence case) — formatting
- Old had AWS and GCP Image Builder authentication subsections with detailed IAM/ECR/GCR permission JSON — **~120 lines of content removed** (not in raw source). **Significant content loss — these were detailed platform-specific docs.**
- `CreateSignedURL` was backticked in old, not in new — minor inconsistency (it's a code identifier)

## Items needing decisions

1. **Appendix G, H, I** (AWS IAM policy, Private Link policy, VPC endpoints) — ~500 lines of detailed JSON permission listings present in old `appendix.md` but absent from raw.md. Preserve separately?
2. **Image Builder auth sections** (AWS ECR, GCP Artifact Registry details) — ~120 lines in old `compute-plane-components-reference.md` but absent from raw. Preserve separately?
3. **Deployment models table** — old had 5 deployment models, new has 2. Were the extras (Air-gapped, Self-Managed+Support) intentional?
4. **Task inputs/outputs transit** — old says "No — direct via presigned URL", new says "Relayed in-memory (not stored)". Which is correct?
5. **Cross-references** — `#anchor` links in the _1 files will need to become `./pagename#anchor` links once pages are split.
6. **AWS wildcard FAQ** — old security-faq had an extra Q&A about AWS `*` resource scopes. Preserve?
