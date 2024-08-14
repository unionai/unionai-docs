# Snowflake agent example

This example shows how to use the `SnowflakeTask` to execute a query in Snowflake.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/7a300ac43f3da41a4e01bd4dae9d45e8c0094ce3/examples/snowflake_agent/snowflake_agent/snowflake_agent_example_usage.py
:language: python
:lines: 8-15
```

Define a Snowflake task to insert data into the `FLYTEAGENT.PUBLIC.TEST` table.
The `inputs` parameter specifies the types of the inputs using `kwtypes`.
The `query_template` uses Python string interpolation to insert these inputs into the SQL query.
The placeholders `%(id)s`, `%(name)s`, and `%(age)s` will be replaced by the actual values
provided when the task is executed.

You can get the SnowflakeConfig's metadata from the Snowflake console by executing the following query:

```{code} SQL
SELECT
    CURRENT_USER() AS "User",
    CONCAT(CURRENT_ORGANIZATION_NAME(), '-', CURRENT_ACCOUNT_NAME()) AS "Account",
    CURRENT_DATABASE() AS "Database",
    CURRENT_SCHEMA() AS "Schema",
    CURRENT_WAREHOUSE() AS "Warehouse";
```

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/7a300ac43f3da41a4e01bd4dae9d45e8c0094ce3/examples/snowflake_agent/snowflake_agent/snowflake_agent_example_usage.py
:language: python
:lines: 36-122
```

