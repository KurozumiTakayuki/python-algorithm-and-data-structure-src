class Cood:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# インスタンス化
obj = Cood(300, 400)
print(obj.x, obj.y)

# インスタンス変数の更新
obj.x = 100
obj.y = 200
print(obj.x, obj.y)
