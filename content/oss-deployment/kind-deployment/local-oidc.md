---
title: Set up local OIDC provider
variants: +flyte -union
weight: 1
---

# Set up local OIDC provider

[Step 7 of the Kind deployment guide](_index#7-add-authentication-with-a-local-idp-optional)
gates the console behind Traefik and oauth2-proxy, using [Dex](https://dexidp.io/)
running **inside the same kind cluster** as the identity provider, so you can test the
whole authentication flow with no cloud account and no real users. This page covers
deploying Dex itself: do it after
[installing Traefik](_index#install-the-ingress-controller) and before
[deploying oauth2-proxy](_index#deploy-oauth2-proxy).

> [!WARNING] For local testing only
> Dex here uses in-memory storage and a static test password baked into its config.
> It is an IdP stand-in for development. Never use this configuration anywhere real.

## The issuer-URL problem

OIDC has one constraint that shapes the Dex setup: the **issuer URL must be identical**
everywhere it's seen.

- **oauth2-proxy** (running in-cluster) reaches Dex over a Kubernetes service name.
- **Your browser** reaches Dex to log in, and must land on the *same* issuer the token
  was minted for, or validation fails.

A service name like `dex.flyte.svc.cluster.local` isn't resolvable from your browser; a
`localhost` URL isn't resolvable from inside the cluster. The fix is to serve Dex under
the **same host as Flyte** (`flyte.local`) at a sub-path (`/dex`), and route to it
through Traefik. One URL, `http://flyte.local/dex`, works from both sides.

## Dex configuration

The issuer is the through-Traefik URL; the two static clients are oauth2-proxy
(confidential, with a secret) and the Flyte CLI (public, for SDK login).
`staticPasswords` gives you a login with no external user store.

The Dex Helm chart renders whatever you pass under its `config` value into a Secret and
mounts it as `config.yaml`, so write the configuration nested under a top-level
`config:` key in a values file:

```yaml
# dex-values.yaml
config:
  issuer: http://flyte.local/dex

  storage:
    type: memory

  web:
    http: 0.0.0.0:5556

  oauth2:
    skipApprovalScreen: true        # auto-approve, no consent screen in dev

  staticClients:
    # oauth2-proxy — confidential client (matches the secret you pass to oauth2-proxy in step 7)
    - id: oauth2-proxy
      name: oauth2-proxy
      secret: oauth2-proxy-secret
      redirectURIs:
        - 'http://flyte.local/oauth2/callback'
        - 'https://flyte.local/oauth2/callback'   # console opened over TLS (websecure)

    # Flyte CLI — public client for SDK/CLI PKCE login
    - id: flytectl
      name: 'Flyte CLI'
      public: true
      redirectURIs:
        - 'http://localhost:53593/callback'

  enablePasswordDB: true
  staticPasswords:
    # login: admin@example.com / password
    - email: "admin@example.com"
      username: "admin"
      userID: "08a8684b-db88-4b73-90a9-3cd1661f5466"
      # bcrypt hash of the literal string "password" — see the note below
      hash: "$2a$10$wi77Jcsjw08l416Q4./OCu6qNvYMaNSvA3Jbo30QeyZAvq9b4BSRK"
```

> [!WARNING] `hash` must be a real bcrypt hash
> Dex validates the hash at startup and crashes (`CrashLoopBackOff`) with
> `malformed bcrypt hash: hashedSecret too short to be a bcrypted password` if it
> isn't a complete 60-character bcrypt string. The hash above is for `password` and
> is known-good, but verify length 60 before pasting (`echo -n "$HASH" | wc -c`); a
> char lost in transit looks fine and crashes Dex. To use a different password:
> ```bash
> htpasswd -bnBC 10 "" 'your-password' | tr -d ':\n' | sed 's/^\$2y/\$2a/'
> ```

## Install Dex

```bash
helm repo add dex https://charts.dexidp.io
helm repo update

helm install dex dex/dex -n flyte -f dex-values.yaml
```

> [!NOTE] Why not a ConfigMap volume mount
> The chart already defines its own `config` volume, so mounting your own with
> `--set volumes[0].name=config` collides with it (`Duplicate value: "config"`). Passing
> the config under the chart's `config` value, as above, is the supported path and avoids
> the clash.

Confirm Dex came up:

```bash
kubectl -n flyte rollout status deploy/dex
kubectl -n flyte get svc dex          # note the port (5556 by default)
```

## Route the issuer path through Traefik

Add an ingress so `http://flyte.local/dex` reaches the Dex service. This is what makes
the single issuer URL resolve from the browser:

```yaml
# dex-ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: dex
  namespace: flyte
spec:
  ingressClassName: traefik
  rules:
  - host: flyte.local
    http:
      paths:
      - path: /dex
        pathType: Prefix
        backend:
          service:
            name: dex
            port:
              number: 5556
```

```bash
kubectl apply -f dex-ingress.yaml
```

Check discovery works through the host path. This is the URL oauth2-proxy will fetch:

```bash
# (with "127.0.0.1 flyte.local" in /etc/hosts and Traefik reachable on the node port)
curl -s http://flyte.local/dex/.well-known/openid-configuration | head
```

A JSON document with `"issuer":"http://flyte.local/dex"` confirms Dex is reachable at
the issuer it advertises.

## Next step

With Dex up and its issuer routable, return to the Kind deployment guide and
[deploy oauth2-proxy](_index#deploy-oauth2-proxy) pointed at `http://flyte.local/dex`.
