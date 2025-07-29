# scaling.py

import asyncio

import flyte

env = flyte.TaskEnvironment("large_fanout")


@env.task
async def my_task(x: int) -> int:
    return x


@env.task
async def main(r: int):
    results = []
    with flyte.group("fanout-group"):
        for i in range(r):
            results.append(my_task(x=i))
        result = await asyncio.gather(*results)
        
    return result


if __name__ == "__main__":
    flyte.init_from_config("config.yaml")

    run = flyte.run(main, r=50)
    print(run.url)
    run.wait(run)
