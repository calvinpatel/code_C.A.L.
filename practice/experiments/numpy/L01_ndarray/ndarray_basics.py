import numpy as np

# A tiny made-up reconstruction: 6 traced points.
# Coordinates are in voxels; point 0 is the soma.
x_vox = [100, 104, 110, 96, 90, 112]
y_vox = [200, 203, 209, 197, 190, 215]
z_vox = [50, 50, 52, 49, 47, 53]

UM_PER_VOXEL = 0.5  # microns per voxel, same along x, y and z

x_raw = np.array(x_vox)
print("x_raw:", x_raw, x_raw.dtype, x_raw.shape)

x = x_raw * UM_PER_VOXEL
y = np.array(y_vox) * UM_PER_VOXEL
z = np.array(z_vox) * UM_PER_VOXEL
print("x (µm):", x, x.dtype, x.shape)

dx = x - x[0]
dy = y - y[0]
dz = z - z[0]
dist = np.sqrt(dx**2 + dy**2 + dz**2)
print("distance from soma (µm):", dist)