Once you have a Union account, install `union`:

```shell
pip install union
```

Export the following environment variable to build and push
images to your own container registry:

```shell
# replace with your registry name
export IMAGE_SPEC_REGISTRY="<your-container-registry>"
```

Then run the following commands to run the workflow:

```shell
git clone https://github.com/unionai/unionai-examples
cd unionai-examples
union run --remote tutorials/sentiment_classifier/sentiment_classifier.py main --model distilbert-base-uncased
```

The source code for this tutorial can be found [here {octicon}`mark-github`](https://www.github.com/unionai/unionai-examples/tree/main/tutorials/sentiment_classifier/sentiment_classifier.py).
