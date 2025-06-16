---
title: Deck
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Deck
  title_expanded: Flytekit Deck Plugin
  name: flytekitplugins-deck-standard
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This Plugin provides more renderers to improve task visibility
  url: https://github.com/flyteorg/flytekit/tree/master/plugins/flytekit-data-fsspec
  long_description: "This Plugin provides more renderers to improve task visibility"
  long_description_content_type: text/markdown
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.deck
  install_requires:
  - flytekit
  extras_require:
    pandas:
    - pandas
    pillow:
    - pillow
    ydata-profiling:
    - ydata-profiling
    markdown:
    - markdown
    plotly:
    - plotly
    pygments:
    - pygments
    all:
    - pandas
    - pillow
    - ydata-profiling
    - markdown
    - plotly
    - pygments
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
  entry_points:
    flytekit.plugins:
    - deck=flytekitplugins.deck
  folder: flytekit-deck-standard
---


This plugin provides additional renderers to improve task visibility within Flytekit.

## Installation

To install the plugin, run the following command:

```bash
pip install flytekitplugins-deck-standard
```

## Renderer Requirements

Each renderer may require additional modules.

The table below outlines the dependencies for each renderer:

| Renderer               | Required Module(s)          |
|------------------------|-----------------------------|
| SourceCodeRenderer      | `pygments`                  |
| FrameProfilingRenderer  | `pandas`, `ydata-profiling` |
| MarkdownRenderer        | `markdown`                  |
| BoxRenderer             | `pandas`, `plotly`          |
| ImageRenderer           | `pillow`    |
| TableRenderer           | `pandas`                    |
| GanttChartRenderer      | `pandas`, `plotly`  |

## Renderer Descriptions

### SourceCodeRenderer
Converts Python source code to HTML using the Pygments library.

### FrameProfilingRenderer
Generates a profiling report based on a pandas DataFrame using `ydata_profiling`.

### MarkdownRenderer
Converts markdown strings to HTML.

### BoxRenderer
Creates a box-and-whisker plot from a column in a pandas DataFrame.

### ImageRenderer
Displays images from a `FlyteFile` or `PIL.Image.Image` object in HTML.

### TableRenderer
Renders a pandas DataFrame as an HTML table with customizable headers and table width.

### GanttChartRenderer
Displays a Gantt chart using a pandas DataFrame with "Start", "Finish", and "Name" columns.
