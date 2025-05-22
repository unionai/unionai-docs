---
title: Polars
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Polars
  title_expanded: Flytekit Polars Plugin
  name: flytekitplugins-polars
  version: 0.0.0+develop
  author: Robin Kahlow
  description: Polars plugin for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.polars
  install_requires:
  - flytekit>=1.3.0b2,<2.0.0
  - polars>=0.8.27
  - pandas
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
    - polars=flytekitplugins.polars
  folder: flytekit-polars
---

[Polars](https://github.com/pola-rs/polars) is a blazingly fast DataFrames library implemented in Rust using Apache Arrow Columnar Format as memory model.

This plugin supports `polars.DataFrame` as a data type with [StructuredDataset](https://docs.flyte.org/en/latest/user_guide/data_types_and_io/structureddataset.html).

To install the plugin, run the following command:

```bash
pip install flytekitplugins-polars
```
