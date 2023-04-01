#filter создает новый список, отфильтровывая значения списка
from geom2d.point import Point

l = []

l = list(map(lambda i: Point(i, i*i), range(-5, 6)))

#отфильтровать оставив только положительные значения х
#l2 = list(filter(lambda p: p.x > 0, l))

#отфильтровать оставив только четные значения х
l2 = list(filter(lambda p: p.x % 2 == 0, l))

print(l)
print(l2)