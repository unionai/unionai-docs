---
title: flytekit.extras.tensorflow.record
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.extras.tensorflow.record

## Directory

### Classes

| Class | Description |
|-|-|
| [`TFRecordDatasetConfig`](../flytekit.extras.tensorflow.record/tfrecorddatasetconfig) | TFRecordDatasetConfig can be used while creating tf. |
| [`TensorFlowRecordFileTransformer`](../flytekit.extras.tensorflow.record/tensorflowrecordfiletransformer) | TypeTransformer that supports serialising and deserialising to and from TFRecord file. |
| [`TensorFlowRecordsDirTransformer`](../flytekit.extras.tensorflow.record/tensorflowrecordsdirtransformer) | TypeTransformer that supports serialising and deserialising to and from TFRecord directory. |

### Methods

| Method | Description |
|-|-|
| [`extract_metadata_and_uri()`](#extract_metadata_and_uri) |  |


## Methods

#### extract_metadata_and_uri()

```python
def extract_metadata_and_uri(
    lv: flytekit.models.literals.Literal,
    t: typing.Type[typing.Union[flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass, flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass]],
) -> typing.Tuple[typing.Union[flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass, flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass], flytekit.extras.tensorflow.record.TFRecordDatasetConfig]
```
| Parameter | Type | Description |
|-|-|-|
| `lv` | `flytekit.models.literals.Literal` | |
| `t` | `typing.Type[typing.Union[flytekit.types.file.file.FlyteFile.__class_getitem__.<locals>._SpecificFormatClass, flytekit.types.directory.types.FlyteDirectory.__class_getitem__.<locals>._SpecificFormatDirectoryClass]]` | |

