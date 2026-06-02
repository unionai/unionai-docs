---
title: Filesystem
weight: 5
variants: -flyte +union
---

# Filesystem

Each session has its own work dir on the sandbox filesystem. State written there during one `run()` is visible to the next, and you can push or pull bytes from outside the sandbox without shelling out.

## Moving bytes in and out

`put_bytes` and `get_bytes` are the simplest way to stage a file into a sandbox before a command, or retrieve a result after:

```python
async with sb.local.session() as sbx:
    await sbx.put_bytes("/tmp/input.json", b'{"x": 1}')

    proc = await sbx.run("python3 /tmp/process.py")
    await proc.communicate()

    result = await sbx.get_bytes("/tmp/result.json", max_bytes=10 * 1024 * 1024)
```

`max_bytes` caps the response size; the call raises if the file is larger. Both methods operate on absolute paths inside the sandbox; the path must land in the RW allow-list. `/tmp` and `/dev/shm` are in the default allow-list on every backend, so they're the safe places to stage files unless you've pinned a `host_work_dir` (see below).

Use them together with `network_mode="blocked"` to keep an untrusted `run()` from doing any I/O of its own: stage inputs via `put_bytes`, run with no network, collect outputs via `get_bytes`.

## The default allow-list

The sandbox grants the sandboxed process read-only access to system paths (`/usr`, `/lib`, `/etc`, `/proc`, `/sys`, and so on) and read-write access to `/tmp`, `/dev/shm`, and the per-session work dir. Everything else on the host is invisible.

These defaults are secure; you don't have to touch them for typical use.

## Extending the allow-list

You can add host paths to the allow-list. Additions never replace the secure defaults:

```python
sbx = sb.local.session(
    read_only_paths=["/opt/models"],         # extend the read-only allow-list
    read_write_paths=["/data/scratch"],      # extend the read-write allow-list
    host_work_dir="/tmp/my-sandbox-work",    # pin the per-session work dir
)
```

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
