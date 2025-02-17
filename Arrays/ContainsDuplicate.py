# https://leetcode.com/problems/contains-duplicate/
def contains_duplicate(nums):
    my_set = set(nums)
    # for x in nums:
    #      my_set.add(x)
    if len(nums) == len(my_set):
        return False
    else:
        return True


nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print(contains_duplicate(nums1))
print(contains_duplicate(nums2))
print(contains_duplicate(nums3))
