# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/1551362011/
def smallerNumbersThanCurrent(nums):

    # def_array = [0]
    sorted_nums = sorted(nums)

    # will contain key will have position
    temp_dict = {}
    for i, val in enumerate(sorted_nums):
        if val not in temp_dict:
            temp_dict[val] = i

    # for i in range(1, len(sorted_nums)):
    #     if sorted_nums[i] == sorted_nums[i-1]:
    #         def_array.append(len(def_array)-1)
    #     else:
    #         def_array.append(len(def_array))

    print(f"This is OG List: {nums}")
    print(f"This is dictionary: {temp_dict}")
    final_arr = []

    for i in nums:
        final_arr.append(temp_dict[i])

    return final_arr


nums = [80, 10, 20, 20, 30]
print(smallerNumbersThanCurrent(nums=nums))
