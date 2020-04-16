# simulated binary crossover (SBX)
# two parents in two dimensions

import numpy as np
import random
import matplotlib.pyplot as plt

# create a solution using SBX operator on [parents]
# precondition: parents is a (x,y) tuple array with two elements


def sbx(parents, bounds, p, di):
    c1 = list(parents[0])
    c2 = list(parents[1])
    if (random.random() <= p):
        for i in range(2):
            if (random.random() <= 0.5):
                x0 = parents[0][i]
                x1 = parents[1][i]
                dx = abs(x0-x1)

                if (dx > 0):

                    lb = bounds[i][0]
                    ub = bounds[i][1]

                    if (x0 < x1):
                        bl = 1 + (2 * (x0 - lb) / dx)
                        bu = 1 + (2 * (ub - x1) / dx)
                    else:
                        bl = 1 + (2 * (x1 - lb) / dx)
                        bu = 1 + (2 * (ub - x0) / dx)

                    if (bl < bu):
                        bu = bl
                    else:
                        bl = bu

                    p_bl = 1 - (1 / (2 * (bl ** (di+1))))
                    p_bu = 1 - (1 / (2 * (bu ** (di+1))))
                    u = random.random()
                    u0 = u * p_bl
                    u1 = u * p_bu

                    if (u0 <= 0.5):
                        b0 = (2 * u0) ** (1 / (di+1))
                    else:
                        b1 = (0.5 / (1-u0)) ** (1 / (di+1))

                    if (u1 <= 0.5):
                        b1 = (2 * u1) ** (1 / (di+1))
                    else:
                        b0 = (0.5 / (1-u1)) ** (1 / (di+1))

                    if (x0 < x1):
                        v1 = 0.5 * (x0 + x1 + b0 * (x0-x1))
                        v2 = 0.5 * (x0 + x1 + b1 * (x1-x0))
                    else:
                        v1 = 0.5 * (x0 + x1 + b1 * (x0-x1))
                        v2 = 0.5 * (x0 + x1 + b0 * (x1-x0))

                    if (random.random() <= 0.5):
                        temp = v1
                        v1 = v2
                        v2 = temp

                    if v1 < lb:
                        v1 = lb
                    elif v1 > ub:
                        v1 = ub

                    if v2 < lb:
                        v2 = lb
                    elif v2 > ub:
                        v2 = ub

                    c1[i] = v1
                    c2[i] = v2

    c1 = list(c1)
    c2 = list(c2)
    return [c1, c2]
