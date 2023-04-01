from geom2d.point import Point

l = []

#список, которая состоит из координат параболы
for i in range(-5, 6):
    l.append(Point(i, i*i))

# повернуть паарболу рогами вниз = элементы по оси у примут отрицательное значение
#for el in l:
    #el.y = -el.y

l2 = []

for el in l:
    l2.append(Point(el.x, -el.y))

print(l)
print(l2)