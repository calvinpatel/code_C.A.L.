import asyncio
import time

async def task(name, delay):
    print(f"{name} starting")
    await asyncio.sleep(delay)     # simulated I/O wait — parks this coroutine
    print(f"{name} done (waited {delay}s)")
    return f"{name}-result"

async def main():
    start = time.perf_counter()
    results = await asyncio.gather(
        task("A", 1),
        task("B", 2),
        task("C", 3),
    )
    elapsed = time.perf_counter() - start
    print(f"results: {results}")
    print(f"total elapsed: {elapsed:.2f}s")

asyncio.run(main())