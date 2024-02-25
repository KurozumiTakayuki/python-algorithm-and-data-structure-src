def my_split(my_list, start_idx, end_idx):
    # 確認用にダンプ
    print(my_list[start_idx: end_idx + 1])

    # start_idx < end_idxではない場合、指定範囲の長さが1以下なので処理終了
    if not (start_idx < end_idx):
        return

    # 分割するインデックス（=右側の最初のインデックス）
    mid_idx = (start_idx + end_idx) // 2

    # 左側をさらに分割
    my_split(my_list, start_idx, mid_idx)

    # 右側をさらに分割
    my_split(my_list, mid_idx + 1, end_idx)


data = [0, 1, 2, 3, 4]
my_split(data, 0, len(data) - 1)
