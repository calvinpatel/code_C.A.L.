from pathlib import Path
import numpy as np

HERE = Path(__file__).parent
cell = np.loadtxt(HERE / 'cell.swc')

# Columns: id, type, x, y, z, radius, parent   (hand-typed in L02)
swc = np.array([
    [1, 1, 100, 200, 50, 6.0, -1],
    [2, 3, 104, 203, 50, 1.2,  1],
    [3, 3, 110, 209, 52, 0.9,  2],
    [4, 3,  96, 197, 49, 1.0,  1],
    [5, 3,  90, 190, 47, 0.8,  4],
    [6, 2, 112, 215, 53, 0.5,  1],
])

# your line: print how many cells differ between cell and swc
diff = np.sum(cell != swc)
print(f"Number of differing cells: {diff}")


ids = np.array([3, 1, 4])
row_of = np.full(ids.max() + 1, -1)
row_of[ids] = np.arange(len(ids))
print(row_of)


swc = np.loadtxt(HERE / "edited.swc")

ids = swc[:, 0].astype(int)              # whole numbers: float positions raise (L02)
row_of = np.full(ids.max() + 1, -1)      # 8 slots, all -1 ("no such id")
row_of[ids] = np.arange(len(ids))        # slot id gets that id's row
print(ids)
print(row_of)

child = swc[swc[:, 6] != -1]                    # every row except the root
parent_pos = row_of[child[:, 6].astype(int)]    # parent id -> parent row
print(parent_pos)
print(child[:, 6])               # parent ids, as written
print(swc[parent_pos, 0])        # ids found at those rows
print(swc[row_of[6], 5])          # radius of id 6
