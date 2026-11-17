import numpy as np

swc = np.array([
    [1, 1, 100, 200, 50, 6.0, -1],
    [2, 3, 104, 203, 50, 1.2,  1],
    [3, 3, 110, 209, 52, 0.9,  2],
    [4, 3,  96, 197, 49, 1.0,  1],
    [5, 3,  90, 190, 47, 0.8,  4],
    [6, 2, 112, 215, 53, 0.5,  1],
])

print(swc[4, 5])                        # P1
print(swc[3, 2:5], swc[3, 2:5].shape)   # P2
print(swc[1:3, :2])                     # P3
print(swc[1:3, :2].shape)

xyz = swc[:, 2:5]
xyz *= 0.5                              # voxels -> microns
print(xyz[0])                           # P4a
print(swc[0])                           # P4b