import pytest
import httpx
import asyncio
from main import app


@pytest.mark.asyncio
async def test_handler_elapsed_time_difference():
    async with httpx.AsyncClient(app=app, base_url="http://testserver") as client:
        responses = await asyncio.gather(
            client.get("/test"),
            client.get("/test"),
        )

    elapsed_times = [response.json()["elapsed"] for response in responses]
    assert abs(elapsed_times[0] - elapsed_times[1]) >= 3.0
