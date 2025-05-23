---
title: DBT
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: DBT
  title_expanded: Flytekit dbt plugin
  name: flytekitplugins-dbt
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: DBT Plugin for Flytekit
  url: https://github.com/flyteorg/flytekit/tree/master/plugins/flytekit-dbt
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
  - flytekitplugins.dbt
  install_requires:
  - flytekit>=1.3.0b2
  - dbt-core>=1.6.0,<1.8.0
  - networkx>=2.5
  license: apache2
  python_requires: '>=3.9'
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
  folder: flytekit-dbt
---


Flytekit plugin for performing DBT tasks. Currently it supports  `dbt run` , `dbt test`, `dbt source freshness` tasks.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-dbt
```

_Example coming soon!_

## Contributors

- [Gojek](https://www.gojek.io/)
