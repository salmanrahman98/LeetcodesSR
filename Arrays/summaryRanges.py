
def formatAndAppend(nums, l, r, arr):
    if nums[l] == nums[r - 1]:
        substring = f"{nums[l]}"
        arr.append(substring)
    else:
        substring = f"{nums[l]}->{nums[r-1]}"
        arr.append(substring)


def summaryRanges(nums):
    l = 0
    r = 0
    arr = []
    if len(nums) == 0:
        return []

    while r < len(nums):
        if nums[l] == nums[r] or nums[r] - 1 == nums[r - 1]:
            r = r + 1
        else:
            formatAndAppend(nums, l, r, arr)
            l = r

    formatAndAppend(nums, l, r, arr)

    return arr


nums = [0, 1, 2, 4, 5, 7]
print(summaryRanges(nums=nums))
