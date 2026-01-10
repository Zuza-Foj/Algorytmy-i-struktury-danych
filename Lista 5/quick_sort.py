def quicksort_iterative(arr):
    if len(arr) <= 1:
        return arr

    # Stack stores (left, right) bounds of subarrays to sort
    stack = [(0, len(arr) - 1)]

    while stack:
        left, right = stack.pop()

        if left >= right:
            continue

        # Partition and get pivot index
        pivot_idx = partition(arr, left, right)

        # Push left and right subarrays onto stack
        # Push larger subarray first for better performance
        if pivot_idx - left > right - pivot_idx:
            stack.append((left, pivot_idx - 1))
            stack.append((pivot_idx + 1, right))
        else:
            stack.append((pivot_idx + 1, right))
            stack.append((left, pivot_idx - 1))

    return arr


def partition(arr, left, right):
    # Use rightmost element as pivot
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


# Test it
arr = [7, 6, 8, 1, 2, 3]
quicksort_iterative(arr)
print(arr)