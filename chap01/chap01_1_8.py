# 西暦
N = 2023

if N % 4 == 0 and (N % 100 != 0 or N % 400 == 0):
    print('閏年です')
else:
    print('平年です')
