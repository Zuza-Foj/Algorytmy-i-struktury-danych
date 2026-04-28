import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

N = 1000
M = 500

# (a) N(0, 1)
samp_e_a = []
for i in range(M + 1):
    x_a = np.random.normal(0, 1, N)
    u_a = max(x_a)
    samp_e_a.append(u_a)

n_a = np.linspace(min(samp_e_a), max(samp_e_a), 100)
pdf_t_a = N * (stats.norm.cdf(n_a)**(N-1)) * stats.norm.pdf(n_a)
cdf_t_a = stats.norm.cdf(n_a, 0, 1)**N

# (b) logN(1, 1)
samp_e_b = []
for i in range(M + 1):
    x_b = np.random.lognormal(1, 1, N)
    u_b = max(x_b)
    samp_e_b.append(u_b)

n_b = np.linspace(min(samp_e_b), max(samp_e_b), 100)
cdf_t_b = stats.lognorm.cdf(n_b, s=1, scale=np.exp(1))**N
pdf_t_b = N * (stats.lognorm.cdf(n_b, s=1, scale=np.exp(1))**(N-1)) * stats.lognorm.pdf(n_b, s=1, scale=np.exp(1))

# (c) Pareto(2, 3)
samp_e_c = []
for i in range(M + 1):
    x_c = (np.random.pareto(3,  N) + 1) * 2
    u_c = max(x_c)
    samp_e_c.append(u_c)

n_c = np.linspace(min(samp_e_c), max(samp_e_c), 1000)
cdf_t_c = stats.pareto.cdf(n_c, b=3, scale=2)**N
pdf_t_c = N * (stats.pareto.cdf(n_c, b=3, scale=2)**(N-1)) * stats.pareto.pdf(n_c, b=3, scale=2)

# rysowanie:
fig, axs = plt.subplots(3, 2, figsize=(20, 10))
fig.suptitle("Porównanie teoretycznych i empirycznych wartości funkcji, dla podanych rozkładów", fontsize=14)

# (a)
# dystrybuanta
axs[0, 0].hist(samp_e_a, bins=30, density=True, cumulative=True, alpha=0.7, color='green')
axs[0, 0].set_title("(a)")
axs[0, 0].set_xlabel("x_a")
axs[0, 0].set_ylabel("CDF")

axs[0, 0].plot(n_a, cdf_t_a, 'r-', label='teoretyczna')

# gęstość
axs[0, 1].hist(samp_e_a, bins=50, density=True, alpha=0.7, color='blue')
axs[0, 1].set_title("(a)")
axs[0, 1].set_xlabel("x_a")
axs[0, 1].set_ylabel("PDF")

axs[0, 1].plot(n_a, pdf_t_a, 'r-', label='teoretyczna')

# (b)
# dystrybuanta
axs[1, 0].hist(samp_e_b, bins=30, density=True, cumulative=True, alpha=0.7, color='green')
axs[1, 0].set_title("(b)")
axs[1, 0].set_xlabel("x_b")
axs[1, 0].set_ylabel("CDF")

axs[1, 0].plot(n_b, cdf_t_b, 'r--', label='teoretyczna')

# gęstość
axs[1, 1].hist(samp_e_b, bins=50, density=True, alpha=0.7, color='blue')
axs[1, 1].set_title("(a)")
axs[1, 1].set_xlabel("x_a")
axs[1, 1].set_ylabel("PDF")

axs[1, 1].plot(n_b, pdf_t_b, 'r--', label='teoretyczna')

# (c)
# dystrybuanta
axs[2, 0].hist(samp_e_c, bins=30, density=True, cumulative=True, alpha=0.7, color='green')
axs[2, 0].set_title("(c)")
axs[2, 0].set_xlabel("x_c")
axs[2, 0].set_ylabel("CDF")

axs[2, 0].plot(n_c, cdf_t_c, 'r--', label='teoretyczna')

# gęstość
axs[2, 1].hist(samp_e_c, bins=50, density=True, alpha=0.7, color='blue')
axs[2, 1].set_title("(c)")
axs[2, 1].set_xlabel("x_c")
axs[2, 1].set_ylabel("PDF")

axs[2, 1].plot(n_c, pdf_t_c, 'r--', label='teoretyczna')

for ax in axs.flatten():
    ax.legend()
plt.tight_layout()

plt.show()