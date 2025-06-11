# hello.py

import asyncio
from typing import List

import flyte

env = flyte.TaskEnvironment(name="hello_world")


@env.task
async def say_hello(data: str, lt: List[int]) -> str:
    print(f"say_hello - {flyte.ctx().action}")
    return f"Hello {data} {lt}"


@env.task
async def square(i: int = 3) -> int:
    print(f"square - {flyte.ctx().action}")
    return i * i


@env.task
async def hello_wf(data: str = "default string") -> str:
    print(f"hello_wf - {flyte.ctx().action}")
    coros = []
    for i in range(3):
        coros.append(square(i=i))

    vals = await asyncio.gather(*coros)
    return await say_hello(data=data, lt=vals)


if __name__ == "__main__":
    flyte.init_auto_from_config("./config.yaml")
    run = flyte.run(hello_wf, data="hello world")
    print(run.name)
    print(run.url)
    run.wait(run)