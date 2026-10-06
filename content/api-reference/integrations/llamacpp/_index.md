---
title: llama.cpp
icon: book
version: 2.11.0
variants: +flyte +union
layout: py_api
---

# llama.cpp



## Directory

### Classes

| Class | Description |
|-|-|
| [`LlamaCppAppEnvironment`](./llamacppappenvironment) | App environment backed by llama.cpp (llama-server) for serving GGUF models. |

### Methods

| Method | Description |
|-|-|
| [`build_llama_cpp_image()`](#build_llama_cpp_image) | Build a Debian image with llama-server compiled from source. |


### Variables

| Property | Type | Description |
|-|-|-|
| `DEFAULT_LLAMA_CPP_IMAGE` | `Image` |  |

## Methods

#### build_llama_cpp_image()

```python
def build_llama_cpp_image(
    name: str = 'llama-cpp-app-image',
    cuda: bool = True,
    cuda_arch: str = '89',
    repo: str = 'https://github.com/ggml-org/llama.cpp',
    ref: str | None = None,
) -> flyte.Image
```
Build a Debian image with llama-server compiled from source.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of the image. |
| `cuda` | `bool` | Build with CUDA support (GGML_CUDA=ON). Set to False for a CPU-only image. |
| `cuda_arch` | `str` | Target CUDA architecture(s) for the kernel build, as a ";"-separated list of compute capabilities (e.g. "89" for L4/L40S, "80;86;89;90" for a fat binary that also covers A100/A10/H100). Ignored when `cuda=False`. |
| `repo` | `str` | Git repository to build llama.cpp from. |
| `ref` | `str \| None` | Git ref (tag, branch, or commit) to check out. None builds the default branch tip; pin a release tag (e.g. "b6148") for reproducible builds. |

