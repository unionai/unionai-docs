---
title: Vaex
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Vaex
  title_expanded: Flytekit Vaex Plugin
  name: flytekitplugins-vaex
  version: 0.0.0+develop
  author: admin@flyte.org
  description: Vaex plugin for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.vaex
  install_requires:
  - flytekit>=1.3.0b2,<2.0.0
  - vaex-core>=4.13.0,<4.14; python_version < '3.10'
  - vaex-core>=4.16.0; python_version >= '3.10'
  - pandas
  - pydantic<2.0
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
  entry_points:
    flytekit.plugins:
    - vaex=flytekitplugins.vaex
  folder: flytekit-vaex
---

[Vaex](https://github.com/vaexio/vaex) is a high-performance Python library for lazy out-of-core DataFrames
(similar to Pandas) to visualize and explore big tabular datasets.

This plugin supports `vaex.DataFrame` as a data type with [StructuredDataset](https://docs.flyte.org/en/latest/user_guide/data_types_and_io/structureddataset.html).

To install the plugin, run the following command:

```bash
pip install flytekitplugins-vaex
```
