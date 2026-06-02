import matplotlib.pyplot as plt
import seaborn as sns

# age = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
# italy = [20, 239, 476, 958, 1856, 2797, 3880, 4823, 6355, 7855, 9799, 12057, 14461, 17382, 20271, 23195, 26221, 27381, 27690, 27152, 25995, 23771, 20082, 16811, 14160, 11023, 8051, 5426, 3384, 2151, 1367, 961, 641, 383, 318]
# poland = [111, 338, 606, 1214, 2058, 2703, 3476, 4424, 5898, 7887, 10375, 13332, 15685, 17717, 19158, 20000, 19394, 18110, 16952, 15018, 12753, 10998, 8882, 7358, 5920, 4386, 2868, 1793, 1097, 592, 345, 157, 80, 29, 14]
#
# sns.set_theme(style="whitegrid")
# plt.figure(figsize=(14, 10))
#
# # słupkowy
# sns.histplot(x=age, weights=italy, bins=len(age), kde=True, color="red", label='Włochy', alpha=0.4, element="step")
# sns.histplot(x=age, weights=poland, bins=len(age), kde=True, color="green", label='Polska', alpha=0.4, element="step")
# plt.title('Liczba urodzeń względem wieku matki')
# plt.xlabel('Wiek')
# plt.ylabel('Liczba urodzeń')
# plt.legend()
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()
#
# # liniowy: rozkład wieku matek
# plt.plot(age, italy, label='Włochy', color='green', marker='o', markersize=4)
# plt.plot(age, poland, label='Polska', color='red', marker='s', markersize=4)
# plt.title('Porównanie trendu (Wykres liniowy)')
# plt.xlabel('Wiek')
# plt.ylabel('Wartość')
# plt.legend()
# plt.show()
#
# plt.plot(age, italy, color='#e74c3c', label='Włochy', linewidth=3, marker='o', markersize=4, markevery=2)
# plt.fill_between(age, italy, color='#e74c3c', alpha=0.1)
# plt.plot(age, poland, color='#2ecc71', label='Polska', linewidth=3, marker='s', markersize=4, markevery=2)
# plt.fill_between(age, poland, color='#2ecc71', alpha=0.1)
#
# max_it_age = age[italy.index(max(italy))]
# max_pl_age = age[poland.index(max(poland))]
# plt.axvline(x=max_it_age, color='#c0392b', linestyle='--', alpha=0.6, label=f'Szczyt Włochy ({max_it_age} lat)')
# plt.axvline(x=max_pl_age, color='#27ae60', linestyle='--', alpha=0.6, label=f'Szczyt Polska ({max_pl_age} lat)')
#
# plt.title('Porównanie trendów urodzeń względem wieku matki', fontsize=16, pad=20)
# plt.xlabel('Wiek matki (lata)', fontsize=12)
# plt.ylabel('Liczba urodzeń', fontsize=12)
#
# plt.xticks(range(15, 51, 2))
# plt.legend(frameon=True, shadow=True, loc='upper right')
#
# plt.annotate('Punkt przecięcia trendów\n(ok. 24 lata)',
#              xy=(24, 7887), xytext=(18, 15000),
#              arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
#              fontsize=10, bbox=dict(boxstyle="round", fc="w"))
#
# plt.tight_layout()
# plt.show()
# # boxplot
# data_to_plot = [italy, poland]
# plt.boxplot(data_to_plot, vert=False, patch_artist=True, tick_labels=['Włochy', 'Polska'], boxprops=dict(facecolor='lightblue'), medianprops=dict(color='black'))
# plt.title('Rozkład wartości (Boxplot)')
# plt.xlabel('Wartości')
# plt.tight_layout()
# plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# 1. Konfiguracja estetyczna wykresów pod publikacje naukowe
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.titlesize': 14
})

# 2. Generowanie syntetycznego zbioru odzwierciedlającego rozkład z Twojej pracy
# (Zastąp to wczytaniem swojego pliku CSV: df = pd.read_csv("sleep_data.csv"))
np.random.seed(42)
n_samples = 150

# Generujemy dane dla kobiet (K) i mężczyzn (M) zgodnie z parametrami w Twoich tabelach
# Kobiety: Średnia ok 7.23, Skośność ujemna, odchylenie ok 1.28
shape_k, loc_k, scale_k = -3, 8.2, 1.4
data_k = stats.skewnorm.rvs(shape_k, loc=loc_k, scale=scale_k, size=n_samples)
data_k = np.clip(data_k, 5.8, 8.5) # przycięcie do min/max z tabeli

# Mężczyźni: Średnia ok 7.04, Skośność ujemna, odchylenie ok 1.0
shape_m, loc_m, scale_m = -2, 7.8, 1.1
data_m = stats.skewnorm.rvs(shape_m, loc=loc_m, scale=scale_m, size=n_samples)
data_m = np.clip(data_m, 5.9, 8.1)

df_k = pd.DataFrame({'Gender': 'Female', 'Quality of Sleep': data_k, 'Stress Level': np.random.randint(3, 9, n_samples)})
df_m = pd.DataFrame({'Gender': 'Male', 'Quality of Sleep': data_m, 'Stress Level': np.random.randint(4, 9, n_samples)})
df = pd.concat([df_k, df_m]).reset_index(drop=True)

# Korelujemy stres z jakością snu (ujemna zależność)
df['Stress Level'] = np.clip(12 - df['Quality of Sleep'] * 1.2 + np.random.normal(0, 0.8, len(df)), 1, 10).astype(int)

# --- WYKRES 1: HISTOGRAM GĘSTOŚCI + KDE ---
plt.figure(figsize=(9, 5))
# Obliczamy liczbę klas metodą Sturgesa: k = 1 + log2(n)
bins_sturges = int(1 + np.log2(n_samples))

sns.histplot(data=df, x='Quality of Sleep', hue='Gender', kde=True, stat='density',
             bins=bins_sturges, common_norm=False, palette='Set2', alpha=0.5, multiple="layer")
plt.title('Histogram gęstości oraz krzywa KDE jakości snu')
plt.xlabel('Jakość snu (skala 1-10)')
plt.ylabel('Gęstość prawdopodobieństwa')
plt.tight_layout()
plt.savefig('histogram_kde.pdf')
plt.close()

# --- WYKRES 2: DYSTRYBUANTA EMPIRYCZNA (ECDF) ---
plt.figure(figsize=(8, 5))
sns.ecdfplot(data=df, x='Quality of Sleep', hue='Gender', palette='Set2', linewidth=2)
plt.title('Dystrybuanta empiryczna (ECDF) jakości snu')
plt.xlabel('Jakość snu (skala 1-10)')
plt.ylabel('Prawdopodobieństwo empiryczne F_n(x)')
plt.tight_layout()
plt.savefig('ecdf_plot.pdf')
plt.close()

# --- WYKRES 3: BOXPLOT ---
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x='Gender', y='Quality of Sleep', palette='Set2', width=0.5)
plt.title('Wykres pudełkowy jakości snu w podziale na płeć')
plt.xlabel('Płeć')
plt.ylabel('Jakość snu (skala 1-10)')
plt.tight_layout()
plt.savefig('boxplot_jnd.pdf')
plt.close()

# --- WYKRES 4: SCATTER PLOT (STRES VS JAKOŚĆ SNU) ---
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x='Stress Level', y='Quality of Sleep', scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
plt.title('Zależność jakości snu od poziomu stresu')
plt.xlabel('Poziom stresu (skala 1-10)')
plt.ylabel('Jakość snu (skala 1-10)')
plt.tight_layout()
plt.savefig('scatter_stres.pdf')
plt.close()

print("Wykresy zostały pomyślnie wygenerowane i zapisane do plików PDF!")