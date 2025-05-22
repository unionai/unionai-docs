---
title: Async FSSpec
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Async FSSpec
  title_expanded: Flytekit Async fsspec Plugin
  name: flytekitplugins-async-fsspec
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This package holds the data persistence plugins for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.async_fsspec
  - flytekitplugins.async_fsspec.s3fs
  install_requires:
  - flytekit
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
    - async_fsspec=flytekitplugins.async_fsspec
  folder: flytekit-async-fsspec
---


The Flyte async fsspec plugin is a powerful addition to the Flyte ecosystem designed to optimize the performance of object transmission. This plugin focuses on overriding key methods of the file systems in fsspec to introduce efficiency improvements, resulting in accelerated data transfers between Flyte workflows and object storage.

Currently, the async fsspec plugin improves the following file systems:
1. s3fs

To install the plugin, run the following command:

```bash
pip install flytekitplugins-async-fsspec
```

Once installed, the plugin will automatically override the original file system and register optimized ones, seamlessly integrating with your Flyte workflows.
