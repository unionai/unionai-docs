---
title: GitStatus
version: 2.0.0b43
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# GitStatus

**Package:** `flyte.git`

A class representing the status of a git repository.



```python
class GitStatus(
    is_valid: bool,
    is_tree_clean: bool,
    remote_url: str,
    repo_dir: pathlib._local.Path,
    commit_sha: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `is_valid` | `bool` | Whether git repository is valid |
| `is_tree_clean` | `bool` | Whether working tree is clean |
| `remote_url` | `str` | Remote URL in HTTPS format |
| `repo_dir` | `pathlib._local.Path` | Repository root directory |
| `commit_sha` | `str` | Current commit SHA |

## Methods

| Method | Description |
|-|-|
| [`build_url()`](#build_url) | Build a git URL for the given path. |
| [`from_current_repo()`](#from_current_repo) | Discover git information from the current repository. |


### build_url()

```python
def build_url(
    path: pathlib._local.Path | str,
    line_number: int,
) -> str
```
Build a git URL for the given path.



| Parameter | Type | Description |
|-|-|-|
| `path` | `pathlib._local.Path \| str` | Path to a file |
| `line_number` | `int` | Line number of the code file :return: Path relative to repo_dir |

### from_current_repo()

```python
def from_current_repo()
```
Discover git information from the current repository.

If Git is not installed or .git does not exist, returns GitStatus with is_valid=False.

:return: GitStatus instance with discovered git information


