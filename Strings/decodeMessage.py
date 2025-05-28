def decodeMessage(key: str, message: str) -> str:

    key_dict = {}
    j = 0
    for k in key:
        if k == ' ':
            continue
        else:
            if k not in key_dict:
                key_dict[k] = j
                j = j + 1

    print(len(key_dict))
    print(key_dict)

    text = ""

    for c in message:
        if c != ' ':
            text = text + chr(key_dict.get(c) + 97)
            # print(f"{key_dict.get(c)+97} - {chr(key_dict.get(c)+97)}")
        else:
            text = text + " "

    return text


print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
