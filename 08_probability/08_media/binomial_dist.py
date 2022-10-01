import numpy as np
import matplotlib.pyplot as plt
from math import comb

p = 0.3
n = 10

m_values = []
p_values = []
for m in range(n + 1):
    prob = comb(n, m) * (p ** m) * ((1 - p) ** (n - m))
    p_values.append(prob)
    m_values.append(m)



fig, ax = plt.subplots(1, 1, figsize=(6, 4), dpi=288)
ax.bar(m_values, p_values, align='center')
ax.set_xlabel('m')
ax.set_ylabel('P')
ax.set_title(f"Probability of m positives (p={p:.1f}, n={n})")

fig.savefig('binomial_dist.png')