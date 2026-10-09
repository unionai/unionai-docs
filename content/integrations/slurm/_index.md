---
title: Slurm
description: Run Flyte tasks as Slurm jobs on an existing HPC or GPU cluster, submitted over SSH.
icon: hdd-stack
weight: 3
variants: +flyte +union
---

# Slurm

The Slurm plugin lets you run Flyte tasks as jobs on an existing [Slurm](https://slurm.schedmd.com/) cluster — an on-premise HPC installation, a cloud GPU cluster, or one managed by an operator such as [Soperator](https://github.com/nebius/soperator). Jobs are submitted over SSH to a login node, so no Flyte component runs on the cluster and Slurm itself needs no reconfiguration. The plugin assumes nothing about which cloud the cluster runs in or where the run's object storage lives.

What the cluster does need depends on the task type. A native `slurm` task runs your container image, so the compute nodes need Pyxis/Enroot or Apptainer and credentials for the run's object storage, and requesting GPUs needs GRES configured. A `slurm_script` task needs none of that. The connector handles submission, state polling, cancellation and log retrieval.

The plugin supports:

- Running Python tasks on Slurm with the same typed inputs and outputs they would have on Kubernetes
- Running existing `sbatch` scripts, including multi-node jobs
- Full `sbatch` scheduling options, either as first-class fields or passed through
- Containerized execution through Pyxis/Enroot or Apptainer
- Slurm state mapping, so a queued job is not counted as running and a preempted job is retried

## Installation

```bash
pip install flyteplugins-slurm
```

The connector must also be installed in the `flyteconnector` image of your data plane. See [Deployment](#deployment).

## Task types

The plugin provides two task types, served by one connector.

| Task type | What is submitted | Typed I/O | Caching | Multi-node |
| --------- | ----------------- | --------- | ------- | ---------- |
| `slurm` | The task's own container image and the Flyte entrypoint, via Pyxis or Apptainer | Yes | Yes | No |
| `slurm_script` | A user-supplied `sbatch` script, with `#SBATCH` directives and input/output exports prepended | `File` and `Dir`, declared | Yes | Yes |

Prefer `slurm` for anything that can be containerized and runs as a single process. Use `slurm_script` when a script cannot be converted, or when you need gang-scheduled multi-node execution.

## Quick start

Create a `Slurm` configuration and pass it as `plugin_config` to a `TaskEnvironment`:

```python
import flyte
from flyte.io import File
from flyteplugins.slurm import Slurm

slurm_env = flyte.TaskEnvironment(
    name="train",
    plugin_config=Slurm(
        partition="main",
        nodes=1,
        gres="gpu:8",
        time_limit="4:00:00",
        # Credentials for the run's object storage, mounted rather than passed in `env`.
        container_mounts=["/home/flyte/.cloud:/etc/cloud:ro"],
        env={"AWS_SHARED_CREDENTIALS_FILE": "/etc/cloud/credentials"},
    ),
    image=flyte.Image.from_debian_base().with_pip_packages("flyteplugins-slurm"),
)


@slurm_env.task(cache="auto", retries=2)
async def train(steps: int = 1000) -> File:
    ...
```

Remove `plugin_config` and the same task runs as a Kubernetes pod with no other changes. That is also the quickest way to tell a Slurm problem apart from a task problem.

> [!WARNING] Do not set `resources` on a Slurm task environment
> The allocation comes from the `Slurm` configuration and is granted by Slurm, not by Kubernetes. Setting `resources` raises an error. Use `cpus_per_task`, `mem`, `gres` or `gpus_per_node` instead.

## Running an existing sbatch script

`SlurmScriptTask` submits an existing script. Scalar inputs are exported as `FLYTE_INPUT_<NAME>`:

```python
import flyte
from flyteplugins.slurm import Slurm, SlurmScriptTask

train = SlurmScriptTask(
    name="train",
    script=open("train.sbatch").read(),
    plugin_config=Slurm(partition="main", nodes=4, time_limit="8:00:00"),
    inputs={"epochs": int},
)

env = flyte.TaskEnvironment.from_task("legacy-train", train)
```

The plugin makes three changes to the script before submitting it:

- The script's own leading `#SBATCH` directives are moved to the top, followed by the plugin's directives. `sbatch` takes the last value for a duplicate option, so the plugin's settings win on conflict and all other options are kept.
- `export` lines for inputs and outputs are added after the directives.
- A leading shebang is dropped.

Keep your `#SBATCH` directives above the first executable line, because `sbatch` stops reading directives there. Because the script drives `srun` itself, this is the task type to use for multi-node work.

> [!NOTE] Script tasks must belong to an environment
> A task has to be attached to a `TaskEnvironment` before it can be serialized. `flyte.TaskEnvironment.from_task` does that for a standalone task.

> [!NOTE] What a script can receive
> `str`, `int`, `float` and `bool` arrive as `FLYTE_INPUT_<NAME>`, and `File`/`Dir` as their URI for the script to fetch with its own tooling. Any other type fails the task at submission, because an environment variable cannot carry it. Pass a URI as a `str` instead.

### Outputs from a script task

A script cannot write Flyte's output format, so a script task returns only the outputs you declare. Without declared outputs, the task returns nothing.

#### Declare what the script will write

```python
train = SlurmScriptTask(
    name="train",
    script=open("train.sbatch").read(),
    plugin_config=Slurm(partition="main"),
    inputs={"epochs": int},
    outputs={"model": File, "shards": Dir},
)
```

**Only `File` and `Dir` may be declared.** Any other type is rejected when the task is defined. A native `slurm` task supports all types; see [Output types](#output-types).

> [!WARNING] A declared output the script never wrote fails the task
> This happens even if the script exits with 0, so a downstream task never receives a URI that points to nothing.

#### Write to the destination the script is given

Each declared output arrives as `FLYTE_OUTPUT_<NAME>`, upper-cased. By default that is a local path, so writing the output is a `cp`:

```bash
python train.py --epochs "$FLYTE_INPUT_EPOCHS" --out ./model.pt
cp ./model.pt "$FLYTE_OUTPUT_MODEL"
```

**Every `$FLYTE_OUTPUT_*` the script uses must be declared in `outputs`, and every declared output must be written.** Both are checked:

| The script has | `outputs` has | What happens |
| --- | --- | --- |
| `$FLYTE_OUTPUT_MODEL` | `{"model": File}` | The output is recorded and a downstream task can read it |
| `$FLYTE_OUTPUT_MODEL` | nothing, or another name | `ValueError` when the task is defined |
| nothing | `{"model": File}` | The task fails when the job finishes, even on exit 0 |

The definition-time check only sees `$NAME` and `${NAME}` expansions in the script. A mention in a comment does not count, and a variable name built at run time is not checked.

When the job succeeds, the connector checks that every destination exists and records it as the declared `File` or `Dir`.

#### Choose who uploads

`output_upload` decides who moves the output bytes to object storage:

| | `"connector"` (default) | `"job"` |
| --- | --- | --- |
| `FLYTE_OUTPUT_<NAME>` holds | a local path | the object-storage URI |
| Who uploads | the connector, after the job | the script, during the job |
| The compute node needs | nothing | a client and credentials for the store |
| The bytes travel | node → connector → storage | node → storage |
| Size limit | 100 MiB by default | none |

**`"connector"`** suits small outputs such as metrics, summaries, configs and small models. The node needs no upload tool and no credentials.

The upload runs in the background after the Slurm job finishes. The task stays in `RUNNING`, with a message naming the outputs being moved, for a poll or two after the job ends. This is expected.

> [!WARNING] The connector refuses to move more than 100 MiB
> The task fails when an output is over the limit. The limit is only checked after the job has run, so the job's work is lost. Use `output_upload="job"` for any output that might be large.

Operators can change the limit with `FLYTE_SLURM_CONNECTOR_UPLOAD_MAX_BYTES` on the connector deployment. It takes a byte count or a size with a suffix (`500MB`, `2GB`, `512MiB`), or `0` for no limit.

**`"job"`** has no size limit, because the bytes go straight from the compute node to storage:

```python
train = SlurmScriptTask(..., outputs={"model": File}, output_upload="job")
```

```bash
# S3, and S3-compatible stores (MinIO, R2, Ceph) with --endpoint-url
aws s3 cp ./model.pt "$FLYTE_OUTPUT_MODEL"

# Google Cloud Storage
gcloud storage cp ./model.pt "$FLYTE_OUTPUT_MODEL"

# Azure Blob
azcopy copy ./model.pt "$FLYTE_OUTPUT_MODEL"

# A directory output: copy the tree
aws s3 cp --recursive ./checkpoints "$FLYTE_OUTPUT_CHECKPOINTS"
```

A script task runs directly on the node, not in a container, so the available tools depend on the site. Check on a compute node, not the login node, since they may differ:

```bash
srun --ntasks=1 bash -c 'command -v aws rclone gcloud azcopy'
```

`rclone` is common on HPC clusters and needs no configured remote if you give it the backend inline. It takes a bucket path rather than a URL, so strip the scheme:

```bash
GCS=":gcs,service_account_file=$HOME/.gcp/sa.json,bucket_policy_only=true:"
rclone copyto ./model.pt "${GCS}${FLYTE_OUTPUT_MODEL#gs://}"

S3=":s3,provider=AWS,env_auth=true:"
rclone copyto ./model.pt "${S3}${FLYTE_OUTPUT_MODEL#s3://}"
```

> [!WARNING] `bucket_policy_only=true` is required on a uniform-access GCS bucket
> Without it, rclone sets a per-object ACL, and a bucket with uniform bucket-level access (the default for new buckets) rejects the write with `Error 400: Cannot insert legacy ACL for an object`. The job fails after doing its work.

Mount credentials the same way as for a native task. See [Object storage from inside the job](#object-storage-from-inside-the-job).

> [!NOTE] This section does not apply to native `slurm` tasks
> A native task runs the Flyte entrypoint inside the job, which writes its outputs to object storage directly. There is no upload mode to choose and no size limit.

## Configuration

### Scheduling

These fields map one-to-one onto `sbatch` options.

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `partition` | `str` | Partition to submit to |
| `nodes` | `int` | Number of nodes to allocate |
| `ntasks` | `int` | Number of tasks (`--ntasks`) |
| `cpus_per_task` | `int` | CPUs per task |
| `gres` | `str` | Generic resources, for example `"gpu:8"`. Requires GRES configured on the cluster; see the warning below |
| `gpus_per_node` | `int` or `str` | GPUs per node, for example `8` or `"h100:8"` |
| `mem` | `str` | Memory per node, for example `"64G"` |
| `time_limit` | `str` | Wall-clock limit in Slurm format, for example `"4:00:00"` |
| `account` | `str` | Account to charge |
| `qos` | `str` | Quality of service |
| `reservation` | `str` | Reservation name |
| `constraint` | `str` | Node feature constraint |
| `sbatch_options` | `Dict[str, Any]` | Any other `sbatch` option, as `--<key>=<value>`. `True` renders a bare flag. Overrides the first-class fields on conflict. The plugin sets `job-name`, `output` and `error` itself, so these are rejected, as are `chdir`, `wrap`, `uid` and `gid` |

### Container and execution

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `container_runtime` | `str` | How the image is launched: `"pyxis"` (default) or `"apptainer"`. See [Container runtimes](#container-runtimes) |
| `container_image` | `str` | Override the image given to the runtime, for example a pre-imported `.sqsh` or `.sif` path. Defaults to the task's image |
| `container_mounts` | `List[str]` | Bind mounts as `src:dst[:ro]`, for example `["/data:/data"]` |
| `container_workdir` | `str` | Working directory inside the container |
| `container_args` | `List[str]` | Extra arguments for the container runtime, for example `["--rocm"]` for AMD GPUs under Apptainer |
| `modules` | `List[str]` | Environment modules to `module load` before the job runs, for example `["apptainer"]` |
| `srun_args` | `List[str]` | Extra arguments inserted before the command on the `srun` line |
| `env` | `Dict[str, str]` | Environment variables exported into the job |
| `working_dir` | `str` | Directory for generated scripts and logs. Relative paths are under the SSH user's home. Defaults to `.flyte/jobs` |

> [!WARNING] `gres` and `gpus_per_node` require GRES on the cluster
> GPU scheduling must be enabled on each cluster: the controller needs `GresTypes` set and each node needs its own `Gres` entry. On a cluster without them, any GPU request is rejected at submission and the task never starts:
>
> ```
> sbatch: error: Invalid generic resource (gres) specification.
> ```
>
> Check what a cluster offers before requesting it:
>
> ```bash
> sinfo -N -o "%N %G"        # per-node GRES; "(null)" means none configured
> ```

> [!WARNING] Never put secrets in `env`
> Values in `env` are written into the generated `sbatch` script in plain text, and that script stays on the cluster filesystem. Mount credentials from the cluster's shared filesystem and reference the path instead.

### Connection

Each of these can be set per task, or once for the whole cluster on the connector deployment.

| Parameter | Connector environment variable | Description |
| --------- | ------------------------------ | ----------- |
| `host` | `FLYTE_SLURM_HOST` | Login node hostname |
| `port` | `FLYTE_SLURM_PORT` | SSH port, default `22` |
| `username` | `FLYTE_SLURM_USERNAME` | SSH user that jobs are submitted as |
| `ssh_private_key` | `FLYTE_SLURM_SSH_PRIVATE_KEY` | Name of the Flyte secret holding the SSH private key |
| `known_hosts` | `FLYTE_SLURM_KNOWN_HOSTS` | Path to a `known_hosts` file on the connector, for host-key verification |
| `known_hosts_secret` | — | Name of a Flyte secret holding the `known_hosts` entries. Needs no file mounted on the connector |
| — | `FLYTE_SLURM_SKIP_HOST_KEY_VERIFICATION` | Disable host-key verification. Development only |
| — | `FLYTE_SLURM_WORKING_DIR` | Cluster-wide default for `working_dir` |
| — | `FLYTE_SLURM_CONNECTOR_UPLOAD_MAX_BYTES` | Largest script-task output the connector will upload; default `100MiB`, `0` for no limit |

Setting the connection once on the connector is usually best: tasks then carry only scheduling options and stay portable.

> [!NOTE] Connector environment variables override task configuration
> For `host`, `port`, `username` and `known_hosts`, a value set on the connector wins over the task's value. This stops a task from sending the deployment's SSH key to a different host. A task's value is used only when the connector sets none. `FLYTE_SLURM_WORKING_DIR` is the exception: a task's `working_dir` overrides it.

## Container runtimes

A native `slurm` task runs your image on the compute node, which needs a container runtime on the cluster. `container_runtime` selects it:

| | `pyxis` (default) | `apptainer` |
|---|---|---|
| How it launches | flags on `srun` | `apptainer exec` in the job |
| Image reference | `ghcr.io#org/img:tag` | `docker://ghcr.io/org/img:tag` |
| `container_mounts` becomes | `--container-mounts` | `--bind` |
| `container_workdir` becomes | `--container-workdir` | `--pwd` |
| Local image | `.sqsh` path | `.sif` path |
| GPUs | Enroot exposes them automatically | `--nv` is added when the job requests GPUs |

```python
Slurm(partition="main", container_runtime="apptainer")
```

Pyxis is common on GPU clusters built on NVIDIA's stack; Apptainer is more common at traditional HPC sites. The rest of the job is the same for both, so a task moves between clusters by changing this one field. Check which runtime the cluster has:

```bash
scontrol show config | grep -i plugstack   # Pyxis: look for spank_pyxis.so
command -v apptainer                       # Apptainer
```

If `apptainer` is only available through environment modules, add it to `modules`. A cluster with neither runtime cannot run native tasks; use `slurm_script` instead. An unknown `container_runtime` value is rejected when the task is defined.

> [!NOTE] Apptainer support is unit-tested only
> The plugin's Apptainer path has not been run against a real Apptainer cluster. See [Known gaps](#known-gaps).

## Container images

The plugin converts the task's image reference into the form the runtime expects:

| Input | Pyxis | Apptainer |
| ----- | ----- | --------- |
| `ghcr.io/myorg/train:v1` | `ghcr.io#myorg/train:v1` | `docker://ghcr.io/myorg/train:v1` |
| `python:3.12-slim` | unchanged | `docker://python:3.12-slim` |
| `/jail/images/train.sqsh` or `.sif` | unchanged | unchanged |

On clusters that pre-import images to a shared filesystem, point at the image file directly and skip the registry pull:

```python
Slurm(container_image="/jail/images/train.sqsh", partition="main")
```

> [!WARNING] Compute nodes need their own registry credentials
> Images are pulled on the compute nodes, as the submitting user. Your local Docker login and Kubernetes `imagePullSecrets` do not apply. For a private registry:
>
> - **Pyxis**: add an entry to `~/.config/enroot/.credentials`:
>
>   ```
>   machine ghcr.io login <username> password <token>
>   ```
>
> - **Apptainer**: run `apptainer registry login --username <username> docker://ghcr.io`, or set `APPTAINER_DOCKER_USERNAME` and `APPTAINER_DOCKER_PASSWORD`.
>
> Without credentials, the pull is anonymous and fails with `401 Unauthorized`.

## Object storage from inside the job

A `slurm` task runs the Flyte entrypoint inside the job, which reads inputs and writes outputs to the run's object storage. Compute nodes therefore need network access to that storage and credentials for it.

The credentials depend on the store:

| Store | Variable the job needs |
| --- | --- |
| S3, and S3-compatible (MinIO, R2, Nebius, …) | `AWS_SHARED_CREDENTIALS_FILE`, or the usual `AWS_*` pair |
| Google Cloud Storage | `GOOGLE_APPLICATION_CREDENTIALS` |
| Azure Blob | `AZURE_STORAGE_*` |

Mount the credential file from the cluster's shared filesystem with `container_mounts` and set its path in `env`, as in the [quick start](#quick-start). Do not put the secret itself in `env`.

Outputs land in the same place they would for a Kubernetes pod task, so a Slurm task can pass results to a task running elsewhere:

```python
slurm_env = flyte.TaskEnvironment(
    name="train",
    plugin_config=Slurm(partition="main", gres="gpu:8"),
    image=image,
)

k8s_env = flyte.TaskEnvironment(name="pipeline", image=image, depends_on=[slurm_env])


@k8s_env.task
async def prepare(rows: int) -> Dir: ...

@slurm_env.task
async def train(dataset: Dir) -> File: ...

@k8s_env.task
async def evaluate(model: File) -> dict[str, str]: ...

@k8s_env.task
async def pipeline() -> dict[str, str]:
    return await evaluate(await train(await prepare(1000)))
```

> [!WARNING] Return `File` or `Dir`, not a cluster filesystem path
> Returning a path such as `"/data/model.pt"` as a `str` passes type checking, then fails when a task on another cluster opens it, because the Slurm cluster's filesystem does not exist there. Return `flyte.io.File` or `flyte.io.Dir` so the contents are uploaded. Plain paths work only between tasks that share a filesystem.

For data read repeatedly, such as a training set read every epoch, copy it to the Slurm cluster's shared filesystem once and pass a path on the cluster. Reading it from object storage on every epoch is slow and expensive.

## Outputs and caching

### Output types

| | `slurm` | `slurm_script` |
| --- | --- | --- |
| Scalars — `int`, `float`, `str`, `bool`, `datetime`, `date`, `timedelta`, `None` | Yes | No |
| Containers — `list`, `dict`, `Union`, `Optional`, `Enum` | Yes | No |
| Structured — dataclass, Pydantic model, protobuf | Yes | No |
| Offloaded — `File`, `Dir`, `DataFrame` | Yes | `File` and `Dir`, declared |
| Anything else, via pickle | Yes | No |
| Several outputs as a `tuple` | Yes | Yes, all declared |

A native `slurm` task runs the same entrypoint as a Kubernetes pod task, so its outputs work exactly as they do on Kubernetes. A `slurm_script` task returns only declared `File` and `Dir` outputs, as described in [Outputs from a script task](#outputs-from-a-script-task).

Because the job does its own I/O, return large values as a `File` or `Dir` rather than directly. Inline inputs and outputs are capped by `max_inline_io_bytes`.

### Caching

Both task types cache with `cache="auto"`:

```python
train = SlurmScriptTask(name="train", script=SCRIPT, outputs={"model": File}, cache="auto")
```

A cache hit restores the declared outputs and does not submit the job.

For a native task, the cache version comes from the task function's source, as for any Python task. A script task has no function, so the plugin computes the version from the script and its configuration instead:

| Change | Cache |
| --- | --- |
| The script body | **Invalidated** |
| A declared output added, removed, or retyped | **Invalidated** |
| Scheduling and container config — `partition`, `nodes`, `time_limit`, `gres`, `sbatch_options`, … | **Invalidated** |
| `host`, `port`, `username`, `ssh_private_key`, `known_hosts` | Reused |
| `output_upload` | Reused |

Moving to a new login node, rotating the SSH secret or changing who uploads does not change what the job computes, so the cache is kept.

An explicit `Cache(behavior="override", version_override=...)` is used as-is; the plugin only computes a version when the behavior is `"auto"`. `cache="disable"` turns caching off.

> [!NOTE] Caching a script task with no declared outputs
> A cache hit skips the job and restores the outputs. With no outputs declared, a hit just skips the job, which is rarely what you want from a script that runs for its side effects. Declare outputs, or set `cache="disable"`.

## Job state mapping

Only the first word of the Slurm state is matched, with any trailing `+` removed, so `CANCELLED by 1234` and `CANCELLED+` are both treated as `CANCELLED`. The table lists every state the connector maps. Any other state is not treated as running: the connector's status check raises `ValueError` (`Unrecognized Slurm job state ...`) instead of reporting a phase, and the connector logs that error.

| Slurm state | Flyte phase | Notes |
| ----------- | ----------- | ----- |
| `PENDING`, `CONFIGURING`, `REQUEUED`, `REQUEUE_HOLD`, `REQUEUE_FED`, `RESV_DEL_HOLD`, `SUSPENDED`, `STOPPED` | `QUEUED` | Time waiting for an allocation does not count as running |
| `RUNNING`, `COMPLETING`, `STAGE_OUT`, `SIGNALING`, `RESIZING` | `RUNNING` | — |
| `COMPLETED` | `SUCCEEDED` | Script tasks with `output_upload="connector"` stay `RUNNING` until the connector has uploaded their outputs |
| `FAILED`, `NODE_FAIL`, `OUT_OF_MEMORY`, `TIMEOUT`, `DEADLINE`, `BOOT_FAIL`, `SPECIAL_EXIT`, `REVOKED` | `FAILED` | The message includes Slurm's reason and the end of stderr |
| `PREEMPTED` | `RETRYABLE_FAILED` | Uses a retry instead of failing the run, but only if the task sets `retries` (default 0) |
| `CANCELLED` | `ABORTED` | Aborting the Flyte run runs `scancel` |

State is polled with `squeue`, falling back to `sacct` for jobs that have left the queue. Make sure accounting works for the submitting user. Without it, the connector falls back to `scontrol`; see [Known gaps](#operations).

## Inspecting a job

Every job leaves three files on the login node under `working_dir`, named `flyte-<task>-<8 hex>`:

```bash
ls -t ~/.flyte/jobs | head
cat  ~/.flyte/jobs/<job>.sbatch   # exactly what was submitted
tail ~/.flyte/jobs/<job>.out      # stdout: a successful job's output
tail ~/.flyte/jobs/<job>.err      # stderr: usually where a failure explains itself
```

The generated `.sbatch` file is a plain script. Reading it answers most questions, and running it by hand with `sbatch` tells a plugin problem apart from a cluster problem. Both log paths are also shown in the task's status message in the UI. Nothing deletes these files, so prune them on a schedule that suits the site.

> [!NOTE] No Kubernetes Pod is created
> A Slurm task runs on a Slurm node, not in a pod. An empty pod list for the action is expected; check `sacct` on the cluster instead.

## Deployment

### Connector image

Add `flyteplugins-slurm` to the `flyteconnector` image:

```dockerfile
FROM ghcr.io/flyteorg/flyte-connectors:<tag matching your data plane>
RUN pip install flyteplugins-slurm
```

Push it to a registry the data plane can pull from.

{{< variant union >}}
{{< markdown >}}

### Data plane values

Create the secret holding the SSH key and the `known_hosts` file:

```bash
kubectl -n <namespace> create secret generic slurm-login \
  --from-file=ssh-privatekey=./slurm-connector \
  --from-file=known_hosts=./known_hosts
```

Then point the connector at your image and give it the connection:

```yaml
flyteconnector:
  # Also enables the connector endpoint in the leaseworker's config.
  enabled: true
  image:
    repository: <your-registry>/slurm-connector
    tag: <your-tag>
  additionalEnvs:
    - { name: FLYTE_SLURM_HOST, value: "<login-host>" }
    - { name: FLYTE_SLURM_USERNAME, value: "flyte" }
    - name: FLYTE_SLURM_SSH_PRIVATE_KEY
      valueFrom:
        secretKeyRef: { name: slurm-login, key: ssh-privatekey }
    - { name: FLYTE_SLURM_KNOWN_HOSTS, value: /etc/slurm-login/known_hosts }
  # These two take a map, not a list. See the warning below.
  additionalVolumeMounts:
    volumeMounts:
      - { name: slurm-login, mountPath: /etc/slurm-login, readOnly: true }
  additionalVolumes:
    volumes:
      - name: slurm-login
        secret:
          secretName: slurm-login
          items: [{ key: known_hosts, path: known_hosts }]
```

`FLYTE_SLURM_SSH_PRIVATE_KEY` holds the key's **contents**, so it comes from a `secretKeyRef`. `FLYTE_SLURM_KNOWN_HOSTS` is a **path**, so its file is mounted. To avoid the mount, use `known_hosts_secret` on the task instead.

> [!WARNING] `additionalVolumes` and `additionalVolumeMounts` take a map, not a list
> The chart inserts these values into the pod spec without its own `volumes:` / `volumeMounts:` key, so your value must include it. A plain list, which the chart's `[]` default suggests, renders invalid YAML and fails the upgrade:
>
> ```
> YAML parse error on dataplane/templates/flyteconnector/deployment.yaml:
> error converting YAML to JSON: yaml: did not find expected key
> ```
>
> `additionalEnvs` takes a plain list. Render the template before upgrading:
>
> ```bash
> helm template t <chart> -s templates/flyteconnector/deployment.yaml -f values-slurm.yaml
> ```
>
> On upgrade, Helm also prints `warning: destination for dataplane.flyteconnector.additionalVolumeMounts is a table. Ignoring non-table value ([])`. This is expected.

### The connector's own object-storage access

With `output_upload="connector"` (the default for script tasks), the connector pod writes to the run's output prefix. By default the `flyteconnector` service account does not have the data plane's cloud identity, unlike `union-system`, `webhook` and `dataproxy`. Without it, every upload fails after the job has succeeded:

```
The operation lacked the necessary privileges to complete for path
metadata/v2/<org>/<project>/<domain>/<run>/<action>/0/<output>:
403 Forbidden ... Caller does not have storage.objects.create access
```

Annotate the service account with the identity that can write the metadata bucket, the same one as in `global.BACKEND_IAM_ROLE_ARN`:

```yaml
flyteconnector:
  serviceAccount:
    annotations:
      # GCP
      iam.gke.io/gcp-service-account: union-system@<project>.iam.gserviceaccount.com
      # AWS
      # eks.amazonaws.com/role-arn: arn:aws:iam::<account>:role/<backend-role>
```

On GKE, also add the workload identity binding, or the annotation has no effect:

```bash
gcloud iam service-accounts add-iam-policy-binding \
  union-system@<project>.iam.gserviceaccount.com \
  --role roles/iam.workloadIdentityUser \
  --member "serviceAccount:<project>.svc.id.goog[<namespace>/flyteconnector]"
```

Then restart the deployment so the pods pick up the new identity. This is not needed for native `slurm` tasks or for script tasks with `output_upload="job"`, because the job uploads with its own credentials.

{{< /markdown >}}
{{< /variant >}}

### Verifying the connector

Task types are discovered at runtime from the connector's metadata service, so there is no task-type routing to configure. Confirm the connector advertises them:

```bash
kubectl -n <namespace> logs deploy/flyteconnector | grep -A6 "Connector Metadata"
```

### Credentials

The SSH private key is a Flyte secret named by `ssh_private_key`, or is set cluster-wide as `FLYTE_SLURM_SSH_PRIVATE_KEY` on the `flyteconnector` deployment. Provide `known_hosts` entries for host-key verification, either as a file (`known_hosts`) or a secret (`known_hosts_secret`). `FLYTE_SLURM_SKIP_HOST_KEY_VERIFICATION` on the connector disables verification for development; it cannot be turned off from a task.

### Network

The connector must reach the login node on its SSH port. Restrict the login node's allowed source ranges to the connector's egress addresses, and test from the connector pod, not from your workstation:

```bash
kubectl -n <namespace> exec deploy/flyteconnector -- \
  python -c "import socket; s=socket.socket(); s.settimeout(10); \
             s.connect(('<login-host>', 22)); print(s.recv(64))"
```

The connector keeps one SSH connection per cluster and reuses it across jobs, reconnecting if it drops.

## Known gaps

### Execution

- **No multi-node execution for `slurm` tasks.** The native task runs `srun --nodes=1 --ntasks=1`, so the Flyte entrypoint runs once even when the allocation spans several nodes. Use a `slurm_script` task, which runs `srun` or `mpirun` itself, for distributed work.
- **Only Pyxis and Apptainer are supported.** A cluster with neither cannot run native tasks; use `slurm_script` instead.
- **The Apptainer path is unit-tested only.** It has not been run against a real Apptainer cluster.

### Data and I/O

- **Script task outputs are `File` and `Dir` only.** See [Outputs from a script task](#outputs-from-a-script-task).
- **Script task inputs are scalars and URIs only.** See [Running an existing sbatch script](#running-an-existing-sbatch-script).
- **The connector uploads at most 100 MiB per output by default.** Raise `FLYTE_SLURM_CONNECTOR_UPLOAD_MAX_BYTES`, or use `output_upload="job"`.
- **No clickable log links.** Job stdout and stderr are files on the login node, so their paths are shown in the task's status message. Live logs are streamed through the connector.

### Operations

- **SSH transport only.** `slurmrestd` is not supported.
- **One identity.** Every job runs as the configured SSH user, so the cluster attributes all work to that account, whoever launched the run.
- **Status is polled per job.** The connector runs one `squeue` per job on each poll.
- **Job files are not cleaned up.** See [Inspecting a job](#inspecting-a-job).
- **Clusters without accounting.** Without `sacct`, a finished job is looked up with `scontrol`, which only keeps it for `MinJobAge` seconds. A job that finishes and ages out between two polls cannot be resolved.

## API reference

See the [Slurm API reference](../../api-reference/integrations/slurm/_index) for full details.
