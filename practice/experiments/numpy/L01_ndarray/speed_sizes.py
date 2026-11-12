import math
import time

import numpy as np

for n in (10_000, 1_000_000):
    xs = [i * 0.001 for i in range(n)]
    ys = [i * 0.002 for i in range(n)]
    zs = [i * 0.0005 for i in range(n)]
    X, Y, Z = np.array(xs), np.array(ys), np.array(zs)

    print(f"n = {n}")
    for run in range(3):
        start = time.perf_counter()
        dist_loop = [math.sqrt(x * x + y * y + z * z) for x, y, z in zip(xs, ys, zs)]
        loop_s = time.perf_counter() - start

        start = time.perf_counter()
        dist_vec = np.sqrt(X * X + Y * Y + Z * Z)
        vec_s = time.perf_counter() - start

        print(f"  run {run}: loop {loop_s * 1000:8.3f} ms   numpy {vec_s * 1000:7.3f} ms   "
              f"speedup {loop_s / vec_s:5.1f}x")