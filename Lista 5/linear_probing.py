def linear_probing(keys, size=11):
    hash_table = [None] * size
    for key in keys:
        index = (3 * key + 5) % size

        start_index = index
        while hash_table[index] is not None:
            index = (index + 1) % size

            if index == start_index:
                raise Exception("Tablica jest pełna!")

        hash_table[index] = key

    return hash_table

keys = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
table_result = linear_probing(keys)
print(table_result)