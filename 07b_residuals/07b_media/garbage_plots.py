import numpy as np
import matplotlib.pyplot as plt
import sys

n = 100
X = np.random.uniform(0.1, 4.0, n)
Y = np.random.normal(0, 4.0, n)

# Draw residual vs actual price
fig1 = plt.figure(1, (4.5, 4.5))
ax1 = fig1.add_axes([0.2, 0.12, 0.7, 0.8])
ax1.scatter(X, Y, alpha=0.3)
ax1.set_xlabel("Age")
ax1.set_ylabel("Residual")
ax1.yaxis.set_major_formatter(lambda x, pos: f"${x:.02f}")

ax1.set_title("Residual")
fig1.savefig("res_garbage.png")
