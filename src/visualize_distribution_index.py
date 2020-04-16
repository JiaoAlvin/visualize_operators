import numpy as np
import pcx
import pm
import matplotlib.pyplot as plt

# initialize parents and parameters
parents = [(3, 3), (6, 3), (4.5, 6)]
eta = 0.1
zeta = 0.1
probability = 1
distributionIndex = [100, 50, 20, 15, 10, 0]
bounds = [(0, 10), (0, 10)]
num_samples = 100

fig, axs = plt.subplots(1, len(distributionIndex))

children = []

for i in range(num_samples):
    # generate [num_samples] children using PCX
    children.append(pcx.pcx(parents, eta, zeta))

for j in range(len(distributionIndex)):
    di = distributionIndex[j]
    axs[j].axis([0, 10, 0, 10])
    title = "DI = " + str(di)
    axs[j].set(aspect='equal')
    axs[j].set_title(title)
    for i in range(num_samples):
        sol = pm.pm(children[i], bounds, probability, di)
        axs[j].scatter(sol[0], sol[1], c='red', s=5)

plt.show()
