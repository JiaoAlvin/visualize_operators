import numpy as np


# sample objective function for a problem
def f(x):
    return abs(x-0.5)


# class for decision variable and objective value
class Solution:
    def __init__(self, x):
        self.d = x
        self.o = f(x)


# in each dimension, mutate the parent with a probabilty distribution equal to
# Boltzmann distribution centered at its objective value
def bm(parent):
    nVar = len(parent)
    sols = []
    for i in len(nVar):
        sols.append(Solution(parent[i]))
    # assume two variables
    if sols[0].o < sols[1].o
