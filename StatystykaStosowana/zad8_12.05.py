import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

mi = 0
sig = 1
n_val = np.arange(10, 1001, 10)
M = 1000

mse1_e = []
mse1_t = []
mse2_e = []
mse2_t = []
for n in n_val:
    th1_l = []
    th2_l = []
    for i in range(M):
        x = np.random.normal(mi, sig, 2*n + 1)
        th1 = np.mean(x)
        th2 = np.median(x)
        th1_l.append(th1)
        th2_l.append(th2)

    mse1_l = []
    for i in range(M):
        m1 = (th1_l[i] - mi)**2
        mse1_l.append(m1)

    mse2_l = []
    for i in range(M):
        m2 = (th2_l[i] - mi)**2
        mse2_l.append(m2)

    MSE1 = sum(mse1_l) / M
    mse1_e.append(MSE1)
    MSE2 = sum(mse2_l) / M
    mse2_e.append(MSE2)

    s_MSE1 = np.mean(mse1_l)
    mse1_t.append(s_MSE1)
    s_MSE2 = np.mean(mse2_l)
    mse2_t.append(s_MSE2)


#plt.plot(n_val, mse1_t, label='mse 1 teoretyczny')
plt.xlabel('n')
plt.ylabel('mse')
plt.plot(n_val, mse1_e, label='mse 1 empiryczny')
#plt.plot(n_val, mse2_t, label='mse 2 teoretyczny')
plt.plot(n_val, mse2_e, label='mse 2 empiryczny')
plt.legend()
plt.show()



