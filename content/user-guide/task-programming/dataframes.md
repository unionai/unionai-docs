---
title: Dataframes
weight: 70
variants: +flyte +serverless +byoc +selfmanaged
---

# Dataframe support

By default, return values in Python are materialized - meaning the actual data is downloaded and stored. This applies to simple types like integers, as well as more complex types like DataFrames.

To avoid having large datasets get downloaded into memory, Flyte V2 exposes [`flyte.io.dataframe`](../../api-reference/flyte-sdk/packages/flyte.io#flyteiodataframe): a thin, uniform wrapper type for dataframe-style objects that allows you to pass a reference to the data, rather than the fully materialized contents.

The `flyte.io.dataframe` type provides serialization support for common engines like `pandas`, `polars`, `pyarrow`, `dask`, etc. 

## Constructing a flyte.io.DataFrame

- Use the `from_df` method to create a `flyte.io.DataFrame` from a native object:

```python
pd_df = pd.DataFrame(BASIC_EMPLOYEE_DATA)
fdf = flyte.io.DataFrame.from_df(pd_df)
```

## How to declare DataFrame inputs and outputs

- To declare a task that returns a native pandas DataFrame, you can use `pd.DataFrame` directly in the signature: the SDK will treat the return as a dataframe-type output and upload it at task completion.

- To use the unified `flyte.io.DataFrame` wrapper (recommended when you want to be explicit about the dataframe type and storage format), use an `Annotated` type where the second argument encodes format or other lightweight hints. 

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

- When a task receives a `flyte.io.DataFrame`, you can open it and request a concrete backend representation. For example, to download as a pandas DataFrame:

```python
downloaded = await flyte_dataframe.open(pd.DataFrame).all()
# or in synchronous contexts: downloaded = flyte_dataframe.open(pd.DataFrame).all()
```

The `open(...)` call delegates to the DataFrame handler for the stored format and converts to the requested in-memory type.

You can also avoid the download step by letting Flyte handle the automatic conversion between types:

```python
@env.task
async def process_dataframe(
    data: pd.DataFrame  # ← Flyte automatically converts flyte.io.DataFrame to pd.DataFrame
) -> pd.DataFrame:
    """
    When you declare the input as pd.DataFrame, Flyte automatically:
    1. Downloads the flyte.io.DataFrame 
    2. Converts it to a pandas DataFrame
    3. Passes it to your function
    """
    # No download step needed - 'data' is already a materialized pd.DataFrame
    return data 

```

## Example — full usage

The following example ([code](https://github.com/flyteorg/flyte-sdk/blob/main/examples/basics/dataframe_usage.py)) demonstrates creating a raw pandas DataFrame, wrapping a pandas DataFrame into `flyte.io.DataFrame`, joining them inside another task, and running locally.

```python
import flyte.io
import pandas as pd
import numpy as np
from typing import Annotated

img = flyte.Image.from_debian_base()
img = img.with_pip_packages("pandas", "pyarrow")

env =flyte.TaskEnvironment(
    name="hello_dataframes",
    image=img,
    resources=flyte.Resources(cpu="1", memory="2Gi"),
)

BASIC_EMPLOYEE_DATA = {
	"employee_id": range(1001, 1009),
	"name": [
		"Alice",
		"Bob",
		"Charlie",
		"Diana",
		"Ethan",
		"Fiona",
		"George",
		"Hannah",
	],
	"department": [
		"HR",
		"Engineering",
		"Engineering",
		"Marketing",
		"Finance",
		"Finance",
		"HR",
		"Engineering",
	],
	"hire_date": pd.to_datetime(
		[
			"2018-01-15",
			"2019-03-22",
			"2020-07-10",
			"2017-11-01",
			"2021-06-05",
			"2018-09-13",
			"2022-01-07",
			"2020-12-30",
		]
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
    """Creates a raw DataFrame with employee data."""
    df = pd.DataFrame(BASIC_EMPLOYEE_DATA)
    return df

@env.task
async def create_flyte_dataframe() -> Annotated [flyte.io.DataFrame, "csv"]:
    """Creates a Flyte DataFrame with additional employee data."""
    pd_df = pd.DataFrame(ADDL_EMPLOYEE_DATA)
    return flyte.io.DataFrame.from_df(pd_df)

@env.task
async def get_employee_data(
    raw_data: pd.DataFrame,      # Automatically materializes pd.DataFrame
    flyte_data: pd.DataFrame     # Automatically materializes flyte.io.DataFrame to pd.DataFrame
) -> pd.DataFrame:
    """
    Demonstrates automatic materialization solving the cumbersome download problem:
    
    MANUAL DOWNLOAD:
    async def get_employee_data(flyte_data: flyte.io.DataFrame) -> pd.DataFrame:
        # Always needs manual download step:
        downloaded_flyte_df = await flyte_data.open(pd.DataFrame).all()
        return downloaded_flyte_df
    
    AUTOMATIC CONVERSION:
    async def get_employee_data(flyte_data: pd.DataFrame) -> pd.DataFrame:
        # No download step needed. Flyte handles it automatically
        return flyte_data
    """
    # No manual download step needed - both inputs are already materialized pd.DataFrames
    joined_df = raw_data.merge(flyte_data, on="employee_id", how="inner")
    return joined_df

if __name__ == "__main__":
    import flyte.git
    flyte.init_from_config(flyte.git.config_from_root())
    
    # Get the data sources first
    raw_run = flyte.with_runcontext(mode="local").run(create_raw_dataframe)
    flyte_run = flyte.with_runcontext(mode="local").run(create_flyte_dataframe)
    
    # Pass both to get_employee_data - Flyte auto-converts flyte.io.DataFrame to pd.DataFrame  
    run = flyte.with_runcontext(mode="local").run(
        get_employee_data, 
        raw_data=raw_run.outputs(), 
        flyte_data=flyte_run.outputs()
    )
    print("Results:", run.outputs())
```



