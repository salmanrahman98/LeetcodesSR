# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/1551362011/
def smallerNumbersThanCurrent(nums):

    # sort the numbers to get their values which each item holds
    sorted_nums = sorted(nums)

    # save indexes of each value in dictionary, but keep key as the value. so that we can fetch it back again from value.
    # we are mainly interested in the index. but have to use the value to fetch it out later.
    dictionary_positions = {}
    for position, val in enumerate(sorted_nums):
        if val not in dictionary_positions:
            dictionary_positions[val] = position

    # use the dictionary to fetch out the values of indexes of sorted array but in the order of the original array
    arr = []
    for value in nums:
        arr.append(dictionary_positions[value])
    print(arr)
    return arr


nums = [80, 10, 20, 20, 30]
print(smallerNumbersThanCurrent(nums=nums))
