---
title: Slurm
version: 1.16.26
variants: +flyte +union
layout: py_api
---

# Slurm



## Directory

### Classes

| Class | Description |
|-|-|
| [`flytekitplugins.slurm.ssh_utils.SSHConfig`](flytekitplugins.slurm.ssh_utils#flytekitpluginsslurmssh_utilssshconfig) | A customized version of SSHClientConnectionOptions, tailored to specific needs. |
| [`flytekitplugins.slurm.ssh_utils.SlurmCluster`](flytekitplugins.slurm.ssh_utils#flytekitpluginsslurmssh_utilsslurmcluster) | A Slurm cluster instance is defined by a pair of (Slurm host, username). |

### Functions

| Function | Description |
|-|-|
| [`flytekitplugins.slurm.ssh_utils.get_ssh_conn()`](flytekitplugins.slurm.ssh_utils#get_ssh_conn) | Get an existing SSH connection or create a new one if needed. |
| [`flytekitplugins.slurm.ssh_utils.ssh_connect()`](flytekitplugins.slurm.ssh_utils#ssh_connect) | Make an SSH client connection. |

### Packages

| Package | Description |
|-|-|
| [`flytekitplugins.slurm.ssh_utils`](flytekitplugins.slurm.ssh_utils) | Utilities of asyncssh connections. |

