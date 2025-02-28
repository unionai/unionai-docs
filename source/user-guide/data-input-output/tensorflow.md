# TensorFlow types

This document outlines the TensorFlow types available in Flyte, which facilitate the integration of TensorFlow models and datasets in Flyte workflows.

### Import necessary libraries and modules
```python
from union
from flytekit.types.directory import TFRecordsDirectory
from flytekit.types.file import TFRecordFile

custom_image = union.ImageSpec(
    packages=["tensorflow", "tensorflow-datasets", "flytekitplugins-kftensorflow"],
    registry="ghcr.io/flyteorg",
)

import tensorflow as tf
```

## Tensorflow model
Flyte supports the TensorFlow SavedModel format for serializing and deserializing `tf.keras.Model` instances. The `TensorFlowModelTransformer` is responsible for handling these transformations.

### Transformer
- **Name:** TensorFlow Model
- **Class:** `TensorFlowModelTransformer`
- **Python Type:** `tf.keras.Model`
- **Blob Format:** `TensorFlowModel`
- **Dimensionality:** `MULTIPART`

### Usage
The `TensorFlowModelTransformer` allows you to save a TensorFlow model to a remote location and retrieve it later in your Flyte workflows.

{@@ if flyte @@}
```{note}
To clone and run the example code on this page, see the [Flytesnacks repo](https://github.com/flyteorg/flytesnacks/tree/master/examples/data_types_and_io/).
```
{@@ endif @@}

```python
@union.task
def train_model() -> tf.keras.Model:
    model = tf.keras.Sequential(
        [tf.keras.layers.Dense(128, activation="relu"), tf.keras.layers.Dense(10, activation="softmax")]
    )
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model


@union.task
def evaluate_model(model: tf.keras.Model, x: tf.Tensor, y: tf.Tensor) -> float:
    loss, accuracy = model.evaluate(x, y)
    return accuracy


@union.workflow
def training_workflow(x: tf.Tensor, y: tf.Tensor) -> float:
    model = train_model()
    return evaluate_model(model=model, x=x, y=y)
```

## TFRecord files
Flyte supports TFRecord files through the TFRecordFile type, which can handle serialized TensorFlow records. The TensorFlowRecordFileTransformer manages the conversion of TFRecord files to and from Flyte literals.

### Transformer
- **Name:** TensorFlow Record File
- **Class:** `TensorFlowRecordFileTransformer`
- **Blob Format:** `TensorFlowRecord`
- **Dimensionality:** `SINGLE`

### Usage
The `TensorFlowRecordFileTransformer` enables you to work with single TFRecord files, making it easy to read and write data in TensorFlow's TFRecord format.

```python
@union.task
def process_tfrecord(file: TFRecordFile) -> int:
    count = 0
    for record in tf.data.TFRecordDataset(file):
        count += 1
    return count


@union.workflow
def tfrecord_workflow(file: TFRecordFile) -> int:
    return process_tfrecord(file=file)
```

## TFRecord directories
Flyte supports directories containing multiple TFRecord files through the `TFRecordsDirectory type`. The `TensorFlowRecordsDirTransformer` manages the conversion of TFRecord directories to and from Flyte literals.

### Transformer
- **Name:** TensorFlow Record Directory
- **Class:** `TensorFlowRecordsDirTransformer`
- **Python Type:** `TFRecordsDirectory`
- **Blob Format:** `TensorFlowRecord`
- **Dimensionality:** `MULTIPART`

### Usage
The `TensorFlowRecordsDirTransformer` allows you to work with directories of TFRecord files, which is useful for handling large datasets that are split across multiple files.

#### Example
```python
@union.task
def process_tfrecords_dir(dir: TFRecordsDirectory) -> int:
    count = 0
    for record in tf.data.TFRecordDataset(dir.path):
        count += 1
    return count


@union.workflow
def tfrecords_dir_workflow(dir: TFRecordsDirectory) -> int:
    return process_tfrecords_dir(dir=dir)
```

## Configuration class: `TFRecordDatasetConfig`
The `TFRecordDatasetConfig` class is a data structure used to configure the parameters for creating a `tf.data.TFRecordDataset`, which allows for efficient reading of TFRecord files. This class uses the `DataClassJsonMixin` for easy JSON serialization.

### Attributes
- **compression_type**: (Optional) Specifies the compression method used for the TFRecord files. Possible values include an empty string (no compression), "ZLIB", or "GZIP".
- **buffer_size**: (Optional) Defines the size of the read buffer in bytes. If not set, defaults will be used based on the local or remote file system.
- **num_parallel_reads**: (Optional) Determines the number of files to read in parallel. A value greater than one outputs records in an interleaved order.
- **name**: (Optional) Assigns a name to the operation for easier identification in the pipeline.

This configuration is crucial for optimizing the reading process of TFRecord datasets, especially when dealing with large datasets or when specific performance tuning is required.
