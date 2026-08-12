---
title: Leases
weight: 9
variants: -flyte +union
---

# Leases

When you run a task on {{< key product_name >}}, your code doesn't execute on the control plane: it runs on a compute cluster, which might be in your cloud account, in another region, or one of several clusters attached to your account. {{< key product_name >}} has to hand a piece of work to a cluster, then keep track of whether that work is actually getting done.

It does this with **leases**.

You normally never have to think about leases. But occasionally you'll see a message like:

```
lease expired for action a0 ...
```

This page explains what that means, why it happens, and why, most of the time, it's the system protecting you rather than something going wrong.

## What a lease is

A lease is a time-bound grant of work. {{< key product_name >}} hands a unit of work (an [action](./runs-and-actions)) to a worker on a cluster and says, in effect: *"You own this for now. Keep telling me you're still on it."*

Think of it like **renting an apartment**:

- The landlord (the {{< key product_name >}} control plane) owns the property (your work) and hands a tenant (a cluster worker) the keys under a lease.
- The tenant doesn't pay rent once a year; they pay on a regular schedule. In {{< key product_name >}}, the worker sends a **heartbeat** every few seconds: *"still working on it."*
- As long as the rent keeps coming in, the tenant keeps the apartment. As long as the heartbeats keep coming in, the worker keeps the work.

This heartbeat is the whole point. It's how {{< key product_name >}} knows (continuously, not just at the start) that your work is alive and progressing.

## Why leases exist

{{< key product_name >}} hands work to machines it doesn't fully control, and machines fail in messy ways:

- A **cluster goes offline**: a network partition, a dropped connection, a zone outage.
- A **component on the cluster fails**: the worker process crashes or hangs.
- The **control plane itself blips**: a brief restart or deployment.

The hard part isn't any single failure. It's that from the control plane's point of view, **all of these look the same**: the heartbeats stopped. When a worker goes silent, {{< key product_name >}} cannot tell the difference between:

- The worker **died** (the work needs to be handed to someone else), and
- The worker is **alive but unreachable** and still grinding away on your task.

This is one of the genuinely hard problems in distributed systems. Leases are how {{< key product_name >}} makes a safe decision without being able to see the truth directly.

## What happens when heartbeats stop

When a worker stops heartbeating, {{< key product_name >}} does **not** evict it immediately. A missed heartbeat is usually nothing: a momentary network hiccup, a quick deployment, a transient glitch. Just like a landlord wouldn't change the locks the day rent is one hour late, the system gives a **grace period**.

During that grace period the lease is still valid. If heartbeats resume (the network heals, the worker reconnects) the worker simply picks up where it left off. **No work is lost and nothing is re-run.** This is the common case, and it's invisible to you.

But if enough time passes (a window that {{< key product_name >}} configures) and the worker is *still* silent, the system reaches a point where it can no longer safely assume the work is in good hands. At that point it has to **reap the lease**. This is what you see as `lease expired`.

The system reaps a silent lease for two reasons, and both are about protecting you:

1. **To make forward progress.** If the original worker really is gone, your run would otherwise hang forever. Reaping the lease frees the work to be reassigned to a healthy worker so it can actually finish.
2. **To guarantee exactly one owner.** {{< key product_name >}} must never have two workers both believing they own the same action: that would corrupt results and waste compute. Reaping the old lease, and refusing to accept any further reports from it, ensures that when the work is reassigned, **exactly one** worker owns it.

The mechanisms behind these are **lease expiration** (the old grant is invalidated) and **lease failover** (the work is handed to a new worker).

## Why this is the safe trade-off

Here's the key design decision, and the part most relevant to you as someone who cares about **failures and cost**:

> [!NOTE] Correctness over runaway compute
> {{< key product_name >}} would rather **occasionally redo a small amount of work** than let a task it can no longer account for keep running unchecked.

Imagine the alternative. A worker becomes unreachable but is secretly still running your job (burning a node, maybe a multi-GPU node) and {{< key product_name >}} can't see it, can't stop it, and can't trust its output. That's exactly the **runaway compute** and surprise cost that you don't want. By bounding every piece of work with a lease, {{< key product_name >}} ensures there's no orphaned, unaccounted-for task quietly running up a bill.

So when a lease expires and the work is reassigned, the cost is at worst **redoing one action**. The benefit is a hard guarantee that compute is always accounted for, and results are always correct.

## How often does this actually happen?

Rarely. {{< key product_name >}} uses sophisticated failure-detection and the grace periods are tuned so that the everyday churn of distributed systems (momentary network issues, routine deployments, brief glitches) is **absorbed automatically**. The system is designed to auto-heal in all of those cases, and in the overwhelming majority of runs you'll never see a lease expiration at all.

When you *do* see one, it generally means a real, sustained failure occurred: a cluster was unreachable for long enough that continuing to trust the lease would have been unsafe.

## What to do when you see `lease expired`

In most cases, **nothing**. The system has already done the right thing:

- The expired lease was reaped, and the action was retried on a healthy worker. The retry you see in the UI is the failover working as intended.
- If the run completed successfully after the retry, your results are correct and complete.

It's worth a closer look only if you see lease expirations **repeatedly** on the same run or cluster. That pattern points to an underlying environment problem (a chronically unhealthy cluster, persistent network issues, or under-provisioned nodes) rather than the lease mechanism itself. In that case, check the health of the affected cluster or reach out to your platform team.

## The takeaway

A lease expiration is **not a system failure**; it's the system doing its job. It's {{< key product_name >}} refusing to let work run unaccounted-for, guaranteeing that every action has exactly one owner, and making sure your run still makes progress when a cluster lets it down.

It's the trade-off in your favor: a small chance of redoing work, in exchange for never paying for runaway compute and never trusting a corrupt result.
