def twoSum(nums, target):
    # temp_dict = {}
    # for i, v in enumerate(nums):
    #     temp_dict[i] = v

    sorted_nums = sorted(nums)
    i = 0
    j = len(nums)-1

    while i <= j:
        sum = sorted_nums[i] + sorted_nums[j]
        if sum == target:
            # save i and j
            # return [temp_dict[i], temp_dict[j]]
            i = sorted_nums[i]
            j = sorted_nums[j]
            break
        elif sum < target:
            i += 1
        elif sum > target:
            j -= 1

    a = -1
    b = -1

    for k in range(0, len(nums)):
        if a == -1 and nums[k] == i:
            a = k
        elif nums[k] == j:
            b = k

    arr = [a, b]
    # arr.sort()
    return arr


nums = [3, 2, 4]
print(twoSum(nums, 6))
