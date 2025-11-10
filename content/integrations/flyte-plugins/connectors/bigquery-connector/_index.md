---
title: BigQuery connector
weight: 1
variants: +flyte -serverless +byoc +selfmanaged
sidebar_expanded: true
---

# BigQuery connector

The BigQuery connector allows you to submit and manage SQL queries against Google BigQuery from within Flyte.


## Installation

To install the BigQuery connector, run the following command:

This connector is purely a spec. Since SQL is completely portable, there is no need to build a Docker container.

## Example usage

For an example query, see [BigQuery connector example usage](./bigquery-connector.md)


> [!NOTE]
> When testing locally, you may need to store and provide Google Cloud credentials in your environment.
> Ensure you’ve authenticated with Google Cloud (gcloud auth application-default login) or set the appropriate service account environment variables.
> 
> For example, you can set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your service account key file.
