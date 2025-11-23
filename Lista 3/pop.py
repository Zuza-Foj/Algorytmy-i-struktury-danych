import timeit
import matplotlib.pyplot as plt

N = 100000
reps = 10

test_index = {"Koniec (n - 1)": N - 1, "Środek (n // 2)": N // 2, "Początek (0)": 0}
exe_time = {}

def make_list(size):
     return list(range(size))

for name_index, index in test_index.items():
    SETUP_CODE = f"L = list(range({N}))"
    STATEMENT_CODE = f"L.pop({index})"
    measure= timeit.repeat(
        stmt=STATEMENT_CODE,
        setup=SETUP_CODE,
        repeat=reps,
        number=1
    )

    min_time = min(measure)
    exe_time[name_index] = min_time

    indexes = list(exe_time.keys())
    times = list(exe_time.values())
    plt.figure(figsize=(8, 6))
    plt.bar(indexes, times, color=['green', 'orange', 'red'])
    plt.ylabel('Minimalny Czas Wykonania (sekundy)')
    plt.title(f'Czas Wykonania Metody list.pop(i) dla N={N}')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for i, czas in enumerate(times):
        plt.text(i, czas + max(times) * 0.01, f'{czas:.6f}', ha='center')

    plt.tight_layout()
    plt.show()