import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 30)
y = np.linspace(-2, 2, 30)
X, Y = np.meshgrid(x, y)
U = 3 * Y * np.cos(X) + 2.0 * X + 0.25
V = 3 * np.sin(X) + 2.0 * Y

Z = 3.0 * np.sin(X) * Y + X**2 + Y**2 + 0.25 * X
fig1 = plt.figure(1, (12,12))
ax1 = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.contour(X, Y, Z, 21)
ax1.quiver(X, Y, -U, -V, Z)
ax1.plot([-1.07117403, 0.9439074],  [1.31662556 , -1.21476033], 'go')
ax1.set_xlabel('x')
ax1.set_ylabel('y')


fig1.savefig('quiverdown.png')