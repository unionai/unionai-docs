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

Each app gets a URL from `serving.publicURLPattern`, for example `https://quiet-river-1a2b3.apps.onebox.example.com`. Point a wildcard DNS record for those hosts at the same proxy or load balancer as onebox, so their requests arrive at onebox's port. Onebox forwards every app host to the apps gateway in the cluster: Union's Kourier and Envoy, as a Union data plane runs them. The gateway routes the request to the app, and its union-apps filter decides who may call it, as in Union's hosted service:

- An app that allows anonymous callers gets every request, including its `Authorization` header (an LLM gateway's virtual key, for example).
- Any other app needs a signed-in caller. The filter asks onebox who the caller is, from the token the proxy in front of onebox passed on, and whether they may use the app. The app receives the caller's identity as `x-user-*` headers.

Onebox doesn't check that token itself: authenticating callers is the proxy's job, for app hosts as for onebox.

## 1. Install Knative Serving

Install Knative Serving 1.16 with Kourier as its networking layer:

```shell
kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.16.0/serving-crds.yaml
kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.16.0/serving-core.yaml
kubectl apply -f https://github.com/knative/net-kourier/releases/download/knative-v1.16.0/kourier.yaml
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

## 2. Switch to Union's Kourier and Envoy

Union's Kourier controller routes each app by the hosts onebox gives it and adds the union-apps filter to the gateway; Union's Envoy carries the filter. Use the images of a Union data plane release (`VERSION` below: the controller is `/bin/kourier` in Union's operator image), and point the filter at onebox's gateway port, 8083. Replace `onebox.onebox` with your release's Service and namespace:

```shell
VERSION=2026.10.0
ONEBOX=http://onebox.onebox.svc.cluster.local:8083

kubectl -n knative-serving patch deployment net-kourier-controller --type json -p '[
  {"op":"replace","path":"/spec/template/spec/containers/0/image","value":"public.ecr.aws/p0i0a9q8/unionoperator:'$VERSION'"},
  {"op":"add","path":"/spec/template/spec/containers/0/command","value":["/bin/kourier"]}]'
kubectl -n knative-serving set env deployment/net-kourier-controller KOURIER_UNION_APPS_ENABLED=true

kubectl -n kourier-system set image deployment/3scale-kourier-gateway \
  kourier-gateway=public.ecr.aws/unionai/envoy:$VERSION
kubectl -n kourier-system set env deployment/3scale-kourier-gateway \
  UNION_AUTH_TENANTAUTHURL=$ONEBOX/me \
  UNION_AUTH_TENANTCONTROLPLANEURL=$ONEBOX \
  UNION_AUTH_TENANTAUTHSIGNINURL=https://onebox.example.com/oauth2/start \
  UNION_AUTH_OVERRIDENORG=onebox
```

`UNION_AUTH_TENANTAUTHSIGNINURL` is where a caller without a session is sent to sign in: your proxy's sign-in page. `UNION_AUTH_OVERRIDENORG` is onebox's `organization`.

The filter reads onebox's OAuth2 metadata when the gateway starts, and the gateway doesn't start without it: set `authMetadata.externalAuthServerBaseUrl` in onebox's values (see [authentication](./authentication)).

The proxy in front of onebox must also authenticate app hosts and pass the signed-in user's token to onebox in the `Authorization` header. With oauth2-proxy, that's `--pass-authorization-header`, with its cookie domain covering the app hosts (`--cookie-domain=.onebox.example.com`).

The gateway needs no external load balancer or Knative domain setup: onebox forwards app hosts to its in-cluster Service (`serving.gateway.url`, `http://kourier.kourier-system.svc.cluster.local` by default). With the chart's network policy on, only the gateway's pods may reach onebox's port 8083, and only onebox may reach the gateway's external listener. For an airgapped install, mirror Knative's images and Union's along with onebox's.

## 3. Turn on apps

```yaml
serving:
  enabled: true
  publicURLPattern: https://%s.apps.onebox.example.com
```

The first `%s` is the app's subdomain; an optional second `%s` is the organization. Upgrade onebox with these values. The chart adds the Knative permissions to onebox's Role.

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
- The proxy in front authenticates every app host, so an app that allows anonymous callers still needs them to get past it. Give such apps a route that skips the proxy's sign-in if they must take unauthenticated calls.
- Onebox's local image runs Union's Kourier with the union-apps filter off: apps there are routed but not authorized per app.
- Apps and gateways were verified on a onebox whose apps run on a Union cluster through a test bridge rather than on Knative in the same cluster. Serving, the app's URL through onebox, status in the UI, and a gateway's policy sync and virtual keys all worked. Provider secrets reaching a gateway's pods weren't covered.
