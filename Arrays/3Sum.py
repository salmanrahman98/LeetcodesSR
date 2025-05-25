# https://leetcode.com/problems/3sum/submissions/1643518462/?envType=problem-list-v2&envId=array
class Solution(object):

    def partition(self, arr, start, end):
        pivot = arr[end]
        i = start - 1

        for j in range(start, end):
            if arr[j] < pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        i = i + 1
        arr[i], arr[end] = arr[end], arr[i]
        return i

    def quickSort(self, arr, start, end):
        if (end <= start):
            return
        pivot = self.partition(arr, start, end)
        self.quickSort(arr, start, pivot - 1)
        self.quickSort(arr, pivot + 1, end)

        return arr

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        arr = self.quickSort(nums, 0, len(nums)-1)
        print(arr)

        finalArr = []
        for i, a in enumerate(arr):

            if i > 0 and arr[i] == arr[i-1]:
                continue
            l = i + 1
            r = len(arr) - 1

            while l < r:
                sum = a + arr[l] + arr[r]

                if sum < 0:
                    l = l + 1
                elif sum > 0:
                    r = r - 1
                else:
                    finalArr.append([a, arr[l], arr[r]])
                    r = r - 1
                    while arr[r] == arr[r + 1] and l < r:
                        r = r - 1

        return finalArr


solution = Solution()
nums = [-1, 1, -1, 1]
print(solution.threeSum(nums))
