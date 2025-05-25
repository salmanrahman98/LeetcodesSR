def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    i = i + 1
    print(pivot)
    print(arr[end])
    print(arr[i])
    arr[i], arr[end] = arr[end], arr[i]
    return i


def quickSort(arr, start, end):
    if end <= start:
        return
    pivot = partition(arr, start, end)
    quickSort(arr=arr, start=start, end=pivot - 1)
    quickSort(arr=arr, start=pivot + 1, end=end)
    return arr


nums = [80, 20, 40, 70, 10, 30, 90, 60, 50]
print(quickSort(nums, 0, len(nums) - 1))
