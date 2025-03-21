---
title: Snowflake agent example
weight: 1
variants: +flyte -serverless +byoc +byok
---

# Snowflake agent example

```python
# %% [markdown]
# (snowflake_agent_example_usage)=
# # Querying data in Snowflake
#
# This example shows how to use the `SnowflakeTask` to execute a query in Snowflake.
#
# %%
import pandas as pd
import {{< key kit_import >}}
from flytekit import kwtypes
from flytekitplugins.snowflake import SnowflakeConfig, SnowflakeTask

image = {{< key kit_as >}}.ImageSpec(
    packages=["flytekitplugins-snowflake", "pandas", "pyarrow"],
    registry="ghcr.io/flyteorg",
)

"""
Define a Snowflake task to insert data into the FLYTEAGENT.PUBLIC.TEST table.
The `inputs` parameter specifies the types of the inputs using `kwtypes`.
The `query_template` uses Python string interpolation to insert these inputs into the SQL query.
The placeholders `%(id)s`, `%(name)s`, and `%(age)s` will be replaced by the actual values
provided when the task is executed.
"""

"""
You can get the SnowflakeConfig's metadata from the Snowflake console by executing the following query:

SELECT
    CURRENT_USER() AS "User",
    CONCAT(CURRENT_ORGANIZATION_NAME(), '-', CURRENT_ACCOUNT_NAME()) AS "Account",
    CURRENT_DATABASE() AS "Database",
    CURRENT_SCHEMA() AS "Schema",
    CURRENT_WAREHOUSE() AS "Warehouse";
"""

snowflake_task_insert_query = SnowflakeTask(
    name="insert-query",
    inputs=kwtypes(id=int, name=str, age=int),
    task_config=SnowflakeConfig(
        user="FLYTE",
        account="FLYTE_SNOFLAKE_ACCOUNT",
        database="FLYTEAGENT",
        schema="PUBLIC",
        warehouse="COMPUTE_WH",
    ),
    query_template="""
            INSERT INTO FLYTEAGENT.PUBLIC.TEST (ID, NAME, AGE)
            VALUES (%(id)s, %(name)s, %(age)s);
            """,
)

snowflake_task_templatized_query = SnowflakeTask(
    name="select-query",
    output_schema_type=StructuredDataset,
    task_config=SnowflakeConfig(
        user="FLYTE",
        account="FLYTE_SNOFLAKE_ACCOUNT",
        database="FLYTEAGENT",
        schema="PUBLIC",
        warehouse="COMPUTE_WH",
    ),
    query_template="SELECT * FROM FLYTEAGENT.PUBLIC.TEST ORDER BY ID DESC LIMIT 3;",
)


@{{< key kit_as >}}.task(
    container_image=image,
    secret_requests=[
        Secret(
            group="private-key",
            key="snowflake",
        )
    ],
)
def print_head(input_sd: {{< key kit_as >}}.StructuredDataset) -> pd.DataFrame:
    # Download the DataFrame from the Snowflake table via StructuredDataset
    # We don't have to provide the uri here because the input_sd already has the uri
    df = input_sd.open(pd.DataFrame).all()
    print(df)
    return df


@{{< key kit_as >}}.task(
    container_image=image,
    secret_requests=[
        {{< key kit_as >}}.Secret(
            group="private-key",
            key="snowflake",
        )
    ],
)
def write_table() -> {{< key kit_as >}}.StructuredDataset:
    df = pd.DataFrame({"ID": [1, 2, 3], "NAME": ["flyte", "is", "amazing"], "AGE": [30, 30, 30]})
    print(df)

    # Upload the DataFrame to the Snowflake table via StructuredDataset
    user = ("FLYTE",)
    account = ("FLYTE_SNOFLAKE_ACCOUNT",)
    database = ("FLYTEAGENT",)
    schema = ("PUBLIC",)
    warehouse = ("COMPUTE_WH",)
    table = "TEST"
    uri = f"snowflake://{user}:{account}/{warehouse}/{database}/{schema}/{table}"

    return {{< key kit_as >}}.StructuredDataset(dataframe=df, uri=uri)


@workflow
def wf() -> {{< key kit_as >}}.StructuredDataset:
    sd = snowflake_task_templatized_query()
    t1 = print_head(input_sd=sd)
    insert_query = snowflake_task_insert_query(id=1, name="Flyte", age=30)
    sd2 = snowflake_task_templatized_query()
    wt = write_table()

    sd >> t1 >> insert_query >> wt >> sd2

    return print_head(input_sd=sd2)
```
