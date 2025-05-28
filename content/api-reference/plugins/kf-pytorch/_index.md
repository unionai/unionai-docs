---
title: Kubeflow PyTorch
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Kubeflow PyTorch
  title_expanded: Flytekit Kubeflow PyTorch Plugin
  name: flytekitplugins-kfpytorch
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: K8s based Pytorch plugin for Flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.kfpytorch
  install_requires:
  - cloudpickle
  - flyteidl>=1.5.1
  - flytekit>=1.6.1
  - kubernetes
  extras_require:
    elastic:
    - torch>=1.9.0
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
  folder: flytekit-kf-pytorch
---


This plugin uses the Kubeflow PyTorch Operator and provides an extremely simplified interface for executing distributed training using various PyTorch backends.

This plugin can execute torch elastic training, which is equivalent to run `torchrun`. Elastic training can be executed
in a single Pod (without requiring the PyTorch operator, see below) as well as in a distributed multi-node manner.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-kfpytorch
```

To set up PyTorch operator in the Flyte deployment's backend, follow the [PyTorch Operator Setup](https://docs.flyte.org/en/latest/flytesnacks/examples/kfpytorch_plugin/index.html) guide.

An [example](https://docs.flyte.org/en/latest/flytesnacks/examples/mnist_classifier/index.html#mnist-classifier-training) showcasing PyTorch operator can be found in the documentation.

## Code Example
```python
from flytekitplugins.kfpytorch import PyTorch, Worker

@task(
    task_config = PyTorch(
        worker=Worker(replicas=5)
    )
    image="test_image",
    resources=Resources(cpu="1", mem="1Gi"),
)
def pytorch_job():
    ...
```

You can specify run policy and restart policy of a pytorch job. The default restart policy for both master and worker group is the never restart,
you can set it to other policy.
```python
from flytekitplugins.kfpytorch import PyTorch, Worker, RestartPolicy, RunPolicy

@task(
    task_config = PyTorch(
        worker=Worker(replicas=5, restart_policy=RestartPolicy.FAILURE),
        run_policy=RunPolicy(
            clean_pod_policy=CleanPodPolicy.ALL,
        )
    )
    image="test_image",
    resources=Resources(cpu="1", mem="1Gi"),
)
def pytorch_job():
    ...
```

## Upgrade Pytorch Plugin from V0 to V1
Pytorch plugin is now updated from v0 to v1 to enable more configuration options.
To migrate from v0 to v1, change the following:
1. Update flytepropeller to v1.6.0
2. Update flytekit version to v1.6.2
3. Update your code from:
    ```
    task_config=Pytorch(num_workers=10),
    ```
    to:
    ```
    task_config=PyTorch(worker=Worker(replicas=10)),
    ```
