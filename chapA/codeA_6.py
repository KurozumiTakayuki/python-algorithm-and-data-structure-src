class Cood:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)

    def __lt__(self, other):
        norm1 = (self.x ** 2 + self.y ** 2)
        norm2 = (other.x ** 2 + other.y ** 2)
        return norm1 < norm2


x = Cood(100, 200)
y = Cood(10, 20)
print(x < y)
