import numpy as np

# Columns: id, type, x, y, z, radius, parent   (x, y, z in voxels)
swc = np.array([
    [1, 1, 100, 200, 50, 6.0, -1],
    [2, 3, 104, 203, 50, 1.2,  1],
    [3, 3, 110, 209, 52, 0.9,  2],
    [4, 3,  96, 197, 49, 1.0,  1],
    [5, 3,  90, 190, 47, 0.8,  4],
    [6, 2, 112, 215, 53, 0.5,  1],
])

thin = swc[:, 5] < 1.0

swc[:, 5][thin] = 1.0                  # W1: the chain, the other way round
print(swc[:, 5])

print(thin)                            # W2a
print((swc[:, 5] < 1.0).sum())         # W2b

overshoot = swc[:, 5] > 5.0
swc[overshoot, 5] = 5.0
print(swc[:, 5])

dend_view = swc[1:5]
dend_copy = swc[swc[:, 1] == 3]
print(np.shares_memory(dend_view, swc), np.shares_memory(dend_copy, swc))   # W4