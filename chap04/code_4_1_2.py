class MyStack:

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def __str__(self):
        return str(self.data)


my_stack = MyStack()

# データを順にpushする
my_stack.push("a")
print(my_stack)
my_stack.push("b")
print(my_stack)
my_stack.push("c")
print(my_stack)

# データを順にpopし、val1～val3に代入する
val1 = my_stack.pop()
print(my_stack)
val2 = my_stack.pop()
print(my_stack)
val3 = my_stack.pop()
print(my_stack)

# 取り出したデータを確認する
print(val1, val2, val3)
