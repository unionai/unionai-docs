---
title: Decks
weight: 9
variants: +flyte +serverless +byoc +byok
---

# Decks

The Decks feature enables you to obtain customizable and default visibility into your tasks.
Think of it as a visualization tool that you can utilize within your Flyte tasks.

Decks are equipped with a variety of renderers,
such as FrameRenderer and MarkdownRenderer. These renderers produce HTML files.
As an example, FrameRenderer transforms a DataFrame into an HTML table, and MarkdownRenderer converts Markdown text into HTML.

Each task has a minimum of three decks: input, output and default.
The input/output decks are used to render the input/output data of tasks,
while the default deck can be used to render line plots, scatter plots or Markdown text.
Additionally, you can create new decks to render your data using custom renderers.

> [!NOTE]
> Decks is an opt-in feature; to enable it, set `enable_deck` to `True` in the task parameters.

> [!NOTE]
> To clone and run the example code on this page, see the [Flytesnacks repo](https://github.com/flyteorg/flytesnacks).

To begin, import the dependencies:

```python
import union
from union import ImageSpec, task
from union.deck.renderer import MarkdownRenderer
from sklearn.decomposition import PCA
```

We create a new deck named `pca` and render Markdown content along with a
[PCA](https://en.wikipedia.org/wiki/Principal_component_analysis) plot.

You can begin by initializing an {ref}`ImageSpec <image_spec_example>` object to encompass all the necessary dependencies.
This approach automatically triggers a Docker build, alleviating the need for you to manually create a Docker image.



Note the usage of `append` to append the Plotly deck to the Markdown deck.
```python
custom_image = ImageSpec(
    packages=[
        "flytekitplugins-deck-standard",
        "markdown",
        "pandas",
        "pillow",
        "plotly",
        "pyarrow",
        "scikit-learn",
        "ydata_profiling",
    ],
    builder="union",
)
```

To view the log output locally, the `UNION_SDK_LOGGING_LEVEL` environment variable should be set to 20.

The following is the expected output containing the path to the `deck.html` file:

```
{"asctime": "2023-07-11 13:16:04,558", "name": "flytekit", "levelname": "INFO", "message": "pca_plot task creates flyte deck html to file:///var/folders/6f/xcgm46ds59j7g__gfxmkgdf80000gn/T/flyte-0_8qfjdd/sandbox/local_flytekit/c085853af5a175edb17b11cd338cbd61/deck.html"}
```

![Union deck plot](https://raw.githubusercontent.com/flyteorg/static-resources/main/flytesnacks/user_guide/flyte_deck_plot_local.webp)


Once you execute this task on the Flyte cluster, you can access the deck by clicking the _Flyte Deck_ button:

![Union deck button](https://raw.githubusercontent.com/flyteorg/static-resources/main/flytesnacks/user_guide/flyte_deck_button.png)


## Deck renderer

The Deck renderer is an integral component of the Deck plugin, which offers both default and personalized task visibility.
Within the Deck, an array of renderers is present, responsible for generating HTML files.

These renderers showcase HTML in the user interface, facilitating the visualization and documentation of task-associated data.

In the Flyte context, a collection of deck objects is stored.
When the task connected with a deck object is executed, these objects employ renderers to transform data into HTML files.

### Available renderers

#### Frame renderer

Creates a profile report from a Pandas DataFrame.

```python
import pandas as pd
from flytekitplugins.deck.renderer import FrameProfilingRenderer


@task(enable_deck=True, container_image=custom_image)
def frame_renderer() -> None:
    df = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    union.Deck("Frame Renderer", FrameProfilingRenderer().to_html(df=df))
```

![Frame renderer](https://raw.githubusercontent.com/flyteorg/static-resources/main/flytesnacks/user_guide/flyte_decks_frame_renderer.png)



#### Top-frame renderer

Renders DataFrame as an HTML table.
This renderer doesn't necessitate plugin installation since it's accessible within the flytekit library.

```python
from typing import Annotated

from union.deck import TopFrameRenderer


@task(enable_deck=True, container_image=custom_image)
def top_frame_renderer() -> Annotated[pd.DataFrame, TopFrameRenderer(1)]:
    return pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
```

![Top frame renderer](https://raw.githubusercontent.com/flyteorg/static-resources/main/flytesnacks/user_guide/flyte_decks_top_frame_renderer.png)

#### Markdown renderer

Converts a Markdown string into HTML, producing HTML as a Unicode string.

```python
@task(enable_deck=True, container_image=custom_image)
def markdown_renderer() -> None:
    flytekit.current_context().default_deck.append(
        MarkdownRenderer().to_html("You can install flytekit using this command: ```import flytekit```")
    )
```

![Markdown renderer](https://raw.githubusercontent.com/flyteorg/static-resources/main/flytesnacks/user_guide/flyte_decks_markdown_renderer.png)

#### Box renderer

Groups rows of DataFrame together into a
box-and-whisker mark to visualize their distribution.

Each box extends from the first quartile (Q1) to the third quartile (Q3).
The median (Q2) is indicated by a line within the box.
Typically, the whiskers extend to the edges of the box,
plus or minus 1.5 times the interquartile range (IQR: Q3-Q1).

```python
from flytekitplugins.deck.renderer import BoxRenderer


@task(enable_deck=True, container_image=custom_image)
def box_renderer() -> None:
    iris_df = px.data.iris()
    flytekit.Deck("Box Plot", BoxRenderer("sepal_length").to_html(iris_df))
```

![Box renderer](https://raw.githubusercontent.com/flyteorg/static-resources/main/flytesnacks/user_guide/flyte_decks_box_renderer.png)

#### Image renderer

Converts a `FlyteFile` or `PIL.Image.Image` object into an HTML string,
where the image data is encoded as a base64 string.

```python
from union import workflow
from union.types.file import FlyteFile
from flytekitplugins.deck.renderer import ImageRenderer


@task(enable_deck=True, container_image=custom_image)
def image_renderer(image: FlyteFile) -> None:
    union.Deck("Image Renderer", ImageRenderer().to_html(image_src=image))


@workflow
def image_renderer_wf(
    image: FlyteFile = "https://bit.ly/3KZ95q4",
) -> None:
    image_renderer(image=image)
```

![Image renderer](https://raw.githubusercontent.com/flyteorg/static-resources/main/flytesnacks/user_guide/flyte_decks_image_renderer.png)

#### Table renderer

Converts a Pandas dataframe into an HTML table.

```python
from flytekitplugins.deck.renderer import TableRenderer


@task(enable_deck=True, container_image=custom_image)
def table_renderer() -> None:
    union.Deck(
        "Table Renderer",
        TableRenderer().to_html(df=pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]}), table_width=50),
    )
```

![Table renderer](https://raw.githubusercontent.com/flyteorg/static-resources/main/flytesnacks/user_guide/flyte_decks_table_renderer.png)

### Contribute to renderers

Don't hesitate to integrate a new renderer into
[renderer.py](https://github.com/flyteorg/flytekit/blob/master/plugins/flytekit-deck-standard/flytekitplugins/deck/renderer.py)
if your deck renderers can enhance data visibility.
Feel encouraged to open a pull request and play a part in enhancing the Flyte deck renderer ecosystem!

## Streaming Decks

Now you can visualize your deck directly if you call `Deck.publish()` in your code.

```python
from union.deck import Deck

@task(enable_deck=True)
def t_deck():
    Deck.publish()
```

You can click the refresh button and see the update until the deck succeeds.

[Union Deck Succeed Video](https://raw.githubusercontent.com/flyteorg/static-resources/2f3c3c26e9c0168c350bb8cb1bef1ece36ee60ee/flyte/user_guide/development_lifecycle/decks/deck_succeed.mp4)

When the task fails, you can also see the deck in the flyte console.

[Union Deck Fail Video](https://raw.githubusercontent.com/flyteorg/static-resources/2f3c3c26e9c0168c350bb8cb1bef1ece36ee60ee/flyte/user_guide/development_lifecycle/decks/deck_fail.mp4)

