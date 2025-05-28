---
title: Perian Job Platform
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Perian Job Platform
  title_expanded: Flytekit Perian Job Platform Plugin
  name: flytekitplugins-perian_job
  version: 0.0.0+develop
  author: Omar Tarabai
  author_email: otarabai@perian.io
  description: Flyte agent for Perian Job Platform (perian.io)
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
  - flytekitplugins.perian_job
  install_requires:
  - flytekit>=1.12.0,<2.0.0
  - perian==0.2.7
  license: apache2
  python_requires: '>=3.9'
  classifiers:
  - 'Intended Audience :: Science/Research'
  - 'Intended Audience :: Developers'
  - 'License :: OSI Approved :: Apache Software License'
  - 'Programming Language :: Python :: 3.9'
  - 'Programming Language :: Python :: 3.10'
  - 'Programming Language :: Python :: 3.11'
  - 'Topic :: Scientific/Engineering'
  - 'Topic :: Scientific/Engineering :: Artificial Intelligence'
  - 'Topic :: Software Development'
  - 'Topic :: Software Development :: Libraries'
  - 'Topic :: Software Development :: Libraries :: Python Modules'
  entry_points:
    flytekit.plugins:
    - perian_job=flytekitplugins.perian_job
  folder: flytekit-perian
---


Flyte Agent plugin for executing Flyte tasks on Perian Job Platform (perian.io).

See the [official docs page](https://perian.io/docs/flyte-getting-started) for more details.
