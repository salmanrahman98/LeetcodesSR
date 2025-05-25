# https://leetcode.com/problems/roman-to-integer/description/?envType=problem-list-v2&envId=string

def getValue(c) -> int:
    if c == 'I':
        return 1
    if c == 'V':
        return 5
    if c == 'X':
        return 10
    if c == 'L':
        return 50
    if c == 'C':
        return 100
    if c == 'D':
        return 500
    if c == 'M':
        return 1000


def romanToInt(s: str) -> int:
    total = 0
    i = 0
    while i < len(s):
        val1 = getValue(s[i])
        if i != len(s) - 1:
            val2 = getValue(s[i+1])

        if (i != len(s) - 1 and val2 > val1):
            total = total + (val2 - val1)
            i = i + 1
            val2 = 0
        else:
            total = total + val1
        i = i + 1

    return total


stringVar = "MDCXCV"
print(romanToInt(stringVar))

# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
