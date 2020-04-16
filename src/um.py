# uniform mutation (UM)
# one parent in two dimensions

import numpy as np
import random
import matplotlib.pyplot as plt

# create a solution using UM operator on [parent]
# precondition: parents is an (x,y) tuple


def um(parent, bounds, p):
    child = list(parent)
    for i in range(2):
        if (random.random() <= p):
            child[i] = random.uniform(bounds[i][0], bounds[i][1])
    return child
