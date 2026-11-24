from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

HERE = Path(__file__).parent
UM_PER_VOXEL = 0.5

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
    [9, 3,  98, 194, 25, 0.5,  4],   # new today (invented): a dendrite off id 4
])

ids = swc[:, 0].astype(int)
row_of = np.full(ids.max() + 1, -1)
row_of[ids] = np.arange(len(ids))
child = swc[swc[:, 6] != -1]
child_pos = row_of[child[:, 0].astype(int)]
parent_pos = row_of[child[:, 6].astype(int)]

xyz_um = swc[:, 2:5] * UM_PER_VOXEL
off = xyz_um - xyz_um[0]                 # µm from the soma, (9, 3)


# print(type(axs), axs.shape, axs.dtype)
# print(type(axs[0]))


segs3 = np.stack([off[parent_pos], off[child_pos]], axis=1)   # (8, 2, 3)

cols = [[0, 1], [0, 2], [1, 2]]          # the two coordinates each panel keeps
names = ["x", "y", "z"]
R = np.abs(off).max() + 1                # farthest reach on any axis, plus 1 µm
print(R)

fig, axs = plt.subplots(1, 3, figsize=(12, 4.4))
for k in range(3):
    a, b = cols[k]                       # panel k's pair, e.g. 0, 2 for x–z
    axs[k].add_collection(LineCollection(segs3[:, :, [a, b]]))
    axs[k].set_xlim(-R, R)
    axs[k].set_ylim(-R, R)
    axs[k].set_aspect("equal")
    axs[k].set_title(names[a] + "–" + names[b])
    axs[k].set_xlabel(names[a] + " from soma (µm)")
    axs[k].set_ylabel(names[b] + " from soma (µm)")

fig.savefig(HERE / "three_views.png", dpi=150)

plt.show()

same_spot = off[row_of[[6, 8]]][:, [0, 2]]   # x and z of ids 6 and 8, which are at the same spot
print(same_spot)