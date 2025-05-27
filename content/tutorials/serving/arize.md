---
title: Trace and Evaluate Models and RAG Apps with Arize
weight: 5
variants: -flyte -serverless +byoc +selfmanaged
layout: py_example
example_file: /external/unionai-examples/tutorials/arize/apps.py
run_on_union_secrets:
  - phoenix-api-key
  - arize-api-key
run_on_union_enforce: true
run_on_union_open: false
example_packages:
  - arize-phoenix-client
example_env:
  - PHOENIX_API_KEY: "<YOUR_PHOENIX_API_KEY>"
example_setup:
  - "# pre-cache the model you'll use in the RAG app with union artifacts."
  - "# replace the model ID if you're using a different LLM."
  - union cache model-from-hf --project <YOUR_PROJECT> deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B \
    --hf-token-key <YOUR_HF_TOKEN> \
    --union-api-key <YOUR_UNION_API_KEY> \
  - "# add the model artifact URI returned from the union cache step to the `vllm-deepseek` app definition."
  - "# to ingest documents into the vector database for the arize app:"
  - union run --remote --project <YOUR_PROJECT> ingestion.py ingest_docs_workflow --file_path <YOUR_FILE>
  - "# update the `ArizeConfig` in the app definition with your arize organization, space, and model IDs, then deploy the arize app."
example_run_cmd: union deploy apps --project <YOUR_PROJECT> apps.py <YOUR_APP> <ARGS>
---
