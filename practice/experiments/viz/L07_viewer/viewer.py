from pathlib import Path

import numpy as np
import plotly.graph_objects as go
from scipy.sparse import csr_array
from scipy.sparse.csgraph import dijkstra

HERE = Path(__file__).parent

# Columns: id, type, x, y, z, radius, parent   (x, y, z in voxels; invented 9-point cell)
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

# --- setup: same maths as L04-L05, written out flat ---
ids = swc[:, 0].astype(int)
xyz_um = swc[:, 2:5] * 0.5                        # (9, 3) µm, 0.5 µm per voxel

row_of = np.full(ids.max() + 1, -1)
row_of[ids] = np.arange(len(ids))
child = swc[swc[:, 6] != -1]
child_pos = row_of[child[:, 0].astype(int)]       # (8,) one row per segment
parent_pos = row_of[child[:, 6].astype(int)]      # (8,)

N = len(swc)
seg = np.linalg.norm(xyz_um[child_pos] - xyz_um[parent_pos], axis=1)
path = dijkstra(csr_array((seg, (child_pos, parent_pos)), shape=(N, N)),
                directed=False, indices=0)        # µm along the tree from the soma

n_children = np.bincount(parent_pos, minlength=N)
order_w = (n_children >= 2)[parent_pos].astype(float)
order = dijkstra(csr_array((order_w, (child_pos, parent_pos)), shape=(N, N)),
                 directed=False, indices=0).astype(int)   # forks passed

segs3 = np.stack([xyz_um[parent_pos], xyz_um[child_pos]], axis=1)   # (8, 2, 3)

# print(path.round(2))
# print(order)
# print(segs3.shape)


# Core idea 1 · A plotly figure is data
dots = go.Scatter3d(x=xyz_um[:, 0], y=xyz_um[:, 1], z=xyz_um[:, 2],
                    mode="markers", name="points")
fig = go.Figure(dots)
fig.update_layout(title="9-point cell")
# print(fig.to_dict().keys())
# print(len(fig.data), fig.data[0].type)
# print(fig.data[0].z)
# fig.write_html(HERE / "cell.html", auto_open=True)

soma = go.Scatter3d(x=xyz_um[:1, 0], y=xyz_um[:1, 1], z=xyz_um[:1, 2],
                    mode="markers", name="soma")
fig = go.Figure([dots, soma])
fig.update_layout(title="soma")
# fig.write_html(HERE / "soma.html", auto_open=True)


# Core idea 2 · One trace for the whole tree
def none_lists(segs):
    xs, ys, zs = [], [], []
    for p, c in segs.tolist():
        xs += [p[0], c[0], None]
        ys += [p[1], c[1], None]
        zs += [p[2], c[2], None]
    return xs, ys, zs

xs, ys, zs = none_lists(segs3)
tree = go.Scatter3d(x=xs, y=ys, z=zs, mode="lines", name="tree")
fig = go.Figure([tree, dots])
# print(len(fig.data))
# fig.write_html(HERE / "cell.html", auto_open=True)

segs3_dend = segs3[swc[child_pos, 1] == 3]   # (7, 2, 3)
xs_d, ys_d, zs_d = none_lists(segs3_dend)
dend = go.Scatter3d(x=xs_d, y=ys_d, z=zs_d, mode="lines", name="dendrites", hoverinfo="skip")

segs3_axon = segs3[swc[child_pos, 1] == 2]   # (1, 2, 3)
xs_a, ys_a, zs_a = none_lists(segs3_axon)
axon = go.Scatter3d(x=xs_a, y=ys_a, z=zs_a, mode="lines", name="axon", hoverinfo="skip")

fig = go.Figure([dend, axon, dots])
# fig.write_html(HERE / "cell_type.html", auto_open=True)


# Core idea 3 · Hover shows each point's own numbers
dist = np.linalg.norm(xyz_um - xyz_um[0], axis=1)   # (9,) µm, soma to each point in one straight line
labels = [f"id {ids[k]}<br>path {path[k]:.2f} µm<br>order {order[k]}<br>straight {dist[k]:.2f} µm"   # <br>: line break in a plotly label
          for k in range(len(ids))]
print(len(labels))
print(labels[8])

dots = go.Scatter3d(x=xyz_um[:, 0], y=xyz_um[:, 1], z=xyz_um[:, 2],
                    mode="markers", name="points",
                    text=labels, hoverinfo="text",
                    marker=dict(color=path, colorscale="Viridis", cmin=0, cmax=15, showscale=True,
                                colorbar=dict(orientation="h", x=0.5, xanchor="center", y=-0.05, yanchor="top", len=0.7, thickness=15)))
fig = go.Figure([dend, axon, dots])
fig.update_layout(title="cell with hover labels and color by path length")
fig.update_layout(scene_aspectmode="data")
fig.write_html(HERE / "cell.html", auto_open=True)