---
title: Work with files
description: Read, write, list, and remove files in a VM sandbox, and copy files and directories between the sandbox and your code.
weight: 4
variants: -flyte +union
---

# Work with files

Before an agent can run its code, the code has to be in the sandbox. After the tests run, you want the report back. `sb.fs` moves files in both directions without going through a shell command.

```python
async with code_runner.session("eval") as sb:
    await sb.fs.upload_dir("./my_project", "project")  # local directory into /work/project
    await sb.run("cd project && pytest --junitxml=report.xml", check=False)
    report = await sb.fs.read_text("project/report.xml")
```

Relative paths are under `/work`. Absolute paths work anywhere in the VM.

## Read and write

| Call | What it does |
| --- | --- |
| `await sb.fs.write_text(path, text)` | Write a text file, replacing any file already at that path. Creates missing parent directories. |
| `await sb.fs.write_bytes(path, data, mode=0o644)` | Write bytes, with a file mode. Replaces and creates parents the same way. |
| `await sb.fs.read_text(path)` | Read a file as text. |
| `await sb.fs.read_bytes(path)` | Read a file as bytes. |

```python
await sb.fs.write_bytes("bin/run.sh", b"#!/bin/sh\necho ok\n", mode=0o755)
```

## List, inspect, and remove

| Call | What it does |
| --- | --- |
| `await sb.fs.ls(path=".")` | List a directory. Returns `FileEntry` objects with `name` and `is_dir`. |
| `await sb.fs.stat(path)` | One `FileEntry`. |
| `await sb.fs.exists(path)` | Whether the path exists. |
| `await sb.fs.mkdir(path, mode=0o755)` | Create a directory and any missing parents. Does nothing if it exists. |
| `await sb.fs.rm(path, recursive=False)` | Remove a file, or a directory with `recursive=True`. |

A missing path raises `FileNotFoundError`.

## Copy between your code and the sandbox

These copy between the sandbox and the file system of the process that runs your code: the task's container, an app, or your laptop.

| Call | What it does |
| --- | --- |
| `await sb.fs.upload(src, dst)` | Copy a local file into the sandbox. |
| `await sb.fs.download(src, dst)` | Copy a file out of the sandbox. Returns the local `Path`. |
| `await sb.fs.upload_dir(src, dst)` | Copy a local directory into the sandbox. |
| `await sb.fs.download_dir(src, dst)` | Copy a directory out of the sandbox. Returns the local `Path`. |

Directory copies move one file per call, 16 files at a time. That is fine for a project of a few hundred files. For a tree of thousands, such as a `node_modules` directory or a dataset of small files, upload one archive and unpack it in the sandbox:

```python
await sb.fs.upload("project.tar.gz", "project.tar.gz")
await sb.run("mkdir -p project && tar -xzf project.tar.gz -C project")
```

`upload_dir` follows symbolic links and copies what they point to. `download_dir` copies regular files and directories, and skips symbolic links.

To move a `flyte.io.File` or `flyte.io.Dir` into a sandbox, download it in the task first, then upload it:

```python
@env.task
async def evaluate(data: flyte.io.Dir) -> str:
    local = await data.download()
    async with code_runner.session("evaluate") as sb:
        await sb.fs.upload_dir(local, "data")
        result = await sb.run("python -c 'import os; print(len(os.listdir(\"data\")))'")
        return result.stdout
```

## Limits

- One file transfer is at most 512 MiB. A larger file raises `ValueError` before anything is sent.
- One command may write a file of at most 4 GiB inside the sandbox.
- A sandbox has 7.8 GiB of disk.

See [Limits and errors](./limits) for the rest of the machine's limits.

To hand a whole disk to another sandbox or task, commit it instead of copying files. See [Save and fork disks](./persist-and-fork).
