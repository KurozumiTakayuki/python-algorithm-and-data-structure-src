from math import sqrt


class Cood:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_distance(self):
        return sqrt(self.x ** 2 + self.y ** 2)


obj = Cood(300, 400)
dist = obj.calc_distance()
print(dist)
