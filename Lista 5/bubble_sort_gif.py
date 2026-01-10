import matplotlib.pyplot as plt
import numpy as np
import imageio
import io

def generate_gif():
     n = 20
     data = np.random.randint(1, 100, n)
     frames = []

     arr = data.copy()
     for i in range(n):
         for j in range(n - i - 1):
             if arr[j] > arr[j + 1]:
                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

             plt.figure(figsize=(10, 6))

             colors = []
             for x in range(n):
                 if x >= n - i:
                     colors.append('green')
                 elif x == j or x == j + 1:
                     colors.append('red')
                 else:
                     colors.append('skyblue')

             plt.bar(range(n), arr, color=colors)
             plt.title(f"Sortowanie bąbelkowe")
             plt.ylim(0, 110)

             buf = io.BytesIO()
             plt.savefig(buf, format='png')
             buf.seek(0)
             frames.append(imageio.v2.imread(buf))
             plt.close()

     imageio.mimsave('sortowanie_babelkowe.gif', frames, fps=10)
     print("Plik sortowanie_babelkowe.gif został wygenerowany!")

generate_gif()