my_list = [7, 5, 6, 4, 3, 0, 2, 1]
n = len(my_list)
interval = n // 2
while interval > 0:
    print(interval)
    # 後でここにソート処理を追加する
    interval //= 2
