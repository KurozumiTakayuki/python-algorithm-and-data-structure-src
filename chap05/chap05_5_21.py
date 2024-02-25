my_list = [7, 5, 6, 4, 3, 0, 2, 1]
n = len(my_list)
interval = 2

# インデックスがintervalから右側にある要素を1つずつソート
for i in range(interval, n):
    target = my_list[i]
    j = i

    # i番目の要素をグループ内の適切な位置に挿入
    while j >= interval and target < my_list[j - interval]:
        my_list[j] = my_list[j - interval]
        j -= interval
    my_list[j] = target
    print(my_list)
