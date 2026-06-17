---
title: Authentication and SSO
variants: -flyte +union
weight: 3
---

# Authentication and SSO

A Flyte 2 deployment has two independent places you can add authentication:

1. **API authentication** — the Flyte binary itself authenticates SDK/CLI clients and
   the console against an OIDC provider. Configured with `configuration.auth`.
2. **Console SSO at the ingress** — the load balancer challenges browsers for login
   *before* the request reaches the console, with no change to the Flyte binary.
   Configured with ingress annotations.

You can use either layer on its own or both together. API authentication is what
protects the API and identifies users; ingress SSO is a convenient way to gate the
console UI at the edge.

## Layer 1: API authentication

Authentication is off by default (`configuration.auth.enabled: false`). Turn it on and
choose where tokens come from. There are two modes.

### Self-hosted authorization server (default)

Flyte issues its own OAuth2 tokens (`enableAuthServer: true`) and uses an external
OIDC provider for browser login:

```yaml
configuration:
  auth:
    enabled: true
    enableAuthServer: true
    oidc:
      baseUrl: https://<your-idp>/oauth2/default   # OIDC issuer URL
      clientId: <oidc-client-id>
      clientSecret: <oidc-client-secret>           # prefer the Secret ref below
    flyteClient:
      clientId: flytectl
      redirectUri: http://localhost:53593/callback # CLI/SDK PKCE callback
      scopes:
        - all
        - offline
    # Every host a redirect might legitimately come back to during the OAuth2 flow.
    authorizedUris:
      - https://<flyte.example.com>
```

### External authorization server

Delegate token issuance to an existing OAuth2 authorization server and have Flyte 2
only **validate** the tokens it receives (`enableAuthServer: false`). This is useful
when you already run an identity service (for example an existing Flyte 1 deployment)
and want Flyte 2 to trust the same tokens:

```yaml
configuration:
  auth:
    enabled: true
    enableAuthServer: false
    oidc:
      baseUrl: https://<your-idp>/oauth2/default
      clientId: <oidc-client-id>
      clientSecret: <oidc-client-secret>
    externalAuthServer:
      baseUrl: https://<external-authz-server>
      metadataUrl: .well-known/oauth-authorization-server
      allowedAudience:
        - https://<external-authz-server>
```

### Keeping secrets out of values

Rather than putting `clientSecret` in your values file, create a Kubernetes Secret
that supplies `client_secret` and `oidc_client_secret`, and reference it. The chart
then mounts it instead of generating its own:

```yaml
configuration:
  auth:
    enabled: true
    clientSecretsExternalSecretRef: <my-flyte-client-secrets>
```

### Connecting a client

Once API auth is enabled, point the SDK/CLI at your Flyte host and authenticate
through the browser PKCE flow advertised by `flyteClient`. The `redirectUri`
(`http://localhost:53593/callback` by default) must be registered as a redirect URI on
the OIDC application.

## Layer 2: Single sign-on for the console at the ingress

On AWS you can put OIDC single sign-on **in front of the console** at the ALB, so that
hitting `https://<host>/v2` challenges the user to log in at your IdP before the
request ever reaches the console. ALB's native `authenticate-oidc` action handles the
login and manages the session cookie; the Flyte binary is unchanged. SDK/machine
clients that send an `Authorization: Bearer` token are matched by higher-precedence
API rules and bypass the cookie flow.

```
Browser ──GET /v2──▶ ALB ──(no session)──▶ 302 ▶ IdP login
                       ▲                              │
                       └──── /oauth2/idpresponse ◀────┘  (ALB swaps code→token,
                              sets session cookie, forwards to the console)
```

### Prerequisites

- The **AWS Load Balancer Controller** managing your ingress (`ingressClassName: alb`).
- An **HTTPS listener** with an ACM certificate covering your host — OIDC auth only
  applies to HTTPS rules.
- An **OIDC application** at your IdP (confidential client, Authorization Code flow)
  with a client ID and secret.

### 1. Configure the OIDC app

On the IdP application:

- Add the **sign-in / redirect URI** exactly (note the path — ALB's callback is fixed):
  ```
  https://<your-host>/oauth2/idpresponse
  ```
- Grant type **Authorization Code**; scopes at least `openid email`.
- Assign the users/groups allowed into the console.

You'll need the issuer plus the authorize/token/userinfo endpoints:

| | Okta (custom auth server) | Google |
|---|---|---|
| issuer | `https://<domain>/oauth2/<id>` | `https://accounts.google.com` |
| authorize | `…/oauth2/<id>/v1/authorize` | `https://accounts.google.com/o/oauth2/v2/auth` |
| token | `…/oauth2/<id>/v1/token` | `https://oauth2.googleapis.com/token` |
| userinfo | `…/oauth2/<id>/v1/userinfo` | `https://openidconnect.googleapis.com/v1/userinfo` |

For Okta, the discovery doc
`https://<domain>/oauth2/<id>/.well-known/openid-configuration` is the source of truth.

### 2. Create the client Secret

In the **same namespace as the ingress**, with keys **exactly** `clientID` /
`clientSecret`:

```bash
kubectl create secret generic flyte2-console-oidc -n flyte \
  --from-literal=clientID='<client-id>' \
  --from-literal=clientSecret='<client-secret>'
```

### 3. Allow the LB controller to read the Secret

The AWS Load Balancer Controller's service account must be able to `get`/`list`/
`watch` Secrets in the ingress namespace. The upstream Helm chart usually grants this
cluster-wide, but hardened installs may not — if yours doesn't, add a namespaced Role
and RoleBinding:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: aws-lb-controller-oidc-secret
  namespace: flyte
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: aws-lb-controller-oidc-secret
  namespace: flyte
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: aws-lb-controller-oidc-secret
subjects:
- kind: ServiceAccount
  name: aws-load-balancer-controller   # adjust to your controller's SA
  namespace: kube-system
```

Without this you'll see `FailedBuildModel … secrets "flyte2-console-oidc" is
forbidden` on the ingress and no auth rule is applied.

### 4. Add the auth annotations

Add the OIDC annotations to `ingress.httpAnnotations` in your values and
`helm upgrade`. They apply to every rule on the HTTP ingress, gating the `/v2`
console:

```yaml
ingress:
  httpAnnotations:
    # … existing ALB annotations (certificate-arn, scheme, listen-ports, …) …
    alb.ingress.kubernetes.io/auth-type: oidc
    alb.ingress.kubernetes.io/auth-scope: openid email
    alb.ingress.kubernetes.io/auth-on-unauthenticated-request: authenticate
    alb.ingress.kubernetes.io/auth-session-timeout: "604800"   # 7 days
    alb.ingress.kubernetes.io/auth-idp-oidc: '{"issuer":"<issuer>","authorizationEndpoint":"<authorize>","tokenEndpoint":"<token>","userInfoEndpoint":"<userinfo>","secretName":"flyte2-console-oidc"}'
```

### 5. Verify

```bash
# Console redirects to the IdP:
curl -s -o /dev/null -D - https://<host>/v2 | grep -i '^location'
# → 302 … https://<issuer>/v1/authorize?client_id=…&redirect_uri=…%2Foauth2%2Fidpresponse…

# API path is NOT gated (a normal response, not a 302 to the IdP):
curl -s -o /dev/null -w '%{http_code}\n' -X POST \
  https://<host>/flyteidl2.project.ProjectService/ListProjects \
  -H 'Content-Type: application/json' -d '{}'
```

Then open `https://<host>/v2` in a browser — you should be bounced through the IdP and
back into the console.

### Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `FailedBuildModel … secrets "…" is forbidden` on the ingress | The LB controller can't read the Secret. Apply the RBAC in step 3. |
| Browser: `'redirect_uri' parameter must be a Login redirect URI` | The exact callback isn't registered. Add `https://<host>/oauth2/idpresponse` (with that path) to the IdP app's redirect URIs. |
| `401 Authorization Required` *after* a successful login | The token exchange failed — almost always a wrong client **secret** or **client_id**. A trailing `%` on a secret copied from a terminal is the shell's no-newline marker, not part of the secret; strip it. |

### Annotation reference

| Annotation | Purpose |
|---|---|
| `auth-type: oidc` | Enable OIDC auth on the ingress's HTTPS rules. |
| `auth-idp-oidc` | JSON: `issuer`, `authorizationEndpoint`, `tokenEndpoint`, `userInfoEndpoint`, `secretName` (Secret with `clientID`/`clientSecret`). |
| `auth-scope` | Space-separated scopes, e.g. `openid email`. |
| `auth-on-unauthenticated-request` | `authenticate` (challenge), `allow`, or `deny`. |
| `auth-session-timeout` | Session cookie lifetime in seconds. |

The ALB callback path is fixed at `/oauth2/idpresponse`, and auth applies only to the
annotated ingress's HTTPS listener rules.
