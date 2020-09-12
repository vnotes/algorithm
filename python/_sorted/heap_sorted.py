def heap_sorted(arr):
    build_heap(arr)
    k = len(arr) - 1
    while k >= 0:
        arr[0], arr[k] = arr[k], arr[0]
        k -= 1
        heapify(arr, 0, k)


def heapify(arr, i, k):
    while True:
        max_pos = i
        left, right = (i << 1) + 1, (i << 1) + 2
        if left <= k and arr[left] > arr[max_pos]:
            max_pos = left
        if right <= k and arr[right] > arr[max_pos]:
            max_pos = right
        if max_pos == i:
            return
        if arr[max_pos] > arr[i]:
            arr[max_pos], arr[i] = arr[i], arr[max_pos]
        i = max_pos


def build_heap(arr):
    for i in range((len(arr) - 1) << 1, -1, -1):
        heapify(arr, i, len(arr) - 1)


if __name__ == '__main__':
    arr = [1, 6, 0, 2, 10, 5, 7, 1, -2]
    heap_sorted(arr)
    print(arr)
