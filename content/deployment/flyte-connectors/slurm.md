---
title: SLURM connector
weight: 17
variants: +flyte -serverless -byoc -selfmanaged
---
# Slurm connector

This guide provides a comprehensive overview of setting up an environment to test the Slurm connector locally and enabling the connector in your Flyte deployment. Before proceeding, the first and foremost step is to spin up your own Slurm cluster, as it serves as the foundation for the setup.

## Spin up a Slurm cluster

Setting up a Slurm cluster can be challenging due to the limited detail in the [official instructions](https://slurm.schedmd.com/quickstart_admin.html#quick_start). This tutorial simplifies the process, focusing on configuring a single-host Slurm cluster with `slurmctld` (central management daemon) and `slurmd` (compute node daemon).

### Install MUNGE

> [MUNGE](https://dun.github.io/munge/) is an authentication service, allowing a process to authenticate the UID and GID of another local or remote process within a group of hosts having common users and groups.

#### 1. Install necessary packages

```shell
sudo apt install munge libmunge2 libmunge-dev
```

#### 2. Generate and verify a MUNGE credential

```shell
munge -n | unmunge | grep STATUS
```

> A status of `STATUS: Success(0)` is expected and the MUNGE key is stored at `/etc/munge/munge.key`. If the key is absent, run the following:

```shell
sudo /usr/sbin/create-munge-key
```

#### 3. Change ownership and permissions of MUNGE directories

```shell
sudo chown -R munge: /etc/munge/ /var/log/munge/ /var/lib/munge/ /run/munge/
sudo chmod 0700 /etc/munge/ /var/log/munge/ /var/lib/munge/
sudo chmod 0755 /run/munge/
sudo chmod 0700 /etc/munge/munge.key
sudo chown -R munge: /etc/munge/munge.key
```

#### 4. Start MUNGE

```shell
sudo systemctl enable munge
sudo systemctl restart munge
```

> Check the status with `systemctl status munge` or inspect the log at `/var/log/munge`.

### Create a dedicated Slurm user

> The *SlurmUser* must be created as needed prior to starting Slurm and must exist on all nodes in your cluster.

```shell
sudo adduser --system --uid <uid> --group --home /var/lib/slurm slurm
```

> A system user usually has a `uid` in the range of 0-999. Refer to [Add a system user](https://manpages.ubuntu.com/manpages/oracular/en/man8/adduser.8.html).

```shell
cat /etc/passwd | grep <uid>
```

```shell
sudo mkdir -p /var/spool/slurmctld /var/spool/slurmd /var/log/slurm
sudo chown -R slurm: /var/spool/slurmctld /var/spool/slurmd /var/log/slurm
```

### Run the Slurm cluster

#### 1. Install Slurm packages

```shell
mkdir <your-clean-dir> && cd <your-clean-dir>
wget https://download.schedmd.com/slurm/slurm-24.05.5.tar.bz2
```

```shell
sudo apt-get update
sudo apt-get install -y build-essential fakeroot devscripts equivs
sudo apt install -y \
  libncurses-dev libgtk2.0-dev libpam0g-dev libperl-dev liblua5.3-dev \
  libhwloc-dev dh-exec librrd-dev libipmimonitoring-dev hdf5-helpers \
  libfreeipmi-dev libhdf5-dev man2html-base libcurl4-openssl-dev \
  libpmix-dev libhttp-parser-dev libyaml-dev libjson-c-dev \
  libjwt-dev liblz4-dev libmariadb-dev libdbus-1-dev librdkafka-dev

tar -xaf slurm-24.05.5.tar.bz2
cd slurm-24.05.5

sudo sed -i 's/^Types: deb$/Types: deb deb-src/' /etc/apt/sources.list.d/ubuntu.sources
sudo apt update
sudo mk-build-deps -i debian/control
debuild -b -uc -us
```

Install the packages:

```shell
cd ..
sudo dpkg -i slurm-smd_24.05.5-1_amd64.deb
sudo dpkg -i slurm-smd-client_24.05.5-1_amd64.deb
sudo dpkg -i slurm-smd-slurmctld_24.05.5-1_amd64.deb
sudo dpkg -i slurm-smd-slurmd_24.05.5-1_amd64.deb
```

#### 2. Generate a Slurm configuration file

Generate `slurm.conf` using the [official configurator](https://slurm.schedmd.com/configurator.html).

Example:

```ini
ClusterName=localcluster
SlurmctldHost=localhost
ProctrackType=proctrack/linuxproc
SlurmctldLogFile=/var/log/slurm/slurmctld.log
SlurmdLogFile=/var/log/slurm/slurmd.log
NodeName=localhost CPUs=<cpus> RealMemory=<available-mem> Sockets=<sockets> CoresPerSocket=<cores-per-socket> ThreadsPerCore=<threads-per-core> State=UNKNOWN
PartitionName=debug Nodes=ALL Default=YES MaxTime=INFINITE State=UP
```

> For GPU support, edit `/etc/slurm/slurm.conf` and `/etc/slurm/gres.conf`:

```ini
# slurm.conf
GresTypes=gpu
NodeName=localhost Gres=gpu:1 CPUs=<cpus> RealMemory=<available-mem> ...
PartitionName=debug Nodes=ALL Default=YES MaxTime=INFINITE State=UP

# gres.conf
AutoDetect=nvml
NodeName=localhost Name=gpu Type=tesla File=/dev/nvidia0
```

#### 3. Start daemons

```shell
sudo systemctl enable slurmctld
sudo systemctl restart slurmctld
sudo systemctl enable slurmd
sudo systemctl restart slurmd
```

#### 4. Try some Slurm commands

```shell
sinfo
srun -N 1 hostname
```

> If the state is `drain`, run:
```shell
scontrol update nodename=<your-nodename> state=idle
```

## Test your Slurm connector locally

This section describes how to test the Slurm connector locally without running the backend gRPC server.

### Overview

The Slurm connector has 3 core methods:

1. `create`: Run `srun` or `sbatch`
2. `get`: Query job status using `scontrol`
3. `delete`: Cancel job using `scancel`

![Basic architecture](https://github.com/flyteorg/static-resources/blob/main/flytekit/plugins/slurm/basic_arch.png?raw=true)

For Python function tasks:

![Function task](https://github.com/flyteorg/static-resources/blob/main/flytekit/plugins/slurm/slurm_function_task.png?raw=true)

### Set up a local test environment

> You need: a client (localhost), a Slurm cluster, and S3-compatible object storage.

#### 1. Install the Slurm connector on your local machine

```shell
pip install flytekitplugins-slurm
```

#### 2. Install the Slurm connector on the cluster

```shell
pip install flytekitplugins-slurm
```

#### 3. Set up SSH configuration

```shell
ssh-keygen -t rsa -b 4096
ssh-copy-id <username>@<fqdn-or-ip>
```

`~/.ssh/config`:

```ini
Host <host-alias>
  HostName <fqdn-or-ip>
  Port <ssh-port>
  User <username>
  IdentityFile <path-to-private-key>
```

Sanity check:

```shell
ssh <host-alias>
```

#### 4. Set up Amazon S3 bucket

> Configure AWS credentials on both client and server.

`~/.aws/config`:

```ini
[default]
region = <your-region>
```

`~/.aws/credentials`:

```ini
[default]
aws_access_key_id = <aws-access-key-id>
aws_secret_access_key = <aws-secret-access-key>
```

> On EC2, assign an IAM role with S3 permissions.

Check access:

```shell
aws s3 ls
```

## Specify connector configuration

### Flyte binary

#### Demo cluster

```bash
kubectl edit configmap flyte-sandbox-config -n flyte
```

```yaml
tasks:
  task-plugins:
    default-for-task-types:
      container: container
      container_array: k8s-array
      sidecar: sidecar
      slurm_fn: connector-service
      slurm: connector-service
    enabled-plugins:
      - container
      - sidecar
      - k8s-array
      - connector-service
```

#### Helm chart

```yaml
tasks:
  task-plugins:
    enabled-plugins:
      - container
      - sidecar
      - k8s-array
      - connector-service
    default-for-task-types:
      - container: container
      - container_array: k8s-array
      - slurm_fn: connector-service
      - slurm: connector-service
```

### Flyte core

`values-override.yaml`:

```yaml
enabled_plugins:
  tasks:
    task-plugins:
      enabled-plugins:
        - container
        - sidecar
        - k8s-array
        - connector-service
      default-for-task-types:
        container: container
        sidecar: sidecar
        container_array: k8s-array
        slurm_fn: connector-service
        slurm: connector-service
```

## Add the Slurm Private Key

### 1. Install flyteconnector pod

```bash
helm repo add flyteorg https://flyteorg.github.io/flyte
helm install flyteconnector flyteorg/flyteconnector --namespace flyte
```

### 2. Set Private Key as a Secret

```bash
SECRET_VALUE=$(base64 < your_slurm_private_key_path) && \
kubectl patch secret flyteconnector -n flyte --patch "{\"data\":{\"flyte_slurm_private_key\":\"$SECRET_VALUE\"}}"
```

### 3. Restart development

```bash
kubectl rollout restart deployment flyteconnector -n flyte
```
