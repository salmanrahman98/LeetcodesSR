def validPalindrome(s: str) -> bool:

    print(s[len(s)-1])

    i = 0
    j = len(s) - 1
    while i <= j:
        if j - i == 0:
            if s[i] == s[j]:
                print("palindrome")
                break
        elif j - i == 1:
            if s[i] != s[j]:
                print("palindrome")
                break
        elif j - i > 1:
            if s[i] == s[j]:
                i = i + 1
                j = j - 1
                continue
            else:
                # neglect each ones and check
                # neglect i check
                dummyI = s[:i] + s[i+1:]
                dummyJ = s[:j] + s[j+1:]
                if dummyI == dummyI[::-1]:
                    print("palindrome")
                    break
                elif dummyJ == dummyJ[::-1]:
                    print("palindrome")
                    break
                else:
                    print("not palindrome")
                    break

    return s


print(validPalindrome("abc"))
