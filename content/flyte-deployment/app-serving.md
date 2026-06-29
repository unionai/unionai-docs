---
title: Serving apps
variants: +flyte -union
weight: 4
---

# Serving apps

Flyte can host long-running **apps** — web services, dashboards, model servers — next to
your workflows. Each app runs as a [Knative](https://knative.dev) Service that Flyte's
built-in app controller creates and manages for you, including scaling to zero when an
app is idle and giving every app a stable URL.

App serving is **off by default**. Because apps depend on Knative, you install Knative
Serving first, then turn app serving on in the `flyte-binary` chart.

## How it works

- You define an app (with the SDK) and Flyte's app controller creates a Knative Service
  (`KService`) in your cluster.
- Knative Serving runs the app, autoscales it (including to zero), and routes traffic.
- Each app is published at a URL derived from a base domain you configure:
  `{name}-{project}-{domain}.{base-domain}`.

## Prerequisites

- A running Flyte deployment (see [Installing Flyte](./installing)).
- Cluster-admin access to install Knative (CRDs and controllers).
- A **wildcard DNS record** and a **TLS certificate** for the app base domain (details
  in steps 2–3).

{{< note >}}
Your cloud's ingress/load-balancer controller (for example the AWS Load Balancer
Controller) **cannot** act as Knative's networking layer — Knative needs one of its own
networking layers: **Kourier**, Istio, or Contour. This guide uses **Kourier**, the
lightweight default. You can still place your cloud load balancer *in front of* Kourier
(see step 3).
{{< /note >}}

## 1. Install Knative Serving and Kourier

Pick a Knative release that supports your Kubernetes version (Knative supports only the
most recent Kubernetes versions — check the
[Knative install docs](https://knative.dev/docs/install/)). Then install Serving and the
Kourier networking layer:

```bash
export KNATIVE_VERSION=knative-v1.17.0   # choose a release compatible with your k8s version

# Knative Serving: CRDs, then core
kubectl apply -f https://github.com/knative/serving/releases/download/$KNATIVE_VERSION/serving-crds.yaml
kubectl apply -f https://github.com/knative/serving/releases/download/$KNATIVE_VERSION/serving-core.yaml

# Kourier networking layer
kubectl apply -f https://github.com/knative-extensions/net-kourier/releases/download/$KNATIVE_VERSION/kourier.yaml

# Tell Knative to route through Kourier
kubectl patch configmap/config-network -n knative-serving --type merge \
  -p '{"data":{"ingress-class":"kourier.ingress.networking.knative.dev"}}'
```

Wait for the control plane and gateway to be ready:

```bash
kubectl wait --for=condition=Available deploy --all -n knative-serving --timeout=180s
kubectl wait --for=condition=Available deploy --all -n kourier-system --timeout=180s
```

{{< note >}}
If `kubectl apply` rejects the manifests, your cluster is probably older than this
Knative release requires. Install an earlier Knative version (Serving and net-kourier
must use the **same** version).
{{< /note >}}

## 2. Configure the apps domain

Apps are published at `{name}-{project}-{domain}.{base-domain}`. Set the base domain
Knative uses, and make each app's hostname a **single label** under it so one wildcard
TLS certificate can cover them all:

```bash
# Base domain for app URLs
kubectl patch configmap/config-domain -n knative-serving --type merge \
  -p '{"data":{"<apps.example.com>":""}}'

# Single-label hostnames: <service>.<apps.example.com>
kubectl patch configmap/config-network -n knative-serving --type merge \
  -p '{"data":{"domain-template":"{{.Name}}.{{.Domain}}"}}'
```

The single-label template matters: a wildcard TLS certificate (`*.apps.example.com`)
matches only **one** label. Knative's default template is
`{{.Name}}.{{.Namespace}}.{{.Domain}}`, which produces a two-label hostname that a
wildcard certificate would not cover, breaking TLS. Dropping the namespace keeps every
app hostname single-label.

You will provision the matching DNS record and certificate for `<apps.example.com>` in
the next step.

## 3. Expose Kourier

Traffic reaches apps through Kourier. Choose how to expose it:

{{< tabs "expose-kourier" >}}
{{< tab "LoadBalancer (simplest)" >}}
{{< markdown >}}
The Kourier install creates a `kourier` Service of type `LoadBalancer`, so your cloud
provisions a network load balancer automatically. Find its address:

```bash
kubectl get svc kourier -n kourier-system
```

Then provision, for `<apps.example.com>`:

- a **wildcard DNS record** `*.<apps.example.com>` → the load balancer's hostname/IP, and
- a **TLS certificate** covering `*.<apps.example.com>` (attach it to the load balancer,
  or use Knative [auto-TLS](https://knative.dev/docs/serving/encryption/)).
{{< /markdown >}}
{{< /tab >}}
{{< tab "AWS (ALB in front)" >}}
{{< markdown >}}
To reuse an existing ALB, ACM certificate, and edge auth, switch the Kourier Service to
`ClusterIP` and front it with an Ingress:

```bash
kubectl patch svc kourier -n kourier-system --type merge -p '{"spec":{"type":"ClusterIP"}}'
```

```yaml
# kourier-alb-ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: kourier-alb
  namespace: kourier-system
  annotations:
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS": 443}]'
    alb.ingress.kubernetes.io/ssl-redirect: "443"
    alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:<region>:<account-id>:certificate/<cert-id>
    # Kourier returns 404 for an unmatched host while it is healthy, so accept it.
    alb.ingress.kubernetes.io/healthcheck-path: /
    alb.ingress.kubernetes.io/success-codes: "200,404"
spec:
  rules:
    - host: "*.<apps.example.com>"
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: kourier
                port:
                  number: 80
```

```bash
kubectl apply -f kourier-alb-ingress.yaml
```

Point a wildcard DNS record `*.<apps.example.com>` at the ALB. The ALB terminates TLS
with your ACM certificate and forwards to Kourier, which routes by hostname to each app.

**Require authentication (optional).** Apps are public by default — anyone who can reach
the ALB can open them. To put the same OIDC login your console uses in front of every app,
add edge authentication to the `kourier-alb` Ingress. The AWS Load Balancer Controller then
programs an `authenticate-oidc` action on the ALB, so unauthenticated requests are bounced
to your identity provider first.

Add these annotations to the Ingress above:

```yaml
    alb.ingress.kubernetes.io/auth-type: oidc
    alb.ingress.kubernetes.io/auth-on-unauthenticated-request: authenticate
    alb.ingress.kubernetes.io/auth-scope: openid email profile
    alb.ingress.kubernetes.io/auth-idp-oidc: |
      {"issuer":"https://<issuer>",
       "authorizationEndpoint":"https://<issuer>/v1/authorize",
       "tokenEndpoint":"https://<issuer>/v1/token",
       "userInfoEndpoint":"https://<issuer>/v1/userinfo",
       "secretName":"apps-oidc"}
```

The controller reads the OIDC `clientID` and `clientSecret` from the Secret named by
`secretName`, which **must live in the same namespace as the Ingress** (`kourier-system`):

```bash
kubectl create secret generic apps-oidc -n kourier-system \
  --from-literal=clientID=<client-id> \
  --from-literal=clientSecret=<client-secret>
```

Grant the controller permission to read Secrets in that namespace (its Secret access is
per-namespace). Without this the Ingress fails to reconcile with `secrets "apps-oidc" is
forbidden`, which stalls reconciliation of the **whole ALB group**, not just this Ingress:

```yaml
# kourier-oidc-rbac.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: alb-oidc-secret-reader
  namespace: kourier-system
rules:
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: alb-oidc-secret-reader
  namespace: kourier-system
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: alb-oidc-secret-reader
subjects:
  - kind: ServiceAccount
    name: aws-load-balancer-controller   # your controller's ServiceAccount
    namespace: kube-system
```

Finally, allow the ALB's callback on your OIDC client. The ALB redirects back to
`https://<app-host>/oauth2/idpresponse`, and every app has a different hostname, so register
the wildcard `https://*.<apps.example.com>/oauth2/idpresponse` as a sign-in redirect URI
(your IdP must permit wildcard redirect URIs). Without it, login dead-ends after the redirect
with a `redirect_uri` error.
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## 4. Enable app serving in Flyte

Turn on the app controller in your Flyte values, then upgrade the release:

```yaml
configuration:
  inline:
    internalApps:
      enabled: true
      baseDomain: <apps.example.com>   # must match config-domain from step 2
      scheme: https
      ingressAppsPort: 0               # apps sit behind the LB on 443; omit the port
```

```bash
helm upgrade flyte flyteorg/flyte-binary -n flyte -f values.yaml
kubectl -n flyte rollout status deploy/flyte
```

{{< note >}}
`baseDomain` must match the domain you set in `config-domain`, so the URLs Flyte
advertises line up with the hostnames Knative actually serves — and with your wildcard
certificate.
{{< /note >}}

## 5. Verify

Confirm the Flyte ServiceAccount can manage Knative resources:

```bash
kubectl auth can-i create services.serving.knative.dev \
  --as=system:serviceaccount:flyte:flyte -n flyte   # -> yes
```

Port-forward the API and call the app service — it should return an empty list (`{}`),
not a 404:

```bash
kubectl -n flyte port-forward service/flyte-http 8090:8090
```

```bash
curl -s -o /dev/null -w '%{http_code}\n' -X POST \
  http://localhost:8090/flyteidl2.app.AppService/List \
  -H 'Content-Type: application/json' -d '{}'        # -> 200
```

The console's **Apps** section now loads. Deploy an app with the SDK and open its URL at
`https://<name>-<project>-<domain>.<apps.example.com>`.

## Troubleshooting

- **`AppService/List` returns 404 / "unimplemented".** App serving is disabled or the
  controller can't start. Check that `internalApps.enabled: true` and that the
  `serving.knative.dev` RBAC rules are present on the Flyte ClusterRole.
- **An app URL shows a TLS certificate error.** The hostname has more labels than your
  wildcard certificate covers. Confirm the single-label `domain-template` (step 2) and
  that `baseDomain` matches `config-domain`.
- **An app URL doesn't resolve.** The wildcard DNS record `*.<apps.example.com>` isn't
  pointing at the load balancer in front of Kourier.
- **Knative manifests are rejected on apply.** The Knative release is newer than your
  Kubernetes version supports — install an older Knative version (step 1).
