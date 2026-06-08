---
title: Filesystem
weight: 5
variants: -flyte +union
---

# Filesystem

Each session has its own work dir, and it's the session's **persistent disk**: files written there during one `run()` are visible to the next, and `cwd` defaults to it. The session venv lives here too, which is why an install in one `run()` survives into later ones. The rest of the filesystem — **including `/tmp`** — is reset for every command, so keep anything you need across calls in the work dir.

You can push or pull bytes from outside the sandbox without shelling out.

## Moving bytes in and out

`put_bytes` and `get_bytes` are the simplest way to stage a file into a sandbox before a command, or retrieve a result after:

```python
import tempfile

with tempfile.TemporaryDirectory() as work:
    async with sb.on_device.session(host_work_dir=work, backend="userns") as sbx:
        await sbx.put_bytes(f"{work}/input.json", b'{"x": 1}')

        proc = await sbx.run(f"python3 {work}/process.py")
        await proc.communicate()

        result = await sbx.get_bytes(f"{work}/result.json", max_bytes=10 * 1024 * 1024)
```

Both methods take absolute paths that must resolve under the session's work directory. Pin it with `host_work_dir=...` when you want a known path to interpolate (as above); leave it unset and the session creates a fresh temp dir for its lifetime. Paths outside the work dir are refused, as are symlinks in the prefix. `max_bytes` caps the response size; the call raises if the file is larger.

The work-dir constraint is its own rule, separate from the filesystem allow-list (covered below). The allow-list governs what the sandboxed process can read or write at runtime; `put_bytes` / `get_bytes` operate on the work dir specifically. Stage files into the work dir and have the sandboxed script read them from there (`/tmp` won't survive between calls).

Use these together with `network_mode="blocked"` to keep an untrusted `run()` from doing any I/O of its own: stage inputs via `put_bytes`, run with no network, collect outputs via `get_bytes`.

## The default allow-list

The sandbox grants the sandboxed process read-only access to system paths (`/usr`, `/lib`, `/etc`, `/proc`, `/sys`, and so on) and read-write access to `/tmp`, `/dev/shm`, and the per-session work dir. Everything else on the host is invisible.

These defaults are secure; you don't have to touch them for typical use.

## Extending the allow-list

You can add host paths to the allow-list. Additions never replace the secure defaults:

```python
sbx = sb.on_device.session(
    backend="userns",
    read_only_paths=["/opt/models"],         # extend the read-only allow-list
    read_write_paths=["/data/scratch"],      # extend the read-write allow-list
    host_work_dir="/tmp/my-sandbox-work",    # pin the per-session work dir
)
```

A common use of `read_only_paths` is exposing a venv baked into the image so the sandboxed interpreter can import it without an in-sandbox install — point it at the image's `VIRTUAL_ENV` (e.g. `/opt/venv`), which lives outside the default `/usr` allow-list.

`host_work_dir` is useful when you want a stable, inspectable location for the work dir (CI artifacts, post-mortem debugging). When omitted, the library picks a fresh directory.

Inspect the effective allow-list at any time:

```python
allowlist = sbx.fs_allowlist()
# {"read_only":  ["/usr", "/lib", ..., "/opt/models"],
#  "read_write": ["/tmp", "/dev/shm", ..., "/data/scratch", "/tmp/my-sandbox-work"]}
```

> [!NOTE] Allow-list additions on remote sandboxes
> `read_only_paths` and `read_write_paths` extend what the **sandboxed process** can see inside the sandbox-server pod. They do not mount host directories onto a remote pod; the pod's filesystem comes from its image. To make external data available to a remote sandbox, push it with `put_bytes` or mount it through the `SandboxEnvironment` (see [Deployment](./deployment)).

## Volumes (coming soon)

Persistent volume support is on the roadmap, so that sandbox sessions can attach durable storage (PVCs, shared scratch, model caches) without redeploying. Today, persistent state across sessions requires either `put_bytes` / `get_bytes` to your own storage, or baking the data into the sandbox image via a custom `SandboxEnvironment`.

If volumes block a use case you care about, let us know on Slack so we can prioritize accordingly.

## Related

- [Running commands](./running-commands). `cwd` lands under the work dir.
- [Networking](./networking). Pair `put_bytes` with `network_mode="blocked"` for isolated, hermetic runs.
- [Deployment](./deployment). `SandboxEnvironment` for baking data and dependencies into the remote sandbox image.
