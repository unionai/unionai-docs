---
title: Add Tracing and Guardrails to an Airbnb RAG App with Weave
weight: 5
variants: -flyte -serverless +byoc +selfmanaged
layout: py_example
example_file: /external/unionai-examples/tutorials/weave/rag_app.py
run_on_union_secrets:
  - weaviate-url
  - weaviate-api-key
  - openai-api-key
  - wandb-api-key
run_on_union_enforce: true
run_on_union_open: false
example_setup:
  - "# retrieve your weaviate URL and API key here: https://weaviate.io/developers/weaviate/connections/connect-cloud"
  - "# retrieve your wandb API key here: https://wandb.ai/settings"
  - "# retrieve your openai API key here: https://platform.openai.com/api-keys"
  - "# pre-cache the model you'll use in the RAG app with union artifacts."
  - "# replace the model ID if you're using a different LLM."
  - union cache model-from-hf microsoft/Phi-3-mini-128k-instruct \
    --hf-token-key <YOUR_HF_TOKEN> \
    --union-api-key <YOUR_UNION_API_KEY> \
  - "# replace `<YOUR_MODEL_ARTIFACT_URI>` with the model artifact URI returned from the union cache step."
  - "# run the following command with the appropriate dataset URL and index name to ingest documents:"
  - union run --remote ingestion.py ingest_data \
    --inside_airbnb_listings_url https://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2025-03-02/data/listings.csv.gz \
    --index_name AirbnbListings
  - "# replace `<YOUR_WANDB_ENTITY>` with your wandb entity. an entity represents a user name or a team name."
example_run_cmd: union deploy apps rag_app.py weave-rag
---
