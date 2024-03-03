def my_rle(my_string):
    """ 指定した文字列をランレングスで圧縮する """

    # 圧縮結果を格納するリスト
    result_list = []

    # 各データの個数を格納するカウンタ
    counter = 1

    pre_char = my_string[0]  # 0番目の文字を予め格納

    # 1番目の文字からループ処理を行う
    for char in my_string[1:]:

        # 1つ前の文字と等しい場合、カウンタをインクリメントする
        if char == pre_char:
            counter += 1
        else:
            result_list.append((pre_char, counter))
            counter = 1
        pre_char = char

    # 最後の文字とそのカウンタの値を格納する
    result_list.append((pre_char, counter))
    print(result_list)


my_rle("AAAAAAAAAABBBBBCCCCCCCC")
