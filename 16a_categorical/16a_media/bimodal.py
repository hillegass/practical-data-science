import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.stats import norm
import csv
import pandas as pd
import seaborn as sns
import random


n = 1000
min=0
max=2000
mus = [600.0, 1200.0]
sigmas = [90.0, 200.0]
p_gender = 0.6

weights = np.zeros(n, float)
for i in range(n) :
    
    gender = 1
    if (np.random.random() < p_gender):
        gender = 0
    w = -1
    while w < 100:
        w = norm.rvs(loc=mus[gender], scale=sigmas[gender], size=1)
    weights[i] = w

fig, ax = plt.subplots(figsize=(9,5))
ax.set_xlabel("Weight")
ax.set_xlim((0,2000))
sns.set_style('whitegrid')
sns.kdeplot(weights, ax=ax)
mean = weights.mean()
print(f"Mean = {mean:.0f}")
std = weights.std()
print(f"Std = {std:.0f}")
xvalues = np.linspace(min, max, 200)
yvalues = norm.pdf(xvalues, loc=mean, scale=std)
ax.plot(xvalues, yvalues, linestyle="dashed", color="red")
fig.savefig('bimodal_density.png')


fig, axs = plt.subplots(2,2, figsize=(9,5))
print(axs)
axs = [item for sublist in axs for item in sublist]
for m in range(2, 10, 2):
    ax = axs[m//2 - 1]
    mean_weights = np.zeros(n-m)
    for k in range(n - m):
        mean_weights[k] = weights[k:(k+m)].mean()
    ax.set_xlim((0,2000))
    ax.text(1300, 0.0008, f"m={m}, $\sigma= {std/np.sqrt(m):.1f}$")
    sns.set_style('whitegrid')
    sns.kdeplot(mean_weights, ax=ax)
    mmean = mean_weights.mean()
    print(f"{m}: Mean = {mmean:.0f}")
    sstd = mean_weights.std()
    print(f"{m}: Std = {sstd:.0f}")
    xvalues = np.linspace(min, max, 200)
    yvalues = norm.pdf(xvalues, loc=mean, scale=std/np.sqrt(m))
    ax.plot(xvalues, yvalues, linestyle="dashed", color="red")
    ax.set_ylabel("")
fig.savefig('m_density.png')

