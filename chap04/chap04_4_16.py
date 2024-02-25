import threading
import queue
import time

q = queue.Queue()


def producer():
    """ キューに処理対象データを追加 """
    print("producer: データ追加処理開始")
    # データをエンキュー（nは処理に要する時間で、順番に実行すると処理時間は14秒かかる）
    q.put({"task": "データ1", "n": 2})
    q.put({"task": "データ2", "n": 3})
    q.put({"task": "データ3", "n": 5})
    q.put({"task": "データ4", "n": 4})
    print("producer: データ追加処理終了")


def worker():
    """ キューからデータを取り出して処理を実行 """
    while True:
        item = q.get()
        if item is None:
            break
        print("worker:", item.get("task") + "の処理を開始します")
        time.sleep(item.get("n"))  # ダミー処理
        print("worker:", item.get("task") + "の処理を終了します")
        q.task_done()


def main():
    print("全体処理開始")
    start_time = time.perf_counter()

    # producerのスレッドを起動
    pt = threading.Thread(target=producer)
    pt.start()

    # workerのスレッドを2つ起動
    wts = []
    for _ in range(2):
        t = threading.Thread(target=worker)
        t.start()
        wts.append(t)

    # キューが空になるまで処理をブロック
    q.join()
    # thread数分Noneをpushして各workerのthreadを終了
    for _ in range(len(wts)):
        q.put(None)

    # 各スレッドが終了するまで待機
    pt.join()
    [t.join() for t in wts]

    # 処理時間を表示
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    print("全体処理終了", elapsed_time)


main()
