---
title: Time series
icon: graph-up
description: Forecasting, backtesting, anomaly detection, and capacity planning with time-series foundation models.
weight: 12
variants: +flyte +union
sidebar_expanded: true
---

# Time series

Tutorials for forecasting and monitoring time series with [Timestral](https://github.com/mistralai/timestral), Mistral AI's family of time-series foundation models.

Timestral forecasts any series zero-shot, with no training on your data. It reads up to 32,768 steps of history, forecasts several variates jointly, and conditions on covariates: past-only, known-future, and categorical. Every forecast is probabilistic, with 21 quantile levels from 0.01 to 0.99. The four checkpoints share one architecture and differ only in size:

| Checkpoint | Hugging Face repo | Weights |
| --- | --- | --- |
| Timestral-5M | `mistralai/Timestral-5M` | 21 MB |
| Timestral-28M | `mistralai/Timestral-28M` | 111 MB |
| Timestral-123M | `mistralai/Timestral-123M` | 490 MB |
| Timestral-209M | `mistralai/Timestral-209M` | 837 MB |

All four run on CPU, so the tutorials scale out across CPU tasks and app replicas instead of GPUs.

{{< grid >}}

{{< link-card target="batch-forecasting" icon="collection" title="Batch forecasting and backtesting" >}}
Backtest every Timestral checkpoint on 321 electricity customers, pick the most accurate one, and forecast every series with it.
{{< /link-card >}}

{{< link-card target="forecast-api" icon="lightning-charge" title="Online forecasting API" >}}
Serve Timestral as an autoscaling FastAPI app that batches concurrent requests into shared forward passes.
{{< /link-card >}}

{{< link-card target="anomaly-monitoring" icon="activity" title="Anomaly monitoring" >}}
Flag pump sensors that leave their forecast band, in a durable monitoring loop that survives crashes and pauses for a human decision.
{{< /link-card >}}

{{< link-card target="capacity-planning" icon="thermometer-sun" title="Capacity planning with covariates" >}}
Forecast Texas grid demand with temperature and calendar covariates, plan capacity under weather scenarios, and gate the plan on approval.
{{< /link-card >}}

{{< /grid >}}

## Setup

The code for all four tutorials is in one directory and shares a `common.py` module with the container image, model loading, and metrics.

```bash
git clone https://github.com/unionai/unionai-examples
cd unionai-examples/v2/tutorials/timestral
pip install "flyte>=2.12.0" fastapi uvicorn
flyte create config --endpoint <your-endpoint> --project <your-project> --domain development --builder remote
```

Replace `<your-endpoint>` with your {{< key product_name >}} endpoint. The remote image builder builds the images on the cluster, so you don't need Docker locally.

## The container image

Timestral isn't on PyPI, so the image installs it from GitHub, pinned to a commit so every task and every replica loads the same code. A CPU build of PyTorch keeps the image small.

{{< code file="/unionai-examples/v2/tutorials/timestral/common.py" fragment=image lang=python >}}

## Loading a checkpoint

`load_forecaster` loads each checkpoint once per process. Within a task, every forecast reuses the loaded model. In an app, every request on a replica reuses it.

{{< code file="/unionai-examples/v2/tutorials/timestral/common.py" fragment=load_forecaster lang=python >}}

A forecast takes a context array shaped `(series, variates, time)`, or `(series, time)` for one variate. NaN marks a missing value. The result holds a quantile tensor shaped `(series, variates, horizon, 21)`:

```python
forecaster = load_forecaster("mistralai/Timestral-28M")
forecast = forecaster.forecast(context, prediction_length=168)
forecast.quantiles  # (series, variates, 168, 21)
forecast.median     # (series, variates, 168)
```

## Measuring accuracy

The tutorials score forecasts with two metrics from the GIFT-Eval benchmark. **MASE** compares the median forecast's error to a seasonal-naive forecast, so a value below 1.0 beats "same as last season". **WQL**, weighted quantile loss, scores all 21 quantiles, so it rewards well-calibrated uncertainty as well as an accurate median.

{{< code file="/unionai-examples/v2/tutorials/timestral/common.py" fragment=metrics lang=python >}}

## Durability in these tutorials

Each tutorial uses {{< key product_name >}} features that keep a forecasting workload correct when something fails. Some protect the logic of a run, so work is never repeated or lost. Others protect the infrastructure, so a failed node or a traffic spike doesn't take the workload down.

| Feature | What it protects | Tutorial |
| --- | --- | --- |
| Task caching | A re-run skips every shard, download, and API call that already finished. | Batch, capacity planning |
| Intra-task checkpoints | A preempted task resumes from its last completed backtest window. | Batch |
| Retries on spot capacity | Preemptions and transient failures are retried, with backoff for rate-limited APIs. | Batch, capacity planning |
| Traces and durable sleep | A crashed loop replays completed steps from the record, without re-reading, re-forecasting, or re-alerting. | Anomaly monitoring |
| External conditions | A run pauses for a typed human decision, with a timeout and a default. | Anomaly monitoring, capacity planning |
| Triggers | A deployed task runs on a schedule. | Anomaly monitoring |
| App scaling and run outputs | A warm, autoscaling API serves the model a pipeline selected. | Online API |
