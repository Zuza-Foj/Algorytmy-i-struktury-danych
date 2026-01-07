def chaining(keys, size=11):
    hash_table = [[] for _ in range(size)]
    for key in keys:
        index = (3 * key + 5) % size
        hash_table[index].append(key)

    return hash_table

keys = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]

table_result = chaining(keys, 11)
print(table_result)