from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-7, 7, 28)
y = np.linspace(-7, 7, 28)
X, Y = np.meshgrid(x, y)
Z = 3.0 * np.sin(X) * Y + X**2 + Y**2 + 0.25 * X

fig = plt.figure(1, (12,12))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)');

fig.savefig('plot3d.png')