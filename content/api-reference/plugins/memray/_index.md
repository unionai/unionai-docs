---
title: Memray Profiling
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Memray Profiling
  title_expanded: Memray Profiling Plugin
  name: flytekitplugins-memray
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This package enables memory profiling for tasks with memray
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.memray
  install_requires:
  - flytekit>=1.12.0
  - memray
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
  folder: flytekit-memray
---


Memray tracks and reports memory allocations, both in python code and in compiled extension modules.
This Memray Profiling plugin enables memory tracking on the Flyte task level and renders a memgraph profiling graph on Flyte Deck.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-memray
```

Example
```python
from flytekit import workflow, task, ImageSpec
from flytekitplugins.memray import memray_profiling
import time


image = ImageSpec(
    name="memray_demo",
    packages=["flytekitplugins_memray"],
    registry="<your_cr_registry>",
)


def generate_data(n: int):
    leak_list = []
    for _ in range(n):  # Arbitrary large number for demonstration
        large_data = " " * 10**6  # 1 MB string
        leak_list.append(large_data)  # Keeps appending without releasing
        time.sleep(0.1)  # Slow down the loop to observe memory changes


@task(container_image=image, enable_deck=True)
@memray_profiling(memray_html_reporter="table")
def memory_usage(n: int) -> str:
    generate_data(n=n)

    return "Well"


@task(container_image=image, enable_deck=True)
@memray_profiling(trace_python_allocators=True, memray_reporter_args=["--leaks"])
def memory_leakage(n: int) -> str:
    generate_data(n=n)

    return "Well"


@workflow
def wf(n: int = 500):
    memory_usage(n=n)
    memory_leakage(n=n)
```
