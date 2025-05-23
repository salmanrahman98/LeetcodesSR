class Solution:
    def isPalindrome(x: int) -> bool:

        if x < 0:
            return False
        num = 0
        og_num = x
        while int(x):
            num = num * 10 + int(x) % 10
            x = x / 10

        if og_num == num:
            return True
        else:
            return False

    print(isPalindrome(121))
