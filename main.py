from fastapi import FastAPI
from pydantic import BaseModel
from time import monotonic
import asyncio

app = FastAPI()

work_semaphore = asyncio.Semaphore(1)


class TestResponse(BaseModel):
    elapsed: float


async def work() -> None:
    await asyncio.sleep(3)


@app.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
    ts1 = monotonic()

    async with work_semaphore:
        await work()

    ts2 = monotonic()

    return TestResponse(elapsed=ts2 - ts1)
