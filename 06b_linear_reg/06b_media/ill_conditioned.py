import numpy as np
import matplotlib.pyplot as plt
import os

fig1, ax = plt.subplots(1, 2, figsize=(12,5))
x = np.linspace(-7, 7, 120)
y = np.linspace(-7, 7, 120)
X, Y = np.meshgrid(x, y)
Z = (X/2)**2 + (Y * 2)**2
ax[0].contour(X, Y, Z, 21)
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')

Z2 = X**2 + Y**2
ax[1].contour(X, Y, Z2, 21)
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')
fig1.savefig('ill_cond.png')
