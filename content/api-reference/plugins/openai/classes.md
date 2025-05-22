---
title: Classes
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Classes

| Class | Description |
|-|-|
| [`flytekitplugins.openai.batch.agent.BatchEndpointAgent`](../packages/flytekitplugins.openai.batch.agent#flytekitpluginsopenaibatchagentbatchendpointagent) |This is the base class for all async agents. |
| [`flytekitplugins.openai.batch.agent.BatchEndpointMetadata`](../packages/flytekitplugins.openai.batch.agent#flytekitpluginsopenaibatchagentbatchendpointmetadata) | |
| [`flytekitplugins.openai.batch.task.BatchEndpointTask`](../packages/flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskbatchendpointtask) |This mixin class is used to run the async task locally, and it's only used for local execution. |
| [`flytekitplugins.openai.batch.task.BatchResult`](../packages/flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskbatchresult) | |
| [`flytekitplugins.openai.batch.task.DownloadJSONFilesExecutor`](../packages/flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskdownloadjsonfilesexecutor) |Please see the notes for the metaclass above first. |
| [`flytekitplugins.openai.batch.task.DownloadJSONFilesTask`](../packages/flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskdownloadjsonfilestask) |Please take a look at the comments for :py:class`flytekit. |
| [`flytekitplugins.openai.batch.task.OpenAIFileConfig`](../packages/flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskopenaifileconfig) | |
| [`flytekitplugins.openai.batch.task.OpenAIFileDefaultImages`](../packages/flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskopenaifiledefaultimages) |Default images for the openai batch plugin. |
| [`flytekitplugins.openai.batch.task.UploadJSONLFileExecutor`](../packages/flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskuploadjsonlfileexecutor) |Please see the notes for the metaclass above first. |
| [`flytekitplugins.openai.batch.task.UploadJSONLFileTask`](../packages/flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskuploadjsonlfiletask) |Please take a look at the comments for :py:class`flytekit. |
| [`flytekitplugins.openai.chatgpt.agent.ChatGPTAgent`](../packages/flytekitplugins.openai.chatgpt.agent#flytekitpluginsopenaichatgptagentchatgptagent) |This is the base class for all sync agents. |
| [`flytekitplugins.openai.chatgpt.task.ChatGPTTask`](../packages/flytekitplugins.openai.chatgpt.task#flytekitpluginsopenaichatgpttaskchatgpttask) |This is the simplest form of a ChatGPT Task, you can define the model and the input you want. |
