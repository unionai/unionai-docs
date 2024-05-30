import base64
import html
import io
from textwrap import dedent

from flytekit import task, workflow, ImageSpec, Resources, current_context, Deck
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
)

image = ImageSpec(
    builder="unionai",
    requirements="requirements.txt",
)


@task(
    cache=True,
    cache_version="3",
    container_image=image,
    requests=Resources(cpu="2", mem="2Gi"),
)
def get_dataset() -> tuple[pd.DataFrame, pd.DataFrame]:
    dataset = fetch_openml(name="penguins", version=1, as_frame=True)
    train_dataset, test_dataset = train_test_split(
        dataset.frame, random_state=0, stratify=dataset.target
    )
    return train_dataset, test_dataset


@task(
    container_image=image,
    requests=Resources(cpu="3", mem="2Gi"),
)
def train_model(dataset: pd.DataFrame, max_bins: int) -> HistGradientBoostingClassifier:
    X_train, y_train = dataset.drop("species", axis="columns"), dataset["species"]
    hist = HistGradientBoostingClassifier(
        random_state=0, max_bins=max_bins, categorical_features="from_dtype"
    )
    return hist.fit(X_train, y_train)


@task(
    container_image=image,
    enable_deck=True,
    requests=Resources(cpu="2", mem="2Gi"),
)
def evaluate_model(
    model: HistGradientBoostingClassifier, dataset: pd.DataFrame
) -> float:
    ctx = current_context()

    X_test, y_test = dataset.drop("species", axis="columns"), dataset["species"]
    y_pred = model.predict(X_test)

    # Plot confusion matrix in deck
    fig, ax = plt.subplots()
    ConfusionMatrixDisplay.from_predictions(y_test, y_pred, ax=ax)

    metrics_deck = Deck("Metrics")
    metrics_deck.append(_convert_fig_into_html(fig))

    # Add classification report
    report = classification_report(y_test, y_pred)
    report_escaped = html.escape(report)
    html_report = dedent(
        f"""\
    <h2>Classification report</h2>
    <pre>{report_escaped}</pre>"""
    )
    metrics_deck.append(html_report)

    ctx.decks.insert(0, metrics_deck)

    return accuracy_score(y_test, y_pred)


@workflow
def main(max_bins: int) -> float:
    train, test = get_dataset()
    model = train_model(dataset=train, max_bins=max_bins)
    return evaluate_model(model=model, dataset=test)


def _convert_fig_into_html(fig: mpl.figure.Figure) -> str:
    img_buf = io.BytesIO()
    fig.savefig(img_buf, format="png")
    img_base64 = base64.b64encode(img_buf.getvalue()).decode()
    return f'<img src="data:image/png;base64,{img_base64}" alt="Rendered Image" />'
