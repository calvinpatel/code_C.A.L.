# fastapi_arc/l6_async_endpoints.py
import asyncio
import time

import httpx
from fastapi import FastAPI

app = FastAPI()


# HOME 1: async def + honest await  -> event loop, cooperating
@app.get("/polite")
async def polite():
    await asyncio.sleep(1)          # stand-in for an async LLM/API call
    return {"endpoint": "polite"}


# HOME 2: async def + blocking call -> event loop, hostage (THE SIN)
@app.get("/hostage")
async def hostage():
    time.sleep(1)                   # stand-in for requests.get / sync DB / file parse
    return {"endpoint": "hostage"}


# HOME 3: plain def + blocking call -> threadpool, tolerated
@app.get("/threadpool")
def threadpool():
    time.sleep(1)                   # same blocking call, different home
    return {"endpoint": "threadpool"}


# HOME 4: async def + a blocking call correctly exiled via the escape hatch
@app.get("/rescued")
async def rescued():
    await asyncio.to_thread(time.sleep, 1)
    return {"endpoint": "rescued"}


async def hammer(path: str, n: int = 5) -> None:
    """Fire n CONCURRENT requests at one endpoint and time the batch."""
    transport = httpx.ASGITransport(app=app)    # fake network: straight into `app`
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        start = time.perf_counter()
        await asyncio.gather(*(client.get(path) for _ in range(n)))
        print(f"{path:<12}  {n} concurrent requests -> {time.perf_counter() - start:.2f}s")


async def main():
    await hammer("/polite")
    await hammer("/hostage")
    await hammer("/threadpool")
    await hammer("/rescued")

asyncio.run(main())