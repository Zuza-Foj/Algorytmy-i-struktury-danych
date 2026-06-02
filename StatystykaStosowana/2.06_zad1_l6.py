import scipy.stats as stats

x_bar = 231.33
s2 = 31.44
alp = 0.05
n = 12

t1 = stats.t.ppf(1 - alp/2, n - 1)
r1 = x_bar - t1

t2 = stats.chi2.ppf(1 - alp/2, n - 1)
r2 = x_bar - t2

print(r1, r2)



