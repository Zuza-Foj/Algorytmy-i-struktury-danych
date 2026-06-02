import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def exp(theta, n):
    e = np.random.exponential(1, n)
    y = e + theta
    return y

def estymator_theta(y):
    theta_e = min(y)
    return theta_e

#testy
theta = 5
n =1000
y = exp(theta, n)

y_s = np.sort(y)
cdf_e = np.arange(1, n + 1) / n

x = np.linspace(theta, max(y_s  ), 500)
cdf_t = 1 - np.exp(-(x - theta))

plt.figure(figsize=(10, 5))
plt.plot(x, cdf_t, label='Teoretyczna', color='red', linewidth=2)
plt.plot(y_s, cdf_e, label='Empiryczna', color='blue', linestyle='--', alpha=0.7)
plt.title('Dystrybuanta Rozkładu Exp(theta=5, n=1000)')
plt.xlabel('Wartość x')
plt.ylabel('F(x)')
plt.grid(True, alpha=0.3)
plt.show()

#weryfikacja
M = 1000
est_th = []
for m in range(M + 1):
    expon = exp(theta, n)
    th = estymator_theta(expon)
    est_th.append(th)

fig = plt.plot(figsize=(12, 4))
plt.boxplot(est_th, vert=False, patch_artist=True, tick_labels=['x0'])
plt.title('estymator theta')
plt.show()
