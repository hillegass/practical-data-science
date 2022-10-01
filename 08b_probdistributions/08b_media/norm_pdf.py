import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

x = np.linspace(-4, 4, 1000)
y = ss.norm.pdf(x)

fig, ax = plt.subplots(1, 1, figsize=(9, 5), dpi=200)
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('p(x)')
ax.xaxis.set_major_formatter('$\mu+{x:.0f}\sigma$')

colors = ['r','g','purple']
labels = ['68%', '95%', '99.7']

for i in range(3):
    x = i + 1
    c = colors[i]
    ax.vlines(x, 0, 0.3, c, linewidth=0.5)
    ax.vlines(-x, 0, 0.3, c, linewidth=0.5)
    ax.text(x - 0.4, 0.035, labels[i], color=c)
 
fig.savefig('norm_pdf.png')