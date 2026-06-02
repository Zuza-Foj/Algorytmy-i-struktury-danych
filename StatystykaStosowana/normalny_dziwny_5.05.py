import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

mi = 2
sig = 2**(1/2)
x = np.random.normal(mi, sig, 7)
theta_1 = np.random.normal(mi, sig/7, 500)
theta_2 = np.random.normal(mi, 3 * sig/2, 500)

M = 500
est_1 = []
est_2 = []
for i in range(M):
    x = np.random.normal(mi, sig, 7)
    th1 = sum(x)/7
    th2 = (2*x[0]-x[5]+x[3])/2
    est_1.append(th1)
    est_2.append(th2)

est_1 = np.array(est_1)
est_2 = np.array(est_2)
x1_sorted = np.sort(est_1)
x2_sorted = np.sort(est_2)

cdf_e_1 = np.arange(1, M + 1) / M
cdf_e_2 = np.arange(1, M + 1) / M

std_1 = sig / np.sqrt(7)
std_2 = np.std(est_2)

x_range_1 = np.linspace(x1_sorted.min(), x1_sorted.max(), 500)
x_range_2 = np.linspace(x2_sorted.min(), x2_sorted.max(), 500)

cdf_t_1 = stats.norm.cdf(x_range_1, loc=mi, scale=std_1)
cdf_t_2 = stats.norm.cdf(x_range_2, loc=mi, scale=std_2)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].step(x1_sorted, cdf_e_1, label='Empiryczna', color='red', linewidth=2)
axes[0].plot(x_range_1, cdf_t_1, label='Teoretyczna', color='blue', linestyle='--', alpha=0.9)
axes[0].set_title('theta 1')
axes[0].set_xlabel('x')
axes[0].set_ylabel('F(x)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].step(x2_sorted, cdf_e_2, label='Empiryczna', color='red', linewidth=2)
axes[1].plot(x_range_2, cdf_t_2, label='Teoretyczna', color='blue', linestyle='--', alpha=0.9)
axes[1].set_title('theta 2')
axes[1].set_xlabel('x')
axes[1].set_ylabel('F(x)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.suptitle('Dystrybuanta Rozkładu', fontsize=14)
plt.tight_layout()
plt.show()