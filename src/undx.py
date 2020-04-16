# unimodal normal distribution crossover (UNDX)
# n parents in two dimensions

import numpy as np
import random
import matplotlib.pyplot as plt
import vector_util as vector

# create a solution using UNDX operator on [parents]
# precondition: parents is a (x,y) tuple array with at least two elements


def undx(parents, zeta, eta):
    n = len(parents)
    g = vector.mean(parents)
    e_zeta = []
    e_eta = []
    for i in range(n):
        d = vector.subtract(parents[i], g)
        if (not vector.isZero(d)):
            dbar = vector.magnitude(d)
            e = vector.orthogonalize_vector(d, e_zeta)
            if (not vector.isZero(e)):
                w = vector.multiply(dbar, vector.normalize(e))
                e_zeta.append(w)

    D = vector.magnitude(vector.subtract(parents[n-1], g))
    if (2 - len(e_zeta) > 0):
        for _ in range(2 - len(e_zeta)):
            d = vector.gaussian(2)
            e = vector.orthogonalize_vector(d, e_eta)
            if (not vector.isZero(e)):
                w = vector.multiply(D, vector.normalize(e))
                e_eta.append(w)
    var = g
    for i in range(len(e_zeta)):
        w = vector.add(var, vector.multiply(
            np.random.normal(0, zeta), e_zeta[i]))
        var = w
    for i in range(len(e_eta)):
        w = vector.add(var, vector.multiply(
            np.random.normal(0, eta), e_eta[i]))
        var = w
    return var
