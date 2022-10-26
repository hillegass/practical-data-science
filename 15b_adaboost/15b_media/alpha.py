import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.01, 0.5, 100)
y = 0.5 * np.log((1 - x) / x )

fig, ax = plt.subplots(figsize=(8,8))
ax.plot(x, y)
ax.set_xlabel('Error')
ax.set_ylabel('$\\alpha$')
fig.savefig('alpha.png')