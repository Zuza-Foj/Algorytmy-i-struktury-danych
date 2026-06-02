import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

n1 = 1000
n2 = 10
mi = 10
sig = 5
proba1 = np.random.normal(loc=mi, scale=sig, size=n1)
ods = np.random.uniform(50, 100, 10)
proba2 = np.concatenate([proba1, ods])

sred1 = np.mean(proba1)
sred2 = np.mean(proba2)
print('średnia normalnego:', sred1)
print('średnia jednostajnego:', sred2)

mediana1 = np.median(proba1)
mediana2 = np.median(proba2)
print('mediana normalnego:', mediana1)
print('mediana jednostajnego:', mediana2)

iqr1 = stats.iqr(proba1)
iqr2 = stats.iqr(proba2)
print('odstęp międzykwartylowy normalnego:', iqr1)
print('omk jednostajego:', iqr2)

war1 = np.var(proba1)
war2 = np.var(proba2)
print('wariancaja normalnego:', war1)
print('w. jednostajnego:', war2)

od1 = np.std(proba1)
od2 = np.std(proba2)
print('odchylenie standardowe normalnego:', od1)
print('os jednostajnego:', od2)

kurt1 = stats.kurtosis(proba1)
kurt2 = stats.kurtosis(proba2)
print('kurtoza normalnego:', kurt1)
print('k. jednostajego:', kurt2)

skos1 = stats.skew(proba1)
skos2 = stats.skew(proba2)
print('skośność normalnego:', skos1)
print('skośność jednostajnego:', skos2)

plt.figure(figsize=(9,4))
plt.subplot(1, 2, 1)
plt.hist(proba1)
plt.subplot(1, 2, 2)
plt.hist(proba2)
plt.show()
plt.boxplot([proba1, proba2])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

