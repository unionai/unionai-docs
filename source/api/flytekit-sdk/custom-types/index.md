# Custom types

Flytekit ships with an extensible type system, which makes it easy for anyone to extend and add new types.

```{note}
To contribute a Flyte type, see the [extensibility contribution guide](https://docs.flyte.org/en/latest/user_guide/extending/custom_types.html#advanced-custom-types).
```

## StructuredDataset type

```{eval-rst}

.. currentmodule:: flytekit.types.structured

.. autosummary::
    :nosignatures:

    ~StructuredDataset
    ~StructuredDatasetEncoder
    ~StructuredDatasetDecoder

```

## File type

```{eval-rst}

.. currentmodule:: flytekit.types.file

.. autosummary::
    :nosignatures:

    ~FlyteFile
    ~HDF5EncodedFile
    ~HTMLPage
    ~JoblibSerializedFile
    ~JPEGImageFile
    ~PDFFile
    ~PNGImageFile
    ~PythonPickledFile
    ~PythonNotebook
    ~SVGImageFile

```

## Directory type

```{eval-rst}

.. currentmodule:: flytekit.types.directory

.. autosummary::
    :nosignatures:

    ~FlyteDirectory
    ~TensorboardLogs
    ~TFRecordsDirectory

```

## Iterator type

```{eval-rst}

.. currentmodule:: flytekit.types.iterator

.. autosummary::
    :nosignatures:

    ~FlyteIterator
    ~JSON

```

## PyTorch type

```{eval-rst}

.. currentmodule:: flytekit.extras.pytorch.checkpoint

.. autosummary::
    :nosignatures:

    ~PyTorchCheckpoint
    ~PyTorchCheckpointTransformer
    ~PyTorchModuleTransformer
    ~PyTorchTensorTransformer

```

## Tensorflow type

```{eval-rst}

.. currentmodule:: flytekit.extras.tensorflow.record

.. autosummary::
    :nosignatures:

    ~TensorFlowRecordFileTransformer
    ~TensorFlowRecordsDirTransformer

```

## Sklearn type

```{eval-rst}

.. currentmodule:: flytekit.extras.sklearn.native

.. autosummary::
    :nosignatures:

    ~SklearnEstimatorTransformer
```
