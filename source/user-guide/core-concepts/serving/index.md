# Serving

Union lets you build and serve your own web apps, enabling you to build interactive dashboards and other interfaces to interact with and visualize data and models from your workflows,
using your favorite Python-based front-end frameworks (Streamlit, Gradio, Tensorboard, FastHTML, Dash, Panel, Voila, FiftyOne).

```{warning}
Serving on Union is an experimental feature. The API is subject to change.
```

## Example app

We will start with a simple Streamlit app (other frameworks are available).
In this case we will use the default Streamlit "Hello, World!" app.

In a local directory, create the following file:

```{code-block} shell
└── app.py
```

## App declaration

The file `app.py` contains the app declaration:

```{code-block} python
:caption: app.py

""" A simple Union app using Streamlit"""

import union

# The `ImageSpec` for the container that will run the `App`.
# `union-runtime` must be declared as a dependency, 
# in addition to any other dependencies needed by the app code.
# Set the environment variable `REGISTRY` to be the URI for your container registry.
image = union.ImageSpec(
    name="streamlit-app",
    packages=["union-runtime>=0.1.10", "streamlit==1.41.1"],
    registry=os.getenv("REGISTRY"),
)

# The `App` declaration.
# Uses the `ImageSpec` declared above.
# In this case we do not need to supply any app code 
# as we are using the built-in Streamlit `hello` app.
app = union.app.App(
    name="streamlit-hello",
    container_image=image,
    args=["streamlit", "hello", "--server.port", "8080"],
    port=8080,
    limits=union.Resources(cpu="2", mem="3Gi"),
)
```

Here the `App` constructor is initialized with the following parameters:

* `name`: The name of the app. This name will be displayed in app listings (via CLI and UI) and used to refer to the app when deploying and stopping.
* `container_image`: The container image that will be used to for the container that will run the app. Here we use a prebuilt container provided by Union that support Streamlit.
* `command`: The command that will be used within the container to start the app. The individual strings in this array will be concatenated and the invoked as a single command.
* `port`: The port of the app container from which the app will be served.
* `limits`: A `union.Resources` object defining the resource limits for the app container.
  The same object is used for the same purpose in the `@union.task` decorator in Union workflows.
  See [The requests and limits settings](../tasks/task-hardware-environment/customizing-task-resources.md#the-requests-and-limits-settings) for details.

The parameters above are the minimum needed to initialize the app.

There are a few additional available parameters that we do not use in this example (but we will cover later):

* `include`: A list of files to be added to the container at deployment time, containing the custom code that defines the specific functionality of your app.
* `inputs`: A `List` of `union.app.Input` objects. Used to provide default inputs to the app on startup.
* `requests`: A `flytekit.Resources` object defining the resource requests for the app container. The same object is used for the same purpose in the `@union.task` decorator in Union workflows (see [The requests and limits settings](../tasks/task-hardware-environment/customizing-task-resources.md#the-requests-and-limits-settings) for details).
* `min_replicas`: The minimum number of replica containers permitted for this app.
  This defines the lower bound for auto-scaling the app. The default is 0 {@# TODO: (see [App autoscaling]() for details) #@}.
* `max_replicas`: The maximum number of replica containers permitted for this app.
  This defines the upper bound for auto-scaling the app. The default is 1 {@# TODO: (see [App autoscaling]() for details) #@}.

## Deploy the app

Deploy the app with:

```{code-block} shell
$ union deploy apps APP_FILE APP_NAME
```

* `APP_FILE` is the Python file that contains one or more app declarations.
* `APP_NAME` is the name of (one of) the declared apps in APP_FILE. The name of an app is the value of the `name` parameter passed into the `App` constructor.

If an app with the name `APP_NAME` does not yet exist on the system then this command creates that app and starts it.
If an app by that name already exists then this command stops the app, updates its code and restarts it.

In this case, we do the following:

```{code-block} shell
$ union deploy apps app.py streamlit-hello
```

This will return output like the following:

```{code-block} shell
✨ Creating Application: streamlit-demo
Created Endpoint at: https://withered--firefly--8ca31.apps.demo.hosted.unionai.cloud/
```

Click on the displayed endpoint to go to the app:

![A simple app](/_static/images/user-guide/core-concepts/serving/streamlit-hello.png)

## Viewing deployed apps

Go to **Apps** in the left sidebar in Union to see a list of all your deployed apps:

![Apps list](/_static/images/user-guide/core-concepts/serving/apps-list.png)

To connect to an app click on its **Endpoint**.
To see more information about the app, click on its **Name**.
This will take you to the **App view**:

![App view](/_static/images/user-guide/core-concepts/serving/app-view.png)

Buttons to **Copy Endpoint** and **Start app** are available at the top of the view.

You can also view all apps deployed in your Union instance from the command-line with:

```{code-block} shell
$ union get apps
```

This will display the app list:

```{code-block} shell
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

```{code-block} shell
$ union stop apps --name APP_NAME
```

* `APP_NAME` is the name of an app deployed on the Union instance.
