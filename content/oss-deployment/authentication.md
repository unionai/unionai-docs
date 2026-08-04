---
title: Authentication and SSO
variants: +flyte -union
weight: 4
---

# Authentication and SSO

Flyte delegates authentication to an **external OIDC identity provider** (Okta,
Google, Auth0, …). Two things are involved:

1. **Auth metadata**: the runs service advertises *which* IdP to use, so SDK/CLI and
   browser clients can discover where to log in and get tokens. Configured under
   `flyte-core-components.runs.authMetadata`.
2. **Enforcement at the ingress**: the load balancer validates those tokens (and
   challenges browsers with SSO) *before* requests reach Flyte. Configured with ingress
   annotations.

## Advertise your identity provider

The runs service serves OAuth2 authorization-server metadata
(`/.well-known/oauth-authorization-server` and the `AuthMetadataService` RPC) that
proxies your external IdP. Clients that discover auth at this deployment are pointed at
the IdP and obtain IdP-issued tokens, which the ingress then validates.

```yaml
flyte-core-components:
  runs:
    authMetadata:
      # Your external OAuth2 authorization server (the IdP issuer URL).
      externalAuthServerBaseUrl: https://<your-idp>/oauth2/default
      # Public (PKCE) client advertised to the SDK/CLI via GetPublicClientConfig
      # for browser login. Register this app at your IdP with the localhost redirect.
      flyteClient:
        clientId: <public-client-id>
        redirectUri: http://localhost:53593/callback
        scopes:
          - openid
          - profile
          - offline_access
```

The `redirectUri` (default `http://localhost:53593/callback`) is the SDK/CLI's local
PKCE callback and must be registered as a redirect URI on the IdP application.

> **Okta note.** PKCE needs an Okta **native app** client ID with the
> `http://localhost:53593/callback` redirect registered; the `client_credentials`
> (machine) flow needs a custom scope on the auth server. Adjust `clientId` / `scopes`
> for the flow you use.

## Enforce auth at the ingress

Browsers and machine clients authenticate differently, and on a controller like AWS
ALB a single ingress can't combine cookie-OIDC (browser) and JWT (token) auth, so the
chart can render up to **three ingresses**:

| Ingress (values key) | Purpose |
|---|---|
| `ingress` (`httpAnnotations`) | Serves the console (`/v2`) and API; challenges **browsers** with cookie-OIDC SSO ([walkthrough below](#single-sign-on-for-the-console-at-the-alb)). |
| `ingress.apiJwtIngress` | **JWT-validates** the `flyteidl2.*` API paths for requests carrying `Authorization: Bearer` (SDK / CLI / machine clients). Give it higher controller precedence than the http ingress so Bearer requests match it first. |
| `ingress.wellknownIngress` | Serves the **unauthenticated** auth-discovery endpoints (`/.well-known/oauth-authorization-server`, `AuthMetadataService`). Clients need these *before* they hold a token, so give it the highest precedence to bypass auth. |

Enable the JWT and discovery ingresses and supply your controller/JWT config via their
`annotations`, e.g. on ALB: the ACM `certificate-arn`, the JWT-validation config, the
`Authorization: Bearer*` match condition, and `group.order` values (lower = evaluated
first) that put `wellknownIngress` first, then `apiJwtIngress`, then the http ingress:

```yaml
ingress:
  create: true
  host: <flyte.example.com>
  # Browser SSO annotations on the main http ingress — see the walkthrough below.
  httpAnnotations: { }
  apiJwtIngress:
    enabled: true
    annotations: { }     # JWT validation + the `Authorization: Bearer*` match
  wellknownIngress:
    enabled: true
    annotations: { }     # highest controller precedence; no auth
```

## Single sign-on for the console at the ALB

This is the browser cookie-OIDC SSO referenced above. It goes on the main http
ingress's `httpAnnotations`. You can put OIDC single sign-on **in front of the console**
at the ALB, so that
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
- An **HTTPS listener** with an ACM certificate covering your host. OIDC auth only
  applies to HTTPS rules.
- An **OIDC application** at your IdP (confidential client, Authorization Code flow)
  with a client ID and secret.

### 1. Configure the OIDC app

On the IdP application:

- Add the **sign-in / redirect URI** exactly (note the path: ALB's callback is fixed):

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
kubectl create secret generic flyte-console-oidc -n flyte \
  --from-literal=clientID='<client-id>' \
  --from-literal=clientSecret='<client-secret>'
```

### 3. Allow the LB controller to read the Secret

The AWS Load Balancer Controller's service account must be able to `get`/`list`/
`watch` Secrets in the ingress namespace. The upstream Helm chart usually grants this
cluster-wide, but hardened installs may not. If yours doesn't, add a namespaced Role
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

Without this you'll see `FailedBuildModel … secrets "flyte-console-oidc" is
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
    alb.ingress.kubernetes.io/auth-idp-oidc: '{"issuer":"<issuer>","authorizationEndpoint":"<authorize>","tokenEndpoint":"<token>","userInfoEndpoint":"<userinfo>","secretName":"flyte-console-oidc"}'
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

Then open `https://<host>/v2` in a browser. You should be bounced through the IdP and
back into the console.

### Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `FailedBuildModel … secrets "…" is forbidden` on the ingress | The LB controller can't read the Secret. Apply the RBAC in step 3. |
| Browser: `'redirect_uri' parameter must be a Login redirect URI` | The exact callback isn't registered. Add `https://<host>/oauth2/idpresponse` (with that path) to the IdP app's redirect URIs. |
| `401 Authorization Required` *after* a successful login | The token exchange failed: almost always a wrong client **secret** or **client_id**. A trailing `%` on a secret copied from a terminal is the shell's no-newline marker, not part of the secret; strip it. |

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

## Sign out

The console's user menu has a **Sign out** action. The session lives at the proxy and
at your IdP, not in Flyte, so signing out takes two steps. The console serves both
from `/v2/logout`:

1. Expire the proxy's session cookies, so the browser stops presenting a valid session.
2. Redirect to a logout endpoint (typically your IdP's; for some proxies, the proxy's sign-out endpoint), so the IdP session ends too.

Step 2 is the one you configure. Without it, only the proxy session is cleared: the
next request bounces to the IdP, which still has a live session, signs the user back in
silently, and sign out appears not to have worked.

Both settings are environment variables on the console container:

```yaml
console:
  env:
    # Logout endpoint to redirect to after clearing cookies. Typically your IdP's logout
    # endpoint; for some proxies, use the proxy sign-out endpoint (see below).
    # Without this, sign out clears the proxy session only and the IdP silently signs the user back in.
      value: https://<your-idp>/oauth2/<id>/v1/logout?client_id=<client-id>&post_logout_redirect_uri=https%3A%2F%2F<your-host>%2Fv2%2Fprojects
    # Session cookies to expire. Defaults to ALB's; see below.
    # - name: LOGOUT_CLEAR_COOKIES
    #   value: ""
```

| Variable | Default | Purpose |
|---|---|---|
| `OIDC_LOGOUT_URL` | *(unset)* | Where to send the browser after clearing cookies. Unset means sign out only clears cookies and returns to the console. |
| `LOGOUT_CLEAR_COOKIES` | `AWSELBAuthSessionCookie-0,…-1,…-2,…-3` | Comma-separated session cookies to expire. Set to `""` to expire none. |

The `post_logout_redirect_uri` must be registered on the IdP application as a
**sign-out redirect URI** (Okta calls it that; the OIDC spec calls it a post-logout
redirect URI). If it isn't registered, the IdP rejects the logout request, typically
with a bare `400 Bad Request` and no explanation.

> **Okta note.** Okta also has an org-level `https://<domain>/login/signout`, which
> needs no registration and does end the session. The tradeoff: it has nowhere to
> return to, so it lands the user on Okta's sign-in page. Signing in there
> re-establishes the session, which looks like sign out failed. Prefer the
> `/oauth2/<id>/v1/logout` endpoint above once the redirect URI is registered.

### Cookies to expire

The default targets AWS ALB, which is the proxy that needs this most: it has **no
logout endpoint of its own**, so the application has to expire its cookies. ALB splits
its session cookie at 4 KB and supports 16 KB total, so `-0` through `-3` covers every
shard it can produce. Override the list if the listener rule sets a custom
`SessionCookieName`.

Expiring a cookie that was never set is a no-op, so the default is harmless on other
platforms. But most other proxies expose a sign-out endpoint that clears their own
cookie. Point `OIDC_LOGOUT_URL` at it and expire nothing yourself:

| Proxy | `OIDC_LOGOUT_URL` | `LOGOUT_CLEAR_COOKIES` |
|---|---|---|
| AWS ALB | IdP logout endpoint | *(default)* |
| oauth2-proxy | `https://<host>/oauth2/sign_out?rd=<idp-logout>` | `""` |
| GCP IAP | `https://<host>/_gcp_iap/clear_login_cookie` | `""` |
| Cloudflare Access | `https://<host>/cdn-cgi/access/logout` | `""` |

Pointing straight at the IdP's logout endpoint on these platforms leaves the proxy's
own cookie alive, and the user stays signed in.

### Troubleshooting

| Symptom | Cause and fix |
|---|---|
| Signed out, but a new tab is still signed in | The IdP session is still live. Set `OIDC_LOGOUT_URL`, and check you didn't sign in again on the IdP's page after being signed out. |
| The proxy's session cookie is still in the browser afterwards | The cookie names don't match what your proxy sets. Check `LOGOUT_CLEAR_COOKIES` against the cookies in your browser's dev tools (ALB's are `HttpOnly`, so they appear under Application → Cookies, not in `document.cookie`). |
| The IdP returns `400 Bad Request` on logout | The post-logout redirect URI isn't registered on the IdP application. |

## Run attribution (`executed_by`)

Once authentication happens at the edge, Flyte records **who created each run**
(surfaced as `executed_by` in run metadata). The runs service does not re-validate
tokens itself. It reads the identity from the headers the proxy forwards. After ALB
`authenticate-oidc` those are:

- `X-Amzn-Oidc-Data`: a signed JWT carrying the full claims (`sub`, `email`,
  `given_name`, `family_name`); used on the browser/cookie path.
- `X-Amzn-Oidc-Identity`: the subject only; used when the data header is absent.
- `Authorization: Bearer <jwt>`: the SDK/CLI path (proxy-agnostic, always honored).
  This token carries only the subject, so name and email are filled from the IdP's
  `userinfo` endpoint when `runs.authMetadata.externalAuthServerBaseUrl` is set.

The defaults match ALB, so a standard ALB SSO deployment needs no extra configuration.

> **Trust boundary.** The forwarded JWTs are decoded but **not** signature-verified by
> the runs service. That is safe only behind a trusted proxy that validates tokens and
> strips any client-supplied copies of these headers. If the service can be reached
> directly, set `trustForwardedIdentityHeaders: false` and `executed_by` is left unset
> rather than risk a spoofed identity.

### Behind a non-ALB proxy (oauth2-proxy / Traefik)

The header names are configurable, so attribution works behind any auth proxy. For
oauth2-proxy or Traefik forward-auth, which forward plain values instead of a JWT:

```yaml
flyte-core-components:
  runs:
    trustForwardedIdentityHeaders: true   # default; gates header-derived attribution
    identityHeaders:
      claimsJwtHeader: ""                  # no JWT header on this path
      subjectHeader: X-Auth-Request-User   # ALB default: X-Amzn-Oidc-Identity
      emailHeader: X-Auth-Request-Email    # ALB default: unset (email is in the JWT)
```

| Setting | Header read | ALB default | oauth2-proxy / Traefik |
|---|---|---|---|
| `claimsJwtHeader` | JWT with full claims | `X-Amzn-Oidc-Data` | *(empty)* |
| `subjectHeader` | subject, plain value | `X-Amzn-Oidc-Identity` | `X-Auth-Request-User` |
| `emailHeader` | email, plain value | *(unset)* | `X-Auth-Request-Email` |

The same trust boundary applies: the proxy must validate identity and strip any
client-supplied copies of these headers, with `trustForwardedIdentityHeaders` enabled.
