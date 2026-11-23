---
title: Teach a humanoid to run
icon: person-walking
description: Train a running gait for the Unitree G1 humanoid with Brax PPO over MuJoCo MJX, 8,192 simulated robots on one GPU, with a live video report and a published policy.
weight: 2
variants: -flyte +union
mermaid: true
---

# Teach a humanoid to run

> [!NOTE]
> Code available [on GitHub](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/humanoid_locomotion).

A humanoid gait takes hundreds of millions of simulation steps to learn. The classic way to get
them is to fan simulators out across many CPU workers and ship their rollouts to a GPU learner.
This tutorial does the opposite: [MuJoCo MJX](https://mujoco.readthedocs.io/en/stable/mjx.html)
compiles the physics into the same XLA program as the learner, so 8,192 copies of the
[Unitree G1](https://www.unitree.com/g1/) step in parallel on one GPU and there is no Python
between simulation, scoring, and the gradient step. Flyte's job is everything around that
loop: the GPU, the image, a live report you can watch the robot learn in, CPU replays that
prove the result, and a versioned artifact for the trained policy.

By the end you will have:

- a running policy for the G1, trained with [Brax](https://github.com/google/brax) PPO on
  DeepMind's tuned [MuJoCo Playground](https://playground.mujoco.org/) environment;
- a training report that streams the reward curve and films the policy every few evaluations;
- three replays filmed side on, a random policy and the trained policy at walking and running
  speed, each measuring the speed it reached and how often both feet left the ground;
- the policy published as the model artifact `g1-run-policy`, with a model card.

## Why one GPU, and where Flyte fits

| Approach | Where the simulator runs | What limits it |
| --- | --- | --- |
| CPU simulators, GPU learner | Many CPU workers | Moving rollouts to the learner, and Python in every step |
| MJX on the GPU (this tutorial) | Inside the learner's XLA program | GPU memory for the parallel worlds |

The single-GPU design keeps the loop simple, but it does not make the infrastructure go away.
The image needs JAX with CUDA, MuJoCo, Brax, Playground, an EGL renderer, and the robot models.
Rendering needs a different backend than training. And a policy is only worth something if you
can see what it does and load it later. Each of those is one Flyte construct:

| Need | Construct |
| --- | --- |
| A reproducible JAX, MuJoCo, and EGL image with the robot models baked in | `flyte.Image` layers, built remotely |
| One GPU for training, CPUs for filming | One `flyte.TaskEnvironment` per role |
| Watch the gait change while it trains | `report=True` and `flyte.report.replace` from a Brax callback |
| Prove the result next to a baseline | Three replay tasks run in parallel with `asyncio.gather` |
| Keep and find the trained policy | `flyte.artifacts` with a model card |

```mermaid
flowchart LR
    D["learn_to_run<br/>CPU driver"] --> T["train_policy<br/>1 GPU, 8,192 MJX worlds<br/>live report"]
    T -- "checkpoint (File)" --> R1["render_replay<br/>random policy"]
    T --> R2["render_replay<br/>walk command"]
    T --> R3["render_replay<br/>run command"]
    R1 & R2 & R3 --> P["publish_policy<br/>g1-run-policy artifact"]

    classDef gpu fill:#3b82f633,stroke:#3b82f6,stroke-width:1.5px
    classDef cpu fill:#94a3b826,stroke:#94a3b8,stroke-width:1px
    class T gpu
    class D,R1,R2,R3,P cpu
```

## Getting started

You need a Union cluster with an NVIDIA L40S, or another GPU with at least 40 GB of memory. To
use a different card, change `gpu_env` in `learn_to_run.py`.

```bash
git clone https://github.com/unionai/unionai-examples
cd unionai-examples/v2/tutorials/humanoid_locomotion
python learn_to_run.py
```

{{< code file="/unionai-examples/v2/tutorials/humanoid_locomotion/learn_to_run.py" fragment=run lang=python >}}

The first run builds the image, which takes a while because of the CUDA build of JAX. Later
runs reuse it. `--smoke` trains 20 million steps in a few minutes, which is enough to check
the plumbing but not enough for the robot to stay up. `--checkpoint` skips training and only
replays and reports an existing policy.

## The image and environments

The image pins JAX to 0.9 because Brax 0.14 still calls a JAX API that 0.10 removed. The last
layer downloads the robot models into Playground's package directory at build time. Without
it, every pod would clone the `mujoco_menagerie` repository at startup.

{{< code file="/unionai-examples/v2/tutorials/humanoid_locomotion/learn_to_run.py" fragment=image lang=python >}}

Three environments share the image. Training gets the GPU, with JAX told not to preallocate
most of the card, because MJX's Warp kernels allocate memory outside JAX's pool. Replays run
MJX's JAX backend on CPU and render with MuJoCo over headless EGL, since MJX has no renderer.
The driver only waits on the other tasks, so it is small.

{{< code file="/unionai-examples/v2/tutorials/humanoid_locomotion/learn_to_run.py" fragment=envs lang=python >}}

## The running environment

The environment is DeepMind's `G1JoystickFlatTerrain`: the policy gets a velocity command and
proprioception, and it is rewarded for tracking the command while staying upright, with feet
in the air on schedule. Upstream it learns to walk at up to 1 m/s. Two changes make it run:

- forward commands go up to `max_speed`, 2.5 m/s by default;
- the gait clock speeds up with the command, so a fast command asks for a faster cadence
  instead of ever-longer strides.

It also raises `njmax`, the constraint budget: upstream's value is a little too small for a G1
in ground contact, and when MJX runs out it drops constraints silently and the feet sink into
the floor. And it turns off a Warp solver warning that is printed for every world on every
step, which otherwise dominates the wall-clock time.

{{< code file="/unionai-examples/v2/tutorials/humanoid_locomotion/g1.py" fragment=env lang=python >}}

## Training with a live report

`train_policy` is one Brax `ppo.train` call. Brax runs the whole loop on the GPU and calls back
into Python twice: `progress_fn` after every evaluation, with the metrics, and
`policy_params_fn`, with the current weights. The task uses the first to redraw its report, and
the second to film the policy on the run command every few evaluations. A failed snapshot is
logged and skipped, so filming can never kill a long run.

{{< code file="/unionai-examples/v2/tutorials/humanoid_locomotion/learn_to_run.py" fragment=train lang=python >}}

The policy is asymmetric: the actor sees sensor-shaped observations, and the critic also sees
privileged simulator state, which it only needs during training. The checkpoint is a pickle of
the parameters, the network configuration, the training history, and the snapshots, returned as
a `flyte.io.File`.

## Replays: proof, not a number

An eval reward says little on its own. The driver films three replays in parallel on CPU: a
random policy, and the trained policy holding a walking and a running command. Each replay
measures what the robot actually did.

{{< code file="/unionai-examples/v2/tutorials/humanoid_locomotion/g1.py" fragment=rollout lang=python >}}

The flight phase is the share of steps with both feet off the ground. It is what separates a
run from a fast walk.

{{< code file="/unionai-examples/v2/tutorials/humanoid_locomotion/learn_to_run.py" fragment=replay lang=python >}}

## The driver and the artifact

The driver trains, replays, writes the final report, and publishes the checkpoint as a model
artifact. A later run, an evaluation job, or an app can load it with
`flyte.remote.Artifact.get("g1-run-policy")`.

{{< code file="/unionai-examples/v2/tutorials/humanoid_locomotion/learn_to_run.py" fragment=driver lang=python >}}

{{< code file="/unionai-examples/v2/tutorials/humanoid_locomotion/learn_to_run.py" fragment=publish lang=python >}}

## Results

A run with the defaults trained 150 million steps in 19 minutes on one L40S, and took 36
minutes end to end. Each replay holds one command for 10 seconds (500 control steps):

| Replay | Speed reached | Flight phase | Distance | Upright |
| --- | --- | --- | --- | --- |
| Random policy, 2.5 m/s command | 0.05 m/s | n/a | 0.1 m | fell at step 8 |
| Trained, 1.0 m/s command | 0.97 m/s | 7% | 8.9 m | 500 of 500 steps |
| Trained, 2.5 m/s command | 2.42 m/s | 15% | 22.3 m | 500 of 500 steps |

At the run command the robot reaches 97% of the commanded speed, and both feet are off the
ground in 15% of steps, twice as often as at walking speed. For a robot with legs about 0.7 m
long, 2.4 m/s is a jog (a Froude number of about 0.85; people switch from walking to running
at about 0.5), not a sprint.

The live report of `train_policy` shows progress, the latest filmed snapshot, and a filmstrip
of the gait as it forms:

![The training report: progress tiles, the latest filmed snapshot, and the gait filmstrip](../../../_static/images/tutorials/humanoid-locomotion/training-report.png)

The driver's final report puts the three replays side by side:

![The final report: running speed and flight phase tiles, and the random, walk, and run replays](../../../_static/images/tutorials/humanoid-locomotion/final-report.png)

The `g1-run-policy` artifact carries the same results in its model card:

![The g1-run-policy model card](../../../_static/images/tutorials/humanoid-locomotion/policy-card.png)

## Going further

- **Train longer.** The speed and the flight phase keep improving past 150 million steps. A
  billion steps takes under 2 hours on one L40S.
- **Rough terrain.** Playground has a `G1JoystickRoughTerrain` environment. Change `BASE_ENV`,
  and train from the flat-terrain checkpoint.
- **Scale out instead.** To run a simulator that cannot be compiled to the GPU, fan rollouts
  out to a warm pool of CPU workers, as the [GRPO tutorial](../grpo-lora/_index) does for LLM
  generation.
- **Sweep it.** Every `train_policy` call is independent, so a hyperparameter sweep is an
  `asyncio.gather` over several calls, each on its own GPU.

## Related

- [Reinforcement learning](../../../user-guide/reinforcement-learning/_index) in the user guide
- [Reports](../../../user-guide/tasks/task-programming/reports)
- [Artifacts](../../../user-guide/artifacts/_index)
