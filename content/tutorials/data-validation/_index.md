---
title: Data validation
icon: shield-check
description: Benchmarks that measure the cost of validating training data with pandera, and the cost of not validating it.
weight: 12
variants: +flyte +union
sidebar_expanded: true
---

# Data validation

Tutorials that validate training data with [pandera](https://pandera.readthedocs.io) and measure what it costs.
Each one is a benchmark you can run on your own cluster, and each pairs a validated mode with an unvalidated one
on the same data, so the difference between them is the thing being measured.

{{< grid >}}

{{< link-card target="validation-overhead" icon="stopwatch" title="Per-batch validation overhead" >}}
How much wall-clock time pandera adds to a training loop when it validates every `TensorDict` batch.
{{< /link-card >}}

{{< link-card target="whole-dataset-validation" icon="database-check" title="Whole-dataset validation" >}}
How validation time grows with dataset size when you validate a dataset once, where it's produced.
{{< /link-card >}}

{{< link-card target="cost-of-not-validating" icon="exclamation-triangle" title="The cost of not validating" >}}
What happens to training when corrupt batches reach the model, in environment steps to solve CartPole.
{{< /link-card >}}

{{< /grid >}}
