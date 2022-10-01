import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

xmin = 250
x = np.linspace(250, 600, 1000)
y = ss.norm.cdf(x, loc=425, scale=40)

fig, ax = plt.subplots(1, 1, figsize=(6, 4), dpi=288)
ax.plot(x, y)
ax.set_xlabel('Kg')
ax.set_ylabel('Proportion of Cows Lighter')

x_0 = 471
y_0 = ss.norm.cdf(x_0, loc=425, scale=40)

print(f"{x_0}, {y_0 * 100.0:.2f}%")

ax.vlines(x_0, 0, y_0, 'r', 'dashed')
ax.hlines(y_0, xmin, x_0, 'r', 'dashed')
ax.text(x_0 + 1, 0, f"{x_0:.0f} Kg")
ax.text(xmin, y_0 +0.01, f"{y_0 * 100.0:.1f}%")

fig.savefig('norm_cdf.png')