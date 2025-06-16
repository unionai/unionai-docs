---
title: Spark
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Spark
  title_expanded: Flytekit Spark Plugin
  name: flytekitplugins-spark
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: Spark 3 plugin for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.spark
  install_requires:
  - flytekit>=1.15.1
  - pyspark>=3.0.0
  - aiohttp
  - flyteidl>=1.11.0b1
  - pandas
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
  scripts:
  - scripts/flytekit_install_spark3.sh
  entry_points:
    flytekit.plugins:
    - spark=flytekitplugins.spark
  folder: flytekit-spark
---


Flyte can execute Spark jobs natively on a Kubernetes Cluster, which manages a virtual cluster’s lifecycle, spin-up, and tear down. It leverages the open-sourced Spark On K8s Operator and can be enabled without signing up for any service. This is like running a transient spark cluster — a type of cluster spun up for a specific Spark job and torn down after completion.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-spark
```

To configure Spark in the Flyte deployment's backend, follow [Step 1](https://docs.flyte.org/en/latest/deployment/plugins/k8s/index.html#deployment-plugin-setup-k8s), [2](https://docs.flyte.org/en/latest/flytesnacks/examples/k8s_spark_plugin/index.html).

All [examples](https://docs.flyte.org/en/latest/flytesnacks/examples/k8s_spark_plugin/index.html) showcasing execution of Spark jobs using the plugin can be found in the documentation.
