import numpy as np
from scipy.sparse import csr_array
from scipy.sparse.csgraph import dijkstra, connected_components   # connected_components: idea 2

# The 6-point cell from NumPy, L01's invented id 7, and an invented id 8
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
N = len(swc)

# --- from L01: rows, parents, segment lengths, the graph, path length ---
xyz_um = swc[:, 2:5] * np.array([0.5, 0.5, 2.0])   # voxels -> µm
ids = swc[:, 0].astype(int)
row_of = np.full(ids.max() + 1, -1)
row_of[ids] = np.arange(N)                          # id -> row
child = swc[swc[:, 6] != -1]                        # every point except the root
child_pos = row_of[child[:, 0].astype(int)]         # each child's own row
parent_pos = row_of[child[:, 6].astype(int)]        # its parent's row
d = xyz_um[child_pos] - xyz_um[parent_pos]
seg = np.sqrt((d ** 2).sum(axis=1))                 # one length per segment, µm

G = csr_array((seg, (child_pos, parent_pos)), shape=(N, N))
path = dijkstra(G, directed=False, indices=0)
print("child_pos :", child_pos)
print("parent_pos:", parent_pos)
print("seg       :", seg.round(2))
print("path      :", path.round(2))

# --- new: same walk, different weights ---
ones = np.ones(len(seg))                            # one 1.0 per segment
G_depth = csr_array((ones, (child_pos, parent_pos)), shape=(N, N))
depth = dijkstra(G_depth, directed=False, indices=0)
print("ones :", ones)
print("depth:", depth)


n_children = np.bincount(parent_pos, minlength=N)   # [3 1 2 1 0 0 0 0]
is_branch = n_children >= 2                         # one True/False per row: is it a fork?

order_w = is_branch[parent_pos].astype(float)       # your line: one weight per segment
G_order = csr_array((order_w, (child_pos, parent_pos)), shape=(N, N))
order = dijkstra(G_order, directed=False, indices=0)
print("order_w:", order_w)
print("order  :", order)


# --- new: how many pieces? ---
n, labels = connected_components(G, directed=False)
print("pieces:", n)
print("labels:", labels)
print("ids of points not in soma piece:", ids[labels != labels[0]])