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

To run one, clone [unionai-examples](https://github.com/unionai/unionai-examples) and run its `main.py` from the
tutorial's directory under `v2/tutorials/`. A cluster run connects to the cluster in your
[Flyte configuration file](../../user-guide/get-started/run-modes/running-remote#configuration-file); each
tutorial's "Run it" section also shows a local run.

{{< grid >}}

{{< link-card target="validation-overhead" icon="stopwatch" title="Per-batch validation overhead" >}}
Measure how much wall-clock time pandera adds to a training loop when it validates every TensorDict batch and skips the ones that fail.
{{< /link-card >}}

{{< link-card target="whole-dataset-validation" icon="database-check" title="Whole-dataset validation" >}}
Measure how pandera validation time grows with dataset size when you validate a whole TensorDict dataset once, where it's produced.
{{< /link-card >}}

{{< link-card target="cost-of-not-validating" icon="exclamation-triangle" title="The cost of not validating" >}}
Measure what happens to training when corrupt batches reach the model, compared with a loop that validates every batch with pandera.
{{< /link-card >}}

{{< /grid >}}
