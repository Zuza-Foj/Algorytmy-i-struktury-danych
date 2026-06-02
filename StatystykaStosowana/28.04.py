import  numpy as np


def pareto(x0, alfa, N):
    x = np.linspace(1, 100, 1)
    l = []
    for i in x:
        F = x0 * (1/((1 - i)**(1/alfa)) - 1)
        l.append(F)
    return l

print(pareto(3, 2, 10))
