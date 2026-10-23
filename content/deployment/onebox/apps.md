---
title: Apps and LLM gateways
description: Serve Union apps from onebox on Knative Serving, and run LLM gateways on them.
icon: window-stack
weight: 9
variants: -flyte +union
---

# Apps and LLM gateways

Onebox serves [apps](../../user-guide/apps/_index) the way a Union data plane does: each app runs as a Knative Service in onebox's namespace, created and updated by the app controller inside onebox. You install Knative Serving beside onebox. Onebox starts without it, and apps stay off until you turn them on.

LLM gateways are apps too, so they come with apps.

## How a request reaches an app

Each app gets a URL from `serving.publicURLPattern`, for example `https://quiet-river-1a2b3.apps.onebox.example.com`. Point a wildcard DNS record for those hosts at the same proxy or load balancer as onebox, so their requests arrive at onebox's port. Onebox forwards every app host to the apps gateway the chart installs beside it: Union's Kourier and Envoy, as a Union data plane runs them. The gateway routes the request to the app, and its union-apps filter decides who may call it, as in Union's hosted service:

- An app that allows anonymous callers gets every request, including its `Authorization` header (an LLM gateway's virtual key, for example).
- Any other app needs a signed-in caller. The filter asks onebox who the caller is, from the token the proxy in front of onebox passed on, and whether they may use the app. The app receives the caller's identity as `x-user-*` headers.

Onebox doesn't check that token itself: authenticating callers is the proxy's job, for app hosts as for onebox.

## 1. Install Knative Serving

Install Knative Serving 1.16 and make Kourier its networking layer. The onebox chart installs Kourier itself, so don't apply Kourier's own manifest:

```shell
kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.16.0/serving-crds.yaml
kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.16.0/serving-core.yaml
kubectl patch configmap/config-network -n knative-serving --type merge \
  -p '{"data":{"ingress-class":"kourier.ingress.networking.knative.dev"}}'
```

Then turn on the Knative features apps use. Union's app controller sets affinity, tolerations, environment values from pod fields and more on each app, and Knative rejects those unless they're enabled:

```shell
kubectl patch configmap/config-features -n knative-serving --type merge -p '{"data":{
  "kubernetes.podspec-affinity":"enabled",
  "kubernetes.podspec-dnsconfig":"enabled",
  "kubernetes.podspec-dnspolicy":"enabled",
  "kubernetes.podspec-fieldref":"enabled",
  "kubernetes.podspec-hostaliases":"enabled",
  "kubernetes.podspec-init-containers":"enabled",
  "kubernetes.podspec-nodeselector":"enabled",
  "kubernetes.podspec-persistent-volume-claim":"enabled",
  "kubernetes.podspec-persistent-volume-write":"enabled",
  "kubernetes.podspec-priorityclassname":"enabled",
  "kubernetes.podspec-runtimeclassname":"enabled",
  "kubernetes.podspec-schedulername":"enabled",
  "kubernetes.podspec-securitycontext":"enabled",
  "kubernetes.containerspec-addcapabilities":"enabled",
  "kubernetes.podspec-shareprocessnamespace":"enabled",
  "kubernetes.podspec-tolerations":"enabled",
  "kubernetes.podspec-topologyspreadconstraints":"enabled",
  "kubernetes.podspec-volumes-emptydir":"enabled",
  "kubernetes.podspec-volumes-hostpath":"enabled"}}'
```

If your apps use images from a registry Knative can't reach over HTTPS, add it to `registries-skipping-tag-resolving` in the `config-deployment` ConfigMap.

For an airgapped install, mirror Knative's images along with onebox's and Union's Kourier images (`serving.gateway.controller.image`, `serving.gateway.envoy.image`).

## 2. Let the proxy pass the user's token

The gateway's filter asks onebox who's calling from the `Authorization` header, so the proxy in front of onebox must authenticate app hosts too and pass the signed-in user's token on. With oauth2-proxy, add `--pass-authorization-header=true` and a cookie domain that covers the app hosts, such as `--cookie-domain=.onebox.example.com` with `--whitelist-domain=.onebox.example.com`.

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

Upgrade onebox with these values. The chart installs Union's Kourier controller and Envoy gateway in onebox's namespace, adds `config-kourier` to Knative's namespace (`serving.knativeNamespace`), and adds the Knative permissions to onebox's Role. With network policy on, only the gateway reaches onebox's port 8083, and only onebox reaches the gateway.

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

With apps on, the **LLM Gateway** pages appear in the UI. A gateway's backing app runs in the `system` project, which onebox creates, and talks to onebox over the in-cluster tasks port. Create the provider secrets the gateway uses as [secrets](../../user-guide/tasks/task-configuration/secrets) first.

The gateway's image, `ghcr.io/unionai/union-llm-gateway`, must be pullable from your cluster, or mirrored for an airgapped install.

## Limitations

- Knative Serving is the only way onebox runs apps.
- Onebox's local image runs Union's Kourier with the union-apps filter off: apps there are routed but not authorized per app.
- Apps and gateways were verified on a onebox whose apps run on a Union cluster through a test bridge rather than on Knative in the same cluster. Serving, the app's URL through onebox, status in the UI, and a gateway's policy sync and virtual keys all worked. Provider secrets reaching a gateway's pods weren't covered.
