---
title: Papermill
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Papermill
  title_expanded: Flytekit Papermill Plugin
  name: flytekitplugins-papermill
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This is the flytekit papermill plugin
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.papermill
  install_requires:
  - flytekit
  - papermill>=1.2.0
  - nbconvert>=6.0.7
  - ipykernel>=5.0.0
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
  folder: flytekit-papermill
---


It is possible to run a Jupyter notebook as a Flyte task using Papermill. Papermill executes the notebook as a whole, so before using this plugin, it is essential to construct your notebook as recommended by Papermill.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-papermill
```

An [example](https://docs.flyte.org/en/latest/flytesnacks/examples/papermill_plugin/index.html) can be found in the documentation. We also have a [tutorial](https://docs.flyte.org/en/latest/flytesnacks/examples/exploratory_data_analysis/index.html) showcasing the various ways in which you can leverage the Papermill plugin.
