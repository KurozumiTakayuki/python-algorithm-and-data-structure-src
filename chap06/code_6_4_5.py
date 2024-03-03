def my_binary_search(data_list, target):
    left = 0
    right = len(data_list) - 1

    while left <= right:
        print(data_list[left: right + 1])

        # left～rightの中央を求める
        mid = (right + left) // 2

        # 範囲の中央の値が対象データより小さい場合、範囲を右側に狭める
        if data_list[mid] < target:
            left = mid + 1

        # 範囲の中央の値が対象データより大きい場合、範囲を左側に狭める
        elif data_list[mid] > target:
            right = mid - 1

        # 一致する場合
        else:
            print(mid, "番目に見つかりました")
            return

    print("見つかりませんでした")


my_binary_search([1, 2, 5, 7, 9, 15, 21, 22, 25, 28, 31, 35], 22)
