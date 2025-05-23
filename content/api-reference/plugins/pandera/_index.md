---
title: Pandera
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Pandera
  title_expanded: Flytekit Pandera Plugin
  name: flytekitplugins-pandera
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: Pandera plugin for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.pandera
  install_requires:
  - flytekit>=1.15.0b2,<2.0.0
  - pandera>=0.7.1
  - pandas
  - great_tables
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
    - pandera=flytekitplugins.pandera
  folder: flytekit-pandera
---


Flytekit python natively supports many data types, including a FlyteSchema type for type-annotating pandas DataFrames. The Flytekit Pandera plugin provides an alternative for defining DataFrame schemas by integrating with Pandera, a runtime data validation tool for pandas DataFrames.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-pandera
```

All [examples](https://docs.flyte.org/en/latest/flytesnacks/examples/pandera_plugin/index.html) can be found in the documentation.
