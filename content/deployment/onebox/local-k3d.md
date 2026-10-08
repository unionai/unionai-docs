---
title: Try onebox on k3d
description: Run onebox on your laptop in a k3d cluster, with throwaway PostgreSQL and S3, and run a workflow against it.
icon: laptop
weight: 1
variants: -flyte +union
---

# Try onebox on k3d

This guide runs onebox on your laptop in a [k3d](https://k3d.io) cluster, with a throwaway PostgreSQL database and S3-compatible store inside the cluster, and runs a workflow against it. Nothing is authenticated, so keep it on your machine.

## Prerequisites

- Docker, [k3d](https://k3d.io), `kubectl`, and [Helm](https://helm.sh) 3.
- Python 3.10 or later.

## Create the cluster

Create a cluster that publishes port `30566` on your machine. The S3-compatible store listens there, so that the SDK on your laptop and the pods in the cluster use the same address for it:

```shell
k3d cluster create onebox \
  --k3s-arg '--disable=traefik@server:0' \
  -p '30566:30566@server:0'
kubectl create namespace union
```

## Install PostgreSQL and an S3-compatible store

Save this as `prereqs.yaml`. It creates a PostgreSQL database, an S3-compatible store with a bucket named `onebox`, and a Secret with the store's credentials. None of it keeps data across restarts.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata: {name: postgres}
spec:
  selector: {matchLabels: {app: postgres}}
  template:
    metadata: {labels: {app: postgres}}
    spec:
      containers:
        - name: postgres
          image: mirror.gcr.io/library/postgres:17-alpine
          env:
            - {name: POSTGRES_USER, value: union}
            - {name: POSTGRES_PASSWORD, value: union}
            - {name: POSTGRES_DB, value: union}
          args: ["-c", "max_connections=300"]
          readinessProbe:
            exec: {command: [pg_isready, -U, union]}
---
apiVersion: v1
kind: Service
metadata: {name: postgres}
spec:
  selector: {app: postgres}
  ports: [{port: 5432}]
---
apiVersion: apps/v1
kind: Deployment
metadata: {name: s3}
spec:
  selector: {matchLabels: {app: s3}}
  template:
    metadata: {labels: {app: s3}}
    spec:
      enableServiceLinks: false
      containers:
        - name: s3
          image: floci/floci:1.7.0
          env:
            - {name: FLOCI_DEFAULT_REGION, value: us-east-1}
          readinessProbe:
            tcpSocket: {port: 4566}
---
apiVersion: v1
kind: Service
metadata: {name: s3}
spec:
  type: NodePort
  selector: {app: s3}
  ports: [{port: 4566, nodePort: 30566}]
---
apiVersion: v1
kind: Secret
metadata: {name: s3-creds}
stringData: {AWS_ACCESS_KEY_ID: test, AWS_SECRET_ACCESS_KEY: test}
---
apiVersion: batch/v1
kind: Job
metadata: {name: create-bucket}
spec:
  backoffLimit: 20
  template:
    spec:
      restartPolicy: OnFailure
      containers:
        - name: mb
          image: curlimages/curl:8.10.1
          # Create the bucket, and let the UI read objects from it (Bucket CORS).
          command:
            - sh
            - -c
            - |
              curl -fsS -X PUT http://s3:4566/onebox &&
              curl -fsS -X PUT -H 'Content-Type: application/xml' 'http://s3:4566/onebox?cors' --data-binary \
                '<CORSConfiguration><CORSRule><AllowedOrigin>*</AllowedOrigin><AllowedMethod>GET</AllowedMethod><AllowedMethod>HEAD</AllowedMethod><AllowedHeader>*</AllowedHeader><MaxAgeSeconds>3600</MaxAgeSeconds></CORSRule></CORSConfiguration>'
```

Apply it and wait for the bucket:

```shell
kubectl -n union apply -f prereqs.yaml
kubectl -n union wait --for=condition=complete job/create-bucket --timeout=300s
```

## Install onebox

The SDK uploads your code straight to the bucket, so the store's address must work from your laptop and from inside the cluster. Your machine's network address does both:

```shell
# macOS; on Linux use: hostname -I | awk '{print $1}'
HOST_IP=$(ipconfig getifaddr en0)
```

Install the chart:

```shell
helm repo add unionai https://unionai.github.io/helm-charts
helm repo update
helm install onebox unionai/onebox -n union \
  --set database.host=postgres \
  --set database.user=union --set database.name=union \
  --set database.password=union --set database.sslMode=disable \
  --set storage.type=s3 --set storage.bucket=onebox \
  --set storage.endpoint=http://${HOST_IP}:30566 \
  --set storage.authType=accesskey --set storage.existingSecret=s3-creds \
  --set resources.requests.cpu=500m --set resources.requests.memory=1Gi \
  --wait --timeout 10m
```

If your network address changes, for example when you switch Wi-Fi networks, run `helm upgrade` with the new address. Uploads and downloads fail until you do.

## Open the UI

```shell
kubectl -n union port-forward svc/onebox 8080:80
```

Open [http://localhost:8080/v2](http://localhost:8080/v2).

## Run a workflow

In another terminal, install the SDK and point the CLI at onebox:

```shell
pip install flyte
flyte create config \
  --endpoint localhost:8080 --insecure \
  --org onebox --project default --domain development \
  --builder local
```

Save this as `hello.py`:

```python
import flyte

env = flyte.TaskEnvironment(name="hello_env")

@env.task
def fn(x: int) -> int:
    return 2 * x + 5

@env.task
def main(x_list: list[int] = [1, 2, 3, 4, 5]) -> float:
    y_list = list(flyte.map(fn, x_list))
    return sum(y_list) / len(y_list)
```

Run it:

```shell
flyte run hello.py main
```

The run, and the `fn` actions it fans out, appear in the UI. Each action runs as a pod in the `union` namespace.

## Clean up

```shell
k3d cluster delete onebox
```

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `flyte run` fails while uploading the code bundle | The SDK cannot reach `storage.endpoint`. Check that `curl http://${HOST_IP}:30566` answers from your machine, and that `HOST_IP` is still your address. |
| Task pods fail to read their inputs | The pods cannot reach `storage.endpoint`. Same check, from a pod: `kubectl -n union run probe --rm -it --image=curlimages/curl:8.10.1 -- curl -sI http://${HOST_IP}:30566`. |
| The onebox pod restarts with database errors | PostgreSQL wasn't ready yet. It recovers on its own once `kubectl -n union get pods` shows postgres ready. |
