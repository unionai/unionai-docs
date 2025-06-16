---
title: Dask
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Dask
  title_expanded: Flytekit Dask Plugin
  name: flytekitplugins-dask
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: Dask plugin for flytekit
  url: https://github.com/flyteorg/flytekit/tree/master/plugins/flytekit-dask
  long_description: "Dask plugin for flytekit"
  long_description_content_type: text/markdown
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.dask
  install_requires:
  - flyteidl>=1.3.2
  - flytekit>=1.3.0b2,<2.0.0
  - dask[distributed]>=2022.10.2
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
  folder: flytekit-dask
---


Flyte can execute `dask` jobs natively on a Kubernetes Cluster, which manages the virtual `dask` cluster's lifecycle
(spin-up and tear down). It leverages the open-source Kubernetes Dask Operator and can be enabled without signing up
for any service. This is like running a transient (ephemeral) `dask` cluster - a type of cluster spun up for a specific
task and torn down after completion. This helps in making sure that the Python environment is the same on the job-runner
(driver), scheduler and the workers.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-dask
```

To configure Dask in the Flyte deployment's backed, follow
[these directions](../../../deployment/flyte-plugins/kubernetes-plugins)

A [usage example](../../../integrations/native-backend-plugins/k8s-dask-plugin)
can be found in the documentation.
