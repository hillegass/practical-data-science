import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.stats import norm
import csv
import pandas as pd
import seaborn as sns
import random

gen_mean = 12
gen_std = 4
whole_data = norm.rvs(loc=gen_mean, scale=gen_std, size=400)



n_s = [2, 4, 8, 16]

min = 0
max = 24

fig, axs = plt.subplots(2,2, figsize=(9,5))
axs = [item for sublist in axs for item in sublist]

for i in range(len(n_s)):
    n = n_s[i]
    data = whole_data[:n]
    if n ==2:
        print(data)

    sample_mean = data.mean()
    sample_std = data.std(ddof=1)

    pop_mean_mean = sample_mean
    pop_mean_std = sample_std/np.sqrt(n)

    ax = axs[i]
    ax.set_xlim(min, max)
    ax.set_ylim(0, .4)
    ax.set_title(f"n={n}, $\mu={sample_mean:.1f}, \sigma={sample_std:.1f}$")
    sns.set_style('whitegrid')
    xvalues = np.linspace(min, max, 200)
    yvalues = norm.pdf(xvalues, loc=pop_mean_mean, scale=pop_mean_std)
    ymax = yvalues.max()
    ax.plot(xvalues, yvalues, linestyle="dashed", color="blue")
    ax.vlines(data, 0, 0.03, color="green")

fig.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)
fig.savefig('n_samples.png')





