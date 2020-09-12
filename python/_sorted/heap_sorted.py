def heap_sort(arr):
    build_heap(arr)
    k = len(arr) - 1
    while k >= 0:
        arr[0], arr[k] = arr[k], arr[0]
        k -= 1
        heapify(arr, 0, k)


def heapify(arr, p, r):
    while True:
        max_pos = p
        left, right = (p << 1) + 1, (p << 1) + 2
        if left <= r and arr[left] > arr[max_pos]:
            max_pos = left
        if right <= r and arr[right] > arr[max_pos]:
            max_pos = right
        if max_pos == p:
            break
        arr[max_pos], arr[p] = arr[p], arr[max_pos]
        p = max_pos


def build_heap(arr):
    k = len(arr) - 1
    for i in range(k >> 1, -1, -1):
        heapify(arr, i, k)


if __name__ == '__main__':
    arr = [100, 1, 7, 2, 8, 1, 9, 2, 10, 23, 67, 12, 1, -8, -6, 92, 52, 1, 4, -2, 89, 23, 12, 200]
    heap_sort(arr)
    print(arr)
