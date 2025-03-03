# ChatGPT agent example

## Basic example

ChatGPT can be used in lots of cases, for example, sentiment analysis, language translation, SQL query generation, and text summarization.

This example shows you how to run ChatGPT tasks in flyte.

```--rli-- https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/chatgpt_agent/chatgpt_agent/chatgpt_agent_example_usage.py
:language: python
:lines: 11-15
```

You have to specify your `name`, `openai_organization` and `chatgpt_config`.

* `name` is for Flyte and it should be unique.
* `openai_organization` is for the OpenAI API. You can find it [here](https://platform.openai.com/account/organization).
* `chatgpt_config` is for OpenAI chat completion. You can find it [here](https://platform.openai.com/docs/api-reference/chat/create).

```--rli-- https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/chatgpt_agent/chatgpt_agent/chatgpt_agent_example_usage.py
:language: python
:lines: 27-50
```

You can execute the workflow locally.

```--rli-- https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/chatgpt_agent/chatgpt_agent/chatgpt_agent_example_usage.py
:language: python
:lines: 56-58
```

## ChatGPT summary bot
These examples show you a real use case of ChatGPT in the production mode.

For more details, see the [FlyteChatGPT Summary Bot GitHub repository](https://github.com/Future-Outlier/FlyteChatGPTSummaryBot) and the [demo video](https://youtu.be/IS6gi4jR7h0?si=hWHZp5LyjDspiwfD).

### Summarize Flyte's latest GitHub releases to Slack

```--rli-- https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/chatgpt_agent/chatgpt_agent/chatgpt_agent_example_usage.py
:language: python
:lines: 69-140
```

### Summarize Flyte's latest YouTube Video to Slack

```--rli-- https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/chatgpt_agent/chatgpt_agent/chatgpt_agent_example_usage.py
:language: python
:lines: 146-271
```

### Summarize the latest MLOps trend from Medium to Twitter

```--note--
This example only works in a local environment.
```

```--rli-- https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/chatgpt_agent/chatgpt_agent/chatgpt_agent_example_usage.py
:language: python
:lines: 277-363
```
