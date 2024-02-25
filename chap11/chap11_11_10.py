def decompress(compressed, codes):
    swapped_codes = {v: k for k, v in codes.items()}
    decompressed = ""
    code = ""
    for c in compressed:
        code += c
        value = swapped_codes.get(code)
        if value:
            decompressed += value
            code = ""

    print(decompressed)


def main():
    codes = {'A': '1', 'B': '00', 'D': '010', 'C': '0110', 'E': '0111'}
    compressed = "0001001011110010110011100000011"
    decompress(compressed, codes)


main()
