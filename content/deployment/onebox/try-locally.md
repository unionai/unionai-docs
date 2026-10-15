---
title: Try Union.ai on your machine
description: Start the whole Union.ai platform on your laptop with one command, for a proof of concept, and run a workflow against it.
icon: laptop
weight: 1
variants: -flyte +union
---

# Try Union.ai on your machine

`flyte start unibox` runs the whole Union.ai platform on your machine, in one Docker container: onebox (the control plane and the data plane), the UI, and a throwaway PostgreSQL database and S3-compatible store for it. It is the quickest way to evaluate Union.ai: the same workflows, CLI, and UI as any other deployment, with nothing to set up first.

Nothing is authenticated and everything runs on one machine, so use it to try things out, not for production or shared use. To install Union.ai on a Kubernetes cluster, follow one of the [deployment guides](./_index#choose-a-guide).

## Prerequisites

- Docker, with at least 4 CPUs and 8 GB of memory available to it.
- Python 3.10 or later.
- Ports `30080` and `30566` free on your machine.

## Start Union.ai

```shell
uv pip install flyte flyteplugins-union
flyte start unibox
```

The first start pulls the unibox image and takes a few minutes; later starts take seconds. When it is ready, it prints where to find everything:

| | |
|---|---|
| UI | `http://localhost:30080/v2` |
| SDK and CLI configuration | `~/.flyte/unibox/config.yaml` (endpoint `dns:///localhost:30080`, org `onebox`, project `flytesnacks`, domain `development`) |
| Kubernetes | `kubectl --kubeconfig ~/.flyte/unibox/kubeconfig -n onebox get pods` |

## Run a workflow

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

Run it against unibox:

```shell
flyte --config ~/.flyte/unibox/config.yaml run hello.py main
```

To use unibox for every command, set `export FLYTECTL_CONFIG=~/.flyte/unibox/config.yaml` instead.

The run, and the `fn` actions it fans out, appear in the UI. Each action runs as a pod inside the container. Secrets (`flyte create secret`), logs, schedules, and triggers work as on any other deployment.

## Use your own images

Tasks run in the SDK's default image unless they name another. Unibox pulls images from any registry your machine can reach. For a private registry, create an image pull secret in the `onebox` namespace and add it to that namespace's `default` service account, which task pods run as:

```shell
export KUBECONFIG=~/.flyte/unibox/kubeconfig
kubectl -n onebox create secret docker-registry my-registry \
  --docker-server=<registry> --docker-username=<user> --docker-password=<password>
kubectl -n onebox patch serviceaccount default -p '{"imagePullSecrets": [{"name": "my-registry"}]}'
```

## Stop, resume, and delete

```shell
flyte stop unibox                     # pause it; flyte start unibox resumes where it left off
flyte stop unibox --delete            # remove the container; runs and data stay in a Docker volume
flyte stop unibox --delete --volume   # remove everything
```

## What a proof of concept on your machine doesn't cover

| | Where to go next |
|---|---|
| Sign-in, users, and roles | [Authentication](./authentication) and [Authorization](./authorization), on a cluster |
| Your own PostgreSQL and object store | [Amazon EKS](./eks), [Google GKE](./gke), or [any Kubernetes cluster](./kubernetes) |
| Logs of tasks that finished a while ago | [Task logs](./logs) |
| The Metrics tab | [Task metrics](./metrics) |
| Remote image builds | [Image builder](./image-builder) |

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `flyte start unibox` says Docker is not reachable | Start Docker and try again. |
| It times out waiting for Union.ai to be ready | Docker has too little memory or CPU. Check `docker logs union-unibox` and `kubectl --kubeconfig ~/.flyte/unibox/kubeconfig -n onebox get pods`. |
| A port is already in use | Something else listens on `30080` or `30566`. Stop it, then run `flyte start unibox --recreate`. |
