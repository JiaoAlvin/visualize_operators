# differential evolution (DE)
# four parents in two dimensions

import numpy as np
import random
import matplotlib.pyplot as plt

# create a solution using DE operator on [parents]
# precondition: parents is a (x,y) tuple array with four elements


def de(parents, cr, f):
    child = [parents[0][0], parents[0][1]]
    irand = random.randint(0, 1)
    for i in range(2):
        if (random.random() <= cr) or (i == irand):
            child[i] = parents[3][i] + f * (parents[1][i] - parents[2][i])
    return child
