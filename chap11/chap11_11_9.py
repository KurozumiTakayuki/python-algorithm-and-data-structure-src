def compress(text, codes):
    compressed = ""
    for c in text:
        code = codes.get(c)
        compressed += code
    return compressed


def main():
    text = "BDDAAAABACEBBBAA"
    codes = {'A': '1', 'B': '00', 'D': '010', 'C': '0110', 'E': '0111'}
    compressed = compress(text, codes)
    print(compressed)


main()
