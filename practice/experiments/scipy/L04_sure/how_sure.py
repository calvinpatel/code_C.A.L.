import numpy as np

tight = np.array([1900, 1950, 2000, 2050, 2100])   # invented: total length of 5 cells, µm
wide = np.array([1600, 1800, 2000, 2200, 2400])    # invented: 5 more cells, same mean

# Core idea 1: Standard deviation
dev = tight - tight.mean()        # each cell's distance from the mean, with a sign
print(dev)
sq = dev ** 2                     # squared: every distance now counts as positive
print(sq)
var = sq.mean()                   # average squared distance (the variance), µm²
print(var)
sd = np.sqrt(var)                 # square root: back to µm
print(sd)
print(tight.std())                # NumPy does all four steps in one call

print("\n")
print(wide.std())
print((tight + 100).std())   # every cell 100 µm longer
print((tight * 2).std())     # every cell twice as long


# Core idea 2: The bootstrap
rng = np.random.default_rng(0)        # a random-number generator; 0 is its seed
print(rng.integers(0, 12, size=12))   # 12 random positions, each from 0 to 11
print(rng.integers(0, 12, size=12))   # the next draw: different positions

rng = np.random.default_rng(0)        # same seed again
print(rng.integers(0, 12, size=12))   # same first draw as before

nums = np.arange(101)                         # toy data: the whole numbers 0, 1, ..., 100
print(np.percentile(nums, 50))                # half the numbers sit below this
print(np.percentile(nums, [2.5, 97.5]))       # the edges of the middle 95%

print("\n")
total_um = np.array([1998, 2345, 2245, 2239, 2534, 1602,
                     1793, 1564, 1964, 2330, 1993, 2164])   # invented: total length of 12 traced cells, µm

n = len(total_um)                        # 12
rng = np.random.default_rng(0)

pos = rng.integers(0, n, size=n)         # one resample: 12 positions, repeats allowed
print(pos)
print(total_um[pos])
print(total_um[pos].mean())

n_boot = 100_000
means = []
for _ in range(n_boot):                  # rerun the study 100,000 times on your own 12 cells
    pos = rng.integers(0, n, size=n)
    means.append(total_um[pos].mean())

lo, hi = np.percentile(means, [2.5, 97.5])   # the middle 95% of the 100,000 means
print(lo, hi)