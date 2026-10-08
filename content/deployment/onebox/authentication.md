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
  - --extra-jwt-issuers=<issuer URL>=<audience>
  - --skip-provider-button=true
```

`<audience>` is the `aud` claim in the tokens the CLI application gets. That is usually its client ID; Okta's custom authorization servers use the server's audience, such as `api://default`.

The SDK sends tokens only over TLS, so serve oauth2-proxy over HTTPS in one of two ways:

- **Behind an ingress or load balancer that terminates TLS** (most common). Add `--reverse-proxy=true` so oauth2-proxy trusts the `X-Forwarded-*` headers the ingress sets; it passes `X-Forwarded-Proto` on to onebox. For example, with ingress-nginx:

  ```yaml
  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    name: onebox
    namespace: union
    annotations:
      nginx.ingress.kubernetes.io/proxy-buffer-size: 16k   # oauth2-proxy's session cookie
      nginx.ingress.kubernetes.io/proxy-body-size: "0"
  spec:
    ingressClassName: nginx
    tls: [{hosts: [<host>], secretName: <tls secret>}]
    rules:
      - host: <host>
        http:
          paths:
            - path: /
              pathType: Prefix
              backend: {service: {name: oauth2-proxy, port: {number: 80}}}
  ```

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

On EKS, an Application Load Balancer can do the sign-in itself: it challenges browsers with OIDC and validates the SDK's tokens. You define three Ingresses that share one ALB:

| Ingress | Matches | Auth |
|---|---|---|
| `onebox-discovery` | The two discovery paths | None, so the SDK can find the IdP |
| `onebox-api` | Requests with `Authorization: Bearer …` | ALB validates the token (JWT validation) |
| `onebox` | Everything else | ALB signs the browser in (OIDC) |

### Prerequisites

- The [AWS Load Balancer Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/) v2.16 or later. JWT validation needs it.
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

Onebox reads the first of the two JWT headers present. Every request that carries `Authorization: Bearer` is routed to `onebox-api`, where ALB has validated the token; every other request has been signed in by ALB, which sets `X-Amzn-Oidc-Data` itself.

### 2. Create the Ingresses

Annotations every Ingress needs (repeat them in each):

```yaml
alb.ingress.kubernetes.io/group.name: onebox
alb.ingress.kubernetes.io/scheme: internet-facing
alb.ingress.kubernetes.io/target-type: ip
alb.ingress.kubernetes.io/listen-ports: '[{"HTTPS": 443}]'
alb.ingress.kubernetes.io/certificate-arn: <ACM certificate ARN>
alb.ingress.kubernetes.io/healthcheck-path: /healthz
```

The health check path matters: onebox answers `/` with a redirect, which ALB counts as unhealthy.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: onebox-discovery
  namespace: union
  annotations:
    # ... the common annotations ...
    alb.ingress.kubernetes.io/group.order: "1"
spec:
  ingressClassName: alb
  rules:
    - host: <host>
      http:
        paths:
          - path: /.well-known/oauth-authorization-server
            pathType: Exact
            backend: {service: {name: onebox, port: {number: 80}}}
          - path: /flyteidl2.auth.AuthMetadataService
            pathType: Prefix
            backend: {service: {name: onebox, port: {number: 80}}}
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: onebox-api
  namespace: union
  annotations:
    # ... the common annotations ...
    alb.ingress.kubernetes.io/group.order: "2"
    alb.ingress.kubernetes.io/conditions.onebox: '[{"field":"http-header","httpHeaderConfig":{"httpHeaderName":"Authorization","values":["Bearer*"]}}]'
    alb.ingress.kubernetes.io/jwt-validation: '{"jwksEndpoint":"<IdP JWKS URL>","issuer":"<issuer URL>"}'
spec:
  ingressClassName: alb
  rules:
    - host: <host>
      http:
        paths:
          - path: /
            pathType: Prefix
            backend: {service: {name: onebox, port: {number: 80}}}
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: onebox
  namespace: union
  annotations:
    # ... the common annotations ...
    alb.ingress.kubernetes.io/group.order: "3"
    alb.ingress.kubernetes.io/auth-type: oidc
    alb.ingress.kubernetes.io/auth-scope: openid email profile
    alb.ingress.kubernetes.io/auth-on-unauthenticated-request: authenticate
    alb.ingress.kubernetes.io/auth-idp-oidc: '{"issuer":"<issuer URL>","authorizationEndpoint":"<authorize URL>","tokenEndpoint":"<token URL>","userInfoEndpoint":"<userinfo URL>","secretName":"onebox-oidc"}'
spec:
  ingressClassName: alb
  rules:
    - host: <host>
      http:
        paths:
          - path: /
            pathType: Prefix
            backend: {service: {name: onebox, port: {number: 80}}}
```

The issuer, JWKS, authorize, token, and userinfo URLs are in your IdP's discovery document, `<issuer URL>/.well-known/openid-configuration`.

ALB's JWT validation checks the token's signature, issuer, and expiry. To accept only tokens minted for the CLI application, also check their audience by adding `"additionalClaims":[{"name":"aud","format":"single-string","values":["<audience>"]}]` to `jwt-validation`.

### 3. Sign in

Point DNS for `<host>` at the ALB, then sign in as in [oauth2-proxy](#4-sign-in): the UI at `https://<host>/v2`, and the CLI with `flyte create config --endpoint <host>`.

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| The UI loads, but every API call returns `401` | Onebox doesn't see the identity headers. Check that `identity.*` names the headers your proxy sets, and, with `identity.proxySecret`, that the proxy sends the secret. |
| The CLI says the endpoint doesn't support authentication, or skips sign-in | `authMetadata.externalAuthServerBaseUrl` isn't set, the proxy requires a login on the discovery paths, or the CLI config has `insecure: true`. |
| The CLI signs in, then API calls are redirected to the IdP or return `401` | The proxy doesn't accept the token. For oauth2-proxy, check that `--extra-jwt-issuers` has the token's issuer and `aud`. For ALB, check the `jwt-validation` issuer and JWKS URL. |
| `flyte run` fails while uploading the code bundle, behind a proxy that terminates TLS itself | Onebox gave the SDK an `http://` address. Set `publicScheme: https`. |
| ALB targets are unhealthy | The health check path isn't `/healthz`. |
| ALB: `FailedBuildModel … secrets "onebox-oidc" is forbidden` on the Ingress | The AWS Load Balancer Controller can't read Secrets in onebox's namespace. Grant its service account `get`, `list`, and `watch` on Secrets there. |
