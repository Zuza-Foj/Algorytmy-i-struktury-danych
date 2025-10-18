import matplotlib.pyplot as plt
import random
import time


def example1(S):
    """Return the sum of the elements in sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]
    return total

def example2(S):
    """Return the sum of the elements with even index in sequence S."""
    n = len(S)
    total = 0
    for j in range(0, n, 2):
        total += S[j]
    return total

def example3(S):
    """Return the sum of the prex sums of sequence S."""
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1+j):
            total += S[k]
    return total

def example4(A, B): # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prex sums in A."""
    n = len(A)
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1 + j):
                total += A[k]
        if B[i] == total:
            count += 1
    return count

num_of_elem = [10**i for i in range(2,5)]
li_of_li = []
for n in num_of_elem:
    li = random.sample(range(1, 10001), n)
    li_of_li.append(li)

functions = [example1, example2, example3]
for f in functions:
    print(f"Testing function {f.__name__}.")
    li_of_time = []
    for j in li_of_li:
        start = time.time()
        if f == example4:
            example4(j, j)
        else:
            f(j)
        end = time.time()
        li_of_time.append(end - start)

    plt.plot(num_of_elem, li_of_time, label=f.__name__)

    plt.xlabel("Number of Elements (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Performance Comparison of Functions")
    plt.legend()
    plt.show()





