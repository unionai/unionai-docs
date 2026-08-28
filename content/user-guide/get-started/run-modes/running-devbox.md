---
title: Run on the Devbox
description: Run tasks and apps in a lightweight Flyte cluster using Docker. Get the full Flyte UI and backend experience on your machine.
icon: box
weight: 5
variants: +flyte +union
---

{{< variant union >}}

{{< markdown >}}

# Run on the Devbox

The Flyte 2 devbox is a great way to try a simplified Union.ai cluster on your local machine. It's a lightweight
local cluster that runs on your machine with Docker. It includes a UI, scheduler, and object store, so you can test remote
execution without deploying to a cluster in the cloud.

{{< /markdown >}}


{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}

<!-- markdownlint-disable-next-line MD024 -- same heading as the union variant block; only one renders per variant -->
# Run on the Devbox

The Flyte devbox is a lightweight local cluster that runs on your machine with Docker. It gives you a full Flyte environment, including the UI, scheduler, and object store, so you can test remote execution without deploying to a real cluster.
{{< /markdown >}}
{{< /variant >}}

> [!NOTE] Try Devbox in your browser
> Prefer not to install anything locally? Create a Devbox in GitHub Codespaces.
>
> [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/flyteorg/flyte-devbox-codespace?quickstart=1)

## What you'll need

- Python 3.10+ in a virtual environment
- [Docker](https://docs.docker.com/get-docker/) installed and running
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

## Install the SDK

If you haven't already, install the `flyte` package:

```bash
pip install flyte
```

## Start the devbox

Launch the local cluster:

{{< tabs "cpu" >}}
{{< tab "CPU" >}}
{{< markdown >}}

```bash
flyte start devbox
```

{{< /markdown >}}
{{< /tab >}}

{{< tab "GPU" >}}
{{< markdown >}}

```bash
flyte start devbox --gpu
```

{{< /markdown >}}

{{< note >}}
The `--gpu` flag requires an NVIDIA-enabled host. It currently *does not* support Apple Silicon or AMD GPUs.
{{< /note>}}

{{< /tab >}}
{{< /tabs >}}

![Devbox start](../../../_static/images/user-guide/run-modes/flyte-start-devbox.png)

This pulls the necessary containers and starts a local Flyte instance. Once ready, the Flyte UI is available at `http://localhost:30080`.

{{< note >}}
The first start may take a few minutes while Docker images are downloaded.
{{< /note >}}

## Check the devbox status

> [!NOTE]
> `flyte get devbox` requires flyte 2.6.2 or later.

To see whether the devbox is up, and where it is:

```bash
flyte get devbox
```

This reports the run state, the UI and image registry endpoints, the container image version in use, and where the cluster keeps its state on disk. It is the quickest way to tell a devbox that is still starting from one that is ready.

Add `--no-probes` to skip the readiness probe and the container resource sample, which makes the check faster and works offline:

```bash
flyte get devbox --no-probes
```

For a machine-readable report, pass an output format to the top-level command:

```bash
flyte -of json-raw get devbox
```

## Configure

Create a config file that points to the devbox:

```bash
flyte create config --devbox
```

This creates `.flyte/config.yaml` configured to talk to your local devbox cluster.

The `--devbox` flag requires flyte 2.6.1 or later. It is a shortcut for the explicit form, which you need on earlier versions:

```bash
flyte create config \
    --endpoint localhost:30080 \
    --project flytesnacks \
    --domain development \
    --builder local \
    --insecure
```

Both forms write the same config file. One difference: in an interactive terminal the explicit form offers to reuse a Docker login as your image registry, while `--devbox` skips that prompt, because the devbox pushes to its own in-cluster registry.

`--devbox` cannot be combined with `--endpoint`, but you can still override the project and domain alongside it:

```bash
flyte create config --devbox --project my-project --domain staging
```

## Run a workflow on the devbox

Using the same `hello.py` from the [Quickstart](../quickstart):

{{< code file="/unionai-examples/v2/user-guide/getting-started/hello.py" lang="python" >}}

Run it on the devbox:

```bash
flyte run hello.py main
```

Without the `--local` flag, the workflow runs on the devbox cluster rather than in your local Python process. Tasks execute inside containers, just like they would on a remote cluster.

## View results in the UI

Open `http://localhost:30080` to see your workflow execution in the Flyte UI. You can inspect task inputs, outputs, logs, and execution timelines.

![Devbox UI](../../../_static/images/user-guide/run-modes/flyte-ui-devbox.png)

## Stop the devbox

When you're done, shut down the cluster:

```bash
flyte stop devbox
```

## Inline configuration

Skip the config file entirely by passing parameters directly.

{{< tabs "inline-config" >}}
{{< tab "Programmatic" >}}
{{< markdown >}}
Use `flyte.init`:

```python
flyte.init(
    endpoint="localhost:30080",
    project="flytesnacks",
    domain="development",
    insecure=True,
)
```

{{< /markdown >}}
{{< /tab >}}
{{< tab "CLI" >}}
{{< markdown >}}
Some parameters go after `flyte`, others after the subcommand:

```bash
flyte \
    --endpoint localhost:30080 \
    --insecure \
    --builder local \
    run \
    --domain development \
    --project flytesnacks \
    hello.py \
    main
```

See the [CLI reference](../../../api-reference/flyte-cli) for details.
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Delete the devbox

```bash
flyte delete devbox  # add the --volume flag to delete the Docker volume
```

## Using a CUDA-enabled GPU host

If you started the devbox with `flyte start devbox --gpu`, you can use GPUs in your workflows.

```python
import flyte

env = flyte.TaskEnvironment(
    name="gpu_env",
    resources=flyte.Resources(gpu=1),
)

@env.task
def gpu_task() -> bool:
    return torch.cuda.is_available()  # returns True if CUDA (provided by a GPU) is available
```

## Next steps

{{< variant flyte >}}
{{< markdown >}}

With your environment fully configured, you're ready to build:

- [**Core concepts**](../core-concepts/_index): Understand `TaskEnvironment`s, tasks, runs, and actions through working examples.

{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}

When you're ready to run on a remote Flyte cluster, see [Run on a remote cluster](./running-remote) to configure the CLI and SDK.

{{< /markdown >}}
{{< /variant >}}
