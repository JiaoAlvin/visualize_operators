# parent-centric crossover (PCX)
# n > 2 parents in two dimensions

import numpy as np
import random
import matplotlib.pyplot as plt
import vector_util as vector

# create a solution using PCX operator on [parents]
# precondition: [parents] is a (x,y) tuple array of length > 1


def pcx(parents, eta, zeta):
    n = len(parents)
    g = vector.mean(parents)
    e_eta = []
    e_eta.append(vector.subtract(parents[n-1], g))
    D = 0
    for i in range(n-1):
        d = vector.subtract(parents[i], g)
        if (not vector.isZero(d)):
            e = vector.orthogonalize_vector(d, e_eta)
            if (not vector.isZero(e)):
                D = D + vector.magnitude(e)
                e_eta.append(vector.normalize(e))
    D = D / (n-1)
    var = parents[np.random.randint(0, n)]
    var = vector.add(var, vector.multiply(np.random.normal(0, zeta), e_eta[0]))
    for i in range(len(e_eta)):
        if (i != 0):
            var = vector.add(var, vector.multiply(
                np.random.normal(0, eta) * D, e_eta[i]))
    return var
