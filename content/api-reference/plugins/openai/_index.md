---
title: OpenAI
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# OpenAI



## Directory

### Classes

| Class | Description |
|-|-|
| [`flytekitplugins.openai.batch.connector.BatchEndpointConnector`](flytekitplugins.openai.batch.connector#flytekitpluginsopenaibatchconnectorbatchendpointconnector) |  |
| [`flytekitplugins.openai.batch.connector.BatchEndpointMetadata`](flytekitplugins.openai.batch.connector#flytekitpluginsopenaibatchconnectorbatchendpointmetadata) |  |
| [`flytekitplugins.openai.batch.connector.State`](flytekitplugins.openai.batch.connector#flytekitpluginsopenaibatchconnectorstate) |  |
| [`flytekitplugins.openai.batch.task.BatchEndpointTask`](flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskbatchendpointtask) |  |
| [`flytekitplugins.openai.batch.task.BatchResult`](flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskbatchresult) |  |
| [`flytekitplugins.openai.batch.task.DownloadJSONFilesExecutor`](flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskdownloadjsonfilesexecutor) |  |
| [`flytekitplugins.openai.batch.task.DownloadJSONFilesTask`](flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskdownloadjsonfilestask) |  |
| [`flytekitplugins.openai.batch.task.OpenAIFileConfig`](flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskopenaifileconfig) |  |
| [`flytekitplugins.openai.batch.task.OpenAIFileDefaultImages`](flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskopenaifiledefaultimages) | Default images for the openai batch plugin. |
| [`flytekitplugins.openai.batch.task.UploadJSONLFileExecutor`](flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskuploadjsonlfileexecutor) |  |
| [`flytekitplugins.openai.batch.task.UploadJSONLFileTask`](flytekitplugins.openai.batch.task#flytekitpluginsopenaibatchtaskuploadjsonlfiletask) |  |
| [`flytekitplugins.openai.chatgpt.connector.ChatGPTConnector`](flytekitplugins.openai.chatgpt.connector#flytekitpluginsopenaichatgptconnectorchatgptconnector) |  |
| [`flytekitplugins.openai.chatgpt.task.ChatGPTTask`](flytekitplugins.openai.chatgpt.task#flytekitpluginsopenaichatgpttaskchatgpttask) | This is the simplest form of a ChatGPT Task, you can define the model and the input you want. |

### Functions

| Function | Description |
|-|-|
| [`flytekitplugins.openai.batch.workflow.create_batch()`](flytekitplugins.openai.batch.workflow#create_batch) | Uploads JSON data to a JSONL file, creates a batch, waits for it to complete, and downloads the output/error JSON files. |

### Packages

| Package | Description |
|-|-|
| [`flytekitplugins.openai.batch.connector`](flytekitplugins.openai.batch.connector) |  |
| [`flytekitplugins.openai.batch.task`](flytekitplugins.openai.batch.task) |  |
| [`flytekitplugins.openai.batch.workflow`](flytekitplugins.openai.batch.workflow) |  |
| [`flytekitplugins.openai.chatgpt.connector`](flytekitplugins.openai.chatgpt.connector) |  |
| [`flytekitplugins.openai.chatgpt.task`](flytekitplugins.openai.chatgpt.task) |  |

