# Batch agent example

The Batch API agent allows you to submit requests for asynchronous batch processing on OpenAI. You can provide either a JSONL file or a JSON iterator, and the agent handles the upload to OpenAI, creation of the batch, and downloading of the output and error files.

This example demonstrates how to send a batch of API requests to GPT models for asynchronous processing.

Every batch input should include `custom_id`, `method`, `url`, and `body`.

You can provide either a `JSONLFile` or `Iterator[JSON]`, and the agent handles the file upload to OpenAI creation of the batch, and downloading of the output and error files.

## Using `Iterator`

Here's how you can provide an `Iterator` as an input to the agent:

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/7a300ac43f3da41a4e01bd4dae9d45e8c0094ce3/examples/openai_batch_agent/openai_batch_agent/openai_batch_agent_example_usage.py
:language: python
:linenos: 16-64
```

The `create_batch` function returns an imperative workflow responsible for uploading the JSON data to OpenAI, creating a batch, polling the status of the batch to check for completion, and downloading the output and error files. It also accepts a `config` parameter, allowing you to provide `metadata`, `endpoint`, and `completion_window` values. These parameters default to their respective default values.

`BatchResult` is a dataclass that contains the paths to the output file and the error file.

## Using `JSONLFile`

The following code snippet demonstrates how to send a JSONL file to the `create_batch` function:

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/7a300ac43f3da41a4e01bd4dae9d45e8c0094ce3/examples/openai_batch_agent/openai_batch_agent/openai_batch_agent_example_usage.py
:language: python
:linenos: 79-91
```

The iterator **streams JSON objects to a JSONL file**. If you have large batches of requests or have distinct JSON objects that you want to run predictions on, we recommend you use the iterator.

You can find more info about the [Batch API in the OpenAI docs](https://help.openai.com/en/articles/9197833-batch-api-faq).