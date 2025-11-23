def iter_permutation(n):
    stack = []
    stack.append(([], list(range(1, n+1))))
    result = []

    while stack:
        perm, remaining = stack.pop()

        if len(remaining) == 0:
            result.append(perm)
            continue

        for i in range(len(remaining)):
            x = remaining[i]
            new_perm = perm + [x] # dokładam element do budowy permutacji
            new_remaining = remaining[:i] + remaining[i+1:] # to co zostało
            stack.append((new_perm, new_remaining))

    return result

print(iter_permutation(3))