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

UM_PER_VOXEL = 0.5

has_parent = swc[:, 6] != -1                  # every row except the root
child = swc[has_parent]                       # (5, 7): one row per segment
parent_pos = child[:, 6].astype(int) - 1      # parent id -> row position
parent = swc[parent_pos]                      # (5, 7): each child's parent, lined up

print(parent_pos)
print(child[:, 0])                            # child ids
print(parent[:, 0])                           # their parents' ids

d = child[:, 2:5] - parent[:, 2:5]            # (5, 3): dx, dy, dz per segment
seg = np.sqrt(d[:, 0]**2 + d[:, 1]**2 + d[:, 2]**2) * UM_PER_VOXEL
print(seg)
print(seg.sum())

print(swc[[5, 5, 1], 1])                                     # G1
print(swc[[1, 3]].shape, np.shares_memory(swc[[1, 3]], swc)) # G2

dendrites = swc[swc[:, 1] == 3]
parent_position = dendrites[:, 6].astype(int) - 1
parent = swc[parent_position]
d = dendrites[:, 2:5] - parent[:, 2:5]
seg = np.sqrt(d[:, 0]**2 + d[:, 1]**2 + d[:, 2]**2) * UM_PER_VOXEL
print(seg.sum())

swc[[1, 3]][:, 5] = 0.0                                      # G4a
swc[[1, 3], 5] = 9.9                                         # G4b
print(swc[:, 5])