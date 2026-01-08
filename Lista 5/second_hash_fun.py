def second_hash_function(keys, size=11):
    hash_table = [None] * size
    for k in keys:
        h1 = (3 * k + 5) % size
        h2 = 7 - (k % 7)

        index = h1
        j = 0
        while hash_table[index] is not None:
            j += 1
            index = (h1 + j * h2) % size

            if j >= size:
                raise Exception(f"Nie znaleziono miejsca dla klucza!")

        hash_table[index] = k
    return hash_table

keys = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
result_table = second_hash_function(keys)
print(result_table)