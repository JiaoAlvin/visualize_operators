import numpy as np
import random
import pm

# mutate a solution using Objective PM mutation operator on [parent]


def obj_pm(parent, objectives, bounds, prob, sigma):
    n = len(parent)
    di = []

    # range of distributino indeces used
    dirange = [0, 100]

    # max distance of parent to objective ??
    max = 10

    # determine the distribution indeces for each variable based on its objectve val
    for i in range(n):
        # x -> how far the parent variable is form its objective value
        x = abs(parent[i] - objectives[i])

        # use a linear model to map x value to an "average" di value
        mean = dirange[1] - (dirange[1]/max) * x

        # generate a di value from a normal distribution centered around [mean]
        # with standard deviation [sigma]
        distIndex = np.random.normal(mean, sigma)
        print(distIndex)
        di.append(distIndex)

    # mutate the solution with the determined distribution index
    solution = []
    for i in range(n):
        p = [parent[i]]
        b = [bounds[i]]
        sol = pm.pm(p, b, prob, di[i])
        solution.append(sol[0])
    return solution


parent1 = [0, 0]
parent2 = [6, 6]
objectives = [0, 0]
bounds = [(0, 10), (0, 10)]
prob = 1
sigma = 2
child1 = obj_pm(parent1, objectives, bounds, prob, sigma)
child2 = obj_pm(parent2, objectives, bounds, prob, sigma)
print(child1)
print(child2)
