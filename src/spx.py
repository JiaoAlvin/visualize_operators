# simplex crossover (SPX)
# three parents in two dimensions

import numpy as np
import random
import matplotlib.pyplot as plt

# create a solution using the solution on [parents]
# precondition: parents is a (x,y) tuple array with three elements


def spx(parents, eps):
 # calculate the COM of the three parents
    com = ((parents[0][0] + parents[1][0] + parents[2][0]) * 1/3,
           (parents[0][1] + parents[1][1] + parents[2][1]) * 1/3)
    v = []
    # expand the triangle by factor of epsilon
    for i in range(len(parents)):
        v = v + [(com[0] + (parents[i][0] - com[0]) * (1 + eps),
                  com[1] + (parents[i][1] - com[1]) * (1 + eps))]
        # generate random floats as weights for uniform sampling
    s, t = sorted([random.random(), random.random()])
    # return a uniform sampled point from vertices v
    return [s * v[0][0] + (t-s) * v[1][0] + (1-t) * v[2][0],
            s * v[0][1] + (t-s) * v[1][1] + (1-t) * v[2][1]]
