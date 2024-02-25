my_list = [1, 3, 4, 6, 2]
print(my_list)

# 3番目の要素を1番目に挿入する場合
from_idx = 3
to_idx = 1

# 3番目の要素を一時的に退避する
tmp = my_list[from_idx]

# 2番目の要素から先頭に向かってループ実行
i = from_idx - 1
while to_idx <= i:
    # 要素を右側にずらす
    my_list[i + 1] = my_list[i]
    print(my_list)
    i -= 1

# ずらし終わったら空いたところに操作対象要素を設定
my_list[i + 1] = tmp
print(my_list)
