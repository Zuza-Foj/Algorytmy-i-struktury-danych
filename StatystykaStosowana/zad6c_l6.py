import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts


mi = 2
sig = 2
n = 1000

M = 1000
Y = []
X = []
for i in range(M):
    x = np.random.normal(mi, sig, n + 1)
    y = x[-1] + sum(x)/n
    X.append(x)
    Y.append(y)

sig_n = sig**2 * (1 + 1/n)
F_t = sts.norm.cdf(Y, 0, sig_n)

plt.plot(X, Y)
plt.show()


