---
title: Authentication
description: Put oauth2-proxy or an AWS ALB in front of onebox for single sign-on in the browser and token login for the SDK and CLI.
icon: shield-lock
weight: 5
variants: -flyte +union
---

# Authentication

Onebox doesn't sign anyone in. Put an authenticating proxy in front of it that logs users in at your identity provider (IdP) and forwards who they are in request headers. Onebox trusts those headers. This page sets that up with [oauth2-proxy](#oauth2-proxy), which runs anywhere, or an [AWS ALB](#aws-alb).

Two kinds of clients go through the proxy:

- **Browsers** sign in at the IdP and get a session cookie from the proxy.
- **The SDK and CLI** get a token from the IdP and send it as `Authorization: Bearer`. They find the IdP by asking onebox, which advertises it from `authMetadata` at two discovery paths. The proxy must let those through without a login, and accept the IdP's tokens.

## How onebox reads identity

| Value | Default | Holds |
|---|---|---|
| `identity.subjectHeaders` | `[X-Forwarded-User]` | The user's stable ID. Required: a request without it is anonymous. |
| `identity.emailHeaders` | `[X-Forwarded-Email]` | Email |
| `identity.nameHeaders` | `[X-Forwarded-Preferred-Username]` | Display name |
| `identity.groupsHeaders` | `[X-Forwarded-Groups]` | Comma-separated groups |
| `identity.claimsJWTHeaders` | `[]` | Headers holding a JWT the proxy has verified. Its `sub`, `email`, `name`, and `groups` claims fill in whatever the headers above didn't. |

The defaults match oauth2-proxy.

> [!WARNING] List only headers your proxy sets
> A proxy overwrites the identity headers it sets and passes every other header through from the client. If you list a header your proxy doesn't set, any signed-in user can send it and act as someone else. List exactly the headers your proxy sets, and empty the lists you don't use.

Onebox also has to be reachable **only** through the proxy. Make sure of it with one or both of these:

- `networkPolicy.proxyFrom`: only the proxy's pods, or its address range, can reach port `80`. See [Authorization](./authorization#network-policy).
- `identity.proxySecret`: the proxy adds a shared secret header to each request, and onebox ignores identity headers on requests without it.

Once requests carry an identity, turn on [Authorization](./authorization) to decide what each user can do.

## oauth2-proxy

[oauth2-proxy](https://oauth2-proxy.github.io/oauth2-proxy/) runs as a Deployment in your cluster, in front of the onebox Service, and works with any OIDC IdP.

### 1. Register two applications at your IdP

| Application | Type | Redirect URI | Used by |
|---|---|---|---|
| Web | Confidential, authorization code | `https://<host>/oauth2/callback` | oauth2-proxy, for browser sign-in |
| CLI | Public (native), authorization code with PKCE | `http://localhost:53593/callback` | The SDK and CLI |

`<host>` is the address your users open. Note the issuer URL, the web application's client ID and secret, and the CLI application's client ID.

### 2. Configure onebox

Add to your onebox `values.yaml`:

```yaml
authMetadata:
  externalAuthServerBaseUrl: <issuer URL>
  flyteClient:
    clientId: <CLI application client ID>
identity:
  logoutRedirect: /oauth2/sign_out
networkPolicy:
  proxyFrom:
    - podSelector:
        matchLabels:
          app: oauth2-proxy
```

If your IdP publishes only OIDC discovery (`/.well-known/openid-configuration`) and not OAuth 2.0 authorization server metadata, as Google and Microsoft Entra ID do, also set `authMetadata.externalMetadataUrl: .well-known/openid-configuration`.

Run `helm upgrade` with the new values.

### 3. Deploy oauth2-proxy

Deploy oauth2-proxy in onebox's namespace with these arguments:

```yaml
args:
  - --provider=oidc
  - --oidc-issuer-url=<issuer URL>
  - --client-id=<web application client ID>
  - --client-secret=<web application client secret>
  - --cookie-secret=<32 random bytes>          # openssl rand -hex 16
  - --redirect-url=https://<host>/oauth2/callback
  - --email-domain=*
  - --scope=openid email profile
  - --code-challenge-method=S256
  - --upstream=http://onebox.union.svc:80
  # Forward the user to onebox in X-Forwarded-User, -Email, -Preferred-Username and -Groups.
  - --pass-user-headers=true
  # Let the SDK and CLI find the IdP before they have a token.
  - --skip-auth-route=^/flyteidl2\.auth\.AuthMetadataService/
  - --skip-auth-route=^/\.well-known/oauth-authorization-server$
  # Accept the IdP's tokens from the SDK and CLI.
  - --skip-jwt-bearer-tokens=true
  # Answer API calls without a token with 401, not a redirect to the sign-in page:
  # the SDK and CLI send their first call without a token and sign in on a 401.
  - --api-route=^/(flyteidl|flyteidl2|cloudidl)\.
  - --api-route=^/api/
  - --oidc-extra-audience=<audience>
  - --skip-provider-button=true
  # Only with OAuth apps: their client-credentials tokens carry no email.
  # - --insecure-oidc-allow-unverified-email=true
```

`<audience>` is the `aud` claim in the tokens the CLI application gets. That is usually its client ID; Okta's custom authorization servers use the server's audience, such as `api://default`. On Keycloak, add an audience mapper to a default client scope so every token, including those of [OAuth apps](./oauth-apps), carries the same audience. If the CLI's tokens come from a different issuer than oauth2-proxy's own sign-in, use `--extra-jwt-issuers=<issuer URL>=<audience>` instead.

The SDK sends tokens only over TLS, so serve oauth2-proxy over HTTPS in one of two ways:

- **Behind a gateway or load balancer that terminates TLS** (most common). Add `--reverse-proxy=true` so oauth2-proxy trusts the `X-Forwarded-*` headers the gateway sets; it passes `X-Forwarded-Proto` on to onebox. For example, with any [Gateway API](https://gateway-api.sigs.k8s.io/) implementation:

  ```yaml
  apiVersion: gateway.networking.k8s.io/v1
  kind: Gateway
  metadata:
    name: onebox
    namespace: union
  spec:
    gatewayClassName: <your gateway class>
    listeners:
      - name: https
        protocol: HTTPS
        port: 443
        hostname: <host>
        tls:
          mode: Terminate
          certificateRefs: [{name: <tls secret>}]
  ---
  apiVersion: gateway.networking.k8s.io/v1
  kind: HTTPRoute
  metadata:
    name: onebox
    namespace: union
  spec:
    parentRefs: [{name: onebox, sectionName: https}]
    hostnames: [<host>]
    rules:
      - backendRefs: [{name: oauth2-proxy, port: 80}]
  ```

  oauth2-proxy's session cookie can be several kilobytes; if your gateway limits request header sizes, allow at least 16 KB. If your gateway doesn't set `X-Forwarded-Proto`, also set `publicScheme: https` in onebox's values.

- **With its own certificate** (`--https-address` and `--tls-cert-file`). Nothing sets `X-Forwarded-Proto` then, so also set `publicScheme: https` in onebox's values.

Expose oauth2-proxy at `<host>`, and only oauth2-proxy: onebox's Service stays `ClusterIP`.

### 4. Sign in

Open `https://<host>/v2`: you sign in at the IdP and land in the UI.

Point the CLI at the same address, without `--insecure`:

```shell
flyte create config --endpoint <host> --org onebox --project default --domain development
flyte run hello.py main
```

The first command opens a browser to sign in at the IdP. After that the CLI refreshes its token itself.

If `<host>`'s certificate is issued by a private CA, point the CLI at the CA certificate in `.flyte/config.yaml`:

```yaml
admin:
  endpoint: dns:///<host>
  caCertFilePath: /path/to/ca.pem
```

### Sign out

Sign out in the UI goes to `/oauth2/sign_out`, which ends the oauth2-proxy session. Your IdP's session stays, so the next visit signs the user straight back in. To end it too, redirect to the IdP's logout page from there:

```yaml
identity:
  logoutRedirect: /oauth2/sign_out?rd=<url-encoded IdP logout URL>
```

and allow that domain in oauth2-proxy with `--whitelist-domain=<IdP domain>`.

## AWS ALB

On EKS, an Application Load Balancer can do the sign-in itself: it challenges browsers with OIDC and validates the SDK's tokens. The [AWS Load Balancer Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/) builds it from a Gateway and one HTTPRoute with three rules:

| Rule | Matches | Auth |
|---|---|---|
| Discovery | The two discovery paths | None, so the SDK can find the IdP |
| API | Requests with `Authorization: Bearer …` | ALB validates the token (JWT validation) |
| Browser | Everything else | ALB signs the browser in (OIDC) |

### Prerequisites

- The AWS Load Balancer Controller v3.5.0 or later, with the [Gateway API CRDs and its own Gateway CRDs](https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/guide/gateway/gateway/#prerequisites) installed. Its ALB Gateway controller starts when they are.
- An ACM certificate for `<host>`. ALB authenticates only on HTTPS listeners.
- Two applications at your IdP, as for [oauth2-proxy](#1-register-two-applications-at-your-idp), except the web application's redirect URI is `https://<host>/oauth2/idpresponse`.

Store the web application's credentials where the controller can read them, in onebox's namespace, with exactly these keys:

```shell
kubectl -n union create secret generic onebox-oidc \
  --from-literal=clientID='<web application client ID>' \
  --from-literal=clientSecret='<web application client secret>'
```

### 1. Configure onebox

ALB forwards the browser's identity as a signed JWT in `X-Amzn-Oidc-Data`, and passes the SDK's token through in `Authorization`. Read identity from those two only, and empty the header lists, since ALB doesn't set those headers:

```yaml
identity:
  subjectHeaders: []
  emailHeaders: []
  nameHeaders: []
  groupsHeaders: []
  claimsJWTHeaders: [Authorization, X-Amzn-Oidc-Data]
  logoutRedirect: <IdP logout URL>
  # ALB has no sign-out endpoint: onebox expires its session cookies.
  logoutClearCookies:
    - AWSELBAuthSessionCookie-0
    - AWSELBAuthSessionCookie-1
    - AWSELBAuthSessionCookie-2
    - AWSELBAuthSessionCookie-3
authMetadata:
  externalAuthServerBaseUrl: <issuer URL>
  flyteClient:
    clientId: <CLI application client ID>
networkPolicy:
  proxyFrom:
    - ipBlock:
        cidr: <VPC CIDR>
```

Onebox reads the first of the two JWT headers present. Every request that carries `Authorization: Bearer` takes the API rule, where ALB has validated the token; every other request has been signed in by ALB, which sets `X-Amzn-Oidc-Data` itself.

### 2. Create the Gateway

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: aws-alb
spec:
  controllerName: gateway.k8s.aws/alb
---
apiVersion: gateway.k8s.aws/v1
kind: LoadBalancerConfiguration
metadata:
  name: onebox
  namespace: union
spec:
  scheme: internet-facing
  listenerConfigurations:
    - protocolPort: HTTPS:443
      defaultCertificate: <ACM certificate ARN>
---
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: onebox
  namespace: union
spec:
  gatewayClassName: aws-alb
  infrastructure:
    parametersRef:
      group: gateway.k8s.aws
      kind: LoadBalancerConfiguration
      name: onebox
  listeners:
    - name: https
      protocol: HTTPS
      port: 443
      hostname: <host>
---
# Targets are onebox's pods, health-checked on /healthz: onebox answers / with
# a redirect, which ALB counts as unhealthy.
apiVersion: gateway.k8s.aws/v1
kind: TargetGroupConfiguration
metadata:
  name: onebox
  namespace: union
spec:
  targetReference:
    name: onebox
  defaultConfiguration:
    targetType: ip
    healthCheckConfig:
      healthCheckPath: /healthz
```

Skip the GatewayClass if your cluster already has one for `gateway.k8s.aws/alb`, and use its name.

### 3. Create the route

The two authentication steps are ListenerRuleConfigurations, attached to their rules as filters. ALB orders the rules by how specific they are: the discovery paths first, then the rule that also matches the `Authorization` header, then the rest.

```yaml
apiVersion: gateway.k8s.aws/v1
kind: ListenerRuleConfiguration
metadata:
  name: onebox-api
  namespace: union
spec:
  actions:
    - type: jwt-validation
      jwtValidationConfig:
        jwksEndpoint: <IdP JWKS URL>
        issuer: <issuer URL>
---
apiVersion: gateway.k8s.aws/v1
kind: ListenerRuleConfiguration
metadata:
  name: onebox-browser
  namespace: union
spec:
  actions:
    - type: authenticate-oidc
      authenticateOIDCConfig:
        issuer: <issuer URL>
        authorizationEndpoint: <authorize URL>
        tokenEndpoint: <token URL>
        userInfoEndpoint: <userinfo URL>
        scope: openid email profile
        onUnauthenticatedRequest: authenticate
        secret:
          name: onebox-oidc
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: onebox
  namespace: union
spec:
  parentRefs: [{name: onebox, sectionName: https}]
  hostnames: [<host>]
  rules:
    # Discovery: no authentication.
    - matches:
        - path: {type: Exact, value: /.well-known/oauth-authorization-server}
        - path: {type: PathPrefix, value: /flyteidl2.auth.AuthMetadataService}
      backendRefs: [{name: onebox, port: 80}]
    # The SDK and CLI: ALB validates the bearer token.
    - matches:
        - path: {type: PathPrefix, value: /}
          headers:
            - name: Authorization
              type: RegularExpression
              value: "^Bearer .+"
      filters:
        - type: ExtensionRef
          extensionRef: {group: gateway.k8s.aws, kind: ListenerRuleConfiguration, name: onebox-api}
      backendRefs: [{name: onebox, port: 80}]
    # Browsers: ALB signs them in.
    - matches:
        - path: {type: PathPrefix, value: /}
      filters:
        - type: ExtensionRef
          extensionRef: {group: gateway.k8s.aws, kind: ListenerRuleConfiguration, name: onebox-browser}
      backendRefs: [{name: onebox, port: 80}]
```

The issuer, JWKS, authorize, token, and userinfo URLs are in your IdP's discovery document, `<issuer URL>/.well-known/openid-configuration`.

ALB's JWT validation checks the token's signature, issuer, and expiry. To accept only tokens minted for the CLI application, also check their audience: add `additionalClaims: [{name: aud, format: single-string, values: [<audience>]}]` to `jwtValidationConfig`.

### 4. Sign in

Point DNS for `<host>` at the ALB (the Gateway's address), then sign in as in [oauth2-proxy](#4-sign-in): the UI at `https://<host>/v2`, and the CLI with `flyte create config --endpoint <host>`.

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| The UI loads, but every API call returns `401` | Onebox doesn't see the identity headers. Check that `identity.*` names the headers your proxy sets, and, with `identity.proxySecret`, that the proxy sends the secret. |
| The CLI says the endpoint doesn't support authentication, or skips sign-in | `authMetadata.externalAuthServerBaseUrl` isn't set, the proxy requires a login on the discovery paths, or the CLI config has `insecure: true`. |
| The CLI signs in, then API calls are redirected to the IdP or return `401` | The proxy doesn't accept the token. For oauth2-proxy, check that `--oidc-extra-audience` (or `--extra-jwt-issuers`) matches the token's `aud`; its log names the audience it expected. For ALB, check the `jwtValidationConfig` issuer and JWKS URL. |
| An OAuth app's token is redirected to the IdP, and oauth2-proxy logs `email in id_token ... isn't verified` | Client-credentials tokens have no email. Add `--insecure-oidc-allow-unverified-email=true`. |
| `flyte run` fails while uploading the code bundle, behind a proxy that terminates TLS itself | Onebox gave the SDK an `http://` address. Set `publicScheme: https`. |
| ALB targets are unhealthy | The health check path isn't `/healthz`. |
| ALB: the Gateway or HTTPRoute reports that it can't read secret `onebox-oidc` | The AWS Load Balancer Controller can't read Secrets in onebox's namespace. Grant its service account `get`, `list`, and `watch` on Secrets there. |
