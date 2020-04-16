import numpy as np
import pcx
import pm
import matplotlib.pyplot as plt

# initialize parents and parameters
parents = [(3, 3), (6, 3), (4.5, 6)]
eta = 0.1
zeta = 0.1
probability = 1
distributionIndex = 1
bounds = [(0, 10), (0, 10)]
num_samples = 100

fig, axs = plt.subplots(1, 2)
axs[0].axis([0, 10, 0, 10])
axs[1].axis([0, 10, 0, 10])
axs[0].set_title('Only PCX')
axs[1].set_title('PCX ---> PM')

for i in range(num_samples):
    # use PCX operator for combination and pm
    child = pcx.pcx(parents, eta, zeta)
    sol = pm.pm(child, bounds, probability, distributionIndex)

    # print the result of pcx
    axs[0].scatter(child[0], child[1], c='red')

    # print the result after pm
    axs[1].scatter(sol[0], sol[1], c='red')

plt.show()
