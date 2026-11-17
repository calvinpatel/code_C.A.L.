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

xyz_um = swc[:, 2:5] * np.array([0.5, 0.5, 2.0])  # voxels -> microns
off = xyz_um - xyz_um[0]                          # (6, 3) arrows from the soma
dist = np.sqrt((off ** 2).sum(axis=1))            # (6,) arrow lengths
unit = off[1:] / dist[1:, None]                   # (5, 3) directions; unit row k = id k + 2
pia = np.array([0.0, 0.8, 0.6])                   # invented direction toward the brain surface

print(off)

#Core idea 1 · A matrix moves every point at once
across = np.array([1.0, 0.0, 0.0])   # the old x axis, kept as it is (chosen)
third = np.array([0.0, -0.6, 0.8])   # invented: at right angles to across and pia

M = np.column_stack([across, pia, third])   # each ruler becomes one column
print(M)

aligned = off @ M                            # (6, 3) @ (3, 3) -> (6, 3)
print(aligned)

print(np.sqrt((aligned ** 2).sum(axis=1)))   # lengths after the turn
print(dist)                                  # lengths before

print("\n")
across_turn = np.array([0.0, 1.0, 0.0])
pia_turn = np.array([-1.0, 0.0, 0.0])
third_turn = np.array([0.0, 0.0, 1.0])

M_turn = np.column_stack([across_turn, pia_turn, third_turn])
print(M_turn)

turned = off @ M_turn
print(turned[1])
print(np.sqrt((turned ** 2).sum(axis=1)))   # lengths after the turn

#Core idea 2 · unit @ unit.T compares every pair at once
print("\n")
cos_all = unit @ unit.T             # (5, 3) @ (3, 5) -> (5, 5)
print(cos_all.shape)
print(np.round(cos_all, 2))         # rounded to 2 decimals for reading
print(np.round(cos_all[:, 4], 2))   # column 4: every branch vs row 4 (id 6, the axon)

ang_all = np.degrees(np.arccos(cos_all))
print(ang_all.shape)
print(ang_all[4])


