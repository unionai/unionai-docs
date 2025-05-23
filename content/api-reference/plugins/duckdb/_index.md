---
title: DuckDB
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: DuckDB
  title_expanded: Flytekit DuckDB Plugin
  name: flytekitplugins-duckdb
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: DuckDB Plugin for Flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.duckdb
  install_requires:
  - flytekit>=1.3.0b2,<2.0.0
  - duckdb<=1.0.0
  - pandas
  license: apache2
  python_requires: '>=3.9,<3.13'
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
  folder: flytekit-duckdb
---


Run analytical workloads with ease using DuckDB.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-duckdb
```
