def shell_sort(my_list):
    n = len(my_list)
    interval = n // 2
    while interval > 0:
        print("インターバル =", interval)

        # インデックスがinterval以降のものをソート
        for i in range(interval, n):
            target = my_list[i]
            j = i

            # グループ内で挿入ソートを実行する
            while j >= interval and target < my_list[j - interval]:
                my_list[j] = my_list[j - interval]
                j -= interval
            my_list[j] = target
            print(my_list)

        interval //= 2


data = [7, 5, 6, 4, 3, 0, 2, 1]
shell_sort(data)
print(data)
