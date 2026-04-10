---
title: Security accuracy
weight: 200
variants: -flyte +union
sidebar_expanded: false
---



# Security Documentation Accuracy Report

**Date:** 2026-04-09
**Baseline:** `unionai/cloud` @ `release/2026.3.9` (pre-zero-trust)
**Documentation:** `/content/security-2/` (restructured from `/content/security/`)

## Summary

| Verdict | Count |
|---------|-------|
| Verified | 11 |
| Partially verified | 5 |
| Inaccurate | 2 |
| Cannot verify from source | 1 |

---

## High Priority Claims

### 1. Control plane stores NO customer data (only metadata/URIs)

**Docs say:** "The control plane never stores customer data payloads. It stores only references (URIs) to data in the customer's object store."

**Code shows:**
- `dataproxy/service/secret.go` -- NO database imports, no persistence logic, immediate relay to data plane
- `dataproxy/service/objectstore_service.go` -- presigned URLs returned but never stored; only org/domain/project logged on error
- `objectstore/service/object_store.go` -- ObjectMetadata contains only Etag/Size/Tags, no content

**Verdict: VERIFIED**

---

### 2. Presigned URL default TTL is 1 hour

**Docs say:** "time-limited (default 1 hour maximum)"

**Code shows:** `flyte/flyteadmin/pkg/config/config.go` lines 279-285:
```go
DataProxy: DataProxyConfig{
    Upload: DataProxyUploadConfig{
        MaxExpiresIn: config.Duration{Duration: time.Hour},
    },
    Download: DataProxyDownloadConfig{
        MaxExpiresIn: config.Duration{Duration: time.Hour},
    },
},
```

**Verdict: VERIFIED** -- both upload and download default to `time.Hour`.

---

### 3. Secrets API is truly write-only (GetSecret returns no values)

**Docs say:** "There is no API to read back secret values. The GetSecret RPC returns only the secret's metadata (name, scope, creation time, cluster presence status) -- never the value itself."

**Code shows:** `dataproxy/service/secret_transformer.go` lines 93-102:
```go
func toSecret(rawSecret *idlSecretProxy.Secret) (*idlSecret.Secret, error) {
    return &idlSecret.Secret{
        Id:             secretID,
        SecretMetadata: toSecretMetadata(rawSecret.GetSecretMetadata()),
    }, nil
}
```
Response includes ONLY Id and SecretMetadata. No value field.

**Verdict: VERIFIED**

---

### 4. Cloudflare Tunnel is outbound-only with mTLS

**Docs say:** "All traffic through the tunnel uses mutual TLS (mTLS) encryption"

**Code shows:**
- `cluster/cloudflared/` -- tunnel configured via standard Cloudflare Go SDK with token authentication (`tunnelSecret` -- a random base64-encoded secret)
- No `tls.Certificate`, `x509`, or client certificate configuration found anywhere in the tunnel code
- Only 2 mTLS references in entire codebase: one in `linkerd.tf` (Linkerd mesh), one in `imagebuild/registry-proxy/` (with comment "consider replacing with linkerd")

**Verdict: INACCURATE**
- **Outbound-only: Verified** -- Cloudflare Tunnel is outbound-only by design
- **mTLS: Not verified** -- Code shows standard TLS with token/secret authentication, not mutual TLS with client certificates. Cloudflare Tunnel provides TLS encryption but the authentication is via a shared tunnel secret, not mutual certificate exchange.

**Correction needed:** Change "mutual TLS (mTLS)" to "TLS encryption with authenticated tunnel" or verify with the infrastructure team whether Cloudflare's tunnel protocol constitutes mTLS at the Cloudflare edge level (it may -- Cloudflare's documentation calls their tunnel protocol "encrypted" but the union codebase doesn't configure mTLS explicitly).

> **Note:** It's possible Cloudflare Tunnel uses mTLS internally at the protocol level (between cloudflared daemon and Cloudflare edge), but this is a Cloudflare implementation detail, not something configured in Union's code. The docs should clarify whether this is a Union-configured security control or an inherited property of the Cloudflare Tunnel service.

---

### 5. Exactly 3 built-in RBAC roles (Admin, Contributor, Viewer)

**Docs say:** "Union.ai implements a policy-based RBAC system with three built-in role types."

**Code shows:** `authorizer/config/config.go` lines 30-34 defines 3 user-facing roles:
```go
RoleTypeAdmin       RoleType = RoleType(common.RoleType_ROLE_TYPE_ADMIN)
RoleTypeContributor RoleType = RoleType(common.RoleType_ROLE_TYPE_CONTRIBUTOR)
RoleTypeViewer      RoleType = RoleType(common.RoleType_ROLE_TYPE_VIEWER)
```

BUT `shared_service/authorization/roles.go` lines 150-161 defines **10 predefined roles**:
- Admin, Contributor, Viewer (user-facing)
- ClusterManager, FlyteProjectAdmin, Support, ServerlessViewer, ServerlessContributor, SystemProvisionedAccess, TenantManager (internal system roles)

Lines 109-121 comment these as "internal system roles" hidden from user-facing assignment.

**Verdict: INACCURATE**
- 3 user-assignable roles: correct
- But 7 additional internal system roles exist
- Docs should say "three user-assignable roles" and mention that additional system-managed roles exist internally

---

### 6. Exactly 2 IAM roles per data plane (adminflyterole, userflyterole)

**Docs say:** "Two IAM roles are provisioned per data plane"

**Code shows:** Both roles consistently present across deployments:
- `deploy/dataplane/staging/*.yaml` -- both `adminflyterole` and `userflyterole` defined
- `deploy/tenant/control-plane.yml` -- `adminflyterole` with IRSA annotation
- `infra/terraform/envs/production/aws-org-root/cur_bucket.tf` -- `userflyterole` IAM reference

**Verdict: VERIFIED**

---

### 7. Org isolation enforced on every database query

**Docs say:** "All database queries are gated by the org context extracted from the caller's authenticated token at the service layer, before any SQL is executed."

**Code shows:**
- `dataproxy/service/secret.go` -- org extracted and injected into every operation (CreateSecret line 146, UpdateSecret line 192, GetSecret line 237, DeleteSecret line 323)
- `flyteadmin-private/service/org_scope.go` -- `scopeOrgForProjectList()` extracts org from identity context
- `authorizer/lib/impl/userclouds/service.go` lines 114-118 -- cross-org access denial with logging

Pattern: `organization := authz.IdentityContextFromContext(ctx).Organization()` appears consistently.

**Verdict: VERIFIED** -- application-layer enforcement is thorough. Schema-level verification (org in primary keys) would require DB migration inspection.

---

## Medium Priority Claims

### 8. K8s ClusterRole definitions match documented roles

**Docs list 12 control plane ClusterRoles:** flyteadmin, scyllacluster-edit, console-clusterrole, authorizer-clusterrole, cluster-clusterrole, dataproxy-clusterrole, executions-clusterrole, queue-clusterrole, run-scheduler-clusterrole, usage-clusterrole, plus ScyllaDB roles.

**Code shows:**
- Only `flyteadmin` found in `deploy/tenant/helm/templates/rbac/_flyteadmin.yaml` -- and it's a namespace-scoped **Role**, not a **ClusterRole**
- Grafana ClusterRole found in generated manifests
- None of the other 11 documented ClusterRole names appear anywhere in the codebase

**Verdict: CANNOT VERIFY FROM SOURCE**
- These roles may be provisioned by the operator at runtime, defined in external Helm charts not in this repo, or managed manually
- The documentation cannot be confirmed or denied from the cloud repo alone

---

### 9. Communication paths use ConnectRPC

**Docs say:** "Client -> Control Plane: ConnectRPC (gRPC-Web) over HTTPS"

**Code shows:**
- ConnectRPC (`connectrpc.com/connect`) extensively used across 20+ files
- Plain gRPC (`google.golang.org/grpc`) also actively used for server setup, health checks, client caching
- Both frameworks coexist

**Verdict: PARTIALLY VERIFIED** -- ConnectRPC is the primary external-facing RPC framework, but plain gRPC is also used internally. Docs accurately describe the client-facing protocol.

---

### 10. Workload identity federation used (no static credentials)

**Docs say:** "These roles use cloud-native workload identity federation... eliminating the need for static credential storage."

**Code shows:**
- IRSA: `eks.amazonaws.com/role-arn` annotations in helm values
- GCP Workload Identity: `google_iam_workload_identity_pool` in terraform
- Azure Workload Identity: `workload_identity_enabled = true` in terraform

Static credentials found in staging cluster configs for **MinIO** (internal dev/test object store):
```yaml
FLYTE_AWS_ACCESS_KEY_ID: minio
FLYTE_AWS_SECRET_ACCESS_KEY: miniostorage
```

**Verdict: PARTIALLY VERIFIED** -- workload identity is used for all cloud provider access. Static credentials exist only for internal MinIO in staging/test environments, not in customer-facing deployments. Docs are accurate for production.

---

### 11. Service components match documented list

**Docs list:** Executor, Queue Service, State Service, Cluster Service, DataProxy, Object Store Service, Log Provider, Image Builder, Tunnel Service, Apps/Serving.

**Code shows** (in `deploy/tenant/helm/templates/union-services/`):
- Queue Service, Cluster Service, DataProxy -- found
- Plus **many undocumented services**: Actions, Artifacts, Auth Proxy, Authorizer, Cloud Admin, Dashboard, Execution, Flyte Console, Hooks, Identity, Leasor, Organizations, Union Console, Usage

**Verdict: PARTIALLY VERIFIED** -- documented services exist, but the docs significantly undercount the actual number of control plane services. The component architecture diagram is a simplified view, which is reasonable for security docs, but the docs could note it's not exhaustive.

---

### 12. Regional endpoints list is current

**Docs list:** us-east-2, us-west-2, eu-west-1, eu-west-2, eu-central-1

**Code shows** (`infra/terraform/envs/production/shared-infra/generated_config.tf` lines 54-70):
```terraform
byoc_domain = {
  eu-central-1 = "eu-central-1.unionai.cloud"
  eu-west-1    = "eu-west-1.unionai.cloud"
  eu-west-2    = "eu-west-2.unionai.cloud"
  us-east-2    = "hosted.unionai.cloud"
  us-west-2    = "us-west-2.unionai.cloud"
}
```

Also confirmed in `shared_service/deploy/region.go`. Note: `region.go` lists only 4 regions (omits eu-west-2), but terraform has all 5.

**Verdict: VERIFIED**

---

## Lower Priority Claims

### 13. Fluent Bit for log collection
**Verdict: VERIFIED** -- referenced in cloudformation templates and deployment configs.

### 14. Prometheus for observability
**Verdict: VERIFIED** -- helm values, grafana-agent configs, and tunnel ingress rules all reference Prometheus.

### 15. Image Builder uses Buildkit
**Verdict: VERIFIED** -- complete Buildkit helm chart at `deploy/devops/charts/buildkit/`.

### 16. ClickHouse for observability metrics
**Verdict: VERIFIED** -- ClickHouse ingress path in tunnel config, backup bucket terraform, nodepool configs.

---

## Additional Claims Verified

### Authentication methods (OIDC/Okta, API Keys, Service Accounts)

**Docs say:** "Union.ai supports three authentication methods: OIDC (Okta), API Keys, Service Accounts"

**Code shows:**
- `shared_service/config/identity.go` -- default IdP hardcoded as `Provider: "okta"` with `ClientRegistrationEndpointURL: "https://unionai.oktapreview.com/"`
- Service accounts via OAuth2 app registration through Okta confirmed in `identity/service/user.go`
- API keys: `shared_service/apikey/config.go` exists but appears to be for task runtime injection, not API authentication

**Verdict: PARTIALLY VERIFIED**
- OIDC via Okta: confirmed, but it's Okta-specific, not generic OIDC. Docs say "OIDC (Okta)" which is accurate.
- Service Accounts: confirmed via OAuth2 client registration
- API Keys: evidence suggests they exist but the mechanism is less clear from source code alone

### Custom RBAC policies

**Docs say:** "Custom policies bind roles to resources scoped at org-wide, domain, or project+domain level"

**Code shows:** `authorizer/lib/impl/userclouds/service.go` -- `CreatePolicyBinding()`, `GetPolicyAssignment()`, `ListPolicies()` functions exist. System distinguishes custom vs predefined roles.

**Verdict: PARTIALLY VERIFIED** -- mechanism exists; YAML format and `uctl` details not verifiable from backend code.

### Tenant context propagation

**Code shows:** `apimachinery/authz/identity_context.go`:
- Org extracted from OIDC token JWT claims (lines 410-420)
- Propagated via `x-overriden-org`, `x-user-subject`, `x-user-claim-identitytype` headers
- `bridgeJWTClaimsToMetadata()` function bridges JWT claims into gRPC metadata
- Applied uniformly across HTTP and gRPC via middleware interceptors

**Verdict: VERIFIED**

### Secret values never persisted to disk/DB during creation

**Code shows:** `dataproxy/service/secret.go` CreateSecret handler:
- No database imports in the file
- Immediate relay via `secretproxyClient.CreateSecret()` to data plane
- Returns empty `CreateSecretResponse{}`

**Verdict: VERIFIED**

### Presigned URLs are single-object scope, operation-specific

**Code shows:**
- `objectstore/service/object_store.go` -- single `key` parameter, explicit GET/PUT switch
- `raw_object_store_s3.go` -- `PresignGetObject` and `PresignPutObject` are separate operations with single `Key`
- `raw_object_store_gcs.go` -- same pattern with `SignedURL` accepting single `id`

**Verdict: VERIFIED**

### Presigned URLs not logged

**Code shows:** No logging of the `SignedUrl` value in any presign flow. Only org/domain/project metadata logged on error.

**Verdict: VERIFIED**

### Four secrets backends

**Code shows:** `operator/dataproxy/config.go` lines 55-63:
```go
const (
    SecretManagerTypeAWS SecretManagerType = iota
    SecretManagerTypeGCP
    SecretManagerTypeAzure
    SecretManagerTypeK8s
)
```

**Verdict: VERIFIED** -- exactly 4 backends.

---

## Corrections Needed

| # | Claim | Issue | Suggested Fix |
|---|-------|-------|--------------|
| 1 | mTLS on Cloudflare Tunnel | Code shows TLS with token auth, not explicit mTLS configuration | Clarify: "TLS-encrypted tunnel with authenticated connection" or verify with infra team whether Cloudflare's protocol constitutes mTLS |
| 2 | "Three built-in role types" | 10 predefined roles exist (7 internal/system) | Change to "three user-assignable roles (Admin, Contributor, Viewer)" and note internal system roles exist |

## Items to Investigate Further

| # | Topic | Question |
|---|-------|----------|
| 1 | K8s ClusterRoles | Where are the 12 documented ClusterRoles defined? Not in cloud repo -- possibly in operator runtime provisioning or external charts |
| 2 | API Keys as auth method | How exactly do API keys work for API authentication? The code evidence for this is thin |
| 3 | mTLS | Does Cloudflare Tunnel's protocol inherently provide mutual authentication at the edge? If so, the docs are architecturally correct even if Union doesn't configure mTLS explicitly |
| 4 | JIT access controls | Docs say "being implemented" -- code shows JIT identity creation exists but no time-bound enforcement visible |
