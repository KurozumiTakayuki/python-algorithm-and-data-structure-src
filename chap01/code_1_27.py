class Cood:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)


obj = Cood(100, 200)
print(obj)
