def is_match(text1, text2):
    # 文字列の長さが異なる場合はFalse
    if len(text1) != len(text2):
        return False

    # 1文字ずつ検査を行い、異なっている場合はFalseを返す
    idx = 0
    while idx < len(text1):
        if text1[idx] != text2[idx]:
            return False
        idx += 1

    return True


result = is_match("abcd", "abcd")
print(result)
