def build_skip_table(pattern):
    skip_table = dict()
    pattern_length = len(pattern)
    for idx, char in enumerate(pattern[:-1]):
        skip_table[char] = pattern_length - idx - 1

    return skip_table


st1 = build_skip_table("abcd")
print(st1)
st2 = build_skip_table("abad")
print(st2)
