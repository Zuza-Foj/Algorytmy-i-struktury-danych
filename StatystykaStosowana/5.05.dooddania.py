import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

#generowanie realizacji pareto
def pareto(a, x0, n):
    x = np.random.uniform(0, 1, n )
    F = x0 / (1 - x)**(1/a)
    return F

# print(pareto(2, 3, 1000))

#estymatory
def estymatory_pareto(F):
    x0 = min(F)
    elem = []
    for xi in F:
        elem.append(np.log(xi / x0))
    mian = sum(elem)
    a = len(F) / mian
    return x0, a

#pareto(5, 2, 1000)
n = 1000
x0 = 2
p = pareto(5, x0, n)
x_e = np.sort(p)
y_e = np.arange(1, n + 1) / n
x_t = np.linspace(x0, np.max(p), n)
y_t = stats.pareto.cdf(x_t, 5, 0, x0)

plt.figure(figsize=(10, 5))
plt.plot(x_t, y_t, label='Teoretyczna', color='red', linewidth=2)
plt.plot(x_e, y_e, label='Empiryczna', color='blue', linestyle='--', alpha=0.7)
plt.title('Dystrybuanta Rozkładu Pareto (alpha=5, x0=2)')
plt.xlabel('Wartość x')
plt.ylabel('F(x)')
plt.grid(True, alpha=0.3)
plt.show()

#weryfikacja
M = 500
est_x = []
est_a = []
for m in range(M + 1):
    par = pareto(5, x0, n)
    x_i, a_i = estymatory_pareto(par)
    est_x.append(x_i)
    est_a.append(a_i)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.boxplot(est_x, vert=False, patch_artist=True, tick_labels=['x0'])
ax1.set_title('estymator x0')
ax2.boxplot(est_a, vert=False, patch_artist=True, tick_labels=['alfa'])
ax2.set_title('estymator alfy')
plt.tight_layout()
plt.show()