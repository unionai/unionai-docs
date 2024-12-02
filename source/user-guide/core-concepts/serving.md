# Serving

Union lets you build and serve your own web apps, enabling you to build interactive dashboards and other interfaces to interact with and visualize data and models from your workflows,
using your favorite Python-based front-end frameworks (Streamlit, Gradio, Tensorboard, FastHTML, Dash, Panel, Voila, FiftyOne).

```{warning}
Serving on Union is an experimental feature. The API is subject to change.
```

## Example app

We will start with a simple app that consists only of the framework code that is need for an app and a small piece of custom logic that provides the functionality of the app.
This example uses Streamlit. Other frameworks are also available.

In a local directory, create the following files:

```{code-block} bash
.
├── app.py
├── main.py
└── utils.py
```

## App declaration

The file `app.py` contains the app declaration:

```{code-block} python
:caption: app.py
from union import App, Resources

app1 = App(
    name="streamlit-demo",
    container_image="ghcr.io/thomasjpfan/streamlit-app:0.1.37",
    command=[
        "streamlit",
        "hello",
        "--server.port",
        "8080",
    ],
    port=8080,
    include=[
        "./main.py",
        "./utils.py",
    ],
)
```
{@# TODO: replace the container_image URL with a permanent public example. #@}

Here the `App` constructor is initialized with the following parameters:

* `name`: The name of tha pp. This name will be displayed in app listings (via CLI and UI) and used to refer to the app when deploying and stopping.
* `container_image`: The container image that will be used to for the container that will run the app. Here we use a prebuilt container provided by Union that support Streamlit.
* `command`: The command that will be used within the container to start the app. The individual strings in this array will be concatenated and the invoked as a single command.
* `port`: The port of the app container from which the app will be served.

The parameters above are the minimum needed to initialize the app.
We add one more parameter:

* `include`: A list of files to be added to the container at deployment time, containing the custom code that defines the specific functionality of your app.

There are a few additional available parameters that we do not use in this example:

* requests:  A `flytekit.Resources` object defining the resource requests for the app container.
  The same object is used for the same purpose in the `@task` decorator in Union workflows  (see [Resource requests]() for details).
* limits: A `union.Resources` object defining the resource limits for the app container.
  The same object is used for the same purpose in the `@task` decorator in Union workflows  (see [Resource limits]() for details).
* min_replicas: The minimum number of replica containers permitted for this app.
  This defines the lower bound for auto-scaling the app. The default is 0 (see [App autoscaling]() for details)
* max_replicas: The maximum number of replica containers permitted for this app.
  This defines the upper bound for auto-scaling the app. The default is 1 (see [App autoscaling]() for details)
* inputs: A `List` of `union.app.Input` objects. Used to provide default inputs to the app on startup (see [App inputs]() for details).

We will examine these parameters in later examples.

## Custom code

In this example we include two files containing custom logic: `main.py` and `utils.py`.

The file `main.py` contains the actual Streamlit code:

```{code-block} python
:caption: main.py
import streamlit as st
from utils import process_user_input

st.title("Custom code demo")

user_input = st.text_input("Enter some text:")

if user_input:
    st.write("You entered:", process_user_input(user_input))
```

The file `utils.py` contains a supporting function that is imported into the Streamlit file, above.

```{code-block} python
:caption: utils.py
def process_user_input(value):
    return f"Processing {value}"
```

## Deploy the app

Deploy the app with:

```{code-block} bash
$ union deploy apps APP_FILE APP_NAME
```

* `APP_FILE` is the Python file that contains one or more app declarations.
* `APP_NAME` is the name of (one of) the declared apps in APP_FILE. The name of an app is the value of the `name` parameter passed into the `App` constructor.

If an app with the name `APP_NAME` does not yet exist on the system then this command creates that app and starts it.
If an ap by that name already exists then this command stops the app, updates its code and restarts it.

In this case, you would execute the following:

```{code-block}bash
$ union deploy apps app.py streamlit-demo
```

This will return output like the following:

```{code-block} bash
✨ Creating Application: streamlit-demo
Created Endpoint at: https://tight--river--9e001.apps.serving-mvp.us-west-2.union.ai
```

Click on the displayed endpoint to go to the app.

{@# TODO: add the screenshot once it is available
You should see something like this:

![A simple app](/_static/images/user-guide/core-concepts/serving/simple-app.png)
#@}

## How app deployment works

When a new app is deployed for the first time (i.e., there is no app registered with the specified `name`),
a container is spun up using the specified `container_image` and the files specified in `include` are
copied into the container. The `command` is the then executed in the container, starting the app.

If you alter the `include` code you need to re-deploy your app.
When `union deploy apps` is called using an app name that corresponds to an already existing app,
the app code is updated in the container and the app is restarted.

You can iterate on your app easily by changing your `include` code and re-deploying.

Because there is a slight performance penalty involved in copying the `include` files into the container,
you may wish to consolidate you code directly into custom built image once you have successfully iterated
to production quality.

## Viewing deployed apps

Go to **Apps** in the left sidebar in Union to see a a list of all your deployed apps:

![Apps list](/_static/images/user-guide/core-concepts/serving/apps-list.png)

To connect to an app click on its **Endpoint**.
To see more information about the app, click on its **Name**.
This will take you to the **App view**:

![Apps view](/_static/images/user-guide/core-concepts/serving/app-view.png)

Buttons to **Copy Endpoint** and **Start app** are available at the top of the view.
The **Overview** tab provides the information about app's properties, configuration, and event history:

The **Logs** tab provides a searchable and filterable view of the app's logs:

![Apps logs](/_static/images/user-guide/core-concepts/serving/app-logs.png)

You can also view all apps deployed in your Union instance from the command-line with:

```{code-block} bash
$ union get apps
```

This will display the app list:

```{code-block} bash
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━┳━━━━━━━━┓
┃ Name                                    ┃ Link       ┃ Status     ┃ Desired State ┃ CPU ┃ Memory ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━╇━━━━━━━━┩
│ streamlit-query-2                       │ Click Here │ Started    │ Stopped       │ 2   │ 2Gi    │
│ streamlit-demo-1                        │ Click Here │ Started    │ Started       │ 3   │ 2Gi    │
│ streamlit-query-3                       │ Click Here │ Started    │ Started       │ 2   │ 2Gi    │
│ streamlit-demo                          │ Click Here │ Unassigned │ Started       │ 2   │ 2Gi    │
└─────────────────────────────────────────┴────────────┴────────────┴───────────────┴─────┴────────┘
```

## Stopping apps

To stop an app from the command-line, perform the following command:

```{code-block} bash
$ union stop apps APP_NAME
```

* `APP_NAME` is the name of an app deployed on the Union instance.
