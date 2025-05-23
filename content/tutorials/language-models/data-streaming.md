---
title: Fine-Tune BERT on Arabic Reviews with Multi-Node Training and Data Streaming
weight: 5
variants: -flyte -serverless +byoc +selfmanaged
layout: py_example
example_file: /external/unionai-examples/tutorials/data_streaming/arabic_bert.py
run_on_union_secrets:
  - wandb-api-key
run_on_union_enforce: true
run_on_union_open: false
example_setup:
  - "# retrieve your wandb API key here: https://wandb.ai/settings"
  - "# replace `<YOUR_WANDB_ENTITY>` with your wandb entity. an entity represents a user name or a team name."
example_run_cmd: union run --remote arabic_bert.py finetune_bert_on_sharded_data
---
