import matplotlib.pyplot as plt

x = []
y = []

current_x = -1.5
while current_x < 1.5:
    x.append(current_x)
    y.append(current_x ** 2 + 1)
    current_x += 0.05

fig,ax = plt.subplots()

ax.plot(x,y)
ax.plot([0.1,1],[1.01,2], 'r')
# ax.plot([-1.2, -0.2],[2.44,1.04], 'r')
fig.savefig('convex.png')
