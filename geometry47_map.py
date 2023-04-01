#map преобразует используемый список
from geom2d.point import Point

l = []
#list comprehension
#l = [Point(i, i*i) for i in range(-5, 6)]

#вместо контсрукции list comprehension можно то же самое написать в map
l = list(map(lambda i: Point(i, i*i), range(-5, 6)))

#парабола рогами вниз, используя map
l2 = list(map(lambda p: Point(p.x, -p.y), l))

print(l)
print(l2)