import asyncio, time

"""Component 1 — Timeouts: cancellation wearing a stopwatch"""
# async def llm_call(name, delay):
#     print(f"{name}: request sent")
#     try:
#         await asyncio.sleep(delay)
#         return f"{name} - response"
#     except asyncio.CancelledError:
#         print(f"{name}: cancelled from the inside")
#         raise
#     finally:
#         print(f"{name}: connection closed")
#
#
# async def main():
#     # Round 1: fast task, generous clock
#     r1 = await asyncio.wait_for(llm_call("FAST", 1), timeout=3.0)
#     print(f"Round 1 result: {r1}")
#
#     # Round 2: slow task, tight clock
#     try:
#         r2 = await asyncio.wait_for(llm_call("SLOW", 5), timeout=2.0)
#         print(f"Round 2 result: {r2}")
#     except TimeoutError:
#         print(f"Round 2: timeout error caught in main")
#
#
# asyncio.run(main())


"""Component 2 - Semaphore: full concurrency, bounded width"""
# START = time.perf_counter()
#
# def t():
#     return f"{time.perf_counter() - START:0.2f}s"
#
# async def fetch(name, sem):
#     async with sem:                         # acquire a permit (may park HERE)
#         print(f"{t()} {name}: start fetch")
#         await asyncio.sleep(1)              # simulate a network operation, API call
#         print(f"{t()} {name}: done fetch")
#         return f"{name} - ok"
#
# async def main():
#     sem = asyncio.Semaphore(1)              # limit to 3 concurrent fetches
#     names = ["A", "B", "C", "D", "E", "F"]
#     results = await asyncio.gather(*(fetch(n, sem) for n in names))
#     print(f"{t()} results: {results}")
#
# asyncio.run(main())


"""Component 3 - asyncio.to_thread: the escape hatch for blocking code"""
# START = time.perf_counter()
# def t(): return f"{time.perf_counter() - START:.2f}s"
#
# def legacy_parse():
#     time.sleep(2)               # sync library code — blocks its thread
#     return "parsed"
#
# async def main():
#     print(f"{t()} batch: shipping three parses")
#     results = await asyncio.gather(
#         asyncio.to_thread(legacy_parse),
#         asyncio.to_thread(legacy_parse),
#         asyncio.to_thread(legacy_parse),
#     )
#     print(f"{t()} batch: {results}")
#
# asyncio.run(main())


"""Component 4 — Async generators: for-looping over the future"""
# START = time.perf_counter()
# def t(): return f"{time.perf_counter() - START:.2f}s"
#
# async def vitals_monitor(n):
#     for i in range(n):
#         await asyncio.sleep(0.5)
#         yield f"HR={70+i}"
#
# async def main():
#     try:
#         async with asyncio.timeout(1.2):
#             async for vitals in vitals_monitor(4):
#                 print(f"{t()} vitals: {vitals}")
#     except asyncio.TimeoutError:
#         print(f"{t()} timeout error caught in main")
#
#
# asyncio.run(main())