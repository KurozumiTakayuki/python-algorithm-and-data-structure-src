# 西暦
N = 2023

# Nが閏年かどうかを判定
if N % 4 != 0:
    print("平年です")
elif N % 100 != 0:
    print("閏年です")
elif N % 400 != 0:
    print("平年です")
else:
    print("閏年です")
