---
title: Union On-Demand
description: Run tasks on GPUs and CPUs that Union.ai provisions, operates, and bills by the minute, by sending runs to the union-ondemand queue.
icon: gpu-card
weight: 6
variants: -flyte +union
---

# Union On-Demand

> [!NOTE] Invitation only
> Union On-Demand is in beta and available by invitation. Union.ai contacts the organizations it
> invites.

Union On-Demand gives your runs GPUs and CPUs that Union.ai provisions, operates, and bills by the
minute. There is no cluster to run and no capacity commitment. Send a run to the `union-ondemand`
queue:

```bash
flyte run --queue union-ondemand my_workflow.py main
```

Union.ai finds the capacity, builds and starts your image, and tears everything down when the run
ends. The run appears in your project like any other run, with queue depth, metrics, progress,
errors, and the image build.

## When to use it

During the beta, use Union On-Demand for work that is not business-critical and does not involve
sensitive IP or data. For critical, IP-sensitive, or data-sensitive workloads, use your own data
plane.

| Your situation | Use |
|---|---|
| Short GPU bursts: evaluations, fine-tuning, batch inference, backfills | Union On-Demand |
| Burst beyond your own clusters, or waiting on cloud quota | Union On-Demand, next to your data plane |
| You want GPUs without signing a capacity contract first | Union On-Demand |
| Steady, around-the-clock GPU work | Reserved capacity (whole nodes, 12-month term, 20% below on-demand rates) |
| Workloads that must stay inside your own cloud account | Your own data plane |

## How it works

Union On-Demand is a queue, `union-ondemand`, that your control plane schedules onto like any other
[queue](./queues). Union.ai operates the compute behind it. The data your tasks read and write
lives in a bucket you own.

1. **You send a run to the queue** from the CLI, the Python SDK, or the launch form in the UI.
2. **Union.ai builds the image.** The remote image builder builds the image for your run and stores
   it privately for your organization.
3. **The control plane schedules each task.** Union.ai finds capacity for the CPUs, memory, and
   GPUs the task requests.
4. **Each task starts in its own sandbox.** It reads its inputs from your bucket, writes its
   outputs back, and reports progress to your control plane.
5. **The sandbox is removed when the task ends**, along with its scratch disk.

### Concepts

| Concept | What it means on Union On-Demand |
|---|---|
| Queue | `union-ondemand` appears in your organization's queue list once enabled. The queue page shows runs and actions completed per day and the CPU, memory, and GPU minutes used. |
| Whole runs | An entire run executes on Union On-Demand. A run that starts on `union-ondemand` keeps all its child actions there, and a run on one of your own queues cannot place children on it. Inside an On-Demand run, CPU and GPU tasks can call each other. |
| Your bucket | One object store bucket you own holds run metadata (inputs, outputs, run context, reports) and raw data (files, directories, dataframes). If Union.ai cannot reach your bucket, runs fail with a retryable error. They are never served from storage that Union.ai owns. |
| Images | Built by the remote image builder. Local image builds are not supported. |
| Sandboxed tasks | Every task, CPU or GPU, runs in a gVisor sandbox. CPU tasks run as Kubernetes pods in a namespace used only by your organization. GPU tasks run as sandboxed containers on the GPU provider's machines. |
| Capacity | Best effort, sourced across providers at request time. There is no uptime commitment. |

## Prerequisites

- An invitation to Union On-Demand.
- An organization admin who can manage clusters and secrets.
- An S3-compatible bucket you own, and an access key scoped to it. Use a bucket that only Union
  On-Demand uses.
- `flyte` 2.13.6 or later, so that `get_logs` returns logs for GPU tasks.

> [!WARNING] Egress charges
> On-Demand compute may run in a different cloud or region from your bucket. If your storage
> provider charges egress, it bills you for every read from Union On-Demand. Cloudflare R2 and
> Tigris do not charge egress fees.

## Enable the queue

Enable the queue once per organization.

1. In the console, open **Settings → Queues** and find the **Union On-Demand** section.
2. Select **Enable** and enter your storage details:

   | Field | Value |
   |---|---|
   | Bucket | The exact bucket name |
   | Endpoint | Empty for Amazon S3. For R2, `https://<account>.r2.cloudflarestorage.com`, where `<account>` is your Cloudflare account ID |
   | Region | The bucket's region. For R2, `auto` |
   | Access key ID and secret access key | The key you created for this bucket |

3. Union.ai validates the store by writing, reading back, and deleting a test object. Only public
   HTTPS endpoints are accepted. The secret access key is stored as a managed secret and is never
   shown again.

The `union-ondemand` queue appears in your queue list, usually within seconds and within 10 minutes
at most.

## Run on Union On-Demand

Set the queue on the run context:

```python
import flyte

env = flyte.TaskEnvironment(
    name="gpu",
    resources=flyte.Resources(gpu="T4:1"),
)


@env.task
async def main() -> str:
    return "Hello from Union On-Demand"


if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.with_runcontext(queue="union-ondemand").run(main)
    print(run.url)
```

You can also set `queue="union-ondemand"` on a `flyte.TaskEnvironment` or a task, or make it the
default queue for an organization, domain, or project in **Default Settings**. See
[Queues](../tasks/task-configuration/queues) for every way to target a queue.

Build images with the remote image builder (`image_builder="remote"`).

A project that uses Union On-Demand offers only `union-ondemand` in the launch form, because a run
cannot mix Union On-Demand with your other queues.

### Watch the run

Follow the run in your project as usual. A GPU task shows **Looking for GPU** while capacity is
found, then **GPU container started**. The queue page's **Overview** tab shows runs and actions
completed and the CPU, memory, and GPU minutes they used over the last 6 hours, 24 hours, or 7 days.

## Change storage, rotate keys, or disable

- **Edit storage or rotate keys** from the same **Union On-Demand** section. Keep the old key valid
  until runs that started before the rotation finish.
- **Moving to a different bucket** leaves earlier outputs and cache entries behind, so a cache hit
  on an earlier output fails.
- **Disable** removes the queue from your organization and keeps your storage settings so you can
  re-enable. Disabling does not wait for runs that are in flight. Let them finish, or abort them,
  before you disable.

## Billing

For rates and the GPU types offered, contact your Union.ai account team.

- **Per minute, while your action runs.** Billing starts when the action starts running and stops
  when it ends.
- **No charge for start-up, idle time, or teardown.** Provisioning machines, pulling images, and
  shutting down are not billed.
- **Billed on what you request.** A CPU task is billed for the vCPUs and memory it requests, for as
  long as it runs. A GPU task is billed for GPU time only. Its CPU and memory are included in the
  GPU rate.
- **Image builds are billed as vCPU time.** A build is billed for its build time multiplied by the
  builder's 16 vCPUs, at the vCPU rate.
- **Local disk included.** Each action gets up to 200 GB of scratch disk at no extra charge.
- **Your object store, your bill.** Your storage provider charges you for storage and egress.
- **No minimum spend.**

The `union-ondemand` queue page shows CPU, memory, and GPU minutes for completed work. Charges
appear on your Union.ai invoice.

## Limits

Union On-Demand runs batch work only.

| Supported | Not supported |
|---|---|
| Batch work: training, fine-tuning, evaluations, batch inference, backfills | Apps and model serving |
| CPU-only and GPU tasks, and runs that mix them | Mixing Union On-Demand and your own queues in one run |
| Up to 8 GPUs of one type in a task | Multi-node or interconnected GPU jobs: Ray, Spark, MPI |
| Images from the remote image builder | Local image builds |
| Data through your bucket, plus scratch space that is removed when the task ends | Persistent volumes |
| | Named pod templates, and pod settings that reach outside the task: host paths and host namespaces, node selectors, tolerations, init containers, security contexts, service accounts, and secret volumes |
| | Reusable containers |
| | Confidential computing and machines dedicated to one customer |

### Capacity and regions

- Capacity is best effort. A task that cannot be placed waits in the queue until capacity is free.
- The number of GPUs of each type running at once is capped across all organizations.
- A task runs until its timeout, or for 24 hours if it sets none.
- CPU tasks run in AWS US East (Ohio), `us-east-2`. GPU tasks run wherever the GPU provider has
  capacity, in a cloud and region it chooses. Region pinning is not available.

### What is kept after a task ends

Nothing is kept on the machine. The task's sandbox and scratch space are torn down when the task
ends, and its outputs are in your bucket. Logs of a finished run stay available in Union.ai for 90
days.

## Security model

Union On-Demand is multi-tenant. Machines are shared between customers, and every task, CPU or
GPU, is isolated in its own gVisor sandbox that is removed when the task ends. Your data stays in
a bucket you own. Union.ai operates the service and holds the access keys you provide.

If your security policy requires machines that no other customer uses, run on your own data plane.
The rest of the platform works the same way there.

### Isolation from other customers

Machines are not dedicated to a customer, and one machine may run tasks for several customers at
once. Isolation comes from the sandbox each task runs in.

- **Its own kernel boundary.** Each task runs on gVisor (the `runsc` runtime), a user-space kernel
  that handles the task's system calls itself. Your code never talks directly to the host's kernel.
  A kernel vulnerability or container escape inside one sandbox does not give access to the machine
  or to other sandboxes.
- **Its own filesystem and processes.** A task sees only its image and its own scratch disk. It
  cannot see processes or files that belong to other tasks or to the host.
- **Short-lived.** A sandbox exists only while your task runs.
- **Network.** Tasks do not accept connections from other customers' tasks. Outbound internet
  access is open, so tasks can reach your bucket and your control plane, install packages, and
  download models. If you need outbound access restricted to an allowlist, contact your Union.ai
  account team.

Pod settings that reach outside the task are refused. If a task is rejected with
`violates PodSecurity baseline`, remove the host access or added privileges it asks for. The
[Limits](#limits) table lists the refused settings.

### Your data

Run data is written to an object store bucket you own:

- **Metadata:** inputs, outputs, run context, and reports.
- **Raw data:** files, directories, and dataframes.

A run on Union On-Demand always uses your configured bucket and path. Union.ai does not copy your
data into storage it owns. Run records in your control plane (names, status, timings, errors) are
kept as they are for any run.

Data travels between your tasks and your bucket over TLS. You and your storage provider control
encryption at rest in your bucket.

### Your bucket and access keys

To read and write your bucket, Union On-Demand needs access keys that you create and give to
Union.ai.

- **Use a separate bucket.** Use a bucket that only Union On-Demand uses, with keys scoped to that
  bucket alone. Keep data that On-Demand runs should not touch in a different bucket.
- **Keys are validated.** Union.ai checks that the keys can read, write, and delete a test object
  before it enables the queue. Only HTTPS endpoints are accepted.
- **Keys are encrypted at rest.** Union.ai stores them encrypted with AES-256-GCM, bound to your
  organization, with the encryption key held in a cloud secret manager separate from the database.
  No API, UI, or notification returns them. Viewers of your settings see only the bucket and
  endpoint.
- **Keys are available to your tasks.** The keys are passed to your tasks as standard environment
  variables, so your code and libraries such as `boto3` and `s3fs` can use your bucket directly.
  Any code you run on Union On-Demand, including third-party packages, can use them.
- **Rotation.** You can rotate the keys at any time. Tasks that start after the rotation receive
  the new keys.

### How tasks talk to your control plane

Tasks report progress, start child actions, and read run metadata by calling your control plane.
They authenticate with credentials that Union.ai manages for your organization's use of Union
On-Demand. These credentials are never shown to you or to anyone outside Union.ai's services, and
they act only within your organization.

### What you are trusting Union.ai with

Running your code on compute that Union.ai operates means trusting Union.ai as the operator.

- **Union.ai and its infrastructure providers run the machines.** The providers host the hardware
  and the sandbox runtime. They are bound by contract to Union.ai's security requirements and are
  named on the Union.ai subprocessor list.
- **A small number of Union.ai engineers can administer the service.** They need this access to
  run and repair it. The access requires single sign-on with multi-factor authentication and is
  logged.
- **Union.ai holds your storage keys.** They are encrypted at rest, and no API or UI returns them.
  Union.ai's services decrypt them only to pass them to your tasks, where the engineers who
  administer the service could read them.
- **Confidential computing is not offered.** Your code and data are processed in normal memory. If
  you need hardware-encrypted memory, customer-held keys, or machines no other customer uses, run
  on your own data plane.

### Who can access your tasks

gVisor protects the machine and other customers from your code. It does not hide a task from
whoever operates the machine the task runs on. A person with root on a machine can enter a sandbox
and read the task's memory and scratch disk. Without root on that machine, the sandbox cannot be
entered.

| Who | What they can reach | How it is limited |
|---|---|---|
| Other customers | Nothing. | Each task runs in its own gVisor sandbox, in a namespace used only by your organization, with network isolation between organizations. |
| People in your organization | Your runs, logs, and results. | The roles and permissions you set in Union.ai. |
| Union.ai staff who do not administer the service | No access to the machines or to running tasks. | Access is granted only to the engineers who run the service. |
| Union.ai engineers who administer the service | A running task's settings, including the storage keys passed to it, and its logs. With root on a machine, they can enter a task's sandbox and read its memory and scratch disk. | A small group. Access requires single sign-on with multi-factor authentication and is logged. Entering a sandbox requires root on the machine. |
| Infrastructure providers | The machines they host. GPU tasks run on a provider's machines and in the provider's gVisor runtime, so the provider's operators hold machine-level access there. | Bound by contract to Union.ai's security requirements and named on the Union.ai subprocessor list. |

### Compliance

During the beta, Union On-Demand is not covered by Union.ai's SOC 2 report, HIPAA commitments, or
business associate agreements (BAAs). Do not run regulated data or protected health information on
Union On-Demand.

### Shared responsibility

| Area | Responsible |
|---|---|
| Machines, operating systems, GPU drivers, and the sandbox runtime | Union.ai |
| Isolation between customers | Union.ai |
| Building and storing your images | Union.ai |
| Encrypting your storage keys and passing them only to your tasks | Union.ai |
| The bucket, its access policy, its encryption, and its egress charges | You |
| Creating, scoping, and rotating the access keys you give Union.ai | You |
| The code and dependencies you run | You |
| Who in your organization can launch runs on Union On-Demand | You |

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `PermissionDenied` when enabling | Your user cannot manage secrets. Ask an organization admin. |
| `bucket ... is claimed by another organization on this pool` | A bucket can back only one organization. Use a different bucket. |
| `AccessDenied` or `NoSuchBucket` during validation | The key or bucket name is wrong, or the key lacks read, write, or delete on the bucket. |
| `endpoint ... not allowed` | Private and internal endpoints are refused. Use a public HTTPS endpoint. |
| Runs fail with `organization storage unavailable` | Union.ai cannot reach your bucket with the stored key. Check the key and bucket, then retry. |
| `accelerator "<x>" is not available on this queue` | Union On-Demand does not offer that GPU type. Ask your Union.ai account team which types are available. |
| Task rejected with `violates PodSecurity baseline` | The task asks for host access or added privileges, which Union On-Demand does not allow. |

## Related pages

- [Queues](../tasks/task-configuration/queues): target a queue from task code.
- [Managing queues](./queues): create and manage your own queues.
- [Container images](../tasks/task-configuration/container-images): build images with the remote
  image builder.
