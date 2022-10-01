import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

a = 2
b = 5
mean = a / (a + b)
mode = (a - 1)/(a + b - 2) 
x = np.linspace(-0.2, 1.2, 200)
y = ss.beta.pdf(x, a, b)

fig, ax = plt.subplots(1, 1, figsize=(9, 5), dpi=200)
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('p(x)')
ax.set_title(f'Beta distribution ($\\alpha=2, \\beta=5$)')
# ax.xaxis.set_major_formatter('$\mu+{x:.0f}\sigma$')

ax.vlines(mean, 0, 2.52, color='g', linewidth=0.6)
ax.vlines(mode, 0, 2.52, color='purple', linewidth=0.6)

 
fig.savefig('beta_pdf.png')