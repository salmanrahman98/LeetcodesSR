def rev(word):
    return word[::-1]


def longestPalindrome(words):

    wordict = {}
    total = 0
    symmetry_counter = 0
    for i, word in enumerate(words):
        if word[0] == word[1]:
            # symmetrical scenario
            if wordict.get(word):
                total = total + 2
                del wordict[word]
                symmetry_counter -= 1
            else:
                wordict[word] = 1
                symmetry_counter = symmetry_counter + 1
        else:
            # unsymmetrical
            if wordict.get(rev(word)):
                total = total + 2
                value = wordict.get(rev(word))
                value = value - 1
                wordict[rev(word)] = value

                # value = wordict.get(word)
                # value = value - 1
                # wordict[word] = value
            elif wordict.get(word):
                value = wordict.get(word)
                value = value + 1
                wordict[word] = value
            else:
                wordict[word] = 1

    if symmetry_counter >= 1:
        total = total + 1
    print(total)
    return total * 2


print(longestPalindrome(["ll", "lb", "bb", "bx", "xx", "lx", "xx", "lx",
      "ll", "xb", "bx", "lb", "bb", "lb", "bl", "bb", "bx", "xl", "lb", "xx"]))

# ["qo","fo","fq","qf","fo","ff","qq","qf","of","of","oo","of","of","qf","qf","of"]
# Ans: 14
# ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
# Ans: 22
# ["ll","lb","bb","bx","xx","lx","xx","lx","ll","xb","bx","lb","bb","lb","bl","bb","bx","xl","lb","xx"]
# Ans: 26
