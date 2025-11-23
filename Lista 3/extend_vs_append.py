import random, time, matplotlib.pyplot as plt, math

initial_list = list(range(100))
num_of_elem = [50, 100, 150, 200, 300, 1000]
li_of_li = [random.sample(range(1, 10**4), n) for n in num_of_elem]

li_of_times_e = []
for l in li_of_li:
    current_list = list(initial_list)
    start = time.time()
    current_list.extend(l)
    end = time.time()
    li_of_times_e.append(end - start)

li_of_times_a = []
for l in li_of_li:
    current_list = list(initial_list)
    start = time.time()
    for i in l:
        current_list.append(i)
    end = time.time()
    li_of_times_a.append(end - start)

n = num_of_elem
plt.figure(figsize=(10, 6))
plt.xscale('log')
plt.yscale('log')
plt.plot(n, li_of_times_e, 'o-', label='extend function')
plt.plot(n, li_of_times_a, 's--', label='append loop')
plt.xlabel("Number of Elements (n) to add")
plt.ylabel("Execution Time (s)")
plt.title("Comparison: Extend vs. Append Loop Efficiency")
plt.xticks(num_of_elem, num_of_elem)
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()