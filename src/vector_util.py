# vector utilities

import numpy as np
import math as m


def add(u, v):
    w = []
    n = len(u)
    for i in range(n):
        w.append(u[i] + v[i])
    return w


def subtract(u, v):
    w = []
    n = len(u)
    for i in range(n):
        w.append(u[i] - v[i])
    return w


def multiply(c, u):
    w = []
    n = len(u)
    for i in range(n):
        w.append(u[i] * c)
    return w


def divide(u, c):
    w = []
    n = len(u)
    for i in range(n):
        w.append(u[i] / c)
    return w


def dot(u, v):
    d = 0
    n = len(u)
    for i in range(n):
        d = d + u[i] * v[i]
    return d


def magnitude(u):
    return m.sqrt(dot(u, u))


def normalize(u):
    return multiply(1 / magnitude(u), u)


def project(u, v):
    return multiply(dot(u, v) / dot(v, v), v)


def orthogonalize_basis(vs):
    n = len(vs)
    w = []
    for i in range(n):
        for j in range(i):
            w.append(subtract(vs[i], project(vs[i], vs[j])))
    return w[n-1]


def orthogonalize_vector(u, vs):
    n = len(vs)
    for i in range(n):
        u = subtract(u, project(u, vs[i]))
    return u


def mean(vs):
    k = len(vs)
    n = len(vs[0])
    w = []
    for j in range(n):
        sum = 0
        for i in range(k):
            sum = sum + vs[i][j]
        w.append(sum/k)
    return w


def isZero(u):
    for i in range(len(u)):
        if u[i] != 0:
            return False
    return True


def gaussian(n):
    w = []
    for _ in range(n):
        w.append(np.random.normal())
    return w


u = [1, 2, 3]
v = [4, 5, 6]
vs = [[1, 2, 3], [1, 2, 0], [1, 0, 0]]
# c = 2
# print(add(u, v))
# print(divide(u, c))
# print(dot(u, v))
# print(magnitude(u))
# print(normalize(u))
# print(project(u, v))
# print(orthogonalize_basis(vs))
# print(orthogonalize_vector(v, []))
# print(orthogonalize_vector(v, vs))
# print(mean(vs))
# print(isZero(u))
# print(isZero([0, 0, 0]))
# print(orthogonalize_vector(u, []))
# print(isZero([]))
# print(random(10))
