# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
def findDisappearedNumbers(self, nums):
    # Zeroing method
    # zero_list = [0] * (len(nums))

    # for i in range(0, len(nums)):
    #     zero_list[nums[i]-1] = 1

    # final_list = []
    # for i in range(0, len(zero_list)):
    #     if zero_list[i] == 0:
    #         final_list.append(i+1)
    # return final_list
    # #############################################

    # Set Method
    num_set = set(nums)
    final_list = []
    for i in range(1, len(nums)+1):
        if i not in num_set:
            final_list.append(i)

    return final_list


nums = [4, 3, 2, 7, 8, 2, 3, 1]
# findDisappearedNumbers(0, nums=nums)
print(findDisappearedNumbers(0, nums))
