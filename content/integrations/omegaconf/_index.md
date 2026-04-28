---
title: OmegaConf
weight: 1
variants: +flyte +union
---

# OmegaConf

[OmegaConf](https://omegaconf.readthedocs.io/) is a hierarchical configuration system used by many ML frameworks (and the foundation of [Hydra](../hydra)). The `flyteplugins-omegaconf` plugin makes OmegaConf's `DictConfig` and `ListConfig` first-class types in Flyte tasks, so you can pass entire configs like plain dicts, YAML files or dataclass-backed structured configs between tasks without flattening them into individual scalar arguments.

The plugin enables:

- `DictConfig` and `ListConfig` as native task input and output types
- Round-tripping of structured configs (dataclass schemas) across task boundaries
- Preservation of OmegaConf-specific values: `MISSING` sentinels, `Enum`s, `pathlib.Path`s, `tuple`s, and `bytes`
- Resolved variable interpolations on the wire
- A YAML-rendered Flyte report tab for human-readable config inspection

## Installation

```bash
pip install flyteplugins-omegaconf
```

Installing the package automatically registers `DictConfig` and `ListConfig` with Flyte's `TypeEngine`. No manual setup is required.

If you are using the [Hydra plugin](../hydra/_index.md), `flyteplugins-omegaconf` is installed as a transitive dependency.

## Quick start

```python{hl_lines=[2, "8-9", "14-17"]}
import flyte
from omegaconf import DictConfig, OmegaConf

env = flyte.TaskEnvironment(name="training", image=...)


@env.task
async def train(cfg: DictConfig) -> float:
    return run_experiment(cfg.optimizer.lr, cfg.training.epochs)


@env.task
async def pipeline() -> float:
    cfg = OmegaConf.create(
        {"optimizer": {"lr": 0.001}, "training": {"epochs": 10}}
    )
    return await train(cfg)
```

The config is serialized when `train` is invoked and reconstructed as a `DictConfig` inside the task. No type registration, manual encoding or schema declaration is required.

## When to use this plugin

Use `flyteplugins-omegaconf` when:

- You already use OmegaConf. For example, you have YAML configs, dataclass-based config trees or a Hydra app, and want to keep that representation intact across task boundaries.
- You want to pass a single composed config object instead of widening task signatures with dozens of scalar arguments.
- You want to enforce schema validation at the task entry point via dataclass-backed structured configs.
- You want resolved interpolations (`${other.value}`) to be materialized at submission time rather than at task runtime.

If you do not use OmegaConf elsewhere, prefer plain dataclasses, `pydantic.BaseModel` or `dict` for task inputs as they are supported by Flyte natively without an extra dependency.

## Building a DictConfig

Any of the standard OmegaConf construction methods produce a value the plugin can serialize.

### From a plain dict

```python{hl_lines=["1-3"]}
cfg = OmegaConf.create(
    {"optimizer": {"lr": 0.001}, "training": {"epochs": 10}}
)
flyte.run(train, cfg=cfg)
```

### From a YAML file

```python{hl_lines=[1]}
cfg = OmegaConf.load("configs/training.yaml")
flyte.run(train, cfg=cfg)
```

The file is read locally on the submitter, not on the worker. If the YAML lives in your project tree and needs to be packaged into the task image, use `flyte.with_runcontext(copy_style="all").run(...)`.

### From a dataclass (structured config)

```python{hl_lines=["3-6", 8]}
from dataclasses import dataclass

@dataclass
class TrainConf:
    lr: float = 0.001
    epochs: int = 10

cfg = OmegaConf.structured(TrainConf())
flyte.run(train, cfg=cfg)
```

Structured configs are covered in detail in [Structured configs](#structured-configs) below.

### From a base config plus overrides

```python{hl_lines=["1-3"]}
base = OmegaConf.load("configs/training.yaml")
override = OmegaConf.create({"optimizer": {"lr": 0.01}})
cfg = OmegaConf.merge(base, override)
flyte.run(train, cfg=cfg)
```

This is the same pattern Hydra uses internally. See the [Hydra integration](../hydra/_index.md) for a full composition layer on top of this plugin.

## Variable interpolation

OmegaConf supports `${...}` interpolations that resolve relative to the config tree:

```python{hl_lines=[3, 4]}
cfg = OmegaConf.create(
    {
        "base_lr": 0.01,
        "optimizer": {"lr": "${base_lr}", "momentum": 0.9},
    }
)
flyte.run(train, cfg=cfg)
```

Interpolations are resolved at serialization time. By the time the task runs, `cfg.optimizer.lr` is the concrete float `0.01`, not the string `"${base_lr}"`. This means:

- The receiving task does not need any context that only existed in the submitter's environment.
- Resolved values appear in the Flyte I/O panel.
- A reference that fails to resolve at submission time fails fast, before any task runs.

If you need lazy resolution on the worker, resolve the reference yourself inside the task or pass the unresolved string through a normal `str` input.

## Nested and deeply structured configs

Nested configs are supported, including deeply structured OmegaConf objects.

```python{hl_lines=["1-13", 18]}
cfg = OmegaConf.create(
    {
        "experiment": {
            "model": {
                "encoder": {
                    "attention": {"num_heads": 8, "head_dim": 64},
                    "ffn": {"hidden_dim": 2048, "activation": "gelu"},
                },
                "decoder": {"num_layers": 6},
            }
        }
    }
)


@env.task
async def extract_leaf(cfg: DictConfig) -> int:
    return int(cfg.experiment.model.encoder.attention.num_heads)
```

## DictConfigs that contain lists

A `DictConfig` may hold list values; they are reconstructed as nested `ListConfig`s on the receiving side.

```python{hl_lines=[4, 5, 8, 9]}
cfg = OmegaConf.create(
    {
        "model": {
            "layer_sizes": [64, 128, 256, 512],
            "activations": ["relu", "relu", "relu", "sigmoid"],
        },
        "data": {
            "augmentations": ["random_flip", "random_crop", "color_jitter"],
            "input_size": [224, 224],
        },
    }
)


@env.task
async def double_layer_sizes(cfg: DictConfig) -> DictConfig:
    doubled = [size * 2 for size in cfg.model.layer_sizes]
    return OmegaConf.merge(cfg, {"model": {"layer_sizes": doubled}})
```

## ListConfig as input and output

`ListConfig` is symmetric with `DictConfig` and supports the same construction patterns.

### Lists of primitives

```python{hl_lines=[2]}
@env.task
async def scale_values(values: ListConfig, factor: float) -> ListConfig:
    return OmegaConf.create([v * factor for v in values])
```

### Building a schedule from another task

```python{hl_lines=[3, 7, 8]}
@env.task
async def build_lr_schedule(base_lr: float, num_stages: int) -> ListConfig:
    return OmegaConf.create([base_lr * (0.5 ** i) for i in range(num_stages)])


@env.task
async def train_with_schedule(cfg: DictConfig, lr_schedule: ListConfig) -> float:
    final_lr = float(lr_schedule[-1])
    ...
```

### Nested lists (list of lists)

```python{hl_lines=[1, 6]}
grid = OmegaConf.create([[0.001, 0.01, 0.1], [10, 20, 50]])


@env.task
async def flatten_grid(grid: ListConfig) -> ListConfig:
    flat = [item for sublist in OmegaConf.to_container(grid) for item in sublist]
    return OmegaConf.create(flat)
```

### Lists of DictConfigs

```python{hl_lines=["2-6"]}
configs = OmegaConf.create(
    [
        {"optimizer": {"lr": 0.001}, "training": {"epochs": 10}},
        {"optimizer": {"lr": 0.01},  "training": {"epochs": 20}},
        {"optimizer": {"lr": 0.1},   "training": {"epochs": 5}},
    ]
)


@env.task
async def select_best_config(configs: ListConfig) -> DictConfig:
    best = max(OmegaConf.to_container(configs), key=lambda c: c["optimizer"]["lr"])
    return OmegaConf.create(best)
```

### Lists of dataclass instances

```python{hl_lines=["9-13"]}
@dataclass
class LayerConf:
    name: str
    width: int
    activation: str


layers = OmegaConf.create(
    [
        LayerConf(name="encoder", width=768, activation="gelu"),
        LayerConf(name="bottleneck", width=128, activation="relu"),
        LayerConf(name="decoder", width=768, activation="linear"),
    ]
)
```

Each element round-trips as a typed `DictConfig` backed by `LayerConf`, so the receiving task can call `OmegaConf.get_type(layers[0])` and access fields with attribute notation.

{{< note >}}
ListConfig is always plain. Even when its elements are dataclass-backed, the outer `ListConfig` does not carry a list-level schema as there is no structured (typed-element) `ListConfig` in OmegaConf. This affects only the outer container; nested elements retain their schemas.
{{< /note >}}

## Structured configs

A structured config is a `DictConfig` that is bound to a Python dataclass. The dataclass acts as a schema: assigning a value of the wrong type raises `omegaconf.ValidationError`, and merging unknown keys raises an error instead of silently extending the config.

### Basic structured config

```python{hl_lines=["5-8", "11-14", 17, 20]}
from dataclasses import dataclass, field
from omegaconf import OmegaConf, DictConfig


@dataclass
class OptimizerConf:
    lr: float = 0.001
    weight_decay: float = 1e-4


@dataclass
class TrainConf:
    optimizer: OptimizerConf = field(default_factory=OptimizerConf)
    epochs: int = 10


cfg = OmegaConf.structured(TrainConf())
flyte.run(train, cfg=cfg)

# cfg.optimizer.lr = "oops"  # raises omegaconf.ValidationError
```

### Schema reconstruction in the receiving task

When a structured `DictConfig` is deserialized in a downstream task, the plugin operates in **Auto mode**: it reads the originating dataclass name from the wire payload and tries to import it. Two outcomes are possible:

- Dataclass importable in the receiving task: `cfg` is reconstructed as a `TrainConf`-backed `DictConfig`. `OmegaConf.get_type(cfg)` returns `TrainConf`, and type validation is enforced.
- Dataclass not importable: `cfg` falls back to a plain `DictConfig` carrying the raw values. `OmegaConf.get_type(cfg)` returns `dict`. The values are intact but the schema is lost.

To keep schemas across task hops, define dataclasses in modules that are importable from every task in the pipeline (for example, in a shared `configs.py` module bundled into the task image).

### Required (`MISSING`) fields

OmegaConf's `MISSING` sentinel marks a required field that has no default:

```python{hl_lines=[1, 5, "8-9", "12-13"]}
from omegaconf import MISSING

@dataclass
class TrainConf:
    data_path: str = MISSING
    epochs: int = 10

# Pass with MISSING still unset — serialization succeeds.
cfg = OmegaConf.structured(TrainConf())
flyte.run(train, cfg=cfg)

# Or fill it before passing.
cfg = OmegaConf.structured(TrainConf(data_path="/data/imagenet"))
flyte.run(train, cfg=cfg)
```

A config with an unset `MISSING` field serializes and deserializes successfully as the sentinel is preserved on the wire. Accessing the field on the receiving side raises `MissingMandatoryValue`.

{{< note >}}
Type annotations are preserved only in Auto mode. When the dataclass is importable on the receiving side, an unfilled `MISSING` field still carries its declared type (e.g. `StringNode` for `str`). When the plugin falls back to a plain `DictConfig` because the dataclass is not importable, the field becomes an `AnyNode` where the value is preserved, but the type annotation is not.
{{< /note >}}

### Advanced field types

Beyond primitives and nested dataclasses, structured configs may declare fields of these types and they will round-trip with their schemas intact:

- `Enum` subclasses
- `pathlib.Path`
- `Optional[T]`
- `bytes`
- `dict[str, T]` where `T` is a dataclass
- `list[T]` where `T` is a dataclass

```python{hl_lines=["6-8", "20-35"]}
from enum import Enum
from pathlib import Path
from typing import Optional


class RunMode(Enum):
    TRAIN = "train"
    EVAL = "eval"


@dataclass
class CallbackConf:
    name: str = "early_stop"
    patience: int = 3
    monitor: str = MISSING


@dataclass
class AdvancedTrainConf:
    mode: RunMode = RunMode.TRAIN
    checkpoint_dir: Path = Path("/tmp/checkpoints")
    maybe_seed: Optional[int] = None
    payload: bytes = b"default-token"
    callbacks_by_name: dict[str, CallbackConf] = field(
        default_factory=lambda: {
            "early_stop": CallbackConf(name="early_stop", patience=3),
            "checkpoint": CallbackConf(name="checkpoint", monitor="val_loss"),
        }
    )
    callbacks: list[CallbackConf] = field(
        default_factory=lambda: [
            CallbackConf(name="lr_monitor", patience=2, monitor="lr"),
            CallbackConf(name="nan_guard", patience=1, monitor="loss"),
        ]
    )
```

Inside a downstream task:

```python
@env.task
async def inspect(cfg: DictConfig) -> str:
    assert OmegaConf.get_type(cfg) == AdvancedTrainConf
    assert OmegaConf.get_type(cfg.callbacks[0]) == CallbackConf
    assert isinstance(cfg.mode, RunMode)
    assert isinstance(cfg.checkpoint_dir, Path)
    assert isinstance(cfg.payload, bytes)
    return cfg.mode.value
```

### Merging overrides on top of a structured base

```python{hl_lines=[3, 11]}
@env.task
async def structured_merge_pipeline() -> str:
    base = OmegaConf.structured(TrainConf())
    overrides = OmegaConf.create(
        {
            "optimizer": {"lr": 0.05},
            "training": {"epochs": 100},
            "experiment_name": "sweep-run-1",
        }
    )
    cfg = OmegaConf.merge(base, overrides)
    return await validate_config(cfg)
```

Merging an unknown key against a structured config raises an error, so define every key the override layer might supply on the dataclass.

## Embedding rich Python values inside a plain DictConfig

A plain `DictConfig` (one not bound to a dataclass) can still hold Python values that OmegaConf does not natively model. The plugin preserves the following types end-to-end whether they appear in plain or structured configs:

- `pathlib.Path` and any subclass of `pathlib.PurePath`
- `enum.Enum` members
- `tuple` (round-trips as `tuple`, not `list`)
- `bytes`

```python{hl_lines=[1]}
cfg = OmegaConf.create({"model_path": Path("/opt/models/model.bin")})


@env.task
async def use_path(cfg: DictConfig) -> str:
    assert isinstance(cfg.model_path, Path)
    return f"model_path={cfg.model_path}"
```

If an `Enum`'s class cannot be imported in the receiving environment, the value is returned as the underlying primitive (`int`, `str`, ...) instead of the enum member.

## Reserved-looking keys

The plugin's wire format uses an internal payload marker (`__flyte_omegaconf__`), which means user-facing keys named `kind`, `values`, `name`, `value`, `type`, or `schema` round-trip unchanged:

```python{hl_lines=[1, 8]}
cfg = OmegaConf.create({"kind": "training-job", "values": {"lr": 0.001}})


@env.task
async def use_payload_shaped_config(cfg: DictConfig) -> str:
    # cfg.values resolves to DictConfig.values() — use bracket notation
    # to reach the user key named "values".
    return f"kind={cfg.kind} lr={cfg['values'].lr}"
```

The only practical consideration is Python's normal attribute-vs-method conflict: `cfg.values` is the `.values()` method, so reach for `cfg["values"]` when your config has a key with that name.

## YAML reports

The Flyte I/O panel displays the literal wire representation of a `DictConfig`.

![Wire Representation](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/integrations/omegaconf/input.png)

For a YAML view, enable a Flyte report on the task and log the config with `log_yaml`:

```python{hl_lines=[1, 4, 6]}
from flyteplugins.omegaconf import log_yaml


@env.task(report=True)
async def train(cfg: DictConfig) -> DictConfig:
    await log_yaml.aio(cfg, title="Input config")
    ...
```

![YAML Report](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/integrations/omegaconf/yaml_repr.png)

The plugin also exposes:

- `to_yaml(cfg)`: render an OmegaConf container as a YAML string.
- `to_html(cfg, title=...)`: wrap the YAML in escaped HTML for embedding in a custom report.
- `replace_yaml(cfg, ...)`: replace the contents of a report tab instead of appending.

```python
from flyteplugins.omegaconf.report import to_yaml, replace_yaml

text = to_yaml(cfg)
await replace_yaml.aio(cfg, tab="Final config")
```

`MISSING` fields appear as `???` in the YAML output, matching OmegaConf's own convention.

## Wire format

Both `DictConfig` and `ListConfig` are serialized as MessagePack blobs with the literal representation:

```
Literal(scalar=Scalar(binary=Binary(value=<msgpack bytes>, tag="msgpack")))
```

The msgpack payload uses an internal tagged structure to distinguish OmegaConf-specific concepts from raw values:

- A `DictConfig` payload includes the originating dataclass name (`builtins.dict` for plain configs) plus its values.
- `MISSING`, `Enum`, `Path`, and `tuple` values carry tagged shapes so they can be reconstructed faithfully.

You normally do not need to inspect this format. It is documented here because:

- The plugin serializes with `resolve=True`, so the wire representation always contains concrete values for `${...}` interpolations.
- Cache-key metadata is set via Flyte's `MESSAGEPACK` serialization format, so two tasks given equivalent configs hit the same cache entry.

## End-to-end example

The example below ties the pieces together: a structured `DictConfig` is created in a parent task, flows through several child tasks that read and modify it, and a `ListConfig` produced midway is consumed by a later stage. Each hop serializes and deserializes the config; the dataclass schema is recovered on the receiving side because `TrainConf` (and friends) are importable in every task in the pipeline.

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/omegaconf/example.py" lang=python >}}

For more focused examples such as plain `DictConfig` patterns, advanced `ListConfig` shapes, all `MISSING`/`Enum`/`Path`/`bytes` cases, see the [plugin repository](https://github.com/flyteorg/flyte-sdk/tree/main/plugins/omegaconf/examples).
