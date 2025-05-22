---
title: SQLAlchemy
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: SQLAlchemy
  title_expanded: Flytekit SQLAlchemy Plugin
  name: flytekitplugins-sqlalchemy
  version: 0.0.0+develop
  author: dolthub
  author_email: max@dolthub.com
  description: SQLAlchemy plugin for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.sqlalchemy
  install_requires:
  - flytekit>=1.3.0b2,<2.0.0
  - sqlalchemy>=1.4.7
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
  folder: flytekit-sqlalchemy
---


SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. Flyte provides an easy-to-use interface to utilize SQLAlchemy to connect to various SQL Databases.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-sqlalchemy
```

An [example](https://docs.flyte.org/en/latest/flytesnacks/examples/sql_plugin/sql_alchemy.html) can be found in the documentation.
