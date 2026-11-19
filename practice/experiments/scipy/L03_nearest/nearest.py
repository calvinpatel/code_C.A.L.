import numpy as np
from scipy.spatial import KDTree

# Columns: id, type, x, y, z, radius, parent   (x, y, z in voxels)
swc = np.array([
    [1, 1, 100, 200, 50, 6.0, -1],
    [2, 3, 104, 203, 50, 1.2,  1],
    [3, 3, 110, 209, 52, 0.9,  2],
    [4, 3,  96, 197, 49, 1.0,  1],
    [5, 3,  90, 190, 47, 0.8,  4],
    [6, 2, 112, 215, 53, 0.5,  1],
    [7, 3, 113, 212, 54, 0.6,  3],
    [8, 3, 112, 207, 53, 0.5,  3],
])
ids = swc[:, 0].astype(int)                         # SWC id of each row
xyz_um = swc[:, 2:5] * np.array([0.5, 0.5, 2.0])    # positions in µm

# Invented for today: three synapse markers, already in µm (one per row)
syn = np.array([
    [45.5,  96.0,  95.0],
    [56.4, 105.0, 107.0],
    [70.0,  90.0, 100.0],
])

print(xyz_um)

kd = KDTree(xyz_um)          # build once: sort the traced points into nested boxes
dd, rows = kd.query(syn)     # each marker's nearest traced point

print(dd)                    # distance to it (µm)
print(rows)                  # its row in xyz_um
print(ids[rows])             # its SWC id

m = np.array([52.0, 101.5, 100.5])
dd_m, rows_m = kd.query(m)             # nearest traced point to a single marker
print(dd_m)                            # distance to it (µm)
print(rows_m)                          # its row in xyz_um
print(ids[rows_m])                     # its SWC id


near = kd.query_ball_point(syn, r=3.0)   # every traced point within 3.0 µm of each marker
print(near)

for k in range(len(syn)):
    print(k, ids[near[k]])               # rows -> SWC ids