---
title: Streaming Data for BERT Training
weight: 5
variants: -flyte -serverless +byoc +byok
layout: py_example
example_file: /external/unionai-examples/tutorials/data_streaming/arabic_bert.py
run_on_union_secrets:
  - wandb-api-key
run_on_union_enforce: true
run_on_union_open: false
example_run_cmd: union run --remote arabic_bert.py finetune_bert_on_sharded_data --wandb_entity <YOUR_WANDB_ENTITY>
---
