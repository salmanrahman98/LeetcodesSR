# https://leetcode.com/problems/first-letter-to-appear-twice/?envType=problem-list-v2&envId=string
def repeatedCharacter(s: str) -> str:
    str_dict = {}
    for c in s:
        if str_dict.get(c):
            return c
        else:
            str_dict[c] = 1


print(repeatedCharacter("aabb"))
