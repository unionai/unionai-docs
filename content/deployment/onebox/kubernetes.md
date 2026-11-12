---
title: Deploy on any Kubernetes cluster
description: Install onebox on any Kubernetes cluster, on-premises or in any cloud, with your own PostgreSQL database and an S3-compatible object store.
icon: hdd-network
weight: 4
variants: -flyte +union
---

# Deploy on any Kubernetes cluster

This guide installs onebox on any conformant Kubernetes cluster, on-premises or in any cloud, with a PostgreSQL database and an S3-compatible object store you already run, such as MinIO, Ceph, or Cloudflare R2. Onebox reads the store's access keys from a Secret.

## Prerequisites

- A Kubernetes cluster, and `kubectl` and [Helm](https://helm.sh) 3 configured for it.
- A PostgreSQL database the cluster's pods can reach, with a user that owns it.
- A bucket in an S3-compatible store, and an access key that can read, write, list, and delete objects in it.

## Make the store reachable

The SDK uploads code and downloads outputs through signed URLs that point at the store, so **the store's endpoint must be reachable at the same address from inside the cluster and from your users' machines**. Use a DNS name that resolves in both places, such as the store's public or corporate hostname, rather than a cluster-internal Service name.

## Allow the UI to read the bucket

Give the bucket a CORS rule that allows `GET` and `HEAD` from the address your users open (see [Bucket CORS](./_index#bucket-cors)). With the AWS CLI against an S3-compatible store:

```shell
cat > cors.json <<EOF
{"CORSRules": [{"AllowedOrigins": ["https://<host>"], "AllowedMethods": ["GET", "HEAD"],
                "AllowedHeaders": ["*"], "MaxAgeSeconds": 3600}]}
EOF
aws s3api put-bucket-cors --endpoint-url https://<store endpoint> --bucket <bucket> --cors-configuration file://cors.json
```

Some stores configure CORS differently, for example per deployment rather than per bucket; follow your store's documentation.

## Install with the CLI

`flyte install onebox`, from `flyteplugins-union` 0.21.0 or later, checks the cluster, collects what the chart needs, and installs it with Helm (3.8 or later, on your `PATH`):

```shell
uv pip install flyte "flyteplugins-union>=0.21.0"
flyte install onebox --db-host <postgres host> --db-password-secret onebox-db \
  --bucket <bucket> --endpoint https://<store endpoint>
```

Before installing, it checks:

- that the cluster is reachable and runs Kubernetes 1.28 or later;
- the namespace, and whether you can create what the chart installs;
- the permissions onebox itself needs;
- that the nodes have at least 4 CPUs and 8 GiB of memory to spare;
- the database, the bucket, and the database password's Secret;
- with apps on, whether the chart can run Knative Serving or the cluster already runs it;
- the namespace's Pod Security level.

Whatever is missing, with a terminal, it opens an editor on a values template to fill in. Without one, it lists the missing inputs. Inputs can also come from `--values`/`-f` files and `--set`, and `--db-password-secret`, `--storage-type` (`s3`, `gcs`, or `azure`), `--region`, `--gcp-project`, and `--azure-account` name the rest.

| Flag | What it does |
|---|---|
| `--preflight-only` | Run the checks and stop. |
| `--dry-run` | Render the install against the cluster without applying it. |
| `--serving` | Turn on [apps and LLM gateways](./apps). |
| `--edit` | Review the inputs in the editor even when nothing is missing. |
| `--skip-preflight` | Install even if a check fails. |
| `-n`/`--namespace`, `--release`, `--version`, `--kubeconfig`, `--context` | Where and what to install. |

It keeps the values it installed with in `~/.flyte/onebox/<release>-values.yaml` (readable only by you, since it can hold the database password) for later `helm upgrade -f` runs. The rest of this guide does each step by hand.

## Install onebox

Create the namespace and two Secrets: the database password, and the store's access key:

```shell
kubectl create namespace union
kubectl -n union create secret generic onebox-db --from-literal=password='<database password>'
kubectl -n union create secret generic onebox-s3 \
  --from-literal=AWS_ACCESS_KEY_ID='<access key id>' \
  --from-literal=AWS_SECRET_ACCESS_KEY='<secret access key>'
```

Save this as `values.yaml`:

```yaml
database:
  host: <postgres host>
  port: 5432
  name: <database>
  user: <user>
  existingSecret: onebox-db
  # disable, require, verify-ca or verify-full
  sslMode: require
storage:
  type: s3
  bucket: <bucket>
  region: us-east-1
  endpoint: https://<store endpoint>
  authType: accesskey
  existingSecret: onebox-s3
```

Install the chart:

```shell
helm repo add unionai https://unionai.github.io/helm-charts
helm repo update
helm install onebox unionai/onebox -n union -f values.yaml --wait --timeout 10m
```

Install onebox in a namespace of its own: task pods, their secrets, and the objects plugins create all live in it. Task pods get the store's access key from the same Secret.

## Check it

```shell
kubectl -n union port-forward svc/onebox 8080:80
```

Open [http://localhost:8080/v2](http://localhost:8080/v2), and run a workflow as in [Install the chart on k3d](./local-k3d#run-a-workflow).

Anyone who can reach port `80` can use onebox until you put an authenticating proxy in front of it. See [Authentication](./authentication).

## Serve under a path of a shared host

To serve onebox under a path of a host something else owns, such as `https://platform.example.com/onebox/`, set `basePath`. This works with any of the install guides:

```yaml
basePath: /onebox
```

The UI is then at `/onebox/v2`, and the API, `/login`, and `/logout` are under `/onebox`. Point the SDK and CLI at `https://platform.example.com/onebox`. Each `basePath` segment must be a lowercase DNS label. It needs `onebox-server` and `onebox-console` images with base path support.

The proxy in front must:

- forward `/onebox/` to onebox's Service **with the path unchanged** (with nginx, give `proxy_pass` no URI);
- keep the `Host` header and set `X-Forwarded-Proto`;
- pass WebSocket upgrades;
- not buffer responses.

[Apps](./apps#apps-under-a-path) can share the host too, each under its own path.

## Settings to review

| Setting | Default | When to change it |
|---|---|---|
| `database.sslMode` | `require` | `disable` for a database without TLS on a network you trust; `verify-full` to check the server certificate. |
| `database.maxOpenConnections` | `40` | Keep it under your database's connection limit. |
| `storage.region` | `us-east-1` | Set the region your store expects; most S3-compatible stores accept any value. |
| `resources` | 1 CPU, 2 GiB requested | Raise them for many concurrent runs. |
| `networkPolicy.enabled` | On when `authz.enabled` is | Needs a CNI that enforces NetworkPolicy. See [Authorization](./authorization#network-policy). |
| `caBundle` | Unset | Your store, database, or identity provider uses a certificate from a private CA. See [A private CA, extra mounts and proxies](./_index#a-private-ca-extra-mounts-and-proxies). |
| `taskPods.extraEnv` | Unset | Task pods reach the internet through an outbound proxy (`HTTPS_PROXY`, `NO_PROXY`). |

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `flyte run` fails while uploading the code bundle | The SDK can't reach `storage.endpoint` from your machine. Use an endpoint that resolves outside the cluster too. |
| Tasks fail reading their inputs | The pods can't reach `storage.endpoint`, or the access key can't read the bucket. |
| The onebox pod restarts with TLS errors from the database | The database doesn't offer TLS. Set `database.sslMode: disable`, only on a network you trust. |
