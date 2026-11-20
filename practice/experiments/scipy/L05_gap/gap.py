import numpy as np
from scipy.stats import ttest_ind

# Invented total lengths (µm), 12 traced cells per group
wt = np.array([1998, 2345, 2245, 2239, 2534, 1602,
               1793, 1564, 1964, 2330, 1993, 2164])   # L04's total_um, now wild-type
mut = np.array([2201, 1866, 2041, 1764, 1490, 1709,
                1851, 1441, 2086, 2091, 1373, 1687])  # invented mutant cells

gap = wt.mean() - mut.mean()     # positive = wild-type longer
print(wt.mean(), mut.mean(), gap)


# Core idea 1: the p-value
rng = np.random.default_rng(0)

length_um = np.concatenate([wt, mut])   # joins arrays end to end: 24 cells, wild-type first
is_mut = np.arange(24) >= 12            # the labels: False for rows 0–11, True for rows 12–23


gaps = []
for i in range(10_000):
    fake = rng.permutation(is_mut)
    gaps.append(length_um[~fake].mean() - length_um[fake].mean())

p_value = (np.abs(np.array(gaps)) >= np.abs(gap)).mean()
print(p_value)


res = ttest_ind(wt, mut)
print(res.statistic, res.pvalue)

res_half = ttest_ind(wt[:6], wt[6:])
print(res_half.pvalue)


# Core idea 2: effect size
print("\n")

sd = np.sqrt((wt.var() + mut.var()) / 2)   # one SD for both groups: average the variances, then square root
d = gap / sd
print(sd, d)

big_rng = np.random.default_rng(6)
big_wt = big_rng.normal(2064, 290, size=2000)    # 2,000 invented cells around 2,064 µm, SD 290
big_mut = big_rng.normal(2044, 290, size=2000)   # 2,000 invented cells around 2,044 µm, SD 290
big_gap = big_wt.mean() - big_mut.mean()
print(big_gap, ttest_ind(big_wt, big_mut).pvalue)

big_sd = np.sqrt((big_wt.var() + big_mut.var()) / 2)
big_d = big_gap / big_sd
print(big_sd, big_d)