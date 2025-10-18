import random, time, matplotlib.pyplot as plt, math

num_of_elem = [200, 400, 800, 1600, 3200, 6400]
li_of_li = [random.sample(range(1, 10**8), n) for n in num_of_elem]

li_of_times = []
for l in li_of_li:
    start = time.time()
    sorted(l)
    end = time.time()
    li_of_times.append(end - start)

n_log_n = []
for x in num_of_elem:
    n_log_n.append(x * math.log2(x))

n_sq = []
for x in num_of_elem:
    n_sq.append(x**2)

scale_for_log = max(li_of_times) / max(n_log_n)
n_log_n_scaled = [scale_for_log * x for x in n_log_n]

scale_for_sq = max(li_of_times) / max(n_sq)
n_sq_scaled = [scale_for_sq * x for x in n_sq]

n = num_of_elem
plt.xscale('log')
plt.yscale('log')
plt.plot(n, li_of_times, 'o-', label='sorted function')
plt.plot(n, n_log_n_scaled, '--', label='O(n log n) (scaled)')
plt.plot(n, n_sq_scaled, ':', label='$O(n^2)$ (scaled)')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Execution Time (s)")
plt.title("Computational Complexity of Function Sorted ")
plt.xticks(num_of_elem, num_of_elem)
plt.legend()
plt.show()