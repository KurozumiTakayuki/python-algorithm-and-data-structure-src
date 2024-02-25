from heap_dump import dump


def shift_down(my_list, i):
    dump(my_list)
    left_idx = i * 2 + 1
    right_idx = i * 2 + 2
    last_idx = len(my_list) - 1
    minimum_val_idx = i

    # 対象ノードとその左子、右子のなかで最小値となるノードのインデックスを格納。初期値に対象ノードのインデックスを設定
    minimum_val_idx = i

    if left_idx <= last_idx and my_list[left_idx] < my_list[i]:
        # 左子 < 対象ノード
        minimum_val_idx = left_idx

    if right_idx <= last_idx and my_list[right_idx] < my_list[minimum_val_idx]:
        # 右子 < 対象ノード
        minimum_val_idx = right_idx

    if minimum_val_idx != i:
        # 左子、右子のどちらかが最小値の場合、対象ノードと交換し、再帰的にシフトダウンを行う
        my_list[i], my_list[minimum_val_idx] = my_list[minimum_val_idx], my_list[i]
        shift_down(my_list, minimum_val_idx)


shift_down([1, 10, 3, 5, 6, 2, 4, 8, 7, 9], 1)
