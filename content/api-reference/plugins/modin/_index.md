---
title: Modin
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Modin
  title_expanded: Flytekit Modin Plugin
  name: flytekitplugins-modin
  version: 0.0.0+develop
  author: Intel
  description: Modin plugin for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.modin
  install_requires:
  - flytekit
  - fsspec
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
  folder: flytekit-modin
---


Modin is a pandas-accelerator that helps handle large datasets. It is a light-weight extension that is similar to the pandas API. It uses the concept of parallelism to reduce overhead, and improve the performance of pandas operations by leveraging the compute resources available.

This plugin supports Modin as a data type.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-modin
```

All [examples](https://docs.flyte.org/en/latest/flytesnacks/examples/modin_plugin/index.html) can be found in the documentation.
