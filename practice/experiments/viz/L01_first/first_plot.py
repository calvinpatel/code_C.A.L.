from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).parent

# Invented total lengths (µm) of the same 12 cells, from SciPy L06.
# ref: stand-in for a published reference table
# ours: stand-in for Dendrometer's numbers
ref = np.array([1998, 2345, 2245, 2239, 2534, 1602,
                1793, 1564, 1964, 2330, 1993, 2164])
ours = np.array([2029, 2327, 2297, 2246, 2598, 1577,
                 1833, 1576, 1955, 2388, 2014, 2191])
shifted = ref + 150

lims = [ref.min(), ref.max()]

fig, ax = plt.subplots()
ax.scatter(ref, ours, color="green", label="ours")
ax.scatter(ref, shifted, color="blue", label="shifted")
ax.plot(lims, lims, color="red", label="ours = ref")
ax.legend()
ax.set_xlabel("ref (µm)")
ax.set_ylabel("ours (µm)")
ax.set_title("Dendrometer vs. reference")
fig.savefig(HERE / "agree.png", dpi=150)
plt.show()