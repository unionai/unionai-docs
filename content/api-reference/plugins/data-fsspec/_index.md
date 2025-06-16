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
  long_description: "This is a deprecated plugin as of flytekit 1.5"
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
