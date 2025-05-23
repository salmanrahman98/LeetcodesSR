# https://leetcode.com/problems/majority-element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dict_nums = {}
        maxVal = 0
        maxKey = nums[0]
        for i in range(len(nums)):
            if dict_nums.get(nums[i]):
                value = dict_nums.get(nums[i])
                value = value + 1
                dict_nums[nums[i]] = value
                # maxVal = max(value, maxVal)
                if value > maxVal:
                    maxVal = value
                    maxKey = nums[i]
            else:
                dict_nums[nums[i]] = 1

        return maxKey
