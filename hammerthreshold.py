import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy.optimize import curve_fit

# Data
data = [
    {"label": "DDR3\n139K", "ddr": "DDR3", "value": 139, "year": 2014},
    {"label": "DDR3\n22K",  "ddr": "DDR3", "value": 22,  "year": 2014},
    {"label": "DDR4\n18K",  "ddr": "DDR4", "value": 18,  "year": 2018},
    {"label": "DDR4\n10K",  "ddr": "DDR4", "value": 10,  "year": 2018},
    {"label": "DDR5\n20K",  "ddr": "DDR5", "value": 20,  "year": 2023},
]

palette = ['#E69F00', '#56B4E9', '#009E73', '#F0E442',
           '#0072B2', '#D55E00', '#CC79A7', '#000000']

color_map = {"DDR3": palette[0], "DDR4": palette[1], "DDR5": palette[2]}
colors = [color_map[d["ddr"]] for d in data]

labels = [d["label"] for d in data]
values = [d["value"] for d in data]
x = np.arange(len(data))

# --- Curve of best fit (exponential decay) ---
def exp_decay(x, a, b):
    return a * np.exp(-b * x)

popt, _ = curve_fit(exp_decay, x, values, p0=(150, 0.5), maxfev=5000)
x_smooth = np.linspace(0, len(data) - 1, 300)
y_fit = exp_decay(x_smooth, *popt)

fig, ax = plt.subplots(figsize=(10, 6))

# Bars
bars = ax.bar(x, values, color=colors, width=0.55, edgecolor='white', linewidth=0.8, zorder=2)

# Value labels
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1.5,
            f"{val}K",
            ha='center', va='bottom', fontsize=10, fontweight='bold')

# Year annotations
year_groups = {2014: [0, 1], 2018: [2, 3], 2023: [4]}
for year, indices in year_groups.items():
    mid = np.mean(indices)
    ax.text(mid, -14, f"({year})", ha='center', va='top',
            fontsize=9, color='#444444', style='italic')

ax.scatter(x, values, color=palette[5], s=60, zorder=4)  # anchor dots

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=11)
ax.set_ylabel("RowHammer Threshold (K activations)", fontsize=11)
ax.set_title("RowHammer Threshold Across DRAM Generations", fontsize=14, fontweight='bold', pad=15)
ax.set_ylim(0, 160)
ax.spines[['top', 'right']].set_visible(False)
ax.yaxis.grid(True, linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

# Legend
gen_patches = [mpatches.Patch(color=color_map[k], label=k) for k in ["DDR3", "DDR4", "DDR5"]]
ax.legend(handles=gen_patches, fontsize=10, loc='upper right')

plt.tight_layout()
plt.savefig("rowhammer_thres.png", dpi=500, bbox_inches='tight')
print("Done.")