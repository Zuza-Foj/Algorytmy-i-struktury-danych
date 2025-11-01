def multiply_rec(m, n):
    if n == 0:
        return 0
    else:
        return m + multiply_rec(m, n-1)

print(multiply_rec(2,5))