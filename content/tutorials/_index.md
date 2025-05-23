---
title: Tutorials
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
top_menu: true
sidebar_expanded: true
---

# Tutorials

This section provides tutorials that walk you through the process of building AI/ML applications on {{< key product_name >}}.
The example applications range from training XGBoost models in tabular datasets to fine-tuning large language models for text generation tasks.

{{< variant serverless byoc selfmanaged >}}
{{< grid >}}

{{< link-card target="language-models/sentiment-classifier" icon="" title="Sentiment Classification with DistilBERT" >}}
Fine-tune a pre-trained language model in the IMDB dataset for sentiment classification.
{{< /link-card >}}

{{< link-card target="language-models/agentic-rag" icon="" title="Agentic Retrieval Augmented Generation" >}}
Build an agentic retrieval augmented generation system with ChromaDB and Langchain.
{{< /link-card >}}

{{< link-card target="language-models/soft-clustering-hdbscan" icon="" title="HDBSCAN Soft Clustering With Headline Embeddings with GPUs" >}}
Use HDBSCAN soft clustering with headline embeddings and UMAP on GPUs.
{{< /link-card >}}

{{< link-card target="language-models/llama_edge_deployment" icon="" title="Deploy a Fine-Tuned Llama Model to an iOS App with MLC-LLM" >}}
Fine-tune a Llama 3 model on the Cohere Aya Telugu subset and generate a model artifact for deployment as an iOS app.
{{< /link-card >}}

{{< link-card target="parallel-processing-and-job-scheduling/reddit-slack-bot" icon="" title="Reddit Slack Bot on a Schedule" >}}
Securely store Reddit and Slack authentication data while pushing relevant Reddit posts to slack on a consistent basis.
{{< /link-card >}}

{{< link-card target="parallel-processing-and-job-scheduling/wikipedia-embeddings" icon="" title=" Wikipedia Embeddings Generation" >}}
Create embeddings for the Wikipedia dataset, powered by {{< key product_name >}} actors.
{{< /link-card >}}

{{< link-card target="time-series/time-series-forecaster-comparison" icon="" title="Time Series Forecaster Comparison" >}}
Visually compare the output of various time series forecasters while
maintaining lineage of the training and forecasted data.
{{< /link-card >}}

{{< link-card target="time-series/gluonts-time-series" icon="" title="GluonTS Time Series On GPUs" >}}
Train and evaluate a time series forecasting model with GluonTS.
{{< /link-card >}}

{{< link-card target="finance/credit-default-xgboost" icon="" title="Credit Default Prediction with XGBoost & NVIDIA RAPIDS" >}}
Use NVIDIA RAPIDS `cuDF` DataFrame library and `cuML` machine learning to predict credit default.
{{< /link-card >}}

{{< link-card target="bioinformatics/alignment" icon="" title="Genomic Alignment using Bowtie 2" >}}
Pre-process raw sequencing reads, build an index, and perform alignment to a reference genome using the Bowtie2 aligner.
{{< /link-card >}}

{{< link-card target="multimodal-ai/video-dubbing" icon="" title="Video Dubbing with Open-Source Models" >}}
Use open-source models to dub videos.
{{< /link-card >}}

{{< link-card target="language-models/vllm-serving-on-actor" icon="" title="Efficient Named Entity Recognition with vLLM" >}}
Serve a vLLM model on a warm container and trigger inference automatically with artifacts.
{{< /link-card >}}

{{< link-card target="diffusion-models/mochi-video-generation" icon="" title="Video Generation with Mochi" >}}
Run the Mochi 1 text-to-video generation model by Genmo on {{< key product_name >}}.
{{< /link-card >}}

{{< link-card target="compound-ai-systems/pdf-to-podcast-blueprint" icon="" title="Optimizing the PDF-to-Podcast NVIDIA Blueprint for Production Use" >}}
Leverage {{< key product_name >}} to productionize NVIDIA blueprint workflows.
{{< /link-card >}}

{{< link-card target="retrieval-augmented-generation/contextual-rag" icon="" title="Contextual RAG with Together AI" >}}
Build a contextual RAG workflow for enterprise use.
{{< /link-card >}}

{{< variant byoc >}}
{{< link-card target="serving/nim-on-actor" icon="" title="Near-Real-Time Inference with NVIDIA NIM" >}}
Serve NVIDIA NIM-supported language models, powered by {{< key product_name >}} actors.
{{< /link-card >}}
{{< /variant >}}

{{< link-card target="retrieval-augmented-generation/lance-db-rag" icon="" title="Creating a RAG App with LanceDB and Google Gemini" >}}
Power your RAG app with {{< key product_name >}} Serving.
{{< /link-card >}}

{{< link-card target="compound-ai-systems/enterprise-rag-blueprint" icon="" title="Taking NVIDIA’s Enterprise RAG Blueprint to Production" >}}
Serve models and run background jobs like data ingestion — all within {{< key product_name >}} using {{< key product_name >}} Serving and {{< key product_name >}} Workflows.
{{< /link-card >}}

{{< variant byoc >}}
{{< link-card target="language-models/data-streaming" icon="" title="Fine-Tune BERT on Arabic Reviews with Multi-Node Training and Data Streaming" >}}
Fine-tune a BERT model on a sizable Arabic review dataset using PyTorch Lightning and the streaming library on a multi-node setup.
{{< /link-card >}}
{{< /variant >}}

{{< variant byoc >}}
{{< link-card target="serving/arize" icon="" title="Trace and Evaluate Models and RAG Apps with Arize" >}}
Integrate Arize with your LLMs or RAG applications to trace model activity and evaluate performance in near-real-time.
{{< /link-card >}}
{{< /variant >}}

{{< variant byoc >}}
{{< link-card target="serving/weave" icon="" title="Add Tracing and Guardrails to an Airbnb RAG App with Weave" >}}
Deploy a self-hosted LLM and RAG app with observability and guardrails powered by Weave.
{{< /link-card >}}
{{< /variant >}}

{{< /grid >}}
{{< /variant>}}
