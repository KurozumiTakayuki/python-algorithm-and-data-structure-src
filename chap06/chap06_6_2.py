def my_linear_search2(my_list, val):
    idx = 0
    N = len(my_list)

    while idx < N:
        if my_list[idx] == val:
            print(str(idx) + "番目に見つかりました")
            return
        idx += 1
    print("見つかりませんでした")


l = [1, 5, 3, 7, 2]
my_linear_search2(l, 3)
my_linear_search2(l, 6)
