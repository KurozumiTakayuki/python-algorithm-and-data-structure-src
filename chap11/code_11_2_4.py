conv_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
              8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def digit_to_hex(digits):
    divided = digits
    result = []
    while divided:
        print(divided, "/ 16 = ", end="")
        mod = divided % 16
        mod_hex = conv_table.get(mod)
        result.insert(0, mod_hex)
        divided = divided // 16
        print(divided, "・・・", mod)

    print("".join(result))


digit_to_hex(759)
