---
title: GPU
weight: 7
variants: -flyte +union
---

# GPU

A sandbox can run GPU workloads: `nvidia-smi`, a CUDA matmul, PyTorch inference, etc. GPU workloads run inside the same isolation boundary as everything else. The sandboxed process gets the GPU devices bound into its namespace, but no broader access to the host than a CPU sandbox would have.

## GPU requires the bubblewrap backend

CUDA's compute path (`cuInit`) does not initialize under the userns-lite backend's unprivileged user namespace. It fails with `cudaErrorOperatingSystem` even though `nvidia-smi` and NVML work and the `/dev/nvidia*` device nodes are visible. The bubblewrap backend runs the workload in a posture the NVIDIA driver accepts, so **GPU sandboxes must use bubblewrap**:

- Remote: set `sandbox_mode="bwrap"` on the `SandboxEnvironment` (or `sb.session(sandbox_mode="bwrap", ...)`).
- On-device: pass `backend="bubblewrap"` to `sb.on_device.session(...)`, which is already the default.

`sb.session()` fails fast if you request a GPU on a non-bubblewrap backend.

## Remote GPU sandbox

The supported path is a remote `SandboxEnvironment` that declares a GPU in its `resources` and bakes the GPU framework into its image. Schedule the pod with the GPU, set `sandbox_mode="bwrap"`, and the sandbox-server binds `/dev/nvidia*` into the sandboxed child.

```python
import flyte
from union import sandbox as sb

gpu_sandbox = sb.SandboxEnvironment(
    name="union-sandbox-gpu-l4",
    sandbox_mode="bwrap",                       # required for CUDA
    image=sb.base_sandbox_image.with_pip_packages("torch"),
    resources=flyte.Resources(cpu="4", memory="16Gi", gpu="L4:1"),
    description="Sandbox with one NVIDIA L4 and PyTorch preinstalled.",
)

env = flyte.TaskEnvironment(
    name="union-sandbox-remote-gpu-l4",
    # `kubernetes` is needed because constructing a SandboxEnvironment builds its
    # pod template (via kubernetes.client). CPU examples that only call
    # sb.session(sandbox_mode=...) without constructing one don't need it.
    image=flyte.Image.from_debian_base().with_pip_packages("kubernetes"),
    resources=flyte.Resources(cpu="500m", memory="512Mi"),
    # Declaring the sandbox env as a dependency means one `flyte deploy` of this
    # env also deploys gpu_sandbox's sandbox-server task, so there's something to launch.
    depends_on=[gpu_sandbox],
)

_TORCH_CHECK = """
import torch
print("cuda available:", torch.cuda.is_available())
assert torch.cuda.is_available(), "CUDA not visible inside sandbox"
dev = torch.device("cuda:0")
print("device:", torch.cuda.get_device_name(dev))
a = torch.randn(2048, 2048, device=dev)
b = torch.randn(2048, 2048, device=dev)
print("matmul sum:", (a @ b).sum().item())
"""

@env.task
async def main() -> dict:
    async with await sb.session(environment=gpu_sandbox) as sbx:
        smi = await sbx.exec("nvidia-smi")
        out = await sbx.run_code(_TORCH_CHECK)
        return {"nvidia_smi": smi.stdout, "torch": out}
```

Deploy the GPU image and sandbox task, then run:

```sh
flyte deploy --all examples/remote/tasks/torch_gpu_matmul.py   # build GPU image + deploy
flyte run examples/remote/tasks/torch_gpu_matmul.py main
```

### How the GPU reaches the sandbox

GPU access is fail-closed. The server's GPU ceiling defaults to zero, which denies the devices. When a session is launched against an environment whose `resources` include a GPU, the pod is scheduled with that GPU count and the ceiling is set to match, so each `run()` asks for the devices and the bubblewrap backend binds `/dev/nvidia*` into the sandboxed child. A sandbox launched on a non-GPU pod or with a zero ceiling, simply can't see a GPU.

## Resource sizing: don't under-cap the sandbox

The in-pod sandbox runs under a memory/CPU ceiling derived from the pod's resources (less a small reserve for sandbox-server itself). If that ceiling is too low, `import torch` fails while memory-mapping libtorch.

To avoid it, size the `SandboxEnvironment.resources` for the framework, not just the GPU. The `cpu="4", memory="16Gi"` above is a sane floor for PyTorch on a single L4. When you set `resources` on the environment (or per launch via `sb.session(resources=...)`), the sandbox ceiling is derived from that value automatically. The fallback `mem_ceiling_mb` / `cpu_ceiling_milli` kwargs apply only when no resources are given.

> [!NOTE] GPU type and count
> The `gpu="L4:1"` form selects the accelerator class and count via `flyte.Resources`. Use whatever GPU classes your cluster offers; the sandbox machinery is agnostic to the specific device.

## On-device GPU

Running a GPU workload on-device (in the calling task's own pod, no sandbox-server) works under the same constraint: `backend="bubblewrap"` on a pod that has a GPU and the bubblewrap prerequisites (`CAP_SYS_ADMIN` + unconfined AppArmor via `flyte.PodTemplate.allow_nested_sandboxing()`). The on-device sandbox runs `script_type="python"` against the current interpreter, so the GPU framework just needs to be importable from the task's own venv.

You usually don't have to expose that venv yourself. When the session builds its shared venv — which it does whenever `uv` is available, as in `base_sandbox_image` — it bridges the image venv's `site-packages` and mounts that venv read-only automatically, so `import torch` resolves with no `read_only_paths`:

```python
import flyte
from union import sandbox as sb

env = flyte.TaskEnvironment(
    name="union-sandbox-on-device-gpu",
    image=sb.base_sandbox_image.with_pip_packages("torch"),
    resources=flyte.Resources(cpu="4", memory="16Gi", gpu="L4:1"),
    pod_template=flyte.PodTemplate().allow_nested_sandboxing(),
)

@env.task
async def main() -> str:
    async with sb.on_device.session(backend="bubblewrap") as sbx:
        return await sbx.run_code("import torch; print(torch.cuda.is_available())")
```

Prefer remote for production GPU work: it isolates the GPU job in its own pod with its own credentials, the same blast-radius argument that applies to any remote sandbox (see [Security model](./security-model)).

## Related

- [Security model](./security-model). Why GPU sandboxes use bubblewrap, and the on-device blast-radius caveat.
- [Deployment](./deployment). Defining a custom `SandboxEnvironment`, per-launch `resources` overrides.
- [Running commands](./running-commands). `exec()` / `run_code()` used above.
