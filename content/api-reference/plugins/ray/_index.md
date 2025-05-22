---
title: Ray
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Ray
  title_expanded: Flytekit Ray Plugin
  name: flytekitplugins-ray
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This package holds the Ray plugins for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.ray
  install_requires:
  - ray[default]
  - flytekit>1.14.5
  - flyteidl>=1.13.6
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
  folder: flytekit-ray
---


Flyte backend can be connected with Ray. Once enabled, it allows you to run flyte task on Ray cluster

To install the plugin, run the following command:

```bash
pip install flytekitplugins-ray
```

All [examples](https://docs.flyte.org/en/latest/flytesnacks/examples/ray_plugin/index.html) showcasing execution of Ray jobs using the plugin can be found in the documentation.
