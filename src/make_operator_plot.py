# recreates Figure 4 in Hadka & Reed 2013
# with monte carlo sampling on operators

from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np
import undx
import pcx
import sbx
import spx
import um
import de

# plot values
num_samples = 1000
parent_color = "blue"
child_color = "black"
child_size = 5
parent_size = 20

# operator parents
bounds = [(0, 10), (0, 10)]
SBX_parents = [(4, 5), (5, 7)]
DE_parents = [(3, 3), (4, 7), (4, 3), (6, 8)]
UM_parent = (3, 4)
PCX_parents = [(3, 3), (6, 3), (4.5, 6)]
UNDX_parents = [(3, 3), (6, 3), (4.5, 6)]
SPX_parents = [(3, 3), (6, 3), (4.5, 5)]

# operator parameters
SBX_probability = 1
SBX_distribution_index = 10
DE_crossover_rate = 0.1
DE_scaling_factor = 0.5
UM_probability = 1
PCX_eta = 0.1
PCX_zeta = 0.1
UNDX_zeta = 0.5
UNDX_eta = 0.35
SPX_epsilon = 0.3

# create SBX plot
plt.subplot(231)
for i in range(num_samples):
    children = sbx.sbx(SBX_parents, bounds, SBX_probability,
                       SBX_distribution_index)
    plt.scatter(children[0][0], children[0][1], c=child_color, s=child_size)
    plt.scatter(children[1][0], children[1][1], c=child_color, s=child_size)
for j in range(len(SBX_parents)):
    plt.scatter(SBX_parents[j][0], SBX_parents[j][1],
                c=parent_color, s=parent_size)
plt.xticks([])
plt.yticks([])
plt.title('Simulated Binary Crossover')

# create DE plot
plt.subplot(232)
for j in range(len(DE_parents)):
    plt.scatter(DE_parents[j][0], DE_parents[j]
                [1], c=parent_color, s=parent_size)
for i in range(10):
    (cx, cy) = de.de(DE_parents, DE_crossover_rate, DE_scaling_factor)
    plt.scatter(cx, cy, c=child_color, s=child_size)
plt.xticks([])
plt.yticks([])
plt.title('Differential Evolution')

# create UM plot
plt.subplot(233)
for i in range(num_samples):
    child = um.um(UM_parent, bounds, UM_probability)
    plt.scatter(child[0], child[1], c=child_color, s=child_size)
plt.scatter(UM_parent[0], UM_parent[1], c=parent_color, s=parent_size)
plt.axhline(y=UM_parent[1], xmin=bounds[0][0], xmax=bounds[0][1], c='black')
plt.axvline(x=UM_parent[0], ymin=bounds[1][0], ymax=bounds[1][1], c='black')
plt.xticks([])
plt.yticks([])
plt.title('Uniform Mutation')

# create PCX plot
plt.subplot(234)
for i in range(num_samples):
    child = pcx.pcx(PCX_parents, PCX_eta, PCX_zeta)
    plt.scatter(child[0], child[1], c=child_color, s=child_size)
for j in range(len(PCX_parents)):
    plt.scatter(PCX_parents[j][0], PCX_parents[j]
                [1], c=parent_color, s=parent_size)
plt.xticks([])
plt.yticks([])
plt.title('Parent-Centric Crossover')

# create UNDX plot
parents = [(3, 3), (6, 3), (4.5, 6)]
plt.subplot(235)
for i in range(num_samples):
    child = undx.undx(UNDX_parents, UNDX_zeta, UNDX_eta)
    plt.scatter(child[0], child[1], c=child_color, s=child_size)
for j in range(len(UNDX_parents)):
    plt.scatter(UNDX_parents[j][0], UNDX_parents[j]
                [1], c=parent_color, s=parent_size)
plt.xticks([])
plt.yticks([])
plt.title('Unimodal Normal Distribution Crossover', size=10)

# create SPX plot
plt.subplot(236)
for i in range(num_samples):
    (c1, c2) = spx.spx(SPX_parents, SPX_epsilon)
    plt.scatter(c1, c2, c=child_color, s=child_size)
for j in range(3):
    plt.scatter(SPX_parents[j][0], SPX_parents[j]
                [1], c=parent_color, s=parent_size)
plt.xticks([])
plt.yticks([])
plt.title('Simplex Crossover')

# show subplots
plt.show()
