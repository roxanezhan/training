
from geom2d.point import Point

l1 = [Point(3, 1), Point(0, 0), Point(1, 2)]

#def x(p): #это функция координаты х
    #return p.x

#def y(p): #это функция координаты у
    #return p.y

#l2 = sorted(l1, key=x)

#l2 = sorted(l1, key = lambda p: p.x) # можно обратиться к кординате без ее объевления через функцию, используя ламбду
l2 = sorted(l1, key = lambda p: p.distance(Point(0,0))) #сравнить по расстоянию от коррдинаты 0,0
print(l1)
print(l2)