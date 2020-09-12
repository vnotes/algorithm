def find_kth_number(arr, k):
    if k <= 0 or k > len(arr):
        return

    pivot = partition(arr, 0, len(arr) - 1)
    while (pivot + 1) != k:
        if pivot + 1 > k:
            pivot = partition(arr, 0, pivot - 1)
        else:
            pivot = partition(arr, pivot + 1, len(arr) - 1)
    return arr[pivot]


def quick_sorted_internal(arr, p, r):
    if p >= r:
        return
    pivot = partition(arr, p, r)
    quick_sorted_internal(arr, p, pivot - 1)
    quick_sorted_internal(arr, pivot + 1, r)


def partition(arr, p, r):
    pivot = arr[r]
    i = p
    for j in range(p, r):
        if arr[j] < pivot:
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


if __name__ == '__main__':
    numbers = [5, 8, 1, 2, 7]
    print(find_kth_number(numbers, 3))
