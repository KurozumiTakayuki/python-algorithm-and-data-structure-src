my_list = [1, 3, 4, 6, 2]
print(my_list)

# 3番目の要素を1番目に挿入する場合
from_idx = 3
to_idx = 1

tmp = my_list.pop(from_idx)
my_list.insert(to_idx, tmp)
print(my_list)
