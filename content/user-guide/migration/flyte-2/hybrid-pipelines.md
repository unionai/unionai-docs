---
title: Hybrid v1 and v2 pipelines
weight: 14
variants: +flyte +union
---

# Hybrid v1 and v2 pipelines

Migrations rarely happen all at once. For a while you'll have Flyte 1 and Flyte 2 workloads running side by side, and you'll want them to call each other: a Flyte 1 workflow that kicks off a newly ported Flyte 2 task, or a Flyte 2 task that triggers a workflow that hasn't been migrated yet.

You can bridge the two in both directions. The idea is the same each way: one task installs **both** SDKs, authenticates to the **other** control plane, fetches the entity it wants to run, and launches it.

{{< note >}}
The bridging task acts as a driver: it authenticates to a remote control plane and launches work there. Keep it lightweight and focused on orchestration — see [Considerations](./considerations).
{{< /note >}}

## Running a Flyte 2 task from a Flyte 1 workflow

The bridge is a single Flyte 1 task — call it `launch_v2_from_v1` — that runs the Flyte 2 client.

**High-level steps:**

1. Give the `launch_v2_from_v1` task an image with **both** `flytekit` (Flyte 1) and `flyte` (Flyte 2) installed.
2. Give it a Flyte 2 **API key** (see [Create the API key](#1-create-the-api-key-and-store-it) below — how you create one differs between Union and open-source Flyte). The key is the `export FLYTE_API_KEY="..."` value it produces.
3. Make the key available to the task, either by storing it as a secret it can read, or by injecting it as the `FLYTE_API_KEY` environment variable.
4. Authenticate inside the task with `flyte.init_from_api_key()`.
5. Fetch the deployed Flyte 2 task with `flyte.remote.Task.get(...)` and run it with `flyte.run(...)`.

### 1. Create the API key and store it

{{< variant union >}}
{{< markdown >}}
Create a key with `flyte create api-key` (a command provided by the `flyteplugins-union` plugin) or through the Union UI, then store it as a secret:

```bash
# Create a Flyte 2 API key (prints `export FLYTE_API_KEY="..."`)
flyte create api-key --name v1-to-v2-bridge

# Store that value as a Flyte 2 secret (you can also create it in the Union UI)
flyte create secret flyte_api_key --value "<the-encoded-key>"
```
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
Obtain a Flyte 2 API key from your control plane's authentication setup and store it as a secret the bridging task can read — see [Run on a remote cluster](../../run-modes/running-remote) for the authentication options.
{{< /markdown >}}
{{< /variant >}}

You can also make the same value available to your Flyte 1 task as a secret through your existing Flyte 1 secret workflow, or set it directly as the `FLYTE_API_KEY` environment variable on the task.

### 2. Write the bridging task

```python
import flytekit
from flytekit import task, workflow, ImageSpec, Secret, current_context

# The bridge image needs BOTH the v1 (flytekit) and v2 (flyte) SDKs.
bridge_image = ImageSpec(
    name="v1-to-v2-bridge",
    packages=["flytekit", "flyte"],
)


@task(
    container_image=bridge_image,
    secret_requests=[Secret(group="flyte", key="flyte_api_key")],
)
def launch_v2_from_v1(x: int) -> str:
    import flyte
    import flyte.remote

    # Authenticate to the Flyte 2 control plane with the API key.
    # Option A: read the mounted secret and pass it explicitly.
    api_key = current_context().secrets.get(group="flyte", key="flyte_api_key")
    flyte.init_from_api_key(api_key=api_key)

    # Option B: if FLYTE_API_KEY is set as an env var, no argument is needed:
    #     flyte.init_from_api_key()

    # Fetch the deployed Flyte 2 task and run it.
    remote_v2_task = flyte.remote.Task.get(
        "my_v2_env.process",
        auto_version="latest",
    )
    run = flyte.run(remote_v2_task, x=x)
    run.wait()  # optional: block until the v2 run finishes
    return run.url


@workflow
def main(x: int) -> str:
    return launch_v2_from_v1(x=x)
```

The referenced Flyte 2 task (`my_v2_env.process` above) must be **deployed** before the bridge runs — `flyte.remote.Task.get()` looks it up by `env_name.task_name`. See [Remote tasks](../../task-programming/remote-tasks) for versioning options (`auto_version="latest"`, `version="v1.2.3"`) and `flyte.run` details.

{{< note >}}
`flyte.init_from_api_key()` is required here — do **not** use `flyte.init_from_config()`, which reads a `config.yaml` that has no API-key field. See [Run on a remote cluster](../../run-modes/running-remote) for the authentication methods.
{{< /note >}}

## Running a Flyte 1 workflow from a Flyte 2 task

The reverse works the same way: a Flyte 2 task installs the Flyte 1 client and uses `{{< key kit_remote >}}` to launch a Flyte 1 workflow.

**High-level steps:**

1. Give the `launch_v1_from_v2` `TaskEnvironment` an image with the Flyte 1 client (`{{< key kit >}}`) installed.
2. Provide the task with credentials for the Flyte 1 control plane (a config file or API key, supplied as a secret).
3. Instantiate a `{{< key kit_remote >}}` client inside the task.
4. Fetch the Flyte 1 workflow with `fetch_workflow(...)`.
5. Launch it with `execute(...)`.

```python
import flyte

env = flyte.TaskEnvironment(
    name="v2_to_v1_bridge",
    # The image needs the Flyte 1 client installed.
    image=flyte.Image.from_debian_base().with_pip_packages("{{< key kit >}}"),
    # Supply credentials for the Flyte 1 control plane (config or API key).
    secrets=[flyte.Secret(key="v1_client_secret", as_env_var="V1_CLIENT_SECRET")],
)


@env.task
async def launch_v1_from_v2(x: int) -> str:
    from flytekit.remote import FlyteRemote
    from flytekit.configuration import Config

    # Point the client at your Flyte 1 cluster.
    remote = FlyteRemote(
        config=Config.for_endpoint(endpoint="my-v1-cluster.example.com"),
        default_project="flytesnacks",
        default_domain="development",
    )

    # Fetch the deployed Flyte 1 workflow and execute it.
    wf = remote.fetch_workflow(name="my_v1_module.main", version="v1.2.3")
    execution = remote.execute(wf, inputs={"x": x}, wait=True)
    return execution.id.name
```

{{< variant union >}}
{{< markdown >}}
On Union, use `union.remote.UnionRemote` instead of `flytekit.remote.FlyteRemote`. It auto-detects your Union configuration, so you can construct it with no arguments:

```python
from union.remote import UnionRemote

remote = UnionRemote(default_project="flytesnacks", default_domain="development")
wf = remote.fetch_workflow(name="my_v1_module.main", version="v1.2.3")
execution = remote.execute(wf, inputs={"x": x}, wait=True)
```
{{< /markdown >}}
{{< /variant >}}

## Considerations

- **Both SDKs in one image.** The bridging task installs `flytekit` and `flyte` together. Pin versions and watch for dependency conflicts; keep the bridge image minimal.
- **Deploy the callee first.** For the v1→v2 direction, the Flyte 2 task must be deployed (`flyte deploy`) before `flyte.remote.Task.get()` can resolve it. For the v2→v1 direction, the Flyte 1 workflow must be registered on its cluster.
- **Wait vs. fire-and-forget.** Both `run.wait()` (v2) and `execute(..., wait=True)` (v1) block until the launched run finishes. Omit them to launch and return immediately, then poll or hand off the execution URL.
- **Credentials cross a boundary.** The bridge authenticates to a *different* control plane than the one it runs on. Store the API key or client credentials as a secret — never hard-code them. See [Secrets](../../task-configuration/secrets) and [Run on a remote cluster](../../run-modes/running-remote).
- **Keep the bridge lightweight.** Like any orchestrating task, it should mostly launch and assemble results rather than do heavy compute — see [Considerations](./considerations).

## See also

- [Remote tasks](../../task-programming/remote-tasks) — fetching and running deployed Flyte 2 tasks
- [Run on a remote cluster](../../run-modes/running-remote) — authentication methods, including `flyte.init_from_api_key()`
{{< variant union >}}
{{< markdown >}}
- [Authenticating](../../authenticating#api-key) — API key authentication in depth
{{< /markdown >}}
{{< /variant >}}
- [Migration](./migration) — mapping Flyte 1 workload patterns to Flyte 2
