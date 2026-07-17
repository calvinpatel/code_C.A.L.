import asyncio, time

# async def fetch(name, delay, *, fail=False):
#     print (f"{name} starting")
#     await asyncio.sleep(delay)
#     if fail:
#         raise ValueError(f"{name} exploded")
#     print(f"{name} done")
#     return f"{name} result"


# async def main():
#     start = time.perf_counter()
#     try:
#         results = await asyncio.gather(
#             fetch("A", 1, fail=True),
#             fetch("B", 2),
#             fetch("C", 3),
#             return_exceptions=True
#         )
#         print(f"results: {results} (t={time.perf_counter() - start:.2f}s)")
#     except ValueError as e:
#         print(f"caught: {e}  (t={time.perf_counter() - start:.2f}s)")
#
#     print("--- main now does 3s of other work ---")
#     await asyncio.sleep(3)
#     print(f"main exiting  (t={time.perf_counter() - start:.2f}s)")

#asyncio.run(main())

# async def worker(name, delay):
#     try:
#         print(f"{name} starting")
#         await asyncio.sleep(delay)
#         print(f"{name} done")
#         return f"{name} result"
#     finally:
#         print(f"{name}: finally ran — cleanup happens on the way down")

# async def main():
#     start = time.perf_counter()
#     t = asyncio.create_task(worker("W", 1))
#     await asyncio.sleep(2)
#     print(f"cancel() returned: {t.cancel()}  (t={time.perf_counter() - start:.2f}s)")
#     try:
#         await t
#     except asyncio.CancelledError:
#         print(f"CancelledError delivered at pickup  (t={time.perf_counter() - start:.2f}s)")
#     print(f"t.cancelled() = {t.cancelled()}")

# asyncio.run(main())

# async def fetch(name, delay, *, fail=False):
#     try:
#         print(f"{name} starting")
#         await asyncio.sleep(delay)
#         if fail:
#             raise ValueError(f"{name} exploded")
#         print(f"{name} done")
#         return f"{name} - result"
#     except asyncio.CancelledError:
#         print(f"{name} was cancelled mid-flight")
#         raise

# async def main():
#     start = time.perf_counter()
#     try:
#         async with asyncio.TaskGroup() as tg:
#             ta = tg.create_task(fetch("A", 1, fail=True))
#             tb = tg.create_task(fetch("B", 2))
#             tc = tg.create_task(fetch("C", 3))
#         print("block exited normally")
#     except* ValueError as eg:
#         print(f"caught group: {eg.exceptions!r} (t={time.perf_counter() - start:.2f}s)")
#     print(f"main exiting (t={time.perf_counter() - start:.2f}s)")

# asyncio.run(main())