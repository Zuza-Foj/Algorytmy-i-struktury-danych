import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

mi = 2
sigm = 2
n1 = 10

X = stats.norm.rvs(mi, sigm, n1)
EX = np.mean(X)
Y = np.mean(X - EX)
EY_t = (2*sigm) / ((2*np.pi)**0.5)

d = []
for i in range(1, n1+1):
    elem = abs(X - EX)
    d.append(elem)

s = 1/n1 * sum(d)

# n_l = range(20, 10000, 10)
# l = []
# for i in n_l:
#     n_X = scipy.norm.rvs(mi, sigm, i)
#     n_EX = np.mean(n_X)
#     n_l = []
#     for j in range(1, i):
#         n_elem = abs(X - EX)
#         n_l.append(n_elem)
#     l.append(n_l)
#
# plt.plot(n_l, l)
# plt.show()

n = range(10, 10001, 10)
l_d = []
for i in n:
    X = stats.norm.rvs(sigm, mi, i)
    X_e = np.mean(X)
    EX_e = np.mean(abs(X - X_e))
    d = np.abs(EY - EY_t)
