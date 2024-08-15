# Snowflake agent

Union can be seamlessly integrated with the [Snowflake](https://www.snowflake.com) service,
allowing you to easily query data in Snowflake.

## Installation

To use the Snowflake agent, run the following command:

```
pip install flytekitplugins-snowflake
```

## Configuring key-pair authentication
1. [Generate the private key](https://docs.snowflake.com/en/user-guide/key-pair-auth#generate-the-private-key)
2. [Assign the public key to a Snowflake user](https://docs.snowflake.com/en/user-guide/key-pair-auth#assign-the-public-key-to-a-snowflake-user)

## Get the metadata for the task
The user, account, database, warehouse, and schema metadata are required to configure the Snowflake task.

Run the following SQL in the Snowflake console to get the metadata:

```sql
SELECT
    CURRENT_USER() AS "User",
    CONCAT(CURRENT_ORGANIZATION_NAME(), '-', CURRENT_ACCOUNT_NAME()) AS "Account",
    CURRENT_DATABASE() AS "Database",
    CURRENT_SCHEMA() AS "Schema",
    CURRENT_WAREHOUSE() AS "Warehouse";
```

## Example usage

For a usage example, see [Snowflake agent example](./snowflake-agent-example).

## Local testing

Create a secret file that contains the Snowflake private key:

```bash
sudo vim /etc/secrets/snowflake
```

{@@ if byoc @@}
## Union cluster deployment

After you have finished testing the agent locally, contact the Union team to enable it in your cluster.
{@@ endif @@}