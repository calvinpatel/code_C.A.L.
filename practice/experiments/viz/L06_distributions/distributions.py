import numpy as np
import matplotlib.pyplot as plt

# SciPy L05's cells: total length per cell in µm (invented), 12 per group
wt = np.array([1998, 2345, 2245, 2239, 2534, 1602, 1793, 1564, 1964, 2330, 1993, 2164])
mut = np.array([2201, 1866, 2041, 1764, 1490, 1709, 1851, 1441, 2086, 2091, 1373, 1687])


def boot_means(cells, rng):
    """SciPy L04's bootstrap: 10,000 resample means of one group."""
    n = len(cells)
    means = []
    for _ in range(10_000):
        pos = rng.integers(0, n, size=n)
        means.append(cells[pos].mean())
    return np.array(means)


rng = np.random.default_rng(0)
wt_means = boot_means(wt, rng)      # wt first, so it matches L04's run
mut_means = boot_means(mut, rng)

print(wt_means.shape, mut_means.shape)
print(np.percentile(wt_means, [2.5, 97.5]))


# Core idea 1: a histogram counts per bin
edges = np.arange(1200, 2801, 200)  # start, stop, step: 1200, 1400, ..., 2800 (stop not included, so 2801)
fig, ax = plt.subplots()
counts, _, _ = ax.hist(wt, bins=edges)                    # hands back 3 things: counts, edges, the drawn bars; we keep counts
ax.set_xlabel("total length (µm)")
ax.set_ylabel("cells")
# print(edges)
# print(counts)

mean_edges = np.arange(1500, 2401, 20)
fig, ax = plt.subplots()
mean_counts, _, _ = ax.hist(wt_means, bins=mean_edges)
lo, hi = np.percentile(wt_means, [2.5, 97.5])
ax.axvline(lo, color="black")
ax.axvline(hi, color="black")
inside = (wt_means >= lo) & (wt_means <= hi)
ax.set_xlabel("10,000 bootstrap wt means (µm)")
ax.set_ylabel("counts")
# print(mean_edges)
# print(mean_counts)
print(lo, hi, inside.sum())


# Core idea 2: the bins change the picture
fig, ax = plt.subplots()
ax.hist(wt_means, bins=mean_edges, alpha=0.5, label="wt")   # alpha: 0 = invisible, 1 = solid
ax.hist(mut_means, bins=mean_edges, alpha=0.5, label="mut") # label: the name shown in the key
ax.set_xlabel("bootstrap means (µm)")
ax.set_ylabel("resamples")
ax.legend()                                                 # draws the key from the labels

fine_edges = np.arange(1500, 2401, 5)
fig, ax = plt.subplots()
ax.hist(wt_means, bins=fine_edges, alpha=0.5, label="wt")
ax.hist(mut_means, bins=fine_edges, alpha=0.5, label="mut")
ax.set_xlabel("bootstrap means, fine edges (µm)")
ax.set_ylabel("resamples")
ax.legend()

plt.show()

