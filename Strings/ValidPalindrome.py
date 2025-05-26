# https://leetcode.com/problems/valid-palindrome/description/?envType=problem-list-v2&envId=string
import re


def isPalindrome(s: str) -> bool:

    s = s.lower()
    print(s)
    pattern = r"[a-z0-9]"
    matches = re.findall(pattern, s)
    print(matches)
    res = ''.join(matches)
    print(res)
    if res == res[::-1]:
        print("palindrome")
    else:
        print("not")


isPalindrome("0P")
