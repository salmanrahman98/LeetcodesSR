# https://leetcode.com/problems/move-zeroes/?envType=problem-list-v2&envId=array
class Solution:
    def moveZeros(nums) -> None:
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l = l+1

        return nums

    nums = [0, 0, 0, 0, 0, 0, 1, 1, 1]
    print(moveZeros(nums))
