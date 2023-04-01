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
        return self.x == other.xaa and self.y == other.y

    def __lt__(self, other):
        return self.y < other.y

    def __repr__(self):
        #return "Point(" + str(self.x) + ", " + str(self.y) + ")"
        return "Point(%s, %s)" % (self.x, self.y)
        #"Point(%s, %s)" - строка описания формата и далее указываем значения, которые будут в нее подставляться
        #% (self.x, self.y) - значения кортежа