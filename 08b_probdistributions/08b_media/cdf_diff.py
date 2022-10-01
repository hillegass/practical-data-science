import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

xmin = 250
x = np.linspace(250, 600, 1000)
y = ss.norm.cdf(x, loc=425, scale=40)

fig, axs = plt.subplots(1, 2, figsize=(10, 4), dpi=288)
ax = axs[0]
y = ss.norm.cdf(x, loc=425, scale=40)
ax.plot(x, y)
ax.set_xlabel('Kg')
ax.set_ylabel('Proportion of Cows Lighter')

x_0 = 410
y_0 = ss.norm.cdf(x_0, loc=425, scale=40)
print(f"{x_0}, {y_0 * 100.0:.2f}%")

ax.vlines(x_0, 0, y_0, 'g')
ax.hlines(y_0, xmin, x_0, 'g')
ax.text(x_0 + -43, 0, f"{x_0:.0f} Kg")
ax.text(xmin, y_0 -0.05, f"{y_0 * 100.0:.1f}%")

x_1 = 420
y_1 = ss.norm.cdf(x_1, loc=425, scale=40)
print(f"{x_1}, {y_1 * 100.0:.2f}%")

ax.vlines(x_1, 0, y_1, 'r')
ax.hlines(y_1, xmin, x_1, 'r')
ax.text(x_1 + 1, 0, f"{x_1:.0f} Kg")
ax.text(xmin, y_1 +0.01, f"{y_1 * 100.0:.1f}%")

ax = axs[1]
y = ss.norm.pdf(x, loc=425, scale=40)
ax.plot(x, y)
ax.set_xlabel('Kg')
ax.set_ylabel('Proportion of Cows Lighter')

y_0 = ss.norm.pdf(x_0, loc=425, scale=40)
print(f"{x_0}, {y_0 * 100.0:.2f}%")

ax.vlines(x_0, 0, y_0, 'g')
ax.text(x_0 + -43, 0, f"{x_0:.0f} Kg")

y_1 = ss.norm.pdf(x_1, loc=425, scale=40)
print(f"{x_1}, {y_1 * 100.0:.2f}%")

ax.vlines(x_1, 0, y_1, 'r')
ax.text(x_1 + 1, 0, f"{x_1:.0f} Kg")

fig.savefig('cdf_pdf.png')