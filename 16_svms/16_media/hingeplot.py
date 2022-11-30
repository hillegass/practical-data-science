import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(10,6))

x_values = np.linspace(-2, 2, 50)

ypos = 1.0 - x_values
ypos[ypos < 0] = 0.0

yneg = 1.0 + x_values
yneg[yneg < 0] = 0.0

ax.set_ylabel("Loss")
ax.set_xlabel("$w^T x - b$")
ax.plot(x_values, ypos, label="$y = 1$")
ax.plot(x_values, yneg, label="$y = -1$")
ax.legend()
fig.savefig('loss.png')