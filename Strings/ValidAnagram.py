def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    str = s

    for c in t:
        if c not in s:
            return False
        else:
            # str = str.replace(c, "")
            index = str.find(c)
            str = str[:index] + str[index+1:]

    if len(str) == 0:
        return True
    else:
        return False


print(isAnagram("aacc", "ccac"))
