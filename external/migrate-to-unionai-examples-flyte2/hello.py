# hello.py

# /// script
# requires-python = "==3.13"
# dependencies = [
#    "flyte==0.2.0b23",
# ]
# ///

import flyte

# A TaskEnvironment provides a way of grouping the configuration used by tasks.
env = flyte.TaskEnvironment(name="hello_world", resources=flyte.Resources(memory="250Mi"))

# Use a TaskEnvironment to define tasks, which are regular Python functions.
@env.task
def fn(x: int) -> int: # Type annotations are recommended.
    slope, intercept = 2, 5
    return slope * x + intercept

# Tasks can call other tasks.
# All tasks defined with a given TaskEnvironment will run in their own separate containers,
# but those containers will all be configured identically.
@env.task
def main(x_list: list[int]) -> float:

    x_len = len(x_list)
    if x_len < 10:
        raise ValueError(f"x_list doesn't have a larger enough sample size, found: {x_len}")

    # flyte.map is like Python map, but runs in parallel.
    y_list = list(flyte.map(fn, x_list))
    y_mean = sum(y_list) / len(y_list)
    return y_mean

# Running this script locally will perform a flyte.run, sending your task code to your remote Union/Flyte instance.
if __name__ == "__main__":

    # Establish a remote connection from within your script.
    flyte.init_from_config("config.yaml")

    # Run your tasks remotely inline and pass parameter data.
    run = flyte.run(main, x_list=list(range(10)))

    # Print various attributes of the run.
    print(run.name)
    print(run.url)

    # Stream the logs from the remote run to the terminal.
    run.wait(run)