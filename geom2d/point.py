from math import sqrt


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def distance(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx*dx + dy*dy)

    #операция сравнения. Если эту функцию закомменить, то в геометри оба списка будут неправильно сравниваться
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y