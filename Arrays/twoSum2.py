
def twoSum(numbers, target: int):

    i = 0
    j = len(numbers)-1
    while (i <= j):
        add = numbers[i] + numbers[j]
        if add == target:
            return [i+1, j+1]
        elif numbers[j] > target:
            j = j - 1
        elif numbers[i] < target:
            i = i + 1
    return []


print(twoSum([-5, -3, 0, 2, 4, 6, 8], 5))
