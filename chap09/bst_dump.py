"""
MyBSTreeの内部確認のための簡易ツールです。
表示可能な最大階層数は0から数えて3となります。また、2桁以上の数字をキーに指定するとレイアウトが崩れることがあります。
"""
from copy import deepcopy

MAX_LV = 3
MAX_COL_NUM = 2 ** (MAX_LV + 2) - 1


def build_matrix(node, pos, lv, data_matrix):
    if not node:
        return

    if len(data_matrix) <= lv:
        return
    interval = int(16 * (1 / 2) ** (lv + 1))
    data_matrix[lv][pos] = node
    if node.left:
        left_pos = pos - int(interval // 2)
        build_matrix(node.left, left_pos, lv + 1, data_matrix)
    if node.right:
        right_pos = pos + int(interval // 2)
        build_matrix(node.right, right_pos, lv + 1, data_matrix)


def dump(bst):
    row = [None] * MAX_COL_NUM
    rows = [deepcopy(row) for _ in range(0, MAX_LV + 1)]
    base_pos = int(MAX_COL_NUM // 2)
    build_matrix(bst.root, base_pos, 0, rows)

    for idx, row in enumerate(rows):
        # 枝の描画
        if idx != 0:
            for node in row:
                if node is None:
                    print("  ", end="")
                else:
                    if node.is_left:
                        print("／", end="")
                    else:
                        print("＼", end="")
            print()

        # キーの描画
        for node in row:
            if node is None:
                print("  ", end="")
            else:
                if node.is_left:
                    print(str(node.key) + " ", end="")
                else:
                    print(" " + str(node.key), end="")

        print()

    print()
