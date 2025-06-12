# error_handling.py

import asyncio

import flyte
import flyte.errors

env = flyte.TaskEnvironment(name="failure_handling", resources=flyte.Resources(cpu=1, memory="250Mi"))


@env.task
async def oomer(x: int):
    large_list = [0] * 100000000 * x  # This will cause an OOM error if x is too large
    print(len(large_list))


@env.task
async def always_succeeds() -> int:
    await asyncio.sleep(1)
    return 42


@env.task
async def error_handling() -> int:
    try:
        await oomer(1000)  # This is likely to cause an OOM error
    except flyte.errors.OOMError as e:
        print(f"Failed with oom trying with more resources: {e}, of type {type(e)}, {e.code}")
        try:
            await oomer.override(resources=flyte.Resources(cpu=1, memory="1Gi"))(5)
        except flyte.errors.OOMError as e:
            print(f"Failed with OOM Again giving up: {e}, of type {type(e)}, {e.code}")
            raise e
    finally:
        await always_succeeds()
    return await always_succeeds()


if __name__ == "__main__":
    flyte.init_from_config("./config.yaml")
    run = flyte.run(error_handling)
    print(run.name)
    print(run.url)
    run.wait(run)