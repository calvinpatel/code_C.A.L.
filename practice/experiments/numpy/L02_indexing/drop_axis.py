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
tmp = swc[thin]                 # rows 2, 4, 5 copied into a new block
tmp[:, 5] = 1.0
print(tmp.shape)

col_int = tmp[:, 5]             # integer on axis 1: axis 1 dropped
print(col_int, col_int.shape)

col_slice = tmp[:, 5:6]         # width-1 slice on axis 1: axis 1 kept
print(col_slice)
print(col_slice.shape)

row = tmp[0]                    # integer on axis 0: axis 0 dropped
print(row, row.shape)