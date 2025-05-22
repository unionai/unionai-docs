---
title: Envd
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Envd
  title_expanded: Flytekit Envd Plugin
  name: flytekitplugins-envd
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This package enables users to easily build a Docker image for tasks or
    workflows.
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.envd
  install_requires:
  - flytekit>=1.12.0
  - envd
  license: apache2
  python_requires: '>=3.9'
  classifiers:
  - 'Intended Audience :: Science/Research'
  - 'Intended Audience :: Developers'
  - 'License :: OSI Approved :: Apache Software License'
  - 'Programming Language :: Python :: 3.9'
  - 'Programming Language :: Python :: 3.10'
  - 'Programming Language :: Python :: 3.11'
  - 'Topic :: Scientific/Engineering'
  - 'Topic :: Scientific/Engineering :: Artificial Intelligence'
  - 'Topic :: Software Development'
  - 'Topic :: Software Development :: Libraries'
  - 'Topic :: Software Development :: Libraries :: Python Modules'
  entry_points:
    flytekit.plugins:
    - envd=flytekitplugins.envd
  folder: flytekit-envd
---


[envd](https://github.com/tensorchord/envd) is a command-line tool that helps you create the container-based development environment for AI/ML.

Environments built with envd provide the following features out-of-the-box:
- Knowledge reuse in your team
- BuiltKit native, build up to 6x faster
- Smaller and leaner images

With `flytekitplugins-envd`, people easily create a docker image for the workflows without writing a docker file.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-envd
```

Example
```python
# from flytekit import task
# from flytekit.image_spec import ImageSpec
#
# @task(image_spec=ImageSpec(packages=["pandas", "numpy"], apt_packages=["git"], registry="flyteorg"))
# def t1() -> str:
#     return "hello"
```

This plugin also supports install packages from `conda`:

```python
from flytekit import task, ImageSpec

image_spec = ImageSpec(
    base_image="ubuntu:20.04",
    python_version="3.11",
    packages=["flytekit"],
    conda_packages=["pytorch", "pytorch-cuda=12.1"],
    conda_channels=["pytorch", "nvidia"]
)

@task(container_image=image_spec)
def run_pytorch():
    ...
```
