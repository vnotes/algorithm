def quick_sorted(arr):
    quick_sorted_internal(arr, 0, len(arr) - 1)


def quick_sorted_internal(arr, p, r):
    while p < r:
        pivot = partition(arr, p, r)
        quick_sorted_internal(arr, pivot + 1, r)
        r = pivot - 1


def partition(arr, p, r):
    pivot = arr[r]
    i = p
    for j in range(p, r):
        if arr[j] <= pivot:
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


if __name__ == '__main__':
    # nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    nums = [18, 12, 6, 8, 1, 2, 9, 3, 4, 10]
    quick_sorted(nums)
    print(nums)
