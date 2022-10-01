import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

x = np.linspace(-4, 4, 1000)
y = ss.norm.cdf(x)

x_0 = 0.2
y_0 = ss.norm.cdf(x_0)

fig, ax = plt.subplots(1, 1, figsize=(9, 5), dpi=200)
ax.plot(x, y)

ax.hlines(y_0, x_0, 4, 'r', linewidth=0.5)
ax.vlines(x_0, 0, y_0, 'g', linewidth=0.5)

ax.set_xlabel('x')

fig.savefig('norm_gen.png')