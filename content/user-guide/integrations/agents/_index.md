---
title: Agents
weight: 4
variants: +flyte -serverless +byoc +byok
---


<!-- Check for vartiant accuracy -->
# Agents

Agents are long-running, stateless services that receive execution requests via gRPC and initiate jobs with appropriate external or internal services.
Each agent service is a Kubernetes deployment that receives gRPC requests from FlytePropeller when users trigger a particular type of task (e.g. the DGX agent handles DGX tasks).
The agent service then initiates a job with the appropriate external service. Agents can be run locally as long as the appropriate connection secrets are locally available, since they are spawned in process.

Agents are designed to be scalable and can handle large workloads efficiently, and decrease load on FlytePropeller, since they run outside it.
You can also test agents locally without having to change the Flyte backend configuration, streamlining workflow development.

Agents enable two key workflows:

* **Asynchronously** launching jobs on hosted platforms (e.g. Databricks or Snowflake).
* Calling external **synchronous** services, such as access control, data retrieval, and model inferencing.

## Using existing agents

In this section you will find documentation on how to use existing agents in your workflows.
Alternatively, you can also create your own agent.

## Creating a new agent

You can implement an agent as a Python class, test it locally, and have the Union team enable it in your Union deployment.
Your teammates will then be able to create tasks of the corresponding task type to connect to the external service.

There are two types of agents: **async** and **sync**.
* **Async agents** enable long-running jobs that execute on an external platform over time.
  They communicate with external services that have asynchronous APIs that support `create`, `get`, and `delete` operations.
  The vast majority of agents are async agents.
* **Sync agents** enable request/response services that return immediate outputs (e.g. calling an internal API to fetch data or communicating with the OpenAI API).

> [!NOTE]
> While agents can be written in any programming language since they use a protobuf interface, we currently only support Python agents. We may support other languages in the future.

### Async agent interface specification

To create a new async agent, extend the `AsyncAgentBase` and implement `create`, `get`, and `delete` methods. These methods must be idempotent.

- `create`: This method is used to initiate a new job. Users have the flexibility to use gRPC, REST, or an SDK to create a job.
- `get`: This method retrieves the job resource (job ID or output literal) associated with the task, such as a BigQuery job ID or Databricks task ID.
- `delete`: Invoking this method will send a request to delete the corresponding job.

For an example implementation, see the [BigQuery agent code](https://github.com/flyteorg/flytekit/blob/master/plugins/flytekit-bigquery/flytekitplugins/bigquery/agent.py).

### Sync agent interface specification

To create a new sync agent, extend the `SyncAgentBase` class and implement a `do` method. This method must be idempotent.

- `do`: This method is used to execute the synchronous task, and the worker in Flyte will be blocked until the method returns.

For an example implementation, see the [ChatGPT agent code](https://github.com/flyteorg/flytekit/blob/master/plugins/flytekit-openai/flytekitplugins/openai/chatgpt/agent.py).

### Testing your agent locally

To test your agent locally, create a class for the agent task that inherits from [`AsyncAgentExecutorMixin`](https://github.com/flyteorg/flytekit/blob/f99d50e4c71a77b8f1c9f8e0fe7aa402e1d1b910/flytekit/extend/backend/base_agent.py#L316). This mixin can handle both asynchronous tasks and synchronous tasks and allows {{< key kit_name >}} to mimic FlytePropeller's behavior in calling the agent.

For testing examples, see the [BigQuery agent](./bigquery-agent/_index.md#local-testing) and [Databricks agent](./databricks-agent/_index.md#local-testing) documentation.

{{< variant byoc >}}
{{< markdown >}}

### Enabling your agent in your Union deployment

After you have finished testing your agent locally, you can contact the Union team to enable the agent in your Union deployment to use it in production.

{{< /markdown >}}
{{< /variant >}}
