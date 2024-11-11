# Tutorials

This section provides tutorials that walk you through the process of building AI/ML applications on Union.
The example applications range from training XGBoost models in tabular datasets to fine-tuning large language models for text generation tasks.

::::{grid} 2

:::{grid-item-card} {octicon}`heart-fill` Sentiment Classification with DistilBERT
:link: language-models/sentiment-classifier
:link-type: doc

Fine-tune a pre-trained language model in the IMDB dataset for sentiment
classification.
:::

:::{grid-item-card} {octicon}`dependabot` Agentic Retrieval Augmented Generation
:link: language-models/agentic-rag
:link-type: doc

Build an agentic retrieval augmented generation system with ChromaDB and Langchain.
:::

:::{grid-item-card} {octicon}`dependabot` HDBSCAN Soft Clustering With Headline Embeddings with GPUs
:link: language-models/soft-clustering-hdbscan
:link-type: doc

Use HDBSCAN soft clustering with headline embeddings and UMAP on GPUs.
:::

:::{grid-item-card} {octicon}`device-mobile` Deploy a Fine-Tuned Llama Model to an iOS App with MLC-LLM
:link: language-models/llama_edge_deployment
:link-type: doc

Fine-tunes a Llama 3 model on the Cohere Aya Telugu subset and generates a model artifact for deployment as an iOS app.
:::

:::{grid-item-card} {octicon}`hubot` Reddit Slack Bot on a Schedule
:link: parallel-processing-and-job-scheduling/reddit-slack-bot
:link-type: doc

Securely store Reddit and Slack authentication data while pushing relevant
Reddit posts to slack on a consistent basis.
:::

:::{grid-item-card} {octicon}`hubot` Wikipedia Embeddings Generation
:link: parallel-processing-and-job-scheduling/wikipedia-embeddings
:link-type: doc

Create embeddings for the Wikipedia dataset, powered by Union actors.
:::

:::{grid-item-card} {octicon}`graph` Time Series Forecaster Comparison
:link: time-series/time-series-forecaster-comparison
:link-type: doc

Visually compare the output of various time series forecasters while
maintaining lineage of the training and forecasted data.
:::

:::{grid-item-card} {octicon}`graph` GluonTS Time Series On GPUs
:link: time-series/gluonts-time-series
:link-type: doc

Train and evaluate a time series forecasting model with GluonTS.
:::

:::{grid-item-card} {octicon}`graph` Credit Default Prediction with XGBoost & NVIDIA RAPIDS
:link: finance/credit-default-xgboost
:link-type: doc

Use NVIDIA RAPIDS `cuDF` DataFrame library and `cuML` machine learning to predict credit default.
:::

:::{grid-item-card} {octicon}`beaker` Genomic Alignment using Bowtie 2
:link: bioinformatics/alignment
:link-type: doc

Pre-process raw sequencing reads, build an index, and perform alignment
to the a reference genome using the Bowtie2 aligner.
:::

:::{grid-item-card} {octicon}`video` Video Dubbing with Open-Source Models
:link: multimodal-ai/video-dubbing
:link-type: doc

Use open-source models to dub videos.
:::

:::{grid-item-card} {octicon}`accessibility-inset` Efficient Named Entity Recognition with vLLM
:link: language-models/vllm-serving-on-actor
:link-type: doc

Serve a vLLM model on a warm container and trigger inference automatically with artifacts.
:::

::::
