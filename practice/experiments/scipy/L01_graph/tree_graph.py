import numpy as np
from scipy.sparse import csr_array
from scipy.sparse.csgraph import dijkstra

# The 6-point cell from NumPy (same points as cell.swc)
# Columns: id, type, x, y, z, radius, parent   (x, y, z in voxels)
swc = np.array([
    [1, 1, 100, 200, 50, 6.0, -1],
    [2, 3, 104, 203, 50, 1.2,  1],
    [3, 3, 110, 209, 52, 0.9,  2],
    [4, 3,  96, 197, 49, 1.0,  1],
    [5, 3,  90, 190, 47, 0.8,  4],
    [6, 2, 112, 215, 53, 0.5,  1],
    [7, 3, 113, 212, 54, 0.6,  3],
])
N = len(swc)

# --- known from NumPy: rows, parents, segment lengths ---
xyz_um = swc[:, 2:5] * np.array([0.5, 0.5, 2.0])   # voxels -> µm
ids = swc[:, 0].astype(int)
row_of = np.full(ids.max() + 1, -1)
row_of[ids] = np.arange(N)                          # id -> row
child = swc[swc[:, 6] != -1]                        # every point except the root
child_pos = row_of[child[:, 0].astype(int)]         # each child's own row
parent_pos = row_of[child[:, 6].astype(int)]        # its parent's row
d = xyz_um[child_pos] - xyz_um[parent_pos]
seg = np.sqrt((d ** 2).sum(axis=1))                 # one length per segment, µm
# print(child_pos, parent_pos, seg.round(2))

# --- new: the tree as a sparse matrix ---
G = csr_array((seg, (child_pos, parent_pos)), shape=(N, N))
print(G)
# print("stored cells:", G.nnz)
# print("G[2, 1] =", G[2, 1])
# print(G.toarray().round(2))


# --- new: path length from the soma to every point ---
path = dijkstra(G, directed=False, indices=2)
print("path:", path.round(2))

# straight-line distance, for comparison (NumPy L03)
off = xyz_um - xyz_um[0]
dist = np.sqrt((off ** 2).sum(axis=1))
print("dist:", dist.round(2))