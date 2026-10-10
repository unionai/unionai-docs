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

Each app gets a URL from `serving.publicURLPattern`, for example `https://quiet-river-1a2b3.apps.onebox.example.com`. Point a wildcard DNS record for those hosts at the same proxy or load balancer as onebox, so their requests arrive at onebox's port. Onebox's edge recognizes an app's host and forwards the request to the app's Knative Service inside the cluster:

- An app that allows anonymous callers gets every request, including its `Authorization` header (an LLM gateway's virtual key, for example).
- With [authorization](./authorization) on, any other app needs a caller the proxy in front has authenticated, as for onebox itself. The caller's credentials for onebox are never passed to the app.

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

Onebox reaches apps at their cluster-local addresses, so Kourier needs no external load balancer or Knative domain setup. For an airgapped install, mirror Knative's images along with onebox's.

## 2. Turn on apps

```yaml
serving:
  enabled: true
  publicURLPattern: https://%s.apps.onebox.example.com
```

The first `%s` is the app's subdomain; an optional second `%s` is the organization. Upgrade onebox with these values. The chart adds the Knative permissions to onebox's Role.

## 3. Serve an app

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
- Apps and gateways were verified on a onebox whose apps run on a Union cluster through a test bridge rather than on Knative in the same cluster. Serving, the app's URL through onebox, status in the UI, and a gateway's policy sync and virtual keys all worked. Provider secrets reaching a gateway's pods weren't covered.
