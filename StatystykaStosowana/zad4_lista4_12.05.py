import numpy as np
import matplotlib.pyplot as plt

th = 2
M = 1000
n_vals = [100, 200, 500, 1000]

for n in n_vals:
    th_mm_l = []
    th_nw_l = []
    for m in range(M):
        y = np.random.exponential(1, n)
        x = y + th
        th_mm = sum(x) / n - 1
        th_nw = min(x)
        th_mm_l.append(th_mm)
        th_nw_l.append(th_nw)


