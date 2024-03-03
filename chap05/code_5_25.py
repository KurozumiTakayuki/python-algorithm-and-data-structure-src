def my_split(my_list, start_idx, end_idx):
    # start_idx < end_idxではない場合、指定範囲の長さが1以下なので処理終了
    if not (start_idx < end_idx):
        return

    # 分割するインデックス
    mid_idx = (start_idx + end_idx) // 2

    # ダンプのため、スライス構文で切り出し
    # スライス構文は指定範囲の1つ手前までなので1を足す

    # 左側（先頭～mid）
    left = my_list[start_idx:mid_idx + 1]

    # 左側（mid～末尾）
    right = my_list[mid_idx + 1:end_idx + 1]

    print(my_list, "=>", left, right)


data = [0, 1, 2, 3, 4]
my_split(data, 0, len(data) - 1)
