my_list = [6, 3, 10, 4, 2, 9, 8, 5, 1, 7]

n = len(my_list)
for j in range(n - 1):
    if my_list[j] > my_list[j + 1]:
        my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print(my_list)
