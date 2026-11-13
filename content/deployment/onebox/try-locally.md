---
title: Try Union.ai on your machine
description: Start the whole Union.ai platform on your laptop with one command, for a proof of concept, and run a workflow against it.
icon: laptop
weight: 1
variants: -flyte +union
---

# Try Union.ai on your machine

`flyte start onebox` runs Union.ai on your machine, in one Docker container: the services that store and run your workflows, the web UI, and a PostgreSQL database and S3-compatible storage for them. Runs and data are kept in a Docker volume. It is the quickest way to evaluate Union.ai.

Nothing is authenticated and everything runs on one machine, so use it to try things out, not for production or shared use. To install Union.ai on a Kubernetes cluster, follow one of the [deployment guides](./_index#choose-a-guide).

## Prerequisites

- Docker, with at least 4 CPUs and 8 GB of memory available to it. Docker Desktop and OrbStack work; Apple's `container` runtime and socktainer don't.
- Python 3.10 or later.
- Ports `30080`, `30566`, and `36443` free on your machine.

## Start Union.ai

Union.ai uses the Flyte Python SDK and its `flyte` CLI; the `flyteplugins-union` package adds the `flyte start onebox` command. Install both, then start Union.ai:

```shell
pip install flyte "flyteplugins-union>=0.21.0"
flyte start onebox
```

The first start pulls the image and takes a few minutes; later starts take seconds. When it is ready, it prints where to find everything:

| Resource | Address or file |
|---|---|
| UI | `http://localhost:30080/v2` |
| SDK and CLI configuration | `~/.flyte/onebox/config.yaml` |
| Kubernetes configuration | `~/.flyte/onebox/kubeconfig` |

The SDK configuration points at organization `onebox`, project `flytesnacks`, and domain `development`. Union.ai organizes work into projects, and each project into domains (`development`, `staging`, `production`); these are Union.ai names, not Kubernetes namespaces or DNS names.

To see the pods inside the container:

```shell
kubectl --kubeconfig ~/.flyte/onebox/kubeconfig -n onebox get pods
```

Union.ai is under the [Union License](https://www.union.ai/licensing/union-license); see [License](./_index#license).

## Add a license key

Union.ai on your machine starts read-only: you can look around, but not run anything, until you add a license key. Get a 30-day trial key:

1. Open the UI, then **Settings > License**, and select **Get a key**. `flyte start onebox` also prints the link.
2. Sign in to Union.ai, or sign up. You land on your organization's **License Keys** page with this install filled in. Issue the key.
3. Back in the UI, select **Add key** and paste it.

See [License key](./_index#license-key) for trial and contract keys, and the limits a key carries.

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

Run it against Union.ai on your machine:

```shell
flyte --config ~/.flyte/onebox/config.yaml run hello.py main
```

To use it for every command, set `export FLYTECTL_CONFIG=~/.flyte/onebox/config.yaml` instead.

The run appears in the UI, with one entry for each call of `fn`; Union.ai calls each of these task invocations an action. Each action runs as a pod inside the container. You can also create [secrets](../../user-guide/tasks/task-configuration/secrets) with `flyte create secret`, view task logs, and [trigger runs](../../user-guide/triggers/_index) on a schedule or an event.

## Add-ons

Choose add-ons when the container is created, with `--with` and a comma-separated list:

| Add-on | What it adds |
|---|---|
| `logs` | Logs of tasks whose pods are gone. On by default. |
| `metrics` | The **Metrics** tab, from a Prometheus in the container. |
| `image-builder` | Building `flyte.Image` images in the container, with BuildKit and a registry; see [Image builder](./image-builder). |
| `apps` | [Apps and LLM gateways](./apps), served at `http://<name>.apps.127-0-0-1.nip.io:30080`. |

```shell
flyte start onebox --with logs,metrics,image-builder,apps            # a new container
flyte start onebox --recreate --with logs,metrics,image-builder,apps # change an existing one
```

`--with none` turns them all off. A container keeps the add-ons it was created with: a later `flyte start onebox` resumes it as it is, and asking for other add-ons without `--recreate` is refused. `--recreate` replaces the container, keeping runs and data in the Docker volume, with the same add-ons unless you pass `--with` again. A `--with` list replaces the add-ons; it doesn't add to them.

## Use your Mac's GPU

On a Mac with Apple Silicon, `--apple-silicon` runs the work of tasks and apps that request the Apple Silicon GPU natively on your Mac, where it can use Metal and MLX, instead of inside the Linux container:

```shell
flyte start onebox --apple-silicon              # a new container
flyte start onebox --recreate --apple-silicon   # add it to an existing one
```

```python
env = flyte.TaskEnvironment(name="mlx_env", resources=flyte.Resources(gpu="AppleSilicon"))
```

It needs flyte 2.13.1 or later. Onebox starts a bridge on your Mac that runs those tasks and apps, and publishes its ports on `localhost` only, since that work runs as you on your machine. The bridge's log is `~/.flyte/onebox/apple-silicon/bridge.log`. Later starts and `--recreate` keep Apple Silicon on.

## Use your own images

Tasks run in the SDK's default image unless they name another. It pulls images from any registry your machine can reach. For a private registry, create an image pull secret in the `onebox` namespace and add it to that namespace's `default` service account, which task pods run as:

```shell
export KUBECONFIG=~/.flyte/onebox/kubeconfig
kubectl -n onebox create secret docker-registry my-registry \
  --docker-server=<registry> --docker-username=<user> --docker-password=<password>
kubectl -n onebox patch serviceaccount default -p '{"imagePullSecrets": [{"name": "my-registry"}]}'
```

## Stop, resume, and delete

```shell
flyte stop onebox                     # pause it; flyte start onebox resumes where it left off
flyte stop onebox --delete            # remove the container; runs and data stay in a Docker volume
flyte stop onebox --delete --volume   # remove everything
```

## Upgrade

`flyte start onebox` runs `ghcr.io/unionai/onebox-local:latest`, which follows each Union.ai release, but it pulls the image only when it isn't on your machine. To move to a new release, pull it and replace the container. Runs and data stay in the Docker volume, and the add-ons and Apple Silicon setting carry over:

```shell
docker pull ghcr.io/unionai/onebox-local:latest
flyte start onebox --recreate
```

To pin a release instead, pass `--image ghcr.io/unionai/onebox-local:<version>`.

## What a proof of concept on your machine doesn't cover

| | Where to go next |
|---|---|
| Sign-in, users, and roles | [Authentication](./authentication) and [Authorization](./authorization), on a cluster |
| Your own PostgreSQL and object store | [Amazon EKS](./eks), [Google GKE](./gke), or [any Kubernetes cluster](./kubernetes) |
| Durable task logs, metrics, and image builds | [Task logs](./logs), [Task metrics](./metrics), and [Image builder](./image-builder), on a cluster. The add-ons above keep them inside the container only. |

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `flyte start onebox` says Docker is not reachable | Start Docker and try again. |
| It fails with Apple's `container` runtime or socktainer | They can't map `host.docker.internal` or forward the container's ports to your machine. Use Docker Desktop or OrbStack. |
| It times out waiting for Union.ai to be ready | Docker has too little memory or CPU. Check `docker logs union-onebox` and `kubectl --kubeconfig ~/.flyte/onebox/kubeconfig -n onebox get pods`. |
| A port is already in use | Something else listens on `30080`, `30566`, or `36443`. Stop it, then run `flyte start onebox --recreate`. |
| `docker pull` says `denied` for `ghcr.io/unionai/onebox-local` | The images are public; Docker is sending expired GHCR credentials. Run `docker logout ghcr.io` and pull again. |
| The container exits with `Apple Silicon needs the host gateway` | The Docker runtime can't reach your Mac at `host.docker.internal`. Use Docker Desktop or OrbStack. |
| A new release doesn't show up | `flyte start onebox` reuses the image on your machine. See [Upgrade](#upgrade). |
