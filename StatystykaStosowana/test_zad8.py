import numpy as np

mi = 0
sig = 1
n = 10
#n = np.linspace(20, 1000, 20)
M = 1000
th1_l = []
th2_l = []

for i in range(M):
    x = np.random.normal(mi, sig, 2 * n + 1)
    th1 = np.mean(x)
    th2 = np.median(x)
    th1_l.append(th1)
    th2_l.append(th2)

mse1_l = []
for i in range(M):
    m1 = (th1_l[i] - mi) ** 2
    mse1_l.append(m1)

mse2_l = []
for i in range(M):
    m2 = (th2_l[i] - mi) ** 2
    mse2_l.append(m2)

MSE1 = sum(mse1_l) / M
MSE2 = sum(mse2_l) / M

s_MSE1 = np.mean(mse1_l)
s_MSE2 = np.mean(mse2_l)

print(s_MSE1, s_MSE2)