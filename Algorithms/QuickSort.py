def partition(arr, start, end) -> int:
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    i = i + 1
    arr[i], arr[end] = arr[end], arr[i]

    return i


def quickSort(arr, start, end):
    if end <= start:
        return

    pivot = partition(arr, start, end)
    quickSort(arr, start, pivot - 1)
    quickSort(arr, pivot + 1, end)

    # print(arr)
    return arr


nums = [8, 2, 4, 7, 1, 3, 9, 6, 5]
print(quickSort(nums, 0, len(nums) - 1))
