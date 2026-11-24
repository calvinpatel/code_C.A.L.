from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection   # draws many line pieces as one object

HERE = Path(__file__).parent

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
xyz_um = swc[:, 2:5] * np.array([0.5, 0.5, 2.0])   # voxels -> µm
ids = swc[:, 0].astype(int)
x = xyz_um[:, 0]
y = xyz_um[:, 1]


row_of = np.full(ids.max() + 1, -1)
row_of[ids] = np.arange(len(ids))
child = swc[swc[:, 6] != -1]
child_pos = row_of[child[:, 0].astype(int)]
parent_pos = row_of[child[:, 6].astype(int)]

parent_xy = xyz_um[parent_pos, :2]   # (7, 2): each segment's parent point, x and y
child_xy = xyz_um[child_pos, :2]     # (7, 2): each segment's child point, x and y
segs = np.stack([parent_xy, child_xy], axis=1)

print(ids[parent_pos])
print(ids[child_pos])
print(segs.shape)
print(segs[:2])


fig, ax = plt.subplots()
ax.plot(x, y, marker="o")          # marker="o": a dot at each point as well
for k in range(len(ids)):
    ax.text(x[k], y[k], ids[k])    # writes id k at its point
ax.set_xlabel("x (µm)")
ax.set_ylabel("y (µm)")
fig.savefig(HERE / "zigzag.png", dpi=150)

fig, ax = plt.subplots()
ax.add_collection(LineCollection(segs))   # one object holding all 7 segments
for k in range(len(ids)):
    ax.text(x[k], y[k], ids[k])
ax.set_xlabel("x (µm)")
ax.set_ylabel("y (µm)")
fig.savefig(HERE / "tree.png", dpi=150)
print(len(ax.collections), len(ax.lines))   # what's on the Axes: collections, lines

dendrites = swc[child_pos, 1] == 3
dend_segs = segs[dendrites]
fig, ax = plt.subplots()
ax.add_collection(LineCollection(dend_segs))
ax.set_xlabel("x (µm)")
ax.set_ylabel("y (µm)")
fig.savefig(HERE / "dendrites.png", dpi=150)
print(dend_segs.shape)

fig, ax = plt.subplots()
ax.add_collection(LineCollection(segs))
ax.plot([51, 56, 56], [95.5, 95.5, 100.5], color="black")   # 5 µm across, then 5 µm up
ax.set_xlabel("x (µm)")
ax.set_ylabel("y (µm)")
fig.savefig(HERE / "bar.png", dpi=150)

fig, ax = plt.subplots()
ax.add_collection(LineCollection(segs))
ax.plot([51, 56, 56], [95.5, 95.5, 100.5], color="black")
ax.set_aspect("equal")                    # 1 µm the same length on x and y
ax.set_xlabel("x (µm)")
ax.set_ylabel("y (µm)")
fig.savefig(HERE / "bar_equal.png", dpi=150)

fig, ax = plt.subplots(figsize=(10, 4.8))   # 10 inches wide, 4.8 inches tall
ax.add_collection(LineCollection(segs))
ax.plot([51, 56, 56], [95.5, 95.5, 100.5], color="black")
ax.set_xlabel("x (µm)")
ax.set_ylabel("y (µm)")
fig.savefig(HERE / "wide.png", dpi=150)

fig, ax = plt.subplots(figsize=(10, 4.8))   # 10 inches wide, 4.8 inches tall
ax.add_collection(LineCollection(segs))
ax.plot([51, 56, 56], [95.5, 95.5, 100.5], color="black")
ax.set_aspect("equal")
ax.set_xlabel("x (µm)")
ax.set_ylabel("y (µm)")
fig.savefig(HERE / "wide_equal.png", dpi=150)

plt.show()