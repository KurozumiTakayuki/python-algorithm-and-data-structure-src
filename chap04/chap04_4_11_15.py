class MyQueue:

    def __init__(self, N):

        self.N = N
        self.que = [None] * N
        self.head = 0  # キューの先頭
        self.tail = 0  # キューの末尾
        self.count = 0

    def enqueue(self, value):
        if self.count == self.N:
            # キューがいっぱいの場合はエンキュー失敗
            print("キューがいっぱいなのでエンキューできません。")
            return

        # キューの最後尾に値を設定
        self.que[self.tail] = value

        # データ件数+1
        self.count += 1

        # キューの最後尾の位置を1つ後ろにずらす。
        self.tail = (self.tail + 1) % self.N

    def dequeue(self):

        # キューに要素がない場合はデキュー失敗
        if self.count == 0:
            print("キューに要素がないのでデキューできません。")
            return

        # キューの先頭からデータを取り出す
        value = self.que[self.head]
        self.que[self.head] = None

        # データ件数-1
        self.count -= 1
        # 先頭の位置を1つ進める
        self.head = (self.head + 1) % self.N

        # 取り出した値を返す
        return value

    def __str__(self):
        return "(head:{head}, tail:{tail}) {que}".format(head=self.head, tail=self.tail, que=self.que)


q = MyQueue(4)
q.enqueue("a")
print(q)
q.enqueue("b")
q.enqueue("c")
print(q)

a = q.dequeue()
print(q)

b = q.dequeue()
print(q)

q.enqueue("d")
q.enqueue("e")
print(q)

c = q.dequeue()
d = q.dequeue()
print(q)
