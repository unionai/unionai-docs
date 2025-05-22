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
  long_description: "# Union.ai Docs Builder\n\n**[union.ai/docs](https://union.ai/docs)**\n\
    \nThis repository builds and publishes all Union.ai documentation.\n\nThe site is\
    \ _automatically published_ when the PR targeting `main` branch is merged.\n\nWhat\
    \ do you want to do today?\n\n- [**Developer & Local environment**](DEVELOPER.md).\n\
    \  How to setup your computer.\n\n- [**Authoring Content**](AUTHOR.md).\n  101 of\
    \ how to create and view content\n\n- [**Advanced Content Creation**](SHORTCODES.md).\n\
    \  Advanced techniques and features to generate content, e.g., audio player.\n\n\
    - [**Building API content**](APIS.md).\n  How to automatically generate content\
    \ for APIs, e.g., Python packages.\n\n- [**Redirecting URLS**](REDIRECTS.md).\n\
    \  How to send users to a new page when the content changed its location."
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
[these directions](https://docs.flyte.org/en/latest/deployment/plugins/k8s/index.html)ernetes/k8s_dask/index.html#step-2-environment-setup)

An [usage example](https://docs.flyte.org/en/latest/flytesnacks/examples/k8s_dask_plugin/index.html)
can be found in the documentation.
