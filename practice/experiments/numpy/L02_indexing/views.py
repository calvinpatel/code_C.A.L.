import numpy as np

swc = np.array([
    [1, 1, 100, 200, 50, 6.0, -1],
    [2, 3, 104, 203, 50, 1.2,  1],
    [3, 3, 110, 209, 52, 0.9,  2],
    [4, 3,  96, 197, 49, 1.0,  1],
    [5, 3,  90, 190, 47, 0.8,  4],
    [6, 2, 112, 215, 53, 0.5,  1],
])


def to_microns(table):
    xyz = table[:, 2:5] * 0.5
    return xyz


a = to_microns(swc)
b = to_microns(swc)
print(a[0])                          # V1
print(b[0])                          # V2
print(swc[0])
print(np.shares_memory(a, b))        # V3

row = swc[5]
row[5] = 99.0
print(swc[5, 5])                     # V4

xyz_um = swc[:, 2:5] * 0.5
print(np.shares_memory(xyz_um, swc)) # V5