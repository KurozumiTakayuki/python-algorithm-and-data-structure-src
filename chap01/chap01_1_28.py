class Cood:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)


class TwoPoints:

    def __init__(self, x1, y1, x2, y2):
        self.p1 = Cood(x1, y1)
        self.p2 = Cood(x2, y2)

    def __str__(self):
        return str(self.p1) + "-" + str(self.p2)


tp = TwoPoints(100, 200, 110, 220)
print(tp)
