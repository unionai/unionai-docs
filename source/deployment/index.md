# Deployment

Union.ai uses a hybrid model cloud service: Union.ai maintains the control plane of the application on its own cloud infrastructure in Amazon Web Services (AWS).
This is where all administration and management functionality resides.

Your data and the actual computation involved in executing your Flyte tasks and workflows takes place on the data plane, a virtual private cloud that you control but that is administered and managed by the Union.ai control plane.
To enable the administration and management of your data plane, you grant Union.ai the required permissions when you set up your data plane.

Union.ai supports data planes on Amazon WebServices (AWS), Google Cloud Platform (GCP), and Microsoft Azure.
