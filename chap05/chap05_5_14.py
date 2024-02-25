my_list = [1, 2, 7, 4, 10, 8, 6, 3, 9, 5]
n = len(my_list)
i = 2  # 2番目から処理を行う
target_idx = i
for j in range(i + 1, n):
    if my_list[j] < my_list[target_idx]:
        target_idx = j

print(target_idx)
