from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from scipy.sparse import csr_array
from scipy.sparse.csgraph import dijkstra

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
    [9, 3,  98, 194, 25, 0.5,  4],
])
N = len(swc)
ids = swc[:, 0].astype(int)
xyz_um = swc[:, 2:5] * 0.5                       # 0.5 µm per voxel
off = xyz_um - xyz_um[0]                         # µm from the soma

# row lookup and segments
row_of = np.full(ids.max() + 1, -1)
row_of[ids] = np.arange(N)
child = swc[swc[:, 6] != -1]
child_pos = row_of[child[:, 0].astype(int)]
parent_pos = row_of[child[:, 6].astype(int)]
d = xyz_um[child_pos] - xyz_um[parent_pos]
seg = np.sqrt((d ** 2).sum(axis=1))              # µm per segment

# path length: µm along the tree from the soma
G = csr_array((seg, (child_pos, parent_pos)), shape=(N, N))
path = dijkstra(G, directed=False, indices=0)

# branch order: forks passed on the way out
n_children = np.bincount(parent_pos, minlength=N)
order_w = (n_children >= 2)[parent_pos].astype(float)
G_order = csr_array((order_w, (child_pos, parent_pos)), shape=(N, N))
order = dijkstra(G_order, directed=False, indices=0)

# top-view segments for drawing
segs = np.stack([xyz_um[parent_pos, :2], xyz_um[child_pos, :2]], axis=1)  # (8, 2, 2)

print("path :", path.round(2))
print("order:", order)


# Core idea 1: Colour carries a number
fig, ax = plt.subplots()
ax.add_collection(LineCollection(segs, color="lightgray"))
dots = ax.scatter(xyz_um[:, 0], xyz_um[:, 1], c=path, cmap="viridis")
fig.colorbar(dots, ax=ax, label="path length (µm)")
ax.set_aspect("equal")
fig.savefig(HERE / "by_path.png", dpi=150)

fig, ax = plt.subplots()
ax.add_collection(LineCollection(segs, color="lightgray"))
dots = ax.scatter(xyz_um[:, 0], xyz_um[:, 1], c=order, cmap="viridis")
fig.colorbar(dots, ax=ax, label="branch order")
ax.set_aspect("equal")
fig.savefig(HERE / "by_order.png", dpi=150)


# Core idea 2: A table as a picture
small = np.array([[0, 1, 2],
                  [3, 4, 5]])
fig, ax = plt.subplots()
im = ax.imshow(small)
fig.colorbar(im, ax=ax)
fig.savefig(HERE / "small_grid.png", dpi=150)

dist = np.sqrt((off ** 2).sum(axis=1))  # µm from soma
unit = off[1:] / dist[1:, None]         # unit vector from soma to each point, (8, 3): row k is id k + 2
cos_all = unit @ unit.T                 # (8, 8) cosine of angle between each pair of points

fig, ax = plt.subplots()
im = ax.imshow(cos_all)
fig.colorbar(im, ax=ax, label="cosine")
ax.set_xticks(range(8), ids[1:])        # tick positions 0–7, labelled with ids 2–9
ax.set_yticks(range(8), ids[1:])
fig.savefig(HERE / "cosine_grid.png", dpi=150)

plt.show()