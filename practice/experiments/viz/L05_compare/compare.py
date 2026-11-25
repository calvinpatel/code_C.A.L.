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


def measure(swc):
    """L04's setup as one function: positions (µm), path length, branch order, top-view segments."""
    N = len(swc)
    ids = swc[:, 0].astype(int)
    xyz_um = swc[:, 2:5] * 0.5                       # 0.5 µm per voxel
    row_of = np.full(ids.max() + 1, -1)
    row_of[ids] = np.arange(N)
    child = swc[swc[:, 6] != -1]
    child_pos = row_of[child[:, 0].astype(int)]
    parent_pos = row_of[child[:, 6].astype(int)]
    d = xyz_um[child_pos] - xyz_um[parent_pos]
    seg = np.sqrt((d ** 2).sum(axis=1))              # µm per segment
    G = csr_array((seg, (child_pos, parent_pos)), shape=(N, N))
    path = dijkstra(G, directed=False, indices=0)
    n_children = np.bincount(parent_pos, minlength=N)
    order_w = (n_children >= 2)[parent_pos].astype(float)
    G_order = csr_array((order_w, (child_pos, parent_pos)), shape=(N, N))
    order = dijkstra(G_order, directed=False, indices=0)
    segs = np.stack([xyz_um[parent_pos, :2], xyz_um[child_pos, :2]], axis=1)
    return xyz_um, path, order, segs


ids = swc[:, 0].astype(int)
xyz_um, path, order, segs = measure(swc)          # the 9-point cell
xyz8, path8, order8, segs8 = measure(swc[:8])     # the 8-point cell: rows 0-7, no id 9

off = xyz_um - xyz_um[0]                          # µm from the soma
dist = np.sqrt((off ** 2).sum(axis=1))            # µm, straight line from the soma
unit = off[1:] / dist[1:, None]                   # (8, 3): row k is id k + 2
cos_all = unit @ unit.T                           # (8, 8)

print("path8 :", path8.round(2))
print("path  :", path.round(2))
print("order8:", order8)
print("order :", order)


# Core idea 1: Pin the colour scale
fig, axs = plt.subplots(1, 2, figsize=(10, 4.8))
for ax, xyz, p, sg, name in [(axs[0], xyz8, path8, segs8, "8 points"),
                             (axs[1], xyz_um, path, segs, "9 points")]:
    ax.add_collection(LineCollection(sg, color="lightgray"))
    dots = ax.scatter(xyz[:, 0], xyz[:, 1], c=p, vmin=0, vmax=15)   # same ends on both panels
    fig.colorbar(dots, ax=ax, label="path length (µm)")
    ax.set_title(name)
    ax.set_aspect("equal")
fig.savefig(HERE / "path_pinned.png", dpi=150)

fig, axs = plt.subplots(1, 2, figsize=(10, 4.8))
for ax, xyz, o, sg, name in [(axs[0], xyz8, order8, segs8, "8 points"),
                             (axs[1], xyz_um, order, segs, "9 points")]:
    ax.add_collection(LineCollection(sg, color="lightgray"))
    dots = ax.scatter(xyz[:, 0], xyz[:, 1], c=o, vmin=0, vmax=2)
    fig.colorbar(dots, ax=ax, label="branch order")
    ax.set_title(name)
    ax.set_aspect("equal")
fig.savefig(HERE / "order_pinned.png", dpi=150)


# Core idea 2: Signed values need a two-sided map centred on 0
row9 = cos_all[7:]
fig, ax = plt.subplots(figsize=(8, 2.5))
im = ax.imshow(row9, cmap="RdBu_r", vmin=-1, vmax=1)
ax.set_xticks(range(8), ids[1:])
ax.set_yticks([0], [9])
fig.colorbar(im, ax=ax, label="cosine")
fig.savefig(HERE / "row9_pinned.png", dpi=150)

fig, ax = plt.subplots(figsize=(8, 8))
im = ax.imshow(cos_all, cmap="RdBu_r", vmin=-1, vmax=1)
ax.set_xticks(range(8), ids[1:])
ax.set_yticks(range(8), ids[1:])
fig.colorbar(im, ax=ax, label="cosine")
fig.savefig(HERE / "cos_pinned.png", dpi=150)


# Core idea 3: Show every cell
wt = np.array([1998, 2345, 2245, 2239, 2534, 1602, 1793, 1564, 1964, 2330, 1993, 2164])
mut = np.array([2201, 1866, 2041, 1764, 1490, 1709, 1851, 1441, 2086, 2091, 1373, 1687])
wt4 = np.array([1450, 2700, 1907, 2200])
mut4 = np.array([1250, 2350, 1700, 1900])

rng = np.random.default_rng(0)
fig, ax = plt.subplots()
for x, cells in [(0, wt), (1, mut)]:
    jitter = rng.uniform(-0.1, 0.1, size=len(cells))
    ax.scatter(x + jitter, cells)
    ax.plot([x - 0.2, x + 0.2], [cells.mean(), cells.mean()], color="black")
ax.set_xticks([0, 1], ["wt", "mut"])
ax.set_ylabel("total length (µm)")
ax.set_ylim(1200, 2800)
fig.savefig(HERE / "strip.png", dpi=150)

rng = np.random.default_rng(0)
fig, ax = plt.subplots()
for x, cells in [(0, wt4), (1, mut4)]:
    jitter = rng.uniform(-0.1, 0.1, size=len(cells))
    ax.scatter(x + jitter, cells)
    ax.plot([x - 0.2, x + 0.2], [cells.mean(), cells.mean()], color="black")
ax.set_xticks([0, 1], ["wt4", "mut4"])
ax.set_ylabel("total length (µm)")
ax.set_ylim(1200, 2800)
fig.savefig(HERE / "strip4.png", dpi=150)

plt.show()