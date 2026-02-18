---
title: flyte.io
version: 2.0.0b60
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.io


## IO data types

This package contains additional data types beyond the primitive data types in python to abstract data flow
of large datasets in Union.


## Directory

### Classes

| Class | Description |
|-|-|
| [`DataFrame`](../flyte.io/dataframe) | A Flyte meta DataFrame object, that wraps all other dataframe types (usually available as plugins, pandas. |
| [`Dir`](../flyte.io/dir) | A generic directory class representing a directory with files of a specified format. |
| [`File`](../flyte.io/file) | A generic file class representing a file with a specified format. |
| [`HashFunction`](../flyte.io/hashfunction) | A hash method that wraps a user-provided function to compute hashes. |

### Variables

| Property | Type | Description |
|-|-|-|
| `PARQUET` | `str` |  |

