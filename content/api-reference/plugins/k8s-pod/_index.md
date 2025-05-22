---
title: Kubernetes Pod
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Kubernetes Pod
  title_expanded: Flytekit Kubernetes Pod Plugin
  name: flytekitplugins-pod
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: Flytekit plugin to support K8s Pod tasks
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.pod
  install_requires:
  - flytekit>=1.3.0b2
  - kubernetes>=12.0.1
  license: apache2
  python_requires: '>=3.9'
  classifiers:
  - 'Intended Audience :: Science/Research'
  - 'Intended Audience :: Developers'
  - 'License :: OSI Approved :: Apache Software License'
  - 'Programming Language :: Python :: 3.9'
  - 'Programming Language :: Python :: 3.10'
  - 'Topic :: Scientific/Engineering'
  - 'Topic :: Scientific/Engineering :: Artificial Intelligence'
  - 'Topic :: Software Development'
  - 'Topic :: Software Development :: Libraries'
  - 'Topic :: Software Development :: Libraries :: Python Modules'
  folder: flytekit-k8s-pod
---


> [!IMPORTANT]
> This plugin is no longer needed and is here only for backwards compatibility. No new versions will be published after v1.13.x
> Please use the `pod_template` and `pod_template_name` args to `@task` as described in https://docs.flyte.org/en/latest/deployment/configuration/general.html#configuring-task-pods-with-k8s-podtemplates
> instead.


By default, Flyte tasks decorated with `@task` are essentially single functions that are loaded in one container. But often, there is a need to run a job with more than one container.

In this case, a regular task is not enough. Hence, Flyte provides a Kubernetes pod abstraction to execute multiple containers, which can be accomplished using Pod's `task_config`. The `task_config` can be leveraged to fully customize the pod spec used to run the task.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-pod
```

An [example](https://docs.flyte.org/en/latest/flytesnacks/examples/k8s_pod_plugin/index.html) can be found in the documentation.
