---
title: PodTemplate
version: 2.4.4
variants: +flyte +union
layout: py_api
---

# PodTemplate

**Package:** `flyte`

Custom PodTemplate specification for a Task.


## Parameters

```python
class PodTemplate(
    pod_spec: Optional['V1PodSpec'],
    primary_container_name: str,
    labels: Optional[Dict[str, str]],
    annotations: Optional[Dict[str, str]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `pod_spec` | `Optional['V1PodSpec']` | |
| `primary_container_name` | `str` | |
| `labels` | `Optional[Dict[str, str]]` | |
| `annotations` | `Optional[Dict[str, str]]` | |

## Methods

| Method | Description |
|-|-|
| [`allow_fuse()`](#allow_fuse) | Return a copy of this template granted everything a container needs to. |
| [`allow_nested_sandboxing()`](#allow_nested_sandboxing) | Return a copy of this template granted the prerequisites for creating. |
| [`from_spec()`](#from_spec) | Create a :class:`PodTemplate` from an existing ``V1PodSpec``. |
| [`to_k8s_pod()`](#to_k8s_pod) |  |


### allow_fuse()

```python
def allow_fuse(
    privileged: bool,
) -> PodTemplate
```
Return a copy of this template granted everything a container needs to
perform an in-process FUSE mount (e.g. for ``Volume`` support).

Specifically, the copy:

* adds a ``hostPath`` volume named ``fuse-device`` pointing at
  ``/dev/fuse`` on the node, mounted into the primary container;
* adds ``CAP_SYS_ADMIN`` to the primary container so the ``mount``
  syscall is permitted;
* with ``privileged=True`` (the default), sets ``privileged: true`` on
  the primary container; with ``privileged=False``, instead sets the
  ``container.apparmor.security.beta.kubernetes.io/&lt;primary&gt;:
  unconfined`` pod annotation (the default AppArmor profile would
  otherwise block ``mount``);
* stamps the ``flyte.org/capability-fuse`` annotation for auditability.

Why privileged is the default: opening ``/dev/fuse`` is gated by the
container runtime's device-cgroup allowlist, which only ``privileged``
bypasses — there is no pod-spec field to whitelist a device for a
non-privileged container. Pass ``privileged=False`` **only** on
clusters that permit ``/dev/fuse`` for non-privileged containers (e.g.
via a FUSE device plugin or runtime device-allowlist configuration);
otherwise the pod deploys fine but ``open("/dev/fuse")`` fails with
``EPERM`` at runtime. ``privileged=False`` composes with
``allow_nested_sandboxing()``; ``privileged=True`` does not (Kubernetes
rejects privileged containers that set
``allowPrivilegeEscalation: false``).

The original template is never mutated; existing volumes, mounts,
sidecars, labels, annotations, and unrelated security-context fields
are preserved. Re-applying with the same arguments is idempotent.

Raises ``ValueError`` if the template already pins a conflicting
security posture (with ``privileged=True``: ``privileged: false`` or
``allowPrivilegeEscalation: false`` pre-set; with ``privileged=False``:
a different AppArmor profile for the primary container).


| Parameter | Type | Description |
|-|-|-|
| `privileged` | `bool` | |

### allow_nested_sandboxing()

```python
def allow_nested_sandboxing()
```
Return a copy of this template granted the prerequisites for creating
nested sandboxes (e.g. the bubblewrap/``bwrap`` backend of
``SandboxEnvironment``) — and nothing more.

bwrap runs as a non-root user via unprivileged user namespaces, but the
containerd default seccomp profile only permits the ``mount`` /
``pivot_root`` / ``setns`` / ``unshare`` syscalls it needs when the
container's capability set includes ``CAP_SYS_ADMIN``, and the default
AppArmor profile must be unconfined so those calls aren't blocked.
The copy carries exactly that:

* ``CAP_SYS_ADMIN`` added to the primary container's capabilities;
* ``allowPrivilegeEscalation: false`` (no other caps, not privileged);
* the ``container.apparmor.security.beta.kubernetes.io/&lt;primary&gt;:
  unconfined`` pod annotation (on K8s &gt;= 1.30 the
  ``securityContext.appArmorProfile: {type: Unconfined}`` field is the
  equivalent; the annotation is used here for version compatibility);
* the ``flyte.org/capability-nested-sandboxing`` annotation for
  auditability.

A cluster that already permits unprivileged user namespaces needs none
of this for the ``userns`` sandbox backend — only use this when the
seccomp/AppArmor defaults block the sandboxing syscalls.

Composes with ``allow_fuse(privileged=False)``; not with the default
``allow_fuse()``, which makes the container privileged.

The original template is never mutated; existing fields are preserved
and re-applying is idempotent. Raises ``ValueError`` if the template
already pins a conflicting security posture (``privileged: true``,
``allowPrivilegeEscalation: true``, or a different AppArmor profile
for the primary container).


### from_spec()

```python
def from_spec(
    pod_spec: 'V1PodSpec',
    primary_container_name: Optional[str],
    labels: Optional[Dict[str, str]],
    annotations: Optional[Dict[str, str]],
) -> PodTemplate
```
Create a :class:`PodTemplate` from an existing ``V1PodSpec``.

The spec is deep-copied, so later mutations of the input (or of the
returned template) don't leak into each other.

The primary container — the one Flyte injects the task image/command
into — is resolved as follows:

1. If ``primary_container_name`` is given, a container with that name
   must exist in the spec.
2. Otherwise, a container named ``primary`` is used if present.
3. Otherwise, if the spec has exactly one container, that container is
   adopted as the primary.
4. Otherwise (multiple containers, none named ``primary``), a
   ``ValueError`` is raised — pass ``primary_container_name`` to pick
   one explicitly.



| Parameter | Type | Description |
|-|-|-|
| `pod_spec` | `'V1PodSpec'` | The ``kubernetes.client.V1PodSpec`` to wrap. |
| `primary_container_name` | `Optional[str]` | Optional explicit name of the primary container within ``pod_spec``. |
| `labels` | `Optional[Dict[str, str]]` | Optional pod labels. |
| `annotations` | `Optional[Dict[str, str]]` | Optional pod annotations. |

### to_k8s_pod()

```python
def to_k8s_pod()
```
