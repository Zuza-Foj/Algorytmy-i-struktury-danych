def sum_of_matrix_elem(matrix):
    sum = 0
    for verse in matrix:
        for elem in verse:
            sum += elem
    return sum

print(sum_of_matrix_elem([[1, 2, 3], [1, 2, 3]]))