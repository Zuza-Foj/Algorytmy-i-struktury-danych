def max_min(elem):
    if len(elem) == 1:
        return elem[0], elem[0]
    else:
        min_res, max_res = max_min(elem[1:])
        if elem[0] < min_res:
            new_min = elem[0]
        else:
            new_min = min_res
        if elem[0] > max_res:
            new_max = elem[0]
        else:
            new_max = max_res
        return new_min, new_max

print(max_min([1, 4, 6, 2]))