import csv
import random

n = 37
p_drug = 0.7
mu = [1.4, 2.2]
sigma = [1.0, 2.0]

with open("data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["participant", "used_drug", "kg_lost"])

    for participant in range(30):
        if random.random() < p_drug:
            used_drug = 1
        else:
            used_drug = 0
        kg_lost = f"{random.normalvariate(mu[used_drug], sigma[used_drug]):.2f}"
        writer.writerow([participant, used_drug, kg_lost])
