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

big = swc[:, 5] > 1.0
print(big)                          # P1

swc_ids = swc[big, 0]
print(swc_ids)                     # P2

print((swc[:, 5] < 1.0).sum())      # P3

apical = swc[swc[:, 1] == 4]        # P4: type 4 = apical dendrite
print(apical)
print(apical.shape)

dend = swc[swc[:, 1] == 3]          # P5
dend[:, 2:5] *= 0.5
print(dend[0])                      # P5a
print(swc[1])                       # P5b

