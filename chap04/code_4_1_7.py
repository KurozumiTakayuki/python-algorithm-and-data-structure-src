class MyStack:

    def __init__(self, N):
        self.N = N
        self.stack = [None] * N
        self.pointer = 0

    def push(self, value):
        if self.N <= self.pointer:
            # スタックがいっぱいの場合はpush失敗
            print("スタックがいっぱいなのでpushできません。")
            return

        self.stack[self.pointer] = value
        self.pointer += 1

    def pop(self):
        # スタックに要素がない場合はpop失敗
        if self.pointer == 0:
            print("スタックに要素がないのでpopできません。")
            return

        value = self.stack[self.pointer - 1]
        self.stack[self.pointer - 1] = None
        self.pointer -= 1
        return value

    def __str__(self):
        return str(self.stack)


my_stack = MyStack(4)

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
