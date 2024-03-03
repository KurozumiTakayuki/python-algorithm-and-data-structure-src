def digit_to_bin(digits):
    divided = digits
    result = []
    while divided:
        print(divided, "/ 2 = ", end="")
        mod = divided % 2
        result.insert(0, str(mod))
        divided = divided // 2
        print(divided, "・・・", mod)

    print("".join(result))


digit_to_bin(234)
