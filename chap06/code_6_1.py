def my_linear_search(my_list, val):
    for i, n in enumerate(my_list):
        if n == val:
            print(str(i) + "番目に見つかりました")
            return

    print("見つかりませんでした")


l = [1, 5, 3, 7, 2]
my_linear_search(l, 3)
