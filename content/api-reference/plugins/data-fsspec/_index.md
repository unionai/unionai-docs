---
title: FSSpec
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: FSSpec
  title_expanded: "fsspec data plugin for Flytekit \u2014 Experimental"
  name: flytekitplugins-data-fsspec
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This is a deprecated plugin as of flytekit 1.5
  url: https://github.com/flyteorg/flytekit/tree/master/plugins/flytekit-data-fsspec
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
  - flytekitplugins.fsspec
  install_requires: []
  extras_require:
    abfs: []
    aws: []
    gcp: []
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
  folder: flytekit-data-fsspec
---


This plugin provides an implementation of the data persistence layer in Flytekit that uses fsspec. Once this plugin
is installed, it overrides all default implementations of the data plugins and provides the ones supported by fsspec. This plugin
will only install the fsspec core. To install all fsspec plugins, please follow the [fsspec documentation](https://filesystem-spec.readthedocs.io/en/latest/).
