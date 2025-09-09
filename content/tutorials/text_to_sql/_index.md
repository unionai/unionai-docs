---
title: Text-to-SQL
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Text-to-SQL

> [!NOTE]
> Code available [here](https://github.com/unionai/unionai-examples/tree/main/tutorials-v2/text_to_sql); based on work by [LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/workflow/advanced_text_to_sql/).

Data analytics drives modern decision-making, but SQL often creates a bottleneck. Writing queries requires technical expertise, so non-technical stakeholders must rely on data teams. That translation layer slows everyone down.

Text-to-SQL narrows this gap by turning natural language into executable SQL queries. It lowers the barrier to structured data and makes databases accessible to more people.

In this tutorial, we build a Text-to-SQL workflow using LlamaIndex and evaluate it on the [WikiTableQuestions dataset](https://ppasupat.github.io/WikiTableQuestions/) (a benchmark of natural language questions over semi-structured tables). We then explore prompt optimization to see whether it improves accuracy and show how to track prompts and results over time. Along the way, we'll see what worked, what didn't, and what we learned about building durable evaluation pipelines. The pattern here can be adapted to your own datasets and workflows.

![Evaluation](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/tutorials/text-to-sql/evaluation.png)

## Ingesting data

We start by ingesting the WikiTableQuestions dataset, which comes as CSV files, into a SQLite database. This database serves as the source of truth for our Text-to-SQL pipeline.

{{< code file="/external/unionai-examples/tutorials-v2/text_to_sql/data_ingestion.py" fragment=data_ingestion lang=python >}}

The ingestion step:

1. Downloads the dataset (a zip archive from GitHub).
2. Extracts the CSV files locally.
3. Generates table metadata (names and descriptions).
4. Creates corresponding tables in SQLite.

The Flyte task returns both the path to the database and the generated table metadata.

{{< code file="/external/unionai-examples/tutorials-v2/text_to_sql/data_ingestion.py" fragment=table_info lang=python >}}

{{< variant byoc selfmanaged >}}

With Union artifacts (coming soon!), you'll be able to persist the ingested SQLite database as an artifact. This removes the need to rerun data ingestion in every pipeline.

{{< /variant >}}

## From question to SQL

Next, we define a workflow that converts natural language into executable SQL using a retrieval-augmented generation (RAG) approach.

{{< code file="/external/unionai-examples/tutorials-v2/text_to_sql/text_to_sql.py" fragment=text_to_sql lang=python >}}

The main `text_to_sql` task orchestrates the pipeline:

- Ingest data
- Build vector indices for each table
- Retrieve relevant tables and rows
- Generate SQL queries with an LLM
- Execute queries and synthesize answers

We use OpenAI GPT models with carefully structured prompts to maximize SQL correctness.

### Vector indexing

We index each table's rows semantically so the model can retrieve relevant examples during SQL generation.

{{< code file="/external/unionai-examples/tutorials-v2/text_to_sql/text_to_sql.py" fragment=index_tables lang=python >}}

Each row becomes a text node stored in LlamaIndex’s `VectorStoreIndex`. This lets the system pull semantically similar rows when handling queries.

### Table retrieval and context building

We then retrieve the most relevant tables for a given query and build rich context that combines schema information with sample rows.

{{< code file="/external/unionai-examples/tutorials-v2/text_to_sql/text_to_sql.py" fragment=retrieve_tables lang=python >}}

The retriever selects tables via semantic similarity, then attaches their schema and example rows. This context grounds the model's SQL generation in the database's actual structure and content.

### SQL generation and response synthesis

Finally, we generate SQL queries and produce natural language answers.

{{< code file="/external/unionai-examples/tutorials-v2/text_to_sql/text_to_sql.py" fragment=sql_and_response lang=python >}}

The SQL generation prompt includes schema, example rows, and formatting rules. After execution, the system returns a final answer.

At this point, we have an end-to-end Text-to-SQL pipeline: natural language questions go in, SQL queries run, and answers come back. To make this workflow production-ready, we leveraged several Flyte 2 capabilities. Caching ensures that repeated steps, like table ingestion or vector indexing, don’t need to rerun unnecessarily, saving time and compute. Containerization provides consistent, reproducible execution across environments, making it easier to scale and deploy. Observability features let us track every step of the pipeline, monitor performance, and debug issues quickly.

While the pipeline works end-to-end, to get a pulse on how it performs across multiple prompts and to gradually improve performance, we can start experimenting with prompt tuning.

Two things help make this process meaningful:

- **A clean evaluation dataset** - so we can measure accuracy against trusted ground truth.
- **A systematic evaluation loop** - so we can see whether prompt changes or other adjustments actually help.

With these in place, the next step is to build a "golden" QA dataset that will guide iterative prompt optimization.

## Building the QA dataset

> [!NOTE]
> The WikiTableQuestions dataset already includes question–answer pairs, available in its [GitHub repository](https://github.com/ppasupat/WikiTableQuestions/tree/master/data). To use them for this workflow, you'll need to adapt the data into the required format, but the raw material is there for you to build on.

We generate a dataset of natural language questions paired with executable SQL queries. This dataset acts as the benchmark for prompt tuning and evaluation.

{{< code file="/external/unionai-examples/tutorials-v2/text_to_sql/create_qa_dataset.py" fragment=build_eval_dataset lang=python >}}

The pipeline does the following:

- Schema extraction – pull full database schemas, including table names, columns, and sample rows.
- Question–SQL generation – use an LLM to produce natural language questions with matching SQL queries.
- Validation – run each query against the database, filter out invalid results, and also remove results that aren't relevant.
- Final export – store the clean, validated pairs in CSV format for downstream use.

### Schema extraction and chunking

We break schemas into smaller chunks to cover all tables evenly. This avoids overfitting to a subset of tables and ensures broad coverage across the dataset.

{{< code file="/external/unionai-examples/tutorials-v2/text_to_sql/create_qa_dataset.py" fragment=get_and_split_schema lang=python >}}

### Question and SQL generation

Using structured prompts, we ask an LLM to generate realistic questions users might ask, then pair them with syntactically valid SQL queries. Deduplication ensures diversity across queries.

{{< code file="/external/unionai-examples/tutorials-v2/text_to_sql/create_qa_dataset.py" fragment=generate_questions_and_sql lang=python >}}

### Validation and quality control

Each generated SQL query runs against the database, and another LLM double-checks that the result matches the intent of the natural language question.

{{< code file="/external/unionai-examples/tutorials-v2/text_to_sql/create_qa_dataset.py" fragment=validate_sql lang=python >}}

Even with automated checks, human review remains critical. Since this dataset serves as the ground truth, mislabeled pairs can distort evaluation. For production use, always invest in human-in-the-loop review.

{{< variant byoc selfmanaged >}}

Support for human-in-the-loop pipelines is coming soon in Flyte 2!

{{< /variant>}}

## Optimizing prompts

With the QA dataset in place, we can turn to prompt optimization. The idea: start from a baseline prompt, generate new variants, and measure whether accuracy improves.

{{< code file="/external/unionai-examples/tutorials-v2/text_to_sql/optimizer.py" fragment=auto_prompt_engineering lang=python >}}

### Evaluation pipeline

We evaluate each prompt variant against the golden dataset, split into validation and test sets, and record accuracy metrics in real time.

{{< code file="/external/unionai-examples/tutorials-v2/text_to_sql/optimizer.py" fragment=evaluate_prompt lang=python >}}

Here's how prompt accuracy evolves over time, as shown in the UI report:

![Prompt accuracies](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/tutorials/text-to-sql/prompt_accuracies.png)

### Iterative optimization

An optimizer LLM proposes new prompts by analyzing patterns in successful and failed generations. Each candidate runs through the evaluation loop, and we select the best performer.

{{< code file="/external/unionai-examples/tutorials-v2/text_to_sql/optimizer.py" fragment=prompt_optimizer lang=python >}}

On paper, this creates a continuous improvement cycle: baseline → new variants → measured gains.

## Run it

To create the QA dataset:

```
python create_qa_dataset.py
```

To run the prompt optimization loop:

```
python optimizer.py
```

## What we observed

Prompt optimization didn't consistently lift SQL accuracy in this workflow. Accuracy plateaued near the baseline. But the process surfaced valuable lessons about what matters when building LLM-powered systems on real infrastructure.

- **Schema clarity matters**: CSV ingestion produced tables with overlapping names, creating ambiguity. This showed how schema design and metadata hygiene directly affect downstream evaluation.
- **Ground truth needs trust**: Because the dataset came from LLM outputs, noise remained even after filtering. Human review proved essential. Golden datasets need deliberate curation, not just automation.
- **Optimization needs context**: The optimizer couldn't “see” which examples failed, limiting its ability to improve. Feeding failures directly risks overfitting. A structured way to capture and reuse evaluation signals is the right long-term path.

Sometimes prompt tweaks alone can lift accuracy, but other times the real bottleneck lives in the data, the schema, or the evaluation loop. The lesson isn't "prompt optimization doesn't work", but that its impact depends on the system around it. Accuracy improves most reliably when prompts evolve alongside clean data, trusted evaluation, and observable feedback loops.

## The bigger lesson

Evaluation and optimization aren’t one-off experiments; they’re continuous processes. What makes them sustainable isn't a clever prompt, it’s the platform around it.

Systems succeed when they:

- **Observe** failures with clarity — track exactly what failed and why.
- **Remain durable** across iterations — run pipelines that are stable, reproducible, and comparable over time.

That's where Flyte 2 comes in. Prompt optimization is one lever, but it becomes powerful only when combined with:

- Clean, human-validated evaluation datasets.
- Systematic reporting and feedback loops.

**The real takeaway: improving LLM pipelines isn't about chasing the perfect prompt. It's about designing workflows with observability and durability at the core, so that every experiment compounds into long-term progress.**
