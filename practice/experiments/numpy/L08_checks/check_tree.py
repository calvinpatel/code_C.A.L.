from pathlib import Path
import numpy as np

HERE = Path(__file__).parent
swc = np.loadtxt(HERE / "broken.swc")
ids = swc[:, 0].astype(int)
row_of = np.full(ids.max() + 1, -1)
row_of[ids] = np.arange(len(ids))

child = swc[swc[:, 6] != -1]                  # every row except the root
parent_pos = row_of[child[:, 6].astype(int)]  # parent id -> parent row
print(child[:, 0])                            # child ids
print(child[:, 6])                            # parent ids, as written
print(parent_pos)
print(swc[parent_pos, 0])                     # ids found at those rows

vox = np.array([0.5, 0.5, 2.0])               # µm per voxel in x, y, z
d = (child[:, 2:5] - swc[parent_pos, 2:5]) * vox
seg = np.sqrt((d ** 2).sum(axis=1))           # segment lengths, µm
print(seg.round(2))


#1 · One answer from a whole mask
print("\n")
found = parent_pos >= 0          # one verdict per child
print(child[:, 0])               # child ids
print(found)
print(found.all())               # did every child find its parent?
print(found.any())               # did at least one?

if found.all():
    print("every parent found")
else:
    print("a parent is missing")

print((swc[:, 5] > 0).all())
print((swc[:, 5] > 0).any())

if (swc[:, 5] > 0).all():
    print("radii ok")
else:
    print("a radius is 0 or less")


#2 · Combining masks
print("\n")
dend = swc[:, 1] == 3            # type 3: dendrite
thin = swc[:, 5] < 1.0           # radius under 1 µm
print(swc[:, 0])                 # ids
print(dend)
print(thin)
print(dend & thin)               # True where BOTH are True
print(swc[dend & thin, 0])       # ids of thin dendrite points

print(swc[(swc[:, 1] == 1) | (swc[:, 1] == 2), 0])
print(child[~found, 0])                 # ids of children with missing parents