import asyncio, time

async def fetch(name, delay):
    print(f"{name} starting")
    await asyncio.sleep(delay)
    print(f"{name} done")
    return f"{name}-result"

async def main():
    start = time.perf_counter()
    tb = asyncio.create_task(fetch("B", 2))   # Task
    a = await fetch("A", 3)                   # bare coroutine!
    b = await tb
    print(f"elapsed: {time.perf_counter() - start:.2f}s")

asyncio.run(main())