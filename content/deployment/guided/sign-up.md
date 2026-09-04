---
title: Sign up and run your first workflow
description: Create a free Union account, then run a workflow on your own machine and watch it in the console. No cluster needed.
icon: person-plus
weight: 0
variants: -flyte +union
---

# Sign up and run your first workflow

Create an account, then run a workflow and watch it in the {{< key product_name >}} console. Nothing runs on a cluster: your first workflow executes on your own machine and reports its progress to {{< key product_name >}}, so you can see how {{< key product_name >}} works before connecting any infrastructure.

## What you'll need

- A Google Workspace account. Sign-up uses your work email; personal Gmail addresses are not accepted.
- Python 3.10+ in a virtual environment.

## Create your account

Go to [signup.union.ai](https://signup.union.ai) and select **Continue with Google**. Choose the account you want to use for {{< key product_name >}}.

<!-- screenshot: sign-in page, frame on "Continue with Google". Capture on staging; crop the URL bar. -->

## Create your organization

An organization is your top-level workspace in {{< key product_name >}}. It is where your projects, workflows, resources, and team members live.

1. **Organization name.** This becomes your organization's web address, so it must be unique across {{< key product_name >}}, and it cannot be changed later. Use lowercase letters, digits, and hyphens. As you type, {{< key product_name >}} checks whether the name is available.

   <!-- screenshot: org form with a name typed and "Available" showing, frame on the name field + availability state. Hold for prod: the region list and the domain suffix differ on staging. -->

2. **Preferred Union region.** This is where your control plane runs. The control plane is the {{< key product_name >}} service that manages your workflows, metadata, and user interface. If you later connect a cluster of your own, choose the region closest to it. If you are not sure, keep the default.

3. Select **Create Organization**.

{{< key product_name >}} sets up your organization in about thirty seconds. You'll see each step complete: receiving the request, creating the organization, setting up sign-in, preparing your workspace, and finalizing.

<!-- screenshot: provisioning phases mid-way, frame on the phase list. -->

## Sign in to your organization

When setup finishes, {{< key product_name >}} takes you to your new organization's sign-in page. Select **Continue with Google** and choose the same account again.

> [!NOTE]
> You may be asked to choose your Google account more than once during sign-up. This is expected: your account, your organization, and the console each confirm who you are.

You land in the {{< key product_name >}} console. Your organization's address is shown at the top of the page, in the form `my-org.hosted.unionai.cloud`. You'll need it in the next step.

> [!NOTE] You don't need a cluster yet
> The console first asks you to set up a cluster pool. That is [connecting your own cluster](./connect-a-cluster), and you can come back to it any time. For your first run, skip it: select **Projects** in the sidebar. Your organization already has a `default` project ready to use.

## Set up the CLI

Install the Flyte SDK, which includes the `flyte` command:

```bash
pip install flyte
```

Create a configuration file that points the CLI at your organization. Replace the endpoint with your organization's address from the previous step:

```bash
flyte create config \
    --endpoint my-org.hosted.unionai.cloud \
    --project default \
    --domain development \
    --builder remote
```

This writes `.flyte/config.yaml` in the current directory. The first command that contacts your organization opens a browser window so you can sign in; after that, the CLI remembers you.

<!-- verify on the capture pass: confirm the exact sign-in behaviour a brand-new user sees from the CLI (device flow vs browser redirect) and reconcile this paragraph to it. -->

## Run your first workflow

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

The example fans a small computation out over a list of inputs with `flyte.map` and averages the results. The path {{< key product_name >}} prints is the run's page in the console.

## See your run in the console

Open the printed path, or select **Tracked Runs** in the sidebar of your project. Tracked runs have their own section, separate from **Runs**, which shows runs that executed on a cluster.

<!-- screenshot: tracked-run details page for the hello run. Frame on the action tree (main + 10 workers). Evidence shot exists at 1x: shots/evidence-tracked-run-details-1x.jpg; recapture at 2x. -->

The run's page shows:

- The run and each of its actions, with status and timing. The example has one parent action and ten child actions, one per input.
- The environment the task belongs to.
- Under **Summary**, the inputs the run received and the outputs it produced.

Everything you see here came from a run on your own machine. {{< key product_name >}} recorded it as it happened.

## Next steps

- **Run your own code the same way.** Write a workflow following the [Quickstart](../../user-guide/get-started/quickstart), then run it with `flyte run --tracked temperatures.py hottest`. See [Track local runs in the console](../../user-guide/get-started/run-modes/running-locally#track-local-runs-in-the-console) for what tracking does and does not report.
- **Connect a cluster.** When you want {{< key product_name >}} to run your workloads for you, with GPUs and cluster-scale resources, return to the cluster pool setup in the console. See [Run on a remote cluster](../../user-guide/get-started/run-modes/running-remote).
- **Learn the concepts.** [Core concepts](../../user-guide/get-started/core-concepts/_index) explains tasks, environments, projects, and runs.
