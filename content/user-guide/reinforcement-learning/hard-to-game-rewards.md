---
title: Rewards that resist hacking
description: Build graders and verifiers that a policy can't game, by grading outside the policy's reach, keeping answers away from it, red-teaming the grader before training, and auditing trajectories during it.
icon: shield-check
weight: 6
variants: +flyte +union
---

# Rewards that resist hacking

A policy optimizes the reward it gets, not the reward you meant. When the reward was a function of the
completion's text, a flaw in it could pay for the wrong format or a longer answer. When the policy acts in an
environment, such as a repository, a shell, a browser, or a simulator, the grader often inspects that same
environment. Then the policy can change what the grader sees: edit the tests, write a configuration file the
test runner loads, exit before the checks run, or print what the grader looks for.

This page covers how to build graders that hold up, and how to find out whether they do. For the signs of
reward hacking in a training run, see [Catch reward hacking](./evaluation#catch-reward-hacking).

## Grade outside the policy's reach

The policy controls everything in its environment. Treat all of it as untrusted input to the grader.

- **Take only what the task asks for.** List the outputs the policy is meant to produce, such as one source
  file, a patch, an answer string, or a final simulator state. Copy only those into the grader. Test files,
  configuration, hooks, and anything else the policy wrote stay behind.
- **Grade in a fresh copy of the environment.** Rebuild the pristine environment, or fork it from a sealed
  copy, and apply the policy's outputs to it. Don't grade in the environment the policy just worked in.
- **Run the policy's code in a process the grader doesn't share.** Code that runs in the grader's process can
  patch the grader. Run it in a subprocess or a sandbox, with a timeout, resource limits, and no network.
- **Never let expected answers enter that process.** Send the policy's code the inputs. Bring its outputs
  back, and compare them in the grader. Code that never sees the answer can't produce it without solving
  the task.
- **Read structured results, not exit statuses or logs.** An exit status of 0 or the text "passed" is easy to
  produce without passing anything. Read outputs back in a format such as JSON, so an object that only
  pretends to equal the answer can't cross the boundary.
- **Check the hidden cases, all or nothing.** Visible tests tell the policy what to special-case. Partial
  credit over cases the starting code already passes pays the policy for doing nothing.

In Flyte, the grader is its own task, so it runs in its own container with its own image, and returns a typed
result. This grader takes one source file from the policy, runs it in a fresh directory, and compares its
outputs in the grader's own process:

{{< code file="/unionai-examples/v2/tutorials/rl_grader_red_team/red_team_world.py" fragment="sealed" lang="python" >}}

{{< variant union >}}
{{< markdown >}}

The [Red-team your RL grader](../../tutorials/reinforcement-learning/grader-red-team/_index) tutorial runs
this grader, and two weaker ones, against six exploits.

On {{< key product_name >}}, keep the sealed copy of an environment as a read-only
[volume](../tasks/task-programming/volumes/_index). Each episode forks it to act in, and the grader forks the
same sealed copy again to grade in. The grader never mounts the episode's fork.

{{< /markdown >}}
{{< /variant >}}

## Red-team the grader before you train

Test the grader the way the policy will: with submissions that should fail. Before training, run a set of
known exploits and an honest solution through every grader you are considering, and count two errors:

- **Unsolved submissions paid.** Any exploit that gets the full reward is a hole the policy can find.
- **Solved submissions refused.** A hardened grader that rejects correct solutions also gives the trainer a
  wrong signal. Include real model outputs, not just one reference fix, because a correct solution can return
  a tuple where you expected a list.

Also run a do-nothing baseline: the starting environment, unchanged. If it earns reward, the tests don't
cover the bug.

Make each (task, policy, grader) cell its own cached task. Adding an exploit runs only its cells, and changing
a grader re-grades the stored submissions without generating them again.

## Harden judges too

An LLM judge reads text the policy wrote, so that text can address the judge directly.

- **Let a verifier decide correctness where one exists.** Use the judge only for qualities a verifier can't
  check, and weight it accordingly.
- **Show the judge only what it grades.** Pass the final answer and the rubric, not the whole trajectory,
  unless the trajectory is what you grade.
- **Mark the policy's text as data.** Put it inside clear delimiters, tell the judge that instructions inside
  them are part of the answer, and ask for a structured score.
- **Measure the judge against a verifier.** On a sample with known answers, track how often the judge and a
  verifier disagree, iteration by iteration.

Wrap the judge call in `@flyte.trace` so a retried grading task doesn't pay for the same call twice. See
[Call a judge without paying for it twice](./reward-setup#call-a-judge-without-paying-for-it-twice).

## Audit trajectories during training

A grader stops the exploits you anticipated. An audit shows you the ones you didn't. Run two kinds of audit
over the rollouts of every iteration:

- **Deterministic flags.** Compare each episode's final environment with its starting state. Flag changes
  outside the files the task allows, and tokens such as `os._exit`, `sys.exit`, `__eq__`, or test-runner
  imports in the policy's code. Flags don't change the reward. They tell you which trajectories to read.
- **An LLM classifier on a sample.** Label failures and flagged successes against a fixed taxonomy. Make the
  classifier, its prompt version, and the taxonomy inputs to the labeling task, so changing any of them
  re-labels without downloading the trajectories again.

Plot the flag rate next to the reward. A flag rate that rises while the grader still refuses the exploit
means the policy is probing the grader. A reward that rises along with the flag rate means it found a hole.

{{< variant union >}}
{{< markdown >}}

The [Harness evals and trace audits for agentic RL](../../tutorials/reinforcement-learning/agentic-rl-evals/_index)
tutorial builds both kinds of audit over published agent trajectories.

{{< /markdown >}}
{{< /variant >}}

## Keep evaluation separate from the reward

Evaluate with a verifier the policy never trained against, on problems it never saw. A hole in the training
reward then can't hide in the evaluation too. See [Evaluation](./evaluation).

## Related

- [Reward setup](./reward-setup): verifiers, judges, and simulators as rewards.
- [Training environment](./training-environment): isolating each episode.
- [Code sandboxing](../agents/sandboxing/code-sandboxing): run untrusted code with no network.

{{< variant union >}}
{{< markdown >}}

- [Red-team your RL grader](../../tutorials/reinforcement-learning/grader-red-team/_index): the exploits and
  graders on this page, with results.

{{< /markdown >}}
{{< /variant >}}
