---
title: Language Models
weight: 1
variants: -flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Language Models

Language models (LMs) are a type of deep learning model that fundamentally predicts
tokens within some context window, either in a [masked](https://huggingface.co/docs/transformers/main/en/tasks/masked_language_modeling) or
[causal](https://huggingface.co/docs/transformers/en/tasks/language_modeling) manner.

Large language models (LLMs) are a type of language model that have many trainable
parameters, which in recent times can be hundreds of millions to trillions of parameters.
LMs can also perform a wider range of inference-time tasks compared to traditional
ML methods because they can operate on structured and unstructured text data. This
means they can perform tasks like text generation, API function calling,
summarization, and question-answering.

In these examples, you'll learn how to use LMs of different sizes for different
use cases, from sentiment analysis to retrieval augmented generation (RAG).
