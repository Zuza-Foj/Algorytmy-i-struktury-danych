def quicksort_iterative(arr):
    if len(arr) <= 1:
        return arr

    # stos przechowujący lewą i prawą granicę (index) sublist do posortowania
    stack = [(0, len(arr) - 1)]

    while stack:
        left, right = stack.pop()

        if left >= right:
            continue

        # podział listy na sublisty i ustalenie indexu pivota
        pivot_idx = partition(arr, left, right)

        # lewa i prawa sublista lądują na stosie
        # najpierw sortujemy mniejszą sublistę (ale jako pierwszą popychamy na stos dłuższą, więc zostanie posortowana jako druga)
        if pivot_idx - left > right - pivot_idx:
            stack.append((left, pivot_idx - 1))
            stack.append((pivot_idx + 1, right))
        else:
            stack.append((pivot_idx + 1, right))
            stack.append((left, pivot_idx - 1))

    return arr


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # ustawienie pivota na pozycji 'i + 1', po przejściu przez całą listę tam jest granica między mniejszymi i większymi od pivota
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

arr = [7, 6, 8, 1, 2, 3]
quicksort_iterative(arr)
print(arr)