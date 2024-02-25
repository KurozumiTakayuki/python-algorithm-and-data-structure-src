def partition(my_list, start_idx, end_idx):
    # 右端の要素をピボットとする
    pivot = my_list[end_idx]
    # 左端-1をパーティションインデックスの初期位置とする
    partition_idx = start_idx - 1

    for idx in range(start_idx, end_idx):

        # 処理対象の要素
        target = my_list[idx]

        # 処理対象の要素がピボット以下かどうか
        if target <= pivot:
            # パーティションインデックスの位置を一つ進める
            partition_idx = partition_idx + 1

            # パーティションインデックスの位置の要素と交換
            my_list[partition_idx], my_list[idx] = my_list[idx], my_list[partition_idx]

    # パーティションインデックスの位置を一つ進める
    partition_idx = partition_idx + 1

    # ピボットをパーティションインデックスの位置の要素と交換
    my_list[partition_idx], my_list[end_idx] = my_list[end_idx], my_list[partition_idx]

    return partition_idx


def quick_sort(my_list, start_idx, end_idx):
    # start_idx < end_idxではない場合、指定範囲の長さが1以下なので処理終了
    if not (start_idx < end_idx):
        return

    partition_idx = partition(my_list, start_idx, end_idx)
    quick_sort(my_list, start_idx, partition_idx - 1)
    quick_sort(my_list, partition_idx + 1, end_idx)


data = [9, 4, 3, 1, 6, 8, 0, 7, 2, 5]
n = len(data)
quick_sort(data, 0, n - 1)
print(data)

