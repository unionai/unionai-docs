---
title: Apps and LLM gateways
description: Serve Union apps from onebox on Knative Serving, and run LLM gateways on them.
icon: window-stack
weight: 9
variants: -flyte +union
---

# Apps and LLM gateways

[Apps](../../user-guide/apps/_index) let you serve HTTP services, such as model endpoints and dashboards, beside your workflows. Turn them on with `serving.enabled`: the chart then runs Knative Serving, which runs each app in onebox's namespace, and a gateway that routes requests to them. Apps are off until you turn them on.

LLM gateways, which give your users one place to reach language model providers, run as apps, so they need apps on too.

## How a request reaches an app

Each app gets a URL from `serving.publicURLPattern`, for example `https://quiet-river-1a2b3.apps.onebox.example.com`. Point a wildcard DNS record for those hosts at the same proxy or load balancer as onebox, so their requests arrive at onebox's port, or serve apps [under a path](#apps-under-a-path) instead. Onebox forwards every app request to the gateway the chart installs. The gateway routes the request to the app and checks who may call it:

- An app that allows anonymous callers gets every request, including its `Authorization` header, for example the key a client uses to call an LLM gateway.
- Any other app needs a signed-in caller. The gateway asks onebox who the caller is, from the token the proxy in front of onebox passed on, and whether they may use the app. It then removes that token, and the app receives the caller's identity as `x-user-*` headers.

Onebox doesn't check that token itself: authenticating callers is the proxy's job, for app hosts as for onebox.

## 1. Knative Serving

The chart runs Knative Serving 1.23 in onebox's namespace, configured to run Union apps. Each Knative component runs one replica with small requests; change replicas, images, resources, and scheduling under `serving.knative.components`. Override any of Knative's `config-*` settings under `serving.knative.config`.

Knative's CRDs are in the chart's `crds/` directory, so Helm installs them with the chart, even with apps off. Helm never upgrades or deletes them. If you install with `helm install --skip-crds`, apply them yourself:

```shell
helm pull unionai/onebox --untar
kubectl apply --server-side -f onebox/crds/
```

A cluster runs one Knative Serving. If yours already runs it, set `serving.knative.install: false` and `serving.knativeNamespace` to its namespace (`knative-serving` by default). The chart then adds `config-kourier` to that namespace. Make these changes to your Knative's own ConfigMaps:

- `config-network`: set `ingress-class` to `kourier.ingress.networking.knative.dev`.
- `config-features`: enable the features listed under `serving.knative.config.features` in the chart's values.
- `config-deployment`: with the [image builder](./image-builder), add its registry to `registries-skipping-tag-resolving`.

For an airgapped install, mirror Knative's images (`gcr.io/knative-releases`) along with onebox's [images](./_index#images), including the gateway's `ghcr.io/unionai/envoy` (`serving.gateway.envoy.image`). Set each component's image under `serving.knative.components.<component>.containers.<component>.image`.

## 2. Let the proxy pass the user's token

The gateway's filter asks onebox who's calling from the `Authorization` header, so the proxy in front of onebox must authenticate app hosts too and pass the signed-in user's token on. With oauth2-proxy, add `--pass-authorization-header=true` and a cookie domain that covers the app hosts, such as `--cookie-domain=.onebox.example.com` with `--whitelist-domain=.onebox.example.com`. [Apps under a path](#apps-under-a-path) of onebox's own host need no cookie domain.

### Apps that allow anonymous callers

The proxy signs in everyone who reaches it, so an app that allows anonymous callers is only open to the world once its host bypasses the proxy. oauth2-proxy can't skip sign-in by host, so route the host past it to onebox's Service, which still forwards it to the gateway. With a Gateway API gateway in front of oauth2-proxy, a route for the exact host wins over the wildcard:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: llm-gateway-app
  namespace: union
spec:
  parentRefs: [{name: <gateway>, namespace: <gateway namespace>}]
  hostnames: ["quiet-river-1a2b3.apps.onebox.example.com"]
  rules:
    - backendRefs: [{name: onebox, port: 80}]
```

With [network policy](./authorization#network-policy) on, add the gateway's pods to `networkPolicy.proxyFrom` too. On an AWS ALB, add a listener rule for the host, at a higher priority than the sign-in rules, that forwards to onebox without authenticating.

Onebox serves such a host only as the app: whatever path or headers a caller sends, the request goes to the gateway with identity headers removed, and the gateway's filter still guards any app that isn't anonymous.

## 3. Turn on apps

```yaml
serving:
  enabled: true
  publicURLPattern: https://%s.apps.onebox.example.com
  gateway:
    auth:
      signInURL: https://onebox.example.com/oauth2/start
authMetadata:
  externalAuthServerBaseUrl: <issuer URL>
```

The first `%s` is the app's subdomain; an optional second `%s` is the organization. `signInURL` is where a caller without a session is sent to sign in: the proxy's sign-in page. The filter reads onebox's OAuth2 metadata when the gateway starts, so `authMetadata.externalAuthServerBaseUrl` must be set (see [authentication](./authentication)).

Upgrade onebox with these values. The chart installs Knative Serving and the gateway in onebox's namespace, and adds the Knative permissions to onebox's Role. With network policy on, only the gateway reaches onebox's port 8083, and only onebox and the Kourier controller reach the gateway.

### Apps under a path

With [`basePath`](./kubernetes#serve-under-a-path-of-a-shared-host) set, apps can share onebox's host instead of needing wildcard DNS, each under its own path:

```yaml
basePath: /onebox
serving:
  enabled: true
  publicURLPattern: https://platform.example.com/onebox/apps/%s/
```

The path must be `<basePath>/apps/%s/`. Everything else under `basePath` belongs to onebox (the UI and its REST routes), and onebox refuses to start with apps anywhere they would shadow it. Requests reach an app with its path intact, and the app finds the path in `_U_APP_BASE_PATH`. The SDK's FastAPI and Streamlit apps serve under it on their own; pass it to other servers, such as Jupyter's `base_url`. For servers that only serve at `/`, set `serving.stripAppPathPrefix: true`: the path is removed before the request reaches the app, and sent as `X-Forwarded-Prefix`.

> [!WARNING] Apps on onebox's host share its origin
> Path-based apps on the host that serves the UI share its origin with the UI and everything else on that host. An app's script can make requests as the user who opens the app, so use them only for apps whose authors you trust as much as the platform.

To keep apps apart without wildcard DNS, give them a host of their own and set `serving.appHostOnly`:

```yaml
serving:
  publicURLPattern: https://apps.example.com/onebox/apps/%s/
  appHostOnly: true
```

That host then serves apps and nothing else, and onebox's own host serves no apps. Point it at the same proxy as onebox. Host-based app URLs, as in [Turn on apps](#3-turn-on-apps), keep apps apart too.

In every mode, onebox never passes the user's session cookie or the proxy's shared secret to an app, and an app can't set the session cookie. For an app that needs a signed-in caller, the gateway removes the caller's token once it has authorized them. An app that allows anonymous callers keeps the request's `Authorization` header.

## 4. Serve an app

```python
import flyte
import flyte.app

app = flyte.app.AppEnvironment(
    name="hello-app",
    image="python:3.12-slim",
    command=["python", "-m", "http.server", "8080"],
    port=8080,
    requires_auth=False,
)

flyte.init_from_config()
print(flyte.serve(app).endpoint)
```

The app shows in the UI under **Apps**, and answers at the printed URL once it's active.

## LLM gateways

With apps on, the **LLM Gateway** pages appear in the UI. Gateway apps run in the `system` project, which onebox creates. Before creating a gateway, create the provider credentials it uses as [secrets](../../user-guide/tasks/task-configuration/secrets).

The gateway's image, `ghcr.io/unionai/union-llm-gateway`, must be pullable from your cluster, or mirrored for an airgapped install.

## Limitations

- Onebox runs apps only on Knative Serving.
- On your machine (`flyte start onebox --with apps`), apps aren't checked per caller: anyone who can reach the UI can call any app. Use it only for local evaluation.
