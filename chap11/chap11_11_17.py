def my_rpn(rpn_text):
    # 計算用のスタックを初期化
    my_stack = []

    # スペース区切りでリストに変換する
    data_list = rpn_text.split(" ")

    for x in data_list:

        # 途中結果の確認
        print(x, my_stack)

        # 1つずつ処理を行う
        if x not in ["+", "-", "*", "+"]:
            # 演算子以外の場合はスタックに挿入する
            my_stack.append(x)
        else:
            # 演算子の場合はスタックから2つ被演算子を取り出して計算を行う
            operand2 = my_stack.pop()
            operand1 = my_stack.pop()
            operator = x
            calc_text = str(operand1) + operator + str(operand2)
            result = eval(calc_text)

            # 計算結果をスタックに挿入する
            my_stack.append(result)

    # 結果を取り出して表示する
    result = my_stack.pop()
    print(result)


my_rpn("3 7 + 2 5 - *")
