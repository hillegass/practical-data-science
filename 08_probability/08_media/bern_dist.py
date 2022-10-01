import numpy as np
import matplotlib.pyplot as plt

p = 0.1

objects = ('x = 1', 'x = 0')
values = [0, 1]
probs = [p, 1-p]

fig, ax = plt.subplots(1, 1, figsize=(6, 4), dpi=288)
ax.bar(values, probs, align='center', tick_label=objects)
ax.set_ylabel('P')

fig.savefig('bern_dist.png')