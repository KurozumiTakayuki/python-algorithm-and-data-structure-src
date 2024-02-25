def merge(my_list, start_idx, mid_idx, end_idx):
    # 右側、左側をコピーしたリストを新たに生成
    left_copy = my_list[start_idx:mid_idx + 1]
    right_copy = my_list[mid_idx + 1:end_idx + 1]

    # 元のリスト、左コピー、右コピーのそれぞれの0番目のインデックス
    idx = start_idx
    left_idx = 0
    right_idx = 0
    left_count = len(left_copy)
    right_count = len(right_copy)

    # 左コピー、右コピーのそれぞれの0番目から順に比較し、小さいものを元のリストに設定
    while left_idx < left_count and right_idx < right_count:
        if left_copy[left_idx] <= right_copy[right_idx]:
            # 左側要素の要素が右側以下の場合（※ ここで、不等号にイコールが入っているため安定なソートとなる）
            my_list[idx] = left_copy[left_idx]

            # インデックスを進める
            idx += 1
            left_idx += 1
        else:
            # 右側要素のほうが小さい場合
            my_list[idx] = right_copy[right_idx]

            # インデックスを進める
            idx += 1
            right_idx += 1

    # 残った要素を元のデータ列に戻す
    while left_idx < left_count:
        my_list[idx] = left_copy[left_idx]
        idx += 1
        left_idx += 1

    while right_idx < right_count:
        my_list[idx] = right_copy[right_idx]
        idx += 1
        right_idx += 1


data = [1, 2, 0, 3]
n = len(data)
start_idx = 0
end_idx = len(data) - 1
mid_idx = (start_idx + end_idx) // 2
merge(data, 0, mid_idx, n - 1)
print(data)
