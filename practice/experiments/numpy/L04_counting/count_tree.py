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

parent_pos = swc[swc[:, 6] != -1, 6].astype(int) - 1

n_children = np.bincount(parent_pos, minlength=len(swc))
print(n_children.sum())

tips_id = swc[n_children == 0, 0]
print(tips_id)

xyz_um = swc[:, 2:5] * np.array([0.5, 0.5, 2.0])
off = xyz_um - xyz_um[0]
dist = np.sqrt((off ** 2).sum(axis=1))
print(dist)

order = np.argsort(dist)      # row positions, smallest dist first
print(order)
print(dist[order])            # gather dist with it: now sorted
print(swc[order, 0])          # gather swc rows with it: ids, nearest first

r_order = np.argsort(swc[:, 5])
print(r_order)
print(swc[r_order, 0])          # gather swc rows with it: ids, smallest radius first
print(swc[r_order[-1], 0])      # the last (largest) radius

step = 3.0                             # shell width, µm
print(dist // step)                    # // divides, then rounds down
shell = (dist // step).astype(int)     # whole-number labels for bincount
print(shell)
counts = np.bincount(shell)            # points per shell
print(counts)
print(np.arange(len(counts)) * step)   # where each shell starts, in µm