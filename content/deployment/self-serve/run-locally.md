---
title: Run your first workflow locally
description: Set up the Flyte CLI, run a workflow on your own machine, and follow it in the Union.ai UI. No cluster needed.
icon: play-circle
weight: 3
variants: -flyte +union
---

# Run your first workflow locally

Your Union.ai account can display locally run workflows before you connect any cloud infrastructure. A workflow you run with `--tracked` executes on your own machine and reports its progress to Union.ai as it goes so you can see how Union.ai works before you create a cluster.

## What you'll need

- A Union.ai organization. See [Sign up and create your Union.ai organization](./sign-up).
- Your organization's address, in the form `<your-org>.hosted.unionai.cloud`. It is in your browser's address bar when you are signed in to the Union.ai UI.
- Python 3.10+ in a virtual environment.

## Set up the CLI

Install the Flyte SDK, which includes the `flyte` command:

```bash
pip install flyte
```

Create a configuration file that points the CLI at your organization. Replace the endpoint with your organization's address:

```bash
flyte create config \
    --endpoint <your-org>.hosted.unionai.cloud \
    --domain development \
    --project default \
    --builder remote
```

This writes `.flyte/config.yaml` in the current directory. The first command that contacts your organization opens a browser window so you can sign in; after that, the CLI remembers you.

## Run the built-in example workflow

Run a built-in example workflow. It needs no files of its own:

```bash
flyte run --tracked hello
```

The `--tracked` flag runs the workflow on your machine and reports its progress to your organization as it goes. You'll see output like this:

```bash
Using the built-in example from /tmp/flyte-hello-<user>/task/hello.py
Copy it into your own project to start editing.

Completed Local Run
Path: https://my-org.hosted.unionai.cloud/v2/domain/development/project/default/tracked-runs/local-54ce6d6e
Outputs: ActionOutputs(o0=14.0)
```

The example fans a small computation out over a list of inputs with `flyte.map` and averages the results. The path Union.ai prints is the run's page in the UI.

## Alternatively, create your own workflow

For example, save this file as `hello.py` in a new directory

```python
import flyte

env = flyte.TaskEnvironment(name="hello_env")

@env.task
def fn(x: int) -> int:
    slope, intercept = 2, 5
    return slope * x + intercept

@env.task
def main(x_list: list[int] = [1,2,3,4,5]) -> float:
    y_list = list(flyte.map(fn, x_list))
    return sum(y_list) / len(y_list)
```

then, run it with

```bash
flyte run --local --tracked hello.py main
```

## See your run in the UI

Open the printed path, or select **Tracked Runs** in the sidebar of your project. Tracked runs have their own section, separate from **Runs**, which shows runs that executed on a cluster.

<!-- screenshot: tracked-run details page for the hello run. Frame on the action tree (main + 10 workers). Evidence shot exists at 1x: shots/evidence-tracked-run-details-1x.jpg; recapture at 2x. -->

The run's page shows:

- The run and each of its actions, with status and timing. The example has one parent action and ten child actions, one per input.
- The environment the task belongs to.
- Under **Summary**, the inputs the run received and the outputs it produced.

Everything you see here came from a run on your own machine. Union.ai recorded it as it happened.

## Next steps

**[Provision your AWS resources](./aws-infrastructure)**, then **[connect your cluster](./connect-a-cluster)**, are the next steps of the setup. Everything so far has run on your own machine. When you want Union.ai to run your workloads for you, with GPUs and cluster-scale resources, give it a Kubernetes cluster and it installs the data plane into it. On a cluster other than EKS, skip straight to connecting it.

Two things you can do without a cluster:

- **Run your own code the same way.** Write a workflow following the [Quickstart](../../user-guide/get-started/quickstart), then run it with `flyte run --tracked temperatures.py hottest`. See [Track local runs in the console](../../user-guide/get-started/run-modes/running-locally#track-local-runs-in-the-console) for what tracking does and does not report.
- **Learn the concepts.** [Core concepts](../../user-guide/get-started/core-concepts/_index) explains tasks, environments, projects, and runs.
