class MyQueue:
    def __init__(self):
        self.que = []

    def enqueue(self, value):
        self.que.append(value)

    def dequeue(self):
        return self.que.pop(0)

    def __str__(self):
        return str(self.que)


q = MyQueue()

# データを順にenqueueする
q.enqueue('a')
print(q)
q.enqueue('b')
print(q)
q.enqueue('c')
print(q)

# データを順にdequeueし、val1～val3に代入する
val1 = q.dequeue()
print(q)
val2 = q.dequeue()
print(q)
val3 = q.dequeue()
print(q)

# 取り出したデータを確認する
print(val1, val2, val3)
