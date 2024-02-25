import time

# 開始
start_time = time.perf_counter()

# ダミー処理
time.sleep(1)

# 終了
end_time = time.perf_counter()

# 経過時間を出力(秒)
elapsed_time = end_time - start_time
print(elapsed_time)
