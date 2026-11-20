import numpy as np
from scipy import stats


# --- a helper: L05's cosine, for arrays of any length ---
def cosine(a, b):
    ua = a / np.sqrt((a ** 2).sum())   # unit arrow: a divided by its own length
    ub = b / np.sqrt((b ** 2).sum())
    return ua @ ub                     # dot of two unit arrows = cosine


# --- warm-up check: the cosine ignores length ---
a = np.array([1.0, 2.0, 3.0, 4.0])
print(round(cosine(a, 2 * a), 4))
print(round(cosine(a, -a), 4))

# --- the data (invented, µm) ---
ref = np.array([1998, 2345, 2245, 2239, 2534, 1602, 1793, 1564, 1964, 2330, 1993, 2164.0])
ours = np.array([2029, 2327, 2297, 2246, 2598, 1577, 1833, 1576, 1955, 2388, 2014, 2191.0])

# --- the problem: raw cosine is fooled ---
rng = np.random.default_rng(7)
shuffled = rng.permutation(ref)   # ref's 12 lengths, dealt out to the wrong cells

print(round(cosine(ref, ours), 4))
print(round(cosine(ref, shuffled), 4))

# --- core idea 1: Pearson r ---
ref_c = ref - ref.mean()      # each cell's distance from ref's mean (2064.25)
ours_c = ours - ours.mean()   # each cell's distance from ours's mean (2085.92)

r = cosine(ref_c, ours_c)
print(round(r, 4))
print(round(stats.pearsonr(ref, ours).statistic, 4))

shuffled_c = shuffled - shuffled.mean()
print(round(cosine(ref_c, shuffled_c), 4))

print("\n")
# --- core idea 2: correlation isn't agreement ---
doubled = 2 * ref                 # invented bug: every length doubled
print(round(stats.pearsonr(ref, doubled).statistic, 4))

diff = ours - ref                 # each cell's error: Dendrometer minus the reference (µm)
print(diff)
print(round(diff.mean(), 2))      # bias
print(round(diff.std(), 2))       # spread

shifted = ref + 150               # invented bug: 150 µm added to every cell
print(round(stats.pearsonr(ref, shifted).statistic, 4))
diff_shifted = shifted - ref
print(round(diff_shifted.mean(), 2), round(diff_shifted.std(), 2))