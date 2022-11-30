import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.stats import norm
import csv
import pandas as pd

df = pd.read_csv("data.csv", index_col="participant")
n = len(df)
print(f"{n} samples")
min = df["kg_lost"].min()
max = df["kg_lost"].max()
print(f"Min lost = {min:.2f} kg, Max lost = {max:.2f} kg")

mask = df["used_drug"] == 1
drugged_n = np.sum(mask)
undrugged_n = n - drugged_n
print(f"N drugged = {drugged_n}, undrugged = {undrugged_n}")

drugged_mean = df["kg_lost"][mask].mean()
undrugged_mean = df["kg_lost"][~mask].mean()
print(f"Mean lost: drugged={drugged_mean:.2f} kg, undrugged={undrugged_mean:.2f} kg")

drugged_std = df["kg_lost"][mask].std()
undrugged_std = df["kg_lost"][~mask].std()
print(
    f"Standard deviation: drugged={drugged_std:.2f} kg, undrugged={undrugged_std:.2f} kg"
)


colors = ["orange", "blue"]
labels = [f"No drug (n={undrugged_n})", f"Drug (n={drugged_n})"]
bins = np.linspace(min, max, num=20)[1:]

fig, ax = plt.subplots(figsize=(10, 6))

n_bins = 10
densities, bins, containers = ax.hist(
    [df["kg_lost"][mask], df["kg_lost"][~mask]],
    n_bins,
    density=True,
    histtype="bar",
    label=[f"Drug (n={drugged_n})", f"No Drug (n={n - drugged_n})"],
)
print(f"bin count = {len(bins)}")
container = containers[0]
ticks = [(patch.get_x() + patch.get_width()) for patch in container.patches]
ticklabels = [f"{bins[i]:.1f} to {bins[i+1]:.1f} kg" for i in range(n_bins)]
plt.xticks(ticks, ticklabels, rotation=25)

ax.set_title("kg lost")
ax.yaxis.set_major_formatter(ticker.PercentFormatter(1.0))
ax.legend()
fig.savefig("histgram.png")

pop_mean_mu = [undrugged_mean, drugged_mean]
pop_mean_sigma = [
    undrugged_std / np.sqrt(undrugged_n),
    drugged_std / np.sqrt(drugged_n),
]

fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(-2, 6, 200)
for i in range(2):
    ax.plot(
        x,
        norm.pdf(x, loc=pop_mean_mu[i], scale=pop_mean_sigma[i]),
        color=colors[i],
        label=labels[i],
    )
    x_text = pop_mean_mu[i] + 0.3 * pop_mean_sigma[i]
    y_text = norm.pdf(x_text, loc=pop_mean_mu[i], scale=pop_mean_sigma[i])
    x_text += 0.1
    ax.text(
        x_text,
        y_text,
        f"$\mu_{i}$ = {pop_mean_mu[i]:.1f}, $\sigma_{i}$ = {pop_mean_sigma[i]:.1f}",
        color=colors[i],
    )

ax.set_title("PDFs for Mean Weight Loss")
ax.legend()
ax.set_xlabel("Mean kg lost")
ax.set_ylabel("Density")
fig.savefig("means.png")

diff_mu = pop_mean_mu[1] - pop_mean_mu[0]
diff_sigma = np.sqrt(pop_mean_sigma[1] ** 2 + pop_mean_sigma[0] ** 2)
print(f"Difference: Mean={diff_mu:2f},  STD={diff_sigma:2f}")

fig, (ax, ax2) = plt.subplots(2, 1, figsize=(10, 6))

x = np.linspace(-2, 6, 200)
for i in range(2):
    ax.plot(
        x,
        norm.pdf(x, loc=pop_mean_mu[i], scale=pop_mean_sigma[i]),
        color=colors[i],
        label=labels[i],
    )
    x_text = pop_mean_mu[i] + 0.3 * pop_mean_sigma[i]
    y_text = norm.pdf(x_text, loc=pop_mean_mu[i], scale=pop_mean_sigma[i])
    x_text += 0.1
    ax.text(
        x_text,
        y_text,
        f"$\mu_{i}$ = {pop_mean_mu[i]:.1f}, $\sigma_{i}$ = {pop_mean_sigma[i]:.1f}",
        color=colors[i],
    )

ax.set_title("PDFs for Mean Weight Loss")
ax.legend()
ax.set_ylabel("Density")

x = np.linspace(-2, 6, 200)
ax2.plot(x, norm.pdf(x, loc=diff_mu, scale=diff_sigma), color="black")
x_text = diff_mu + 0.3 * diff_sigma
y_text = norm.pdf(x_text, loc=diff_mu, scale=diff_sigma)
x_text += 0.1
ax2.text(
    x_text, y_text, f"$\mu$ = {diff_mu:.1f}, $\sigma$ = {diff_sigma:.1f}", color="black"
)
ax2.set_ylabel("Density")
ax2.set_xlabel("Difference in Mean Between Groups")
ax2.vlines(0, 0, 0.3, linestyle="dashed", colors="green")
fig.savefig("diff_means.png")

p = norm.cdf(0.0, loc=diff_mu, scale=diff_sigma)
print(
    f"Probability that mean of drugged participants will be greater that mean of undrugged patients: {100.0 * (1 -p):.2f} %"
)

diff_sigma_2 = np.sqrt((drugged_std ** 2)/drugged_n + (undrugged_std ** 2)/undrugged_n)
print(f"Diff sigma = {diff_sigma_2:.2f}")