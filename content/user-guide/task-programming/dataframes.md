---
title: Dataframes
weight: 70
variants: +flyte +serverless +byoc +selfmanaged
---

# Dataframe support

By default, return values from tasks are materialized - meaning the actual data is downloaded and stored. This applies to simple types like integers, as well as more complex types like DataFrames.

To avoid having large datasets get downloaded into memory, Union V2 exposes [`flyte.io.dataframe`](../../api-reference/flyte-sdk/packages/flyte.io#flyteiodataframe); a thin, uniform wrapper type for dataframe-style objects that allows you to pass a reference to the data, rather than the full materialized data.

The `flyte.io.dataframe` type provides full serialization support for common engines like `pandas`, `polars`, `pyarrow`, etc. 

## Constructing a flyte.io.DataFrame

- Use the `from_df` factory to create a `flyte.io.DataFrame` from a native object:

```python
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

When a task returns a native pandas DataFrame (or a `flyte.io.DataFrame` created via `from_df`), Flyte serializes the object and uploads it to blob storage at task exit.


## Example — full usage

The following example (adapted from upstream SDK examples) demonstrates creating a raw pandas DataFrame, wrapping a pandas DataFrame into `flyte.io.DataFrame`, joining them inside another task, and running locally.

```python
from typing import Annotated

import numpy as np
import pandas as pd

import flyte
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
	"""
	Create a raw pandas DataFrame and return it. The SDK will serialize and upload
	the dataframe (parquet/pyarrow for pandas) when the task completes.
	"""
	return pd.DataFrame(BASIC_EMPLOYEE_DATA)


@env.task
async def create_flyte_dataframe() -> Annotated[flyte.io.DataFrame, "csv"]:
	"""
	Create a Flyte DataFrame wrapper from a pandas DataFrame. The annotated
	format string is where type-level format hints live; the wrapper itself is
	created with `from_df`.
	"""
	pd_df = pd.DataFrame(ADDL_EMPLOYEE_DATA)
	fdf = flyte.io.DataFrame.from_df(pd_df)
	return fdf


@env.task
async def get_employee_data() -> pd.DataFrame:
	raw_dataframe = await create_raw_dataframe()
	flyte_dataframe = await create_flyte_dataframe()

	# Download the stored flyte dataframe into a pandas DataFrame
	downloaded_fdf = await flyte_dataframe.open(pd.DataFrame).all()

	joined_df = raw_dataframe.merge(downloaded_fdf, on="employee_id", how="inner")
	return joined_df


if __name__ == "__main__":
	# Run locally with runcontext
	flyte.init()
	run = flyte.with_runcontext(mode="local").run(get_employee_data)
	print("Results:", run.outputs())
```



