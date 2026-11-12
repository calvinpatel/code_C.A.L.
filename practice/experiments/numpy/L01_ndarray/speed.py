import math
import time

import numpy as np

n = 1_000_000
xs = [i * 0.001 for i in range(n)]
ys = [i * 0.002 for i in range(n)]
zs = [i * 0.0005 for i in range(n)]

start = time.perf_counter()
dist_loop = [math.sqrt(x * x + y * y + z * z) for x, y, z in zip(xs, ys, zs)]
loop_s = time.perf_counter() - start
print(f"loop:    {loop_s:.4f} s")

# --- your NumPy version below ---

start = time.perf_counter()
xs_np = np.array(xs)
ys_np = np.array(ys)
zs_np = np.array(zs)
convert_s = time.perf_counter() - start
print(f"NumPy convert:   {convert_s:.4f} s")

start = time.perf_counter()
dist_np = np.sqrt(xs_np * xs_np + ys_np * ys_np + zs_np * zs_np)
vec_s = time.perf_counter() - start
print(f"NumPy vectorized:   {vec_s:.4f} s")
print(f"NumPy speedup: {loop_s / vec_s:.4f}x")
print(dist_np.dtype, dist_np.shape)
print(dist_np[-1])
