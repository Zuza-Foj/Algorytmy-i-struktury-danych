def power(x, n, depth=0):
    """Compute the value x**n for integer n."""
    print("\t" * depth + f"--> Wywołanie: power({x}, {n})")
    if n == 0:
        print("\t" * depth + f"--> Zwraca 1 dla n = 0")
        return 1
    else:
        res = x * power(x, n - 1, depth + 1)
        print("\t" * depth + f"--> Wynik: power({x}, {n}) = {res}")
        return res

print(f"Ostateczny wynikpower:", power(2, 5))