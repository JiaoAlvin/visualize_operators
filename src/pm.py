import numpy as np
import random

# mutate a solution using PM mutation operator on [parent]
# precondition: [parents] is an array


def pm(parent, bounds, p, di):
    n = len(parent)
    child = []
    for i in range(n):
        if (random.random() <= p):
            x = parent[i]
            u = random.random()
            lb = bounds[i][0]
            ub = bounds[i][1]
            dx = ub - lb

            if (u < 0.5):
                bl = (x - lb) / dx
                b = 2 * u + (1 - 2 * u) * ((1 - bl) ** (di + 1))
                delta = (b ** (1 / (di + 1))) - 1
            else:
                bu = (ub - x) / dx
                b = 2 * (1 - u) + 2 * (u - 0.5) * ((1 - bu) ** (di + 1))
                delta = 1 - (b ** (1 / (di + 1)))

            x = x + delta * dx

            if (x < lb):
                x = lb
            elif (x > ub):
                x = ub

        else:
            x = parent[i]

        child.append(x)

    return child
