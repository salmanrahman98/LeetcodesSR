# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
class Solution:
    def finalValueAfterOperations(operations):

        x = 0
        for i in operations:
            if i[1] == '-':
                x -= 1
            elif i[1] == '+':
                x += 1
        return x

    operations = ["--X", "X++", "X++"]
    print(finalValueAfterOperations(operations))
