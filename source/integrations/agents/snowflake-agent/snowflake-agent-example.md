# Snowflake agent example

This example shows how to use the `SnowflakeTask` to execute a query in Snowflake.

```{code-block} python
from flytekit import kwtypes, workflow
from flytekitplugins.snowflake import SnowflakeConfig, SnowflakeTask

# Instantiate a flytekitplugins.snowflake.SnowflakeTask to execute a query.
# Incorporate flytekitplugins.snowflake.SnowflakeConfig within the task to define the appropriate configuration.
snowflake_task_no_io = SnowflakeTask(
    name="sql.snowflake.no_io",
    inputs={},
    query_template="SELECT 1",
    output_schema_type=None,
    task_config=SnowflakeConfig(
        account="<SNOWFLAKE_ACCOUNT_ID>",
        database="SNOWFLAKE_SAMPLE_DATA",
        schema="TPCH_SF1000",
        warehouse="COMPUTE_WH",
    ),
)

# For successful registration, ensure that your Snowflake task is assigned a unique
# name within your project/domain for your Union installation.
#
# In practical applications, we often use Snowflake to query datasets.
# Here, we use `SNOWFLAKE_SAMPLE_DATA`, a default dataset in the Snowflake service.
# For more information, see https://docs.snowflake.com/en/user-guide/sample-data.html
# The data uses the following schema:
#
# ```{eval-rst}
# +----------------------------------------------+
# | C_CUSTKEY (int)                              |
# +----------------------------------------------+
# | C_NAME (string)                              |
# +----------------------------------------------+
# | C_ADDRESS (string)                           |
# +----------------------------------------------+
# | C_NATIONKEY (int)                            |
# +----------------------------------------------+
# | C_PHONE (string)                             |
# +----------------------------------------------+
# | C_ACCTBAL (float)                            |
# +----------------------------------------------+
# | C_MKTSEGMENT (string)                        |
# +----------------------------------------------+
# | C_COMMENT (string)                           |
# +----------------------------------------------+
# ```
#
# You can parameterize the query to filter results for a specific country.
# This country will be provided as user input, using a nation key to specify it.
snowflake_task_templatized_query = SnowflakeTask(
    name="sql.snowflake.w_io",
    # Define inputs as well as their types that can be used to customize the query.
    inputs=kwtypes(nation_key=int),
    task_config=SnowflakeConfig(
        account="<SNOWFLAKE_ACCOUNT_ID>",
        database="SNOWFLAKE_SAMPLE_DATA",
        schema="TPCH_SF1000",
        warehouse="COMPUTE_WH",
    ),
    query_template="SELECT * from CUSTOMER where C_NATIONKEY =  {{ .inputs.nation_key }} limit 100",
)


@workflow
def snowflake_wf(nation_key: int):
    return snowflake_task_templatized_query(nation_key=nation_key)

# To review the query results, access the Snowflake console at
# https://<SNOWFLAKE_ACCOUNT_ID>.snowflakecomputing.com/console#/monitoring/queries/detail
# You can also execute the task and workflow locally.
if __name__ == "__main__":
    print(snowflake_task_no_io())
    print(snowflake_wf(nation_key=10))
```
