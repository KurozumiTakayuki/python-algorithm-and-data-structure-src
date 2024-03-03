# 計算対象の行列
X = [[0, 1, 0, 0],
     [1, 0, 0, 1],
     [0, 1, 0, 0],
     [0, 1, 1, 0],
     ]

# 結果格納用
result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          ]

N = len(X)

# 以下A^2を計算する

# 行方向にループ
for i in range(N):
    # 列方向にループ
    for j in range(N):
        # 要素積を足し上げてi行j列の要素を計算する
        for k in range(N):
            result[i][j] += X[i][k] * X[k][j]

# 元の行列と足し算
# 結果格納用
result2 = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           ]

for i in range(N):
    # 行方向にループ
    for j in range(N):
        # 列方向にループ
        result2[i][j] += X[i][j] + result[i][j]

# 結果を表示
print()
for r in result2:
    print(r)
