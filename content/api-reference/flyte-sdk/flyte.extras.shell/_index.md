---
title: flyte.extras.shell
version: 2.6.2
variants: +flyte +union
layout: py_api
---

# flyte.extras.shell

Shell task — wrap a CLI tool packaged in a container image.

Designed as the foundation for bio module libraries (bedtools, samtools,
bcftools, GATK, etc.) and any other case where a user wants to call a
pre-built binary in a published container with typed inputs and outputs.

Compared to `flyte.extras.ContainerTask`, this layer adds:

- A Python `str.format`-style template surface (`{inputs.x}`, `{flags.x}`,
  `{outputs.x}`) instead of `{{.inputs.x}}` syntax.
- A closed type vocabulary for inputs: `File`, `Dir`, `list[File]`,
  `dict[str, str]`, scalars (`int` / `float` / `str`), `bool`,
  and `T | None` of any of those.
- `flags.<name>` rendering: bool inputs become `-name` / `""`,
  scalar inputs become `-name value`, list inputs render with one of
  three modes (`join` / `repeat` / `comma`), dict inputs with one
  of two (`pairs` / `equals`).
- Output declarations use **bare types** for the common cases —
  `File`, `Dir`, `int` / `float` / `str` / `bool` — and
  three small collector classes for the cases that need extra semantics:

  * `flyte.extras.shell.Glob` — pattern-filtered `list[File]` (the script writes
    files into `/var/outputs/<name>/` and the wrapper unpacks).
  * `flyte.extras.shell.Stdout` / `flyte.extras.shell.Stderr` — wrapper redirects the
    corresponding stream straight to `/var/outputs/<name>`.

`Glob` has two observable shapes:

- on the serialized task / remote wire interface, it is a `Dir`
- when you call the Python shell wrapper (`await my_shell_task(...)`),
  that `Dir` is unpacked back into `list[File]`

Example:

```python
from flyte.extras.shell import create, Glob
from flyte.io import File

bedtools_intersect = create(
    name="bedtools_intersect",
    image="quay.io/biocontainers/bedtools:2.31.1--hf5e1c6e_0",
    inputs={"a": File, "b": list[File], "wa": bool, "f": float},
    outputs={"bed": Glob("*.bed")},
    script=r'''
        bedtools intersect {flags.wa} \
            -a {inputs.a} \
            -b {inputs.b} \
            -f {inputs.f} \
            > {outputs.bed}/out.bed
    ''',
)
```
## Directory

### Classes

| Class | Description |
|-|-|
| [`FlagSpec`](../flyte.extras.shell/flagspec) | How to render a typed input as a CLI flag in `{flags.<name>}`. |
| [`Glob`](../flyte.extras.shell/glob) | A multi-file output bundle. |
| [`Stderr`](../flyte.extras.shell/stderr) | Capture the task's stderr as a typed output. |
| [`Stdout`](../flyte.extras.shell/stdout) | Capture the task's stdout as a typed output. |

### Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Wrap a CLI tool packaged in a container as a Flyte task. |


## Methods

#### create()

```python
def create(
    name: str,
    image: Union[str, flyte.Image],
    inputs: dict[str, Type] | None = None,
    outputs: dict[str, Any] | None = None,
    script: str,
    flag_aliases: dict[str, Union[str, Tuple[str, listMode], FlagSpec]] | None = None,
    defaults: dict[str, Any] | None = None,
    shell: str = '/bin/bash',
    debug: bool = False,
    resources: flyte.Resources | None = None,
    retries: int = 0,
    timeout: int | None = None,
    cache: str = 'auto',
    env_vars: dict[str, str] | None = None,
    secrets: list | None = None,
    local_logs: bool = True,
) -> _Shell
```
Wrap a CLI tool packaged in a container as a Flyte task.

```python
# bedtools.py
from flyte.io import File
from flyte.extras.shell import create, Glob

bedtools_intersect = create(
    name="bedtools_intersect",
    image="quay.io/biocontainers/bedtools:2.31.1--hf5e1c6e_0",
    inputs={"a": File, "b": list[File], "wa": bool, "f": float},
    outputs={"bed": Glob("*.bed")},
    script=r'''
        bedtools intersect {flags.wa} \
            -a {inputs.a} \
            -b {inputs.b} \
            -f {inputs.f} \
            > {outputs.bed}/out.bed
    ''',
)

# user_pipeline.py
import flyte
from bio_modules.bedtools import bedtools_intersect

env = flyte.TaskEnvironment(
    name="genomics_pipeline",
    depends_on=[bedtools_intersect.env],
)

@env.task
async def pipeline(a: File, b: list[File]) -> list[File]:
    return await bedtools_intersect(a=a, b=b, wa=True, f=0.5)
```


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Task name; should be unique within the project. |
| `image` | `Union[str, flyte.Image]` | Either a pre-built URI string (e.g. `"quay.io/biocontainers/bedtools:2.31.1--hf5e1c6e_0"`, `"debian:12-slim"`) or a `flyte.Image` / ImageSpec instance (layered: base + apt / pip / Dockerfile layers). When you pass a `flyte.Image`, the shell layer builds it for you on first call via `flyte.build` — using the configured builder (`cfg.image_builder`: `"local"` by default, `"remote"` when opted in) — and hands the resulting URI down to ContainerTask. Subsequent calls reuse the cached URI; the build engine itself is also memoised, so cross-task duplication is cheap. **Requirements on the image:** 1. `bash` (4+) at `/bin/bash` — the generated preamble    uses bash-only features (arrays, `$'\x1e'` ANSI-C    quoting, `read -ra`, `$((..))` arith, `<<<`    here-strings, `set -o pipefail`). 2. **No custom ENTRYPOINT.** ContainerTask passes the bash    invocation via `CMD`; if the image sets    `ENTRYPOINT=["..."]`, docker prepends it and the    resulting invocation breaks. |
| `inputs` | `dict[str, Type] \| None` | Mapping of input name to type. Supported types: - `File`, `Dir` — mounted at `/var/inputs/<name>` - `list[File]` — mounted under `/var/inputs/<name>/` and   expanded as `${name}/*` (or via `{flags.<name>}` with a   `list_mode`) - `dict[str, str]` — passthrough "extras" dict; values are   **strings only** (see recipes below) - `int`, `float`, `str`, `bool` scalars - `T \| None` of any of the above (`None` collapses to empty) **Recipes for things that look like they need a richer dict but don't:** - *Bool as a CLI switch* (`--verbose`) — declare `verbose: bool`   as a separate input and use `{flags.verbose}`. - *Bool as a value* (`REMOVE_DUPLICATES=true`) — already works   with `dict[str, str]`; the value is just the string `"true"`. - *List of values under a repeated flag* (`-I a.bam -I b.bam`) —   declare `list[File]` (or another typed list) with   `flag_aliases={"name": ("-I", "repeat")}`. - *List of strings, comma-joined* (`--exclude a,b,c`) — pass a   pre-joined string yourself: `extras={"--exclude": "a,b,c"}`. Resist the urge to extend `dict[str, str]` to mixed value types — declaring inputs individually gives you better type hints, IDE autocomplete, and clearer error messages. |
| `outputs` | `dict[str, Any] \| None` | Mapping of output name to declaration. Each value is either a **bare type** (the common case) or a small **collector** class for behaviour the type system can't express: - `File` — single file at `/var/outputs/<name>` - `Dir` — directory at `/var/outputs/<name>` (wrapper   pre-creates it via `mkdir -p`) - `int` / `float` / `str` / `bool` — primitive; the   script writes the value as text to `/var/outputs/<name>`   and CoPilot casts to the declared type - `flyte.extras.shell.Glob` (`pattern="*"`) — pattern-filtered   `list[File]`. The wrapper pre-creates the directory; the   script writes files into it; the serialized task exposes   that output as `Dir` on the wire, and the Python shell   wrapper unpacks it back to `list[File]` post-execution. - `flyte.extras.shell.Stdout` (`type=File` by default) — the wrapper   redirects the script's stdout straight to   `/var/outputs/<name>`. `type` can also be a primitive,   in which case the captured text is cast. - `flyte.extras.shell.Stderr` — symmetric for stderr. All declared outputs live at `/var/outputs/<name>`; the user references them as `{outputs.<name>}` in the script (except `flyte.extras.shell.Stdout` / `flyte.extras.shell.Stderr`, which are managed by the wrapper). |
| `script` | `str` | Bash script template. Reference inputs as `{inputs.x}`, CLI flags as `{flags.x}`, and outputs as `{outputs.x}` (which renders to `/var/outputs/<x>`). `flyte.extras.shell.Stdout` / `flyte.extras.shell.Stderr` outputs cannot be referenced — the wrapper redirects the corresponding stream there for you. **Do not wrap `{inputs.x}` in your own quotes**. Scalar values travel through bash positional args (`$1`, `$2`) so they survive arbitrary content (single quotes, tabs, dollar signs) without escaping, and the wrapper already emits scalar references as `"${_VAL_name}"` (quoted, single token). Wrapping them in `"..."` again breaks out of the wrapper's quoting and re-enables word splitting. |
| `flag_aliases` | `dict[str, Union[str, Tuple[str, listMode], FlagSpec]] \| None` | Per-input override for `{flags.<name>}` rendering. Values may be a string (just the flag, default join mode) or `(flag, list_mode)` to pick a list rendering mode (`"join"`, `"repeat"`, `"comma"`) or `(flag, dict_mode)` for dicts (`"pairs"`, `"equals"`). |
| `defaults` | `dict[str, Any] \| None` | Per-input fallback value used when the caller omits that input at call time. Lets you mark inputs as "optional at call site" while still emitting their flag, independent of the `T \| None` axis. The interaction with `T \| None` is: ====================  =========================  ================================= Type                  In `defaults`            Behavior when caller omits ====================  =========================  ================================= `T`                 No                         `TypeError` at submit time `T`                 Yes                        Default used; flag emitted `T \| None`          No                         Empty value; flag suppressed `T \| None`          Yes                        Default used; flag emitted ====================  =========================  ================================= |
| `shell` | `str` | Shell binary to use. Defaults to `/bin/bash`. |
| `debug` | `bool` | If True, container prints the rendered script to stderr before running. Invaluable when authoring a new wrapper. secrets: Standard task knobs forwarded to ContainerTask. |
| `resources` | `flyte.Resources \| None` | |
| `retries` | `int` | |
| `timeout` | `int \| None` | |
| `cache` | `str` | |
| `env_vars` | `dict[str, str] \| None` | |
| `secrets` | `list \| None` | |
| `local_logs` | `bool` | When `True` (default), the rendered command and the container's captured stdout/stderr are emitted through the flyte logger at `DEBUG` level during local docker execution. Set to `False` to silence them entirely (e.g. when running many sub-tasks locally and per-task chatter would clutter output even at DEBUG). Only affects local docker execution; remote execution never invokes the code path that produces these messages. |

**Returns**

A configured `_Shell` instance. Call it like a coroutine for
local execution; access `.env` to plug it into a pipeline's
`depends_on` for deploy-time image building and registration.


