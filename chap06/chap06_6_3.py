def my_linear_search_sentinel(my_list, val):
    idx = 0
    N = len(my_list)
    # 番兵を末尾に追加
    my_list.append(val)

    while True:
        if my_list[idx] == val:
            break
        idx += 1

    if idx == N:
        print("見つかりませんでした")
    else:
        print(str(idx) + "番目に見つかりました")


l = [1, 5, 3, 7, 2]
my_linear_search_sentinel(l, 3)
my_linear_search_sentinel(l, 6)
