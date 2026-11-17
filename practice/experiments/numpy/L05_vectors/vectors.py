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

xyz_um = swc[:, 2:5] * np.array([0.5, 0.5, 2.0])   # voxels -> µm
off = xyz_um - xyz_um[0]                           # arrow from soma to each point
dist = np.sqrt((off ** 2).sum(axis=1))             # length of each arrow
unit = off[1:] / dist[1:, None]                    # each arrow at length 1 (soma skipped)

print(off)
print(dist)
print(unit)

axon_dir = off[5] / dist[5]     # unit vector from the soma toward the axon tip (row 5, id 6)
reach = off @ axon_dir
print(reach.shape)
print(reach)

a = unit[0]                          # id 2's direction (length 1)
b = unit[2]                          # id 4's direction (length 1)

c = a @ b                            # the cosine of the angle between them
print(c)
print(np.degrees(np.arccos(c)))      # arccos gives radians; np.degrees converts

print(np.degrees(np.arccos(np.array([1.0, 0.0, -1.0]))))   # the three landmarks

ang = np.degrees(np.arccos(unit @ unit[4]))
print(ang.shape)
print(ang)