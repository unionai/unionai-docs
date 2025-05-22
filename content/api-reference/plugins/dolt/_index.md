---
title: Dolt
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Dolt
  title_expanded: Flytekit Dolt Plugin
  name: flytekitplugins-dolt
  version: 0.0.0+develop
  author: dolthub
  author_email: max@dolthub.com
  description: Dolt plugin for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.dolt
  install_requires:
  - flytekit>=1.3.0b2,<2.0.0
  - dolt_integrations>=0.1.5
  - networkx<3.2; python_version<'3.9'
  extras_resquire:
    dev:
    - pytest-mock>=3.6.1
  cmdclass:
    develop: !!python/name:docs_builder.PostDevelopCommand ''
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
  scripts:
  - scripts/flytekit_install_dolt.sh
  folder: flytekit-dolt
---


The DoltTable plugin is a wrapper that uses [Dolt](https://github.com/dolthub/dolt) to move data between pandas.DataFrame’s at execution time and database tables at rest.

The Dolt plugin and Dolt command-line tool can be installed as follows:

```bash
pip install flytekitplugins.dolt
sudo bash -c 'curl -L https://github.com/dolthub/dolt/releases/latest/download/install.sh | sudo bash'
```

Dolt requires a user configuration to run init:

```
dolt config --global --add user.email <email>
dolt config --global --add user.name <name>
```

All the [examples](https://docs.flyte.org/en/latest/flytesnacks/examples/dolt_plugin/index.html) can be found in the documentation.
