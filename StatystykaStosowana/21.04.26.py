import matplotlib.pyplot as plt
import numpy as np

mi = 2
sigm = 0.5
n = 10000

x = np.random.lognormal(mi, sigm, n)
e_theta = 1/n * np.sum(x)
print(e_theta)

M = 501
l_e1 = []
for i in range(M):
    x = np.random.lognormal(mi, sigm, n)
    e_theta = 1/n * np.sum(x)
    l_e1.append(e_theta)
e1 = np.exp(mi + (0.5**2/2))
v1 = 1/n * np.exp(2 * mi + 0.5**2) * (np.exp(0.5**2) - 1)

l_e2 = []
for i in range(M):
    x = np.random.lognormal(mi, 1, n)
    e_theta = np.mean(x)
    l_e2.append(e_theta)
e2 = np.exp(mi + (1**2/2))
v2 = 1/n * np.exp(2 * mi + 1**2) * (np.exp(1**2) - 1)

l_e3 = []
for i in range(M):
    x = np.random.lognormal(mi, 1.5, n)
    e_theta = 1/n * np.sum(x)
    l_e3.append(e_theta)
e3 = np.exp(mi + (1.5**2/2))
v3 = 1/n * np.exp(2 * mi + 1.5**2) * (np.exp(1.5**2) - 1)

plt.figure(figsize=(10, 5))
plt.boxplot([l_e1, l_e2, l_e3], labels=['sigma = 0.5','sigma = 1','sigma = 1.5'])
plt.axhline(e1)
plt.axhline(e2)
plt.axhline(e3)
plt.show()

print("Wartości statystyk dla sigma = 0.5:")
print("Wartość średnia (empiryczna):", np.mean(l_e1), ", Wartość średnia (teoretyczna):", e1 )
print("Wariancja (empiryczna):", np.var(l_e1), ", Wariancja (teoretyczna):", v1)
print("Wartości statystyk dla sigma = 1:")
print("Wartość średnia (empiryczna):", np.mean(l_e2), ", Wartość średnia (teoretyczna):", e2)
print("Wariancja (empiryczna):", np.var(l_e2), ", Wariancja (teoretyczna):", v2)
print("Wartości statystyk dla sigma = 1.5:")
print("Wartość średnia (empiryczna):", np.mean(l_e3), ", Wartość średnia (teoretyczna):", e3)
print("Wariancja (empiryczna):", np.var(l_e3), ", Wariancja (teoretyczna):", v3)

# zadanie