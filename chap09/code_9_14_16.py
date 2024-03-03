from heap_dump import dump


def shift_down(my_list, start_idx, i):  # ← 引数追加
    dump(my_list, start_idx)  # ← 引数追加
    left_idx = (i - start_idx) * 2 + 1 + start_idx  # ← 式修正
    right_idx = (i - start_idx) * 2 + 2 + start_idx  # ← 式修正
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
        shift_down(my_list, start_idx, minimum_val_idx)  # ← 引数追加


def heapify(my_list, start_idx):  # ← 引数追加
    last_idx = len(my_list) - 1  # 末尾のインデックス
    last_parent_idx = ((last_idx - start_idx - 1) // 2) + start_idx  # 子を持つ最も深い要素のインデックス
    for i in reversed(range(start_idx, last_parent_idx + 1)):
        print("シフトダウン対象ノード:", my_list[i])
        shift_down(my_list, start_idx, i)  # ← 引数追加
        print("------------------------------------------------")


def heap_sort(my_list):
    # ソート対象のlist型変数
    for start_idx in range(0, len(my_list) - 1):
        print(f"=========={start_idx}番目以降のヒープ化開始==========")
        heapify(my_list, start_idx)  # ← 引数追加
        print(f"=========={start_idx}番目以降のヒープ化終了==========")


data = [7, 6, 2, 3, 5, 4, 1]
heap_sort(data)
print(data)
