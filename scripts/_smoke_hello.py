"""Minimal hello task used as the smoke-test workload.

Kept in its own file so ``flyte.run`` bundles just this module (plus any
sys.path roots it depends on) instead of the entire ``scripts`` directory.
Smoke callers import ``run_hello`` — the task itself stays private.
"""

from __future__ import annotations

import logging
import uuid

import flyte

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-7s %(name)s - %(message)s",
)
logger = logging.getLogger("flyte.e2e.hello")

env = flyte.TaskEnvironment(name="e2e-hello", cache="disable")


@env.task
async def hello(nonce: str) -> str:
    logger.info(f"hello from e2e test! nonce={nonce}")
    return f"hello-{nonce}"


async def run_hello(nonce: str | None = None) -> "flyte.Run":
    """Submit the hello task with a fresh nonce. Returns the ``Run`` object.

    Caller is responsible for ``flyte.init`` having set endpoint+project+org;
    this function does not init.
    """
    return await flyte.run.aio(hello, nonce=nonce or str(uuid.uuid4()))
