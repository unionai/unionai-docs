---
title: Slurm
description: "Configuration for running a task on a Slurm cluster."
icon: braces
version: 2.11.1
variants: +flyte +union
layout: py_api
---

# Slurm

**Package:** `flyteplugins.slurm`

Configuration for running a task on a Slurm cluster.

Scheduling fields map one-to-one onto `sbatch` options; anything not covered
goes in `sbatch_options` verbatim. Connection fields may be left unset and
supplied cluster-wide on the connector via `FLYTE_SLURM_HOST`,
`FLYTE_SLURM_USERNAME` and `FLYTE_SLURM_SSH_PRIVATE_KEY` instead.

Do not set `resources` on a Slurm task environment: the allocation is
described here and granted by Slurm, not by Kubernetes.



## Parameters

```python
class Slurm(
    partition: typing.Optional[str] = None,
    nodes: typing.Optional[int] = None,
    ntasks: typing.Optional[int] = None,
    cpus_per_task: typing.Optional[int] = None,
    gres: typing.Optional[str] = None,
    gpus_per_node: typing.Optional[typing.Any] = None,
    mem: typing.Optional[str] = None,
    time_limit: typing.Optional[str] = None,
    account: typing.Optional[str] = None,
    qos: typing.Optional[str] = None,
    reservation: typing.Optional[str] = None,
    constraint: typing.Optional[str] = None,
    sbatch_options: typing.Dict[str, typing.Any] = <factory>,
    container_runtime: str = 'pyxis',
    container_args: typing.List[str] = <factory>,
    modules: typing.List[str] = <factory>,
    container_image: typing.Optional[str] = None,
    container_mounts: typing.List[str] = <factory>,
    container_workdir: typing.Optional[str] = None,
    srun_args: typing.List[str] = <factory>,
    env: typing.Dict[str, str] = <factory>,
    working_dir: typing.Optional[str] = None,
    host: typing.Optional[str] = None,
    port: int = 22,
    username: typing.Optional[str] = None,
    ssh_private_key: typing.Optional[str] = None,
    known_hosts: typing.Optional[str] = None,
    known_hosts_secret: typing.Optional[str] = None,
    skip_host_key_verification: bool = False,
)
```
| Parameter | Type | Description |
|-|-|-|
| `partition` | `typing.Optional[str]` | Slurm partition to submit to. |
| `nodes` | `typing.Optional[int]` | Number of nodes to allocate. |
| `ntasks` | `typing.Optional[int]` | Number of tasks (`--ntasks`). Leave unset for a single-process task. |
| `cpus_per_task` | `typing.Optional[int]` | CPUs per task. |
| `gres` | `typing.Optional[str]` | Generic resources, e.g. `"gpu:8"`. |
| `gpus_per_node` | `typing.Optional[typing.Any]` | GPUs per node, e.g. `8` or `"h100:8"`. |
| `mem` | `typing.Optional[str]` | Memory per node, e.g. `"64G"`. |
| `time_limit` | `typing.Optional[str]` | Wall-clock limit in Slurm format, e.g. `"4:00:00"`. |
| `account` | `typing.Optional[str]` | Account to charge. |
| `qos` | `typing.Optional[str]` | Quality of service. |
| `reservation` | `typing.Optional[str]` | Reservation name. |
| `constraint` | `typing.Optional[str]` | Node feature constraint. |
| `sbatch_options` | `typing.Dict[str, typing.Any]` | Extra `--<key>=<value>` options passed through verbatim. Use `True` for a bare flag. Overrides the first-class fields on conflict. |
| `container_runtime` | `str` | How the image is launched on the node: `"pyxis"` (default) or `"apptainer"`. Pyxis is a SPANK plugin that adds `--container-image` to `srun` and ships with NVIDIA-shaped clusters; Apptainer is an ordinary command the job invokes and is more common at traditional HPC sites. Check which the cluster has with `scontrol show config \| grep -i plugstack` or `command -v apptainer`. A cluster with neither cannot run native `slurm` tasks; use `slurm_script` there. |
| `container_args` | `typing.List[str]` | Extra arguments for the container runtime itself, e.g. `["--rocm"]` for AMD GPUs under Apptainer. `--nv` is added automatically when the job requests GPUs, so it does not belong here. |
| `modules` | `typing.List[str]` | Environment modules to `module load` before the job runs, e.g. `["apptainer"]`. Many HPC sites keep tooling off the default PATH and expose it only through Lmod or environment-modules, in which case the runtime is not found without this. |
| `container_image` | `typing.Optional[str]` | Override the image submitted to the runtime, e.g. a pre-imported squashfs or `.sif` path on the shared filesystem. Defaults to the task's image. |
| `container_mounts` | `typing.List[str]` | Bind mounts as `src:dst[:ro]`, e.g. `["/data:/data"]`. Rendered as `--container-mounts` for Pyxis and `--bind` for Apptainer. |
| `container_workdir` | `typing.Optional[str]` | Working directory inside the container. |
| `srun_args` | `typing.List[str]` | Extra arguments inserted before the command on the `srun` line. |
| `env` | `typing.Dict[str, str]` | Environment variables exported into the job, e.g. object-storage settings the Flyte entrypoint needs on the cluster. |
| `working_dir` | `typing.Optional[str]` | Directory on the cluster for scripts and logs. Relative paths are under the SSH user's home. Defaults to `.flyte/jobs`. |
| `host` | `typing.Optional[str]` | Login node hostname. |
| `port` | `int` | SSH port. |
| `username` | `typing.Optional[str]` | SSH user jobs are submitted as. |
| `ssh_private_key` | `typing.Optional[str]` | Name of the Flyte secret holding the SSH private key. |
| `known_hosts` | `typing.Optional[str]` | Path to a known_hosts file on the connector. Requires the deployment to mount one, so prefer `known_hosts_secret` unless a file is already there. |
| `known_hosts_secret` | `typing.Optional[str]` | Name of a Flyte secret holding the known_hosts entries themselves. Resolved by the platform and handed to the connector, so host-key verification needs nothing in the data plane's Helm values. |
| `skip_host_key_verification` | `bool` | Disable host-key verification. Not for production. |

## Methods

| Method | Description |
|-|-|
| [`to_custom_config()`](#to_custom_config) |  |


### to_custom_config()

```python
def to_custom_config()
```
