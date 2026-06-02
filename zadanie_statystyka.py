import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats

# mi = 0
# sigma = 1
# n = 1000
#
# x = np.random.normal(mi, sigma, n)
# y = np.exp(x)
#
# # dla x:
#
#
# plt.subplot(1, 3, 1)
# seaborn.histplot(x, stat='count')
#
# plt.subplot(1, 3, 2)
# seaborn.histplot(x, stat='probability')
#
# plt.subplot(1, 3, 3)
# seaborn.histplot(x, stat='density')
# d1 = np.linspace(-3, 3)
# f1 = scipy.stats.norm.pdf(d1, mi, sigma)
# g = plt.plot(d1, f1, color='red')
#
# plt.plot()
#
# #plt.show()
#
# dla y:
plt.subplot(1, 3, 1)
seaborn.histplot(y, stat='count')

plt.subplot(1, 3, 2)
seaborn.histplot(y, stat='probability')

plt.subplot(1, 3, 3)
seaborn.histplot(y, stat='density')
d2 = np.linspace(0, 20)
f2 = scipy.stats.lognorm.pdf(d2, sigma, np.exp(mi))
#f2 = scipy.stats.norm.pdf(np.log(d2), mi, sigma) / d2
h = plt.plot(d2, f2, color='red')

plt.show()
print("X", x)
print("Y", y)

#zadanie 2.
def pareto(lamb, alfa, n):
    res = []
    list_u = []
    for i in range(n):
        u = np.random.uniform(0, 1, 1)
        formula = lamb / (u)**(1/alfa) - lamb
        res.append(formula)
        list_u.append(u)
    return res, list_u

# r, r_u = pareto(1, 3, 1000)
#plt.show()

lamb = 1
alfa = 3
u = np.random.uniform(0,1, 1000)
f = lamb / ((1 - u)**(1/alfa)) - lamb
plt.plot(u, f)
plt.show()


# sns.ecdfplot(f)
# plt.plot(u, f)
# plt.show()



