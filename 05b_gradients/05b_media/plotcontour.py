import numpy as np
import matplotlib.pyplot as plt
import os

print(os.getcwd())
x = np.linspace(-7, 7, 120)
y = np.linspace(-7, 7, 120)
X, Y = np.meshgrid(x, y)
Z = 3.0 * np.sin(X) * Y + X**2 + Y**2 + 0.25 * X
fig1 = plt.figure(1, (12,12))
ax1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.contour(X, Y, Z, 21)
ax1.plot([-1.07117403, 0.1, 0.9439074],  [1.31662556 , -0.1, -1.21476033], 'go')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
fig1.savefig('contour.png')