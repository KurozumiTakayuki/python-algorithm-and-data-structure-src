"""
list型を二分木とみなして内容を確認するのための簡易ツールです。
表示可能な最大階層数は0から数えて3となります。また、3桁以上の数字をキーに指定するとレイアウトが崩れることがあります。
"""
from math import log2, ceil


def dump(my_list, start_idx=0):
    dump_list = my_list[start_idx:]
    N = len(dump_list)

    # 段数 = log2(n + 1) 切り上げ
    step_num = ceil(log2(N + 1))

    # 空白を含めた最下段の長さ
    lower_length = 2 ** step_num

    start_idx = 0
    upper_idx_list = []
    interval = 0
    for i in range(1, step_num + 1):
        end_idx = 2 ** i - 1
        data_row = ["   "] * (lower_length - 1)
        branch_row = ["   "] * (lower_length - 1)

        if not upper_idx_list:
            # 上の要素からの間隔
            interval = lower_length // 2
            current_idx = interval - 1
            data_row[current_idx] = str(dump_list[0]).center(3)
            upper_idx_list.append(current_idx)
        else:
            interval = interval // 2
            current_idx_list = []
            for upper_pos in upper_idx_list:
                current_idx1 = upper_pos - interval
                current_idx2 = upper_pos + interval
                current_idx_list.append(current_idx1)
                current_idx_list.append(current_idx2)

            for idx, (current_idx, val) in enumerate(zip(current_idx_list, dump_list[start_idx: end_idx])):
                data_row[current_idx] = str(val).center(3)
                if idx % 2 == 0:
                    branch_row[current_idx] = str("／").rjust(2)
                else:
                    branch_row[current_idx] = str("＼").ljust(2)

            upper_idx_list = current_idx_list

        print("".join(branch_row))
        print("".join(data_row))

        start_idx = end_idx
