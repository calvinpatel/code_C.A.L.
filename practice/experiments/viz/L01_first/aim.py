import matplotlib.pyplot as plt

fig_a, ax_a = plt.subplots()
fig_b, ax_b = plt.subplots()

ax_a.set_xlabel("ref (µm)")
ax_b.set_title("shifted")

print(repr(ax_a.get_xlabel()), repr(ax_b.get_xlabel()), repr(ax_a.get_title()), repr(ax_b.get_title()))