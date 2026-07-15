---
title: Consuming a message queue
weight: 18
variants: +flyte +union
---

# Consuming a message queue

A common production pattern is a **queue consumer**: a long-running task that pulls messages
from an external message queue (such as [AWS SQS](https://aws.amazon.com/sqs/)) and processes
each message concurrently.
Flyte 2 expresses this naturally by combining three building blocks you have already seen:

- **Async tasks**: the consumer loop is an `async def` task that awaits I/O against the queue.
- [**Fanout**](./fanout): each received message is dispatched to its own `process_message` action with `asyncio.create_task()`, so processing runs in parallel across the cluster.
- [**Reusable containers**](../task-configuration/reusable-containers): a `ReusePolicy` keeps a warm pool of replicas ready, so messages are processed without per-message container cold-start.

The complete, runnable source for this example, a producer (`generator.py`) and a consumer
(`processor.py`), lives in the Flyte SDK repository under
[`examples/queue-reader`](https://github.com/flyteorg/flyte-sdk/tree/main/examples/queue-reader).

> [!NOTE]
> This example reads from AWS SQS and therefore requires an SQS queue and AWS credentials
> available to the running task (here the queue is passed as an ARN via the `QUEUE_ARN`
> environment variable). The Flyte pattern shown below applies to any external queue: swap
> the SQS client calls for your queue's client.

## The consumer

### Define the task environment

The consumer runs in a [reusable](../task-configuration/reusable-containers) `TaskEnvironment`.
`replicas=3` keeps a warm pool of at least two replicas to avoid starvation while the parent
consumer task occupies one, and `idle_ttl=300` shuts the pool down after five minutes of
inactivity.
The image is built from the script's own inline dependencies with
`flyte.Image.from_uv_script`, plus the `unionai-reuse` runtime library that reusable containers
require:

```python
import asyncio
import json
import os
from typing import List

import aioboto3

import flyte

env = flyte.TaskEnvironment(
    name="sqs_processor",
    resources=flyte.Resources(memory="500Mi", cpu=1),
    image=flyte.Image.from_uv_script(
        __file__,
        name="flyte",
    ).with_pip_packages("unionai-reuse>=0.1.3"),
    reusable=flyte.ReusePolicy(
        replicas=3,  # 1 for the consumer loop + 2 workers, so processing never starves
        idle_ttl=300,  # Idle time to keep the task environment alive
    ),
)

# The queue is passed as an ARN via the QUEUE_ARN environment variable.
DEFAULT_QUEUE_ARN = os.getenv("QUEUE_ARN")


def get_queue_url_from_arn(queue_arn: str) -> str:
    """Convert an SQS ARN to a queue URL."""
    parts = queue_arn.split(":")
    region = parts[3]
    account = parts[4]
    queue_name = parts[5]

    return f"https://sqs.{region}.amazonaws.com/{account}/{queue_name}"
```

### Process a single message

Each message is handled by its own task. Because it is an `async def` task, many invocations
can run concurrently across the reusable pool:

```python
@env.task
async def process_message(message: dict) -> str:
    """Process a single message asynchronously and return the extracted word."""
    body = json.loads(message["Body"])
    word = body.get("word", "unknown")
    print(f"Task Processing message {body.get('message_id')}: {word}")
    return word
```

### The consumer loop

The driver task long-polls the queue, and for each message it receives it **dispatches a
`process_message` action with `asyncio.create_task()`** rather than awaiting it inline. This
is what fans the work out in parallel. It deletes each message once processing has started, then
awaits all dispatched tasks with `asyncio.gather()`:

```python
@env.task
async def main(queue_arn: str = DEFAULT_QUEUE_ARN, max_messages: int = 10) -> List[str]:
    queue_url = get_queue_url_from_arn(queue_arn)
    session = aioboto3.Session(region_name="us-east-2")

    results = []
    tasks = []
    messages_received = 0

    async with session.client("sqs") as sqs:
        while messages_received < max_messages:
            response = await sqs.receive_message(
                QueueUrl=queue_url,
                AttributeNames=["All"],
                MaxNumberOfMessages=1,   # one message at a time
                WaitTimeSeconds=20,      # long-polling timeout (max 20 seconds)
            )

            messages = response.get("Messages", [])
            if not messages:
                continue

            message = messages[0]
            messages_received += 1

            # Fan out: dispatch processing as a parallel action.
            process_task = asyncio.create_task(process_message(message))
            tasks.append(process_task)

            # Delete the message once we've started processing it.
            await sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=message["ReceiptHandle"])

    # Wait for all dispatched processing tasks to complete.
    if tasks:
        completed_tasks = await asyncio.gather(*tasks)
        results.extend(completed_tasks)

    return results
```

### Run it

Initialize Flyte from your config and run the consumer remotely:

```python
if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(main, queue_arn=DEFAULT_QUEUE_ARN, max_messages=10)
    print(run.url)
```

## The producer

To exercise the consumer, the example includes a standalone
[`generator.py`](https://github.com/flyteorg/flyte-sdk/tree/main/examples/queue-reader) that
pushes ten JSON messages onto the same SQS queue with `boto3`. It is an ordinary Python script,
not a Flyte task. Any producer that writes to the queue will do.

## Notes and gotchas

- **Delete after receive, not after processing completes.** The example deletes each message as
  soon as it dispatches the processing task. If a `process_message` action can fail and you need
  at-least-once semantics, delete the message only after the task succeeds instead.
- **`max_messages` bounds the run.** The consumer loop here stops after `max_messages`. For a
  continuously running consumer, drive it on a [trigger](../task-configuration/triggers) or remove
  the bound and manage the task lifecycle explicitly.
- **Reusable containers require a Union backend.** See
  [Reusable containers](../task-configuration/reusable-containers) for the `ReusePolicy` parameters
  (`replicas`, `concurrency`, `idle_ttl`, `scaledown_ttl`) and their capacity math.
