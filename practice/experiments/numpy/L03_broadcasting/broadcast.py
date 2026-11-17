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

xyz = swc[:, 2:5]
voxel = np.array([0.5, 0.5, 2.0])   # µm per voxel along x, y, z

xyz_um = xyz * voxel
print(xyz.shape, voxel.shape, xyz_um.shape)
print(xyz_um)

off = xyz_um - xyz_um[0]
print(off)
print(off.shape)
print(xyz_um[0].shape)
print(off[0])

sq = off ** 2
print(sq.shape)
print(sq.sum(), sq.sum().shape)
print(sq.sum(axis=0), sq.sum(axis=0).shape)
print(sq.sum(axis=1), sq.sum(axis=1).shape)

dist = np.sqrt(sq.sum(axis=1))   # distance from the soma, in µm, one per point
print(dist)

lo = xyz_um.min(axis=0)
hi = xyz_um.max(axis=0)
print(lo, hi)
print(lo.shape, hi.shape)

pts = off[1:]      # every point except the soma, (5, 3)
r = dist[1:]       # their distances, (5,)
print(pts.shape, r.shape)
print(r[:, None].shape)   # None in an index adds a new axis of length 1 at that spot

unit = pts / r[:, None]
print(unit)
print(np.sqrt((unit ** 2).sum(axis=1)))   # each unit vector's length

rad = swc[:, 5]
scale = xyz_um * rad[:, None]   # scale each point by its radius, broadcasting the radius to match the shape of xyz_um
print(scale.shape)
summation = scale.sum(axis=0)   # sum of scaled coordinates for each point
center = summation / rad.sum()  # weighted average of coordinates, weighted by radius
print(center.shape)
print(center)