def max_in_S(elem):
    if len(elem) == 1:
        result = elem[0]
    else:
        max_res = max_in_S(elem[1:])
        if elem[0] > max_res:
            result = elem[0]
        else:
            result = max_res
    return result

print(max_in_S([1, 3, 2, 10, 7, 14, 2]))