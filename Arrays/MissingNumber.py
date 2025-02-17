# https://leetcode.com/problems/missing-number/
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        elif len(nums) == 1 or nums[1] != 1:
            return 1
        for i in nums:
            if i + 1 == len(nums):
                return i+1
            if nums[i+1] - nums[i] != 1:
                return i+1

    nums = [3, 0, 1]
    print(missingNumber(0, nums))
