# 西暦
N = 2023

# Nが閏年かどうかを判定
if N % 4 == 0:
    if N % 100 == 0:
        if N % 400 == 0:
            print("閏年です")
        else:
            print("平年です")
    else:
        print("閏年です")
else:
    print("平年です")
