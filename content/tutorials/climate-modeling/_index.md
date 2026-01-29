---
title: GPU-accelerated climate modeling
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# GPU-accelerated climate modeling

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/v2/tutorials/climate_modeling/simulation.py).

This tutorial demonstrates how to build a GPU-accelerated climate modeling workflow using Flyte. You'll learn how to ingest multi-source atmospheric data, run ensemble simulations on H200 GPUs, detect extreme weather events, and visualize results in real-time.

## Use case

In this tutorial, you'll learn how to:

- Ingest data from multiple sources: GOES satellites, ERA5 reanalysis, and weather stations
- Preprocess atmospheric data using Dask for scalable computation
- Run ensemble forecasts on H200 GPUs with PyTorch
- Detect hurricanes and heatwaves in real-time
- Visualize simulation progress with live Flyte Reports

## Why Flyte for climate modeling?

Climate modeling presents unique computational challenges:

1. **Multi-source data**: Satellite imagery, reanalysis products, and station observations must be combined and harmonized.

2. **Massive compute**: Atmospheric simulations require GPU acceleration for physics calculations across millions of grid points.

3. **Ensemble forecasting**: Running hundreds of ensemble members in parallel requires orchestration across multiple GPUs.

4. **Real-time monitoring**: Long-running simulations need live dashboards for convergence tracking and event detection.

5. **Adaptive workflows**: Simulations may need to refine resolution or adjust parameters based on detected phenomena.

## Architecture overview

The climate modeling pipeline consists of five main stages:

1. **Data ingestion**: Parallel ingestion from GOES satellites, ERA5 reanalysis, and NOAA weather stations
2. **Preprocessing**: Data fusion and quality control using Dask
3. **GPU simulation**: Ensemble atmospheric physics on H200 GPUs
4. **Analytics**: Real-time convergence monitoring and extreme event detection
5. **Adaptive refinement**: Dynamic mesh refinement based on detected phenomena

## Define dependencies and imports

Start by importing the necessary modules:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="imports" lang="python" >}}

Key imports include:
- `flyte` for orchestration
- `xarray` for handling multi-dimensional climate data
- `flyteplugins.dask` for distributed preprocessing

## Define data structures

Create dataclasses to organize simulation parameters and results:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="dataclasses" lang="python" >}}

These structures define:
- **SimulationParams**: Grid resolution, physics schemes, ensemble size, and convergence criteria
- **ClimateMetrics**: Per-iteration metrics including wind speed, pressure, and detected phenomena
- **SimulationSummary**: Final summary with total events and convergence status

## Build the container image

Create a specialized image for climate modeling:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="image" lang="python" >}}

The image includes:
- NetCDF and HDF5 libraries for climate data formats
- ECMWF tools for GRIB format support
- xarray and Dask for scalable data processing
- PyTorch for GPU-accelerated physics

## Configure task environments

Define specialized environments for different computational needs:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="task-envs" lang="python" >}}

Three environments handle different workloads:

1. **`gpu_env`**: H200 GPU for atmospheric simulation
2. **`dask_env`**: Distributed cluster for preprocessing (scheduler + workers)
3. **`cpu_env`**: Data ingestion and orchestration, with secrets for ERA5 API access

## Ingest satellite data

Fetch GOES satellite imagery from NOAA's public S3 buckets:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="ingest-satellite" lang="python" >}}

This task:
- Selects GOES-East or GOES-West based on region
- Fetches cloud imagery and precipitable water products
- Applies geographic filtering to the requested region
- Combines multiple days into a single dataset

## Ingest reanalysis data

Fetch ERA5 reanalysis from the Copernicus Climate Data Store:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="ingest-reanalysis" lang="python" >}}

ERA5 provides:
- 3D atmospheric fields (temperature, wind, humidity)
- Multiple pressure levels from surface to stratosphere
- Consistent global coverage at ~30km resolution

## Ingest weather station data

Fetch ground observations from NOAA's Integrated Surface Database:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="ingest-station" lang="python" >}}

Station data provides:
- Real-time surface observations
- Temperature, pressure, wind, and visibility
- Ground truth for model validation

## Preprocess atmospheric data

Combine and quality-control data using Dask:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="preprocess" lang="python" >}}

Preprocessing includes:
- Merging satellite and reanalysis datasets
- Interpolating to common grids
- Filling missing values
- Adding station metadata

## Run GPU-accelerated simulation

Execute ensemble atmospheric physics on H200 GPUs:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="gpu-simulation" lang="python" >}}

The GPU simulation:
- Generates ensemble members with perturbed initial conditions
- Runs atmospheric physics (advection, pressure gradients, condensation)
- Uses `torch.compile` for optimized kernel execution
- Detects extreme events during simulation
- Returns ensemble mean, spread, and detected phenomena

## Distribute across multiple GPUs

Scale ensemble forecasts across multiple GPUs:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="distributed-ensemble" lang="python" >}}

This task:
- Distributes ensemble members evenly across GPUs
- Launches parallel tasks with `asyncio.gather`
- Aggregates results from all GPUs

## Real-time analytics

Monitor convergence and detect extreme events:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="analytics" lang="python" >}}

Analytics functions:
- **analyze_simulation_convergence**: Check if ensemble spread has stabilized
- **detect_extreme_events**: Identify hurricanes (high winds + low pressure) and heatwaves
- **recommend_parameter_adjustments**: Suggest timestep or resolution adjustments

## Orchestrate the adaptive workflow

The main workflow coordinates all stages with real-time reporting:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="main-workflow" lang="python" >}}

The workflow:
1. **Ingests data in parallel** from satellites, reanalysis, and stations
2. **Preprocesses** the combined atmospheric state
3. **Runs iterative simulation** with convergence checking
4. **Detects extreme events** and refines mesh if needed
5. **Streams updates** to a live dashboard

Key features:
- `flyte.group()` for visual organization in the UI
- Real-time Flyte Reports with HTML/JavaScript dashboards
- Adaptive mesh refinement when hurricanes are detected
- Early stopping when convergence is achieved

## Run the simulation

Execute the workflow:

{{< code file="/external/unionai-examples/v2/tutorials/climate_modeling/simulation.py" fragment="main" lang="python" >}}

Before running, set up your ECMWF API credentials:

```bash
flyte create secret cds_api_key <YOUR_CDS_API_KEY>
flyte create secret cds_api_url https://cds.climate.copernicus.eu/api
```

Then run the simulation:

```bash
flyte create config --endpoint <FLYTE_OR_UNION_ENDPOINT> --project <PROJECT_NAME> --domain <DOMAIN_NAME> --builder remote
uv run simulation.py
```

## Key features

### Ensemble forecasting

Ensemble methods quantify forecast uncertainty by:
- Perturbing initial conditions within observational error bounds
- Running multiple independent forecasts
- Computing ensemble mean (most likely outcome) and spread (uncertainty)

### Extreme event detection

The simulation monitors for:
- **Hurricanes**: Wind speed > 33 m/s with pressure < 980 mb
- **Heatwaves**: Temperature anomalies exceeding thresholds

### Adaptive mesh refinement

When extreme events are detected:
- Grid resolution doubles (e.g., 10 km → 5 km)
- Timestep reduces for numerical stability
- Ensemble size adjusts for computational efficiency

### Real-time reporting

Flyte Reports provide:
- Live convergence tracking
- Extreme event timeline
- Per-GPU performance metrics
- Interactive parameter display

## Next steps

- Add sophisticated physics (radiation, boundary layer schemes)
- Integrate ML surrogates for accelerated simulation
- Add post-processing for forecast products (precipitation, wind gusts)
- Implement data assimilation for improved initial conditions
