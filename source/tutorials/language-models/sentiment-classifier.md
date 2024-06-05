# Sentiment Classification with Language Models

This tutorial demonstrates how to fine-tune a pre-trained language model to
classify the sentiment of IMDB movie reviews. We're going to use the
`transformers` library and the `imdb` dataset to classify the sentiment of movie
review.

::::{dropdown} Run on Union Serverless

You can run this example on Union serverless.

:::{button-link} https://signup.union.ai/
:color: secondary

Create an account
:::

Once you have a Union account, install `unionai`

```{code}
pip install unionai
```

Then run the following commands to run the workflow:

```{code}
git clone https://github.com/unionai/examples
cd examples
unionai run --remote tutorials/sentiment_classifier/sentiment_classifier.py main --model distilbert-base-uncased 
```

::::

## Overview

The power of language models lies in their flexibility: as long as you
operate in the same token space as a pre-trained model, you can leverage the
patterns learned from a much wider data distribution than you could learn from
just a small data domain.

In this example, we're going to fine-tune the [DistilBERT](https://huggingface.co/distilbert/distilbert-base-uncased) model on the [IMDB dataset](https://huggingface.co/datasets/stanfordnlp/imdb) to classify the sentiment of movie reviews.

We'll start by importing the workflow dependencies:

```{rli} https://raw.githubusercontent.com/unionai/examples/main/tutorials/sentiment_classifier/sentiment_classifier.py
:language: python
:lines: 20-26
```

## Defining the container image

We'll define the container image that will be used to run the workflow with
the `ImageSpec` object:

```{rli} https://raw.githubusercontent.com/unionai/examples/main/tutorials/sentiment_classifier/sentiment_classifier.py
:language: python
:lines: 29-39
```

We've pinned the versions of the package dependencies to ensure reproducibility.
Under the hood, Union will build the container image so we don't have to
worry about writing a `Dockerfile`.

## Downloading the dataset and model

Next, we download the dataset. Specifying `cache=True` in the `@task`
definition makes sure that we don't waste compute resources downloading the
data multiple times:

```{rli} https://raw.githubusercontent.com/unionai/examples/main/tutorials/sentiment_classifier/sentiment_classifier.py
:language: python
:lines: 42-56
```

Then we'll do the same for the model:

```{rli} https://raw.githubusercontent.com/unionai/examples/main/tutorials/sentiment_classifier/sentiment_classifier.py
:language: python
:lines: 59-74
```

## Fine-tuning the model

Now we're ready to fine-tune the model using the dataset and model from the previous
steps. The task below does the following:

1. Loads the dataset and model.
2. Tokenizes the dataset.
3. Initializes a weights and biases session to track the training process.
4. Trains the model based on the number of epochs (`n_epochs`) specified.
5. Compresses the model to a tarfile and saves it to the specified path.

```{rli} https://raw.githubusercontent.com/unionai/examples/main/tutorials/sentiment_classifier/sentiment_classifier.py
:language: python
:lines: 77-176
```

## Creating the workflow

We can put all of these tasks together into a workflow:

```{rli} https://raw.githubusercontent.com/unionai/examples/main/tutorials/sentiment_classifier/sentiment_classifier.py
:language: python
:lines: 179-194
```

Each task is actually running in its own container, but Union takes care of
storing the intermediate outputs and passing them between tasks.

## Trying out different models

Now that you've run the fine-tuning workflow once, you can try out different
models by passing in a different model name to the `model` argument, which can
be supplied to the `--model` flag when you invoke `unionai run`. For example,
you can try out the `google-bert/bert-base-uncased` model, or any text
[classification model](https://huggingface.co/models?pipeline_tag=text-classification&sort=trending) available on HuggingFace hub.
