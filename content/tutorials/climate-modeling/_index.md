---
title: GPU-accelerated climate modeling
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# GPU-accelerated climate modeling

Climate modeling is hard for two reasons: data and compute. Satellite imagery arrives continuously from multiple sources. Reanalysis datasets have to be pulled from remote APIs. Weather station data shows up in different formats and schemas. And once all of that is finally in one place, running atmospheric physics simulations demands serious GPU compute.

In practice, many climate workflows are held together with scripts, cron jobs, and a lot of manual babysitting. Data ingestion breaks without warning. GPU jobs run overnight with little visibility into what's happening. When something interesting shows up in a simulation, like a developing hurricane, no one notices until the job finishes hours later.

In this tutorial, we build a production-grade climate modeling pipeline using Flyte. We ingest data from three different sources in parallel, combine it with Dask, run ensemble atmospheric simulations on H200 GPUs, detect extreme weather events as they emerge, and visualize everything in a live dashboard. The entire pipeline is orchestrated, cached, and fault-tolerant, so it can run reliably at scale.

![Report](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/tutorials/climate-modeling/report.png)

> [!NOTE]
> Full code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/climate_modeling/simulation.py).

## Overview

We're building an ensemble weather forecasting system. Ensemble forecasting runs the same simulation multiple times with slightly different initial conditions. This quantifies forecast uncertainty. Instead of saying "the temperature will be 25°C", we can say "the temperature will be 24-26°C with 90% confidence".

The pipeline has five stages:

1. **Data ingestion**: Pull satellite imagery from NOAA GOES, reanalysis data from ERA5, and surface observations from weather stations in parallel.
2. **Preprocessing**: Fuse the datasets, interpolate to a common grid, and run quality control using Dask for distributed computation.
3. **GPU simulation**: Run ensemble atmospheric physics on H200 GPUs. Each ensemble member evolves independently. PyTorch handles the tensor operations; `torch.compile` optimizes the kernels.
4. **Event detection**: Monitor for hurricanes (high wind + low pressure) and heatwaves during simulation. When extreme events are detected, the pipeline can adaptively refine the grid resolution.
5. **Real-time reporting**: Stream metrics to a live Flyte Reports dashboard showing convergence and detected events.

This workflow is a good example of where Flyte shines!

- **Parallel data ingestion**: Three different data sources, three different APIs, all running concurrently. Flyte's async task execution handles this naturally.
- **Resource heterogeneity**: Data ingestion needs CPU and network. Preprocessing needs a Dask cluster. Simulation needs GPUs. Flyte provisions exactly what each stage needs.
- **Caching**: ERA5 data fetches can take minutes. Run the pipeline twice with the same date range, and Flyte skips the fetch entirely.
- **Adaptive workflows**: When a hurricane is detected, we can dynamically refine the simulation. Flyte makes this kind of conditional logic straightforward.

## Implementation

### Dependencies and container image

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="imports" lang="python" >}}

The key imports include `xarray` for multi-dimensional climate data, `flyteplugins.dask` for distributed preprocessing, and `flyte` for orchestration.

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="image" lang="python" >}}

Climate data comes in specialized formats such as NetCDF, HDF5, and GRIB. The container image includes libraries to work with all of them, along with PyTorch for GPU computation and the ECMWF client for accessing ERA5 data.

### Simulation parameters and data structures

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="dataclasses" lang="python" >}}

`SimulationParams` defines the core behavior of the simulation, including grid resolution, physics schemes, and ensemble size. The default configuration runs 800 ensemble members, which is sufficient to produce statistically meaningful uncertainty estimates.

> [!NOTE]
> Decreasing the grid spacing via `grid_resolution_km` (for example, from 10 km to 5 km) increases grid resolution and significantly increases memory usage because it introduces more data points and intermediate state. Even with 141 GB of H200 GPU memory, high-resolution or adaptively refined simulations may exceed available VRAM, especially when running large ensembles.
>
> To mitigate this, consider reducing the ensemble size, limiting the refined region, running fewer physics variables, or scaling the simulation across more GPUs so memory is distributed more evenly.

`ClimateMetrics` collects diagnostics at each iteration, such as convergence rate, energy conservation, and detected phenomena. These metrics are streamed to the real-time dashboard so you can monitor how the simulation evolves as it runs.

### Task environments

Different stages need different resources. Flyte's `TaskEnvironment` declares exactly what each task requires:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="task-envs" lang="python" >}}

Here’s what each environment is responsible for:

- **`gpu_env`**: Runs the atmospheric simulations on H200 GPUs. The 130 GB of GPU memory is used to hold the ensemble members in VRAM during execution.
- **`dask_env`**: Provides a distributed Dask cluster for preprocessing. A scheduler and multiple workers handle data fusion and transformation in parallel.
- **`cpu_env`**: Handles data ingestion and orchestration. This environment also includes the secrets required to access the ERA5 API.

The `depends_on` setting on `cpu_env` ensures that Flyte builds the GPU and Dask images first. Once those environments are ready, the orchestration task can launch the specialized simulation and preprocessing tasks.

### Data ingestion: multiple sources in parallel

Climate models need data from multiple sources. Each source has different formats, APIs, and failure modes. We handle them as separate Flyte tasks that run concurrently.

**Satellite imagery from NOAA GOES**

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="ingest-satellite" lang="python" >}}

This task fetches cloud imagery and precipitable water products from NOAA's public S3 buckets. GOES-16 covers the Atlantic; GOES-17 covers the Pacific. The task selects the appropriate satellite based on region, fetches multiple days in parallel using `asyncio.gather`, and combines everything into a single xarray Dataset.

**ERA5 reanalysis from Copernicus**

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="ingest-reanalysis" lang="python" >}}

ERA5 provides 3D atmospheric fields such as temperature, wind, humidity at multiple pressure levels from surface to stratosphere. The ECMWF datastores client handles authentication via Flyte secrets. Each day fetches in parallel, then gets concatenated.

**Surface observations from weather stations:**

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="ingest-station" lang="python" >}}

Ground truth comes from NOAA's Integrated Surface Database. The task filters stations by geographic bounds, fetches hourly observations, and returns a Parquet file for efficient downstream processing.

All three tasks return Flyte `File` objects that hold references to data in blob storage. No data moves until a downstream task actually needs it.

### Preprocessing with Dask

The three data sources need to be combined into a unified atmospheric state. This means:
- Interpolating to a common grid
- Handling missing values
- Merging variables from different sources
- Quality control

This is a perfect fit for Dask to handle lazy evaluation over chunked arrays:

```python
@dask_env.task
async def preprocess_atmospheric_data(
    satellite_data: File,
    reanalysis_data: File,
    station_data: File,
    target_resolution_km: float,
) -> File:
```

This task connects to the Dask cluster provisioned by Flyte, loads the datasets with appropriate chunking, merges satellite and reanalysis grids, fills in missing values, and persists the result. Flyte caches the output, so preprocessing only runs when the inputs change.

### GPU-accelerated atmospheric simulation

Now the core: running atmospheric physics on the GPU. Each ensemble member is an independent forecast with slightly perturbed initial conditions.

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="gpu-simulation-signature" lang="python" >}}

The task accepts a subset of ensemble members (`ensemble_start` to `ensemble_end`). This enables distributing 800 members across multiple GPUs.

The physics step is the computational kernel. It runs advection (wind transport), pressure gradients, Coriolis forces, turbulent diffusion, and moisture condensation:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="physics-step" lang="python" >}}

`@torch.compile(mode="reduce-overhead")` compiles this function into optimized CUDA kernels. Combined with mixed precision (`torch.cuda.amp.autocast`), this runs 3-4x faster than eager PyTorch.

Every 10 timesteps, the simulation checks for extreme events:
- **Hurricanes**: Wind speed > 33 m/s with low pressure
- **Heatwaves**: Temperature anomalies exceeding thresholds

Detected phenomena get logged to the metrics, which flow to the live dashboard.

### Distributing across multiple GPUs

800 ensemble members is a lot for one GPU, so we distribute them:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="distributed-ensemble" lang="python" >}}

The task splits the ensemble members evenly across the available GPUs, launches the simulation runs in parallel using `asyncio.gather`, and then aggregates the results. With five GPUs, each GPU runs 160 ensemble members. Flyte takes care of scheduling, so GPU tasks start automatically as soon as resources become available.

### The main workflow

Everything comes together in the orchestration task:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="main-workflow" lang="python" >}}

`report=True` enables Flyte Reports for live monitoring.

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="workflow-ingestion" lang="python" >}}

`flyte.group("data-ingestion")` visually groups the ingestion tasks in the Flyte UI. Inside the group, three tasks launch concurrently. `asyncio.gather` waits for all three to complete before preprocessing begins.

The workflow then enters an iterative loop:
1. Run GPU simulation (single or multi-GPU)
2. Check convergence by comparing forecasts across iterations
3. Detect extreme events
4. If a hurricane is detected and we haven't refined yet, double the grid resolution
5. Stream metrics to the live dashboard
6. Repeat until converged or max iterations reached

Adaptive mesh refinement is the key feature here. When the simulation detects a hurricane forming, it automatically increases resolution to capture the fine-scale dynamics. This is expensive, so we limit it to one refinement per run.

### Running the pipeline

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="main" lang="python" >}}

Before running, set up ERA5 API credentials:

```bash
flyte create secret cds_api_key <YOUR_CDS_API_KEY>
flyte create secret cds_api_url https://cds.climate.copernicus.eu/api
```

Then launch:

```bash
flyte create config --endpoint <FLYTE_OR_UNION_ENDPOINT> --project <PROJECT_NAME> --domain <DOMAIN_NAME> --builder remote
uv run simulation.py
```

The default configuration uses the Atlantic region for September 2024, which is hurricane season.

## Key concepts

### Ensemble forecasting

Weather prediction is inherently uncertain. Small errors in the initial conditions grow over time due to chaotic dynamics, which means a single forecast can only ever be one possible outcome.

Ensemble forecasting addresses this uncertainty by:
- Perturbing the initial conditions within known observational error bounds
- Running many independent forecasts
- Computing the ensemble mean as the most likely outcome and the ensemble spread as a measure of uncertainty

### Adaptive mesh refinement

When a hurricane begins to form, coarse spatial grids are not sufficient to resolve critical features like eyewall dynamics. Adaptive mesh refinement allows the simulation to focus compute where it matters most by:
- Increasing grid resolution, for example from 10 km to 5 km
- Reducing the timestep to maintain numerical stability
- Refining only the regions of interest instead of the entire domain

This approach is computationally expensive, but it is essential for producing accurate intensity forecasts.

### Real-time event detection

Rather than analyzing results after a simulation completes, this pipeline detects significant events as the simulation runs.

The system monitors for conditions such as:
- **Hurricanes**: Wind speeds exceeding 33 m/s (Category 1 threshold) combined with central pressure below 980 mb
- **Heatwaves**: Sustained temperature anomalies over a defined period

Detecting these events in real time enables adaptive responses, such as refining the simulation or triggering alerts, and supports earlier warnings for extreme weather.

## Where to go next

This example is intentionally scoped to keep the ideas clear, but there are several natural ways to extend it for more realistic workloads.

To model different ocean basins, change the `region` parameter to values like `"pacific"` or `"indian"`. The ingestion tasks automatically adjust to pull the appropriate satellite coverage for each region.

To run longer forecasts, increase `simulation_hours` in `SimulationParams`. The default of 240 hours, or 10 days, is typical for medium-range forecasting, but you can run longer simulations if you have the compute budget.

Finally, the physics step here is deliberately simplified. Production systems usually incorporate additional components such as radiation schemes, boundary layer parameterizations, and land surface models. These can be added incrementally as separate steps without changing the overall structure of the pipeline.

