---
title: DataFrames
weight: 80
variants: +flyte +serverless +byoc +selfmanaged
---

# DataFrames

By default, return values in Python are materialized - meaning the actual data is downloaded and loaded into memory. This applies to simple types like integers, as well as more complex types like DataFrames.

To avoid downloading large datasets into memory, Flyte V2 exposes [`flyte.io.dataframe`](../../api-reference/flyte-sdk/packages/flyte.io#flyteiodataframe): a thin,  uniform wrapper type for DataFrame-style objects that allows you to pass a reference to the data, rather than the fully materialized contents.

The `flyte.io.DataFrame` type provides serialization support for common engines like `pandas`, `polars`, `pyarrow`, `dask`, etc.; enabling you to move data between different DataFrame backends. 

## Constructing a flyte.io.DataFrame

- Use the `from_df` method to create a `flyte.io.DataFrame` from a native object:

```python
@env.task
async def create_flyte_dataframe() -> Annotated[flyte.io.DataFrame, "csv"]:
    pd_df = pd.DataFrame(ADDL_EMPLOYEE_DATA)
    fdf = flyte.io.DataFrame.from_df(pd_df) 
    return fdf
```

## Declaring DataFrame inputs and outputs

To declare a task that returns a native pandas DataFrame, you can use `pd.DataFrame` directly in the signature, the SDK will treat the return as a DataFrame-type output and upload it at task completion.

```python
@env.task
async def create_raw_dataframe() -> pd.DataFrame:
```

To use the unified `flyte.io.DataFrame` wrapper (recommended when you want to be explicit about the DataFrame type and storage format), use an `Annotated` type where the second argument encodes format or other lightweight hints.

## Example

```python
from typing import Annotated
import pandas as pd
import flyte.io

def my_task() -> Annotated[flyte.io.DataFrame, "parquet"]:
	# create a pandas DataFrame and convert it to a flyte DataFrame
	df = pd.DataFrame(...)
	return flyte.io.DataFrame.from_df(df)
```

## Reading a DataFrame value inside a task

When a task receives a `flyte.io.DataFrame`, you can open it and request a concrete backend representation. For example, to download as a pandas DataFrame:

```python
# Download all data at once
downloaded = await flyte_dataframe.open(pd.DataFrame).all()
# or in synchronous contexts: downloaded = flyte_dataframe.open(pd.DataFrame).all()
```

The `open(...)` call delegates to the DataFrame handler for the stored format and converts to the requested in-memory type.

You can also leverage Flyte to automatically download and convert the dataframe between types when needed:


```python
@env.task
async def get_employee_data(raw_dataframe: pd.DataFrame, flyte_dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    This task takes two dataframes as input. We'll pass one raw pandas dataframe, and one flyte.io.DataFrame.
    Flyte automatically converts the flyte.io.DataFrame to a pandas DataFrame. The actual download and conversion 
    happens only when we access the data (in this case, when we do the merge)."""
    joined_df = raw_dataframe.merge(flyte_dataframe, on="employee_id", how="inner")

    return joined_df

```

## Example — full usage

The following example ([code](https://github.com/flyteorg/flyte-sdk/blob/main/examples/basics/dataframe_usage.py)) demonstrates creating a raw pandas DataFrame, wrapping a pandas DataFrame into `flyte.io.DataFrame`, joining them inside another task, and running locally.

```python
from typing import Annotated

import numpy as np
import pandas as pd

import flyte.io

# Create task environment with required dependencies
img = flyte.Image.from_debian_base()
img = img.with_pip_packages("pandas", "pyarrow")

env = flyte.TaskEnvironment(
    "dataframe_usage",
    image=img,
    resources=flyte.Resources(cpu="1", memory="2Gi"),
)

BASIC_EMPLOYEE_DATA = {
    "employee_id": range(1001, 1009),
    "name": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah"],
    "department": ["HR", "Engineering", "Engineering", "Marketing", "Finance", "Finance", "HR", "Engineering"],
    "hire_date": pd.to_datetime(
        ["2018-01-15", "2019-03-22", "2020-07-10", "2017-11-01", "2021-06-05", "2018-09-13", "2022-01-07", "2020-12-30"]
    ),
}

ADDL_EMPLOYEE_DATA = {
    "employee_id": range(1001, 1009),
    "salary": [55000, 75000, 72000, 50000, 68000, 70000, np.nan, 80000],
    "bonus_pct": [0.05, 0.10, 0.07, 0.04, np.nan, 0.08, 0.03, 0.09],
    "full_time": [True, True, True, False, True, True, False, True],
    "projects": [
        ["Recruiting", "Onboarding"],
        ["Platform", "API"],
        ["API", "Data Pipeline"],
        ["SEO", "Ads"],
        ["Budget", "Forecasting"],
        ["Auditing"],
        [],
        ["Platform", "Security", "Data Pipeline"],
    ],
}


@env.task
async def create_raw_dataframe() -> pd.DataFrame:
    """
    This task creates a raw pandas DataFrame with basic employee information.
    This is the most basic use-case of how to pass dataframes (of all kinds, not just pandas). Create the dataframe
    as normal, and return it. Note that the output signature is of the dataframe library type.
    Uploading of the actual bits of the dataframe (which for pandas is serialized to parquet) happens at the
    end of the task, the TypeEngine uploads from memory to blob store.
    """
    return pd.DataFrame(BASIC_EMPLOYEE_DATA)


@env.task
async def create_flyte_dataframe() -> Annotated[flyte.io.DataFrame, "csv"]:
    """
    This task creates a Flyte DataFrame with compensation and project data.
    Because there's no generic type in Python that means any dataframe type, Flyte ships with its own. The
    flyte.io.DataFrame class is a thin wrapper around the various dataframe libraries (pandas, pyarrow, dask, etc).
    """
    pd_df = pd.DataFrame(ADDL_EMPLOYEE_DATA)

    fdf = flyte.io.DataFrame.from_df(pd_df)
    return fdf


@env.task
async def get_employee_data(raw_dataframe: pd.DataFrame, flyte_dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    This task takes two dataframes as input. We'll pass one raw pandas dataframe, and one flyte.io.DataFrame.
    Flyte automatically converts the flyte.io.DataFrame to a pandas DataFrame. The actual download and conversion 
    happens only when we access the data (in this case, when we do the merge)."""
    joined_df = raw_dataframe.merge(flyte_dataframe, on="employee_id", how="inner")

    return joined_df


if __name__ == "__main__":
    import flyte.git
    flyte.init_from_config(flyte.git.config_from_root())
    # Get the data sources
    
    raw_df = flyte.with_runcontext(mode="local").run(create_raw_dataframe)
    flyte_df = flyte.with_runcontext(mode="local").run(create_flyte_dataframe)

    # Pass both to get_employee_data - Flyte auto-converts flyte.io.DataFrame to pd.DataFrame
    run = flyte.with_runcontext(mode="local").run(
        get_employee_data,
        raw_dataframe=raw_df.outputs(),
        flyte_dataframe=flyte_df.outputs(), 
    )
    print("Results:", run.outputs())
```