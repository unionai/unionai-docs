---
title: Slurm
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Slurm
  title_expanded: Flytekit Slurm Plugin
  name: flytekitplugins-slurm
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This package holds the Slurm plugins for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.slurm
  - flytekitplugins.slurm.script
  - flytekitplugins.slurm.function
  install_requires:
  - flytekit>=1.15.0
  - flyteidl>=1.15.0
  - asyncssh
  license: apache2
  python_requires: '>=3.9'
  classifiers:
  - 'Intended Audience :: Science/Research'
  - 'Intended Audience :: Developers'
  - 'License :: OSI Approved :: Apache Software License'
  - 'Programming Language :: Python :: 3.9'
  - 'Programming Language :: Python :: 3.10'
  - 'Programming Language :: Python :: 3.11'
  - 'Programming Language :: Python :: 3.12'
  - 'Topic :: Scientific/Engineering'
  - 'Topic :: Scientific/Engineering :: Artificial Intelligence'
  - 'Topic :: Software Development'
  - 'Topic :: Software Development :: Libraries'
  - 'Topic :: Software Development :: Libraries :: Python Modules'
  entry_points:
    flytekit.plugins:
    - slurm=flytekitplugins.slurm
  folder: flytekit-slurm
---


The Slurm agent is designed to integrate Flyte workflows with Slurm-managed high-performance computing (HPC) clusters, enabling users to leverage Slurm's capability of compute resource allocation, scheduling, and monitoring.

This [guide](https://github.com/JiangJiaWei1103/flytekit/blob/slurm-agent-dev/plugins/flytekit-slurm/demo.md) provides a concise overview of the design philosophy behind the Slurm agent and explains how to set up a local environment for testing the agent.
