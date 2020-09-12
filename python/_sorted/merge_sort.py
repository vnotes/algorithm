def merge_sort(arr):
    _merge_sort_internal(arr, 0, len(arr) - 1)


def _merge_sort_internal(arr, p, r):
    if p >= r:
        return
    q = p + ((r - p) >> 1)
    _merge_sort_internal(arr, p, q)
    _merge_sort_internal(arr, q + 1, r)
    merge(arr, p, q, r)


def merge(arr, p, q, r):
    i = p
    j = q + 1
    tmp = []
    while i <= q and j <= r:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    if i <= q:
        tmp.extend(arr[i:q + 1])
    if j <= r:
        tmp.extend(arr[j: r + 1])
    arr[p:r + 1] = tmp


if __name__ == '__main__':
    arr = [2, -1, 0, 4, 5, 1, -5]
    merge_sort(arr)
    print(arr)
