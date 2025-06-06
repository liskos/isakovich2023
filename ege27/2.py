import math, turtle

def clasterisation(data, r):
    clasters = []
    while data: # пока data не пустой
        clasters.append([data.pop()]) # pop удаляет точку из data и добавляет в clasters
        for p1 in clasters[-1]: #перебираем звезды последнего кластера
            sosedi = [p2 for p2 in data if math.dist(p1, p2) <= r] #находим соседей звёзд последнего кластера, r - расстояние
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters



def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [(sum(math.dist(p1, p2) for p2 in claster), p1)] #картеж суммы расстояний точек и точки от которой находили сумму
    return min(r)[1]


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ['red', 'green', 'yellow', 'pink', 'purple', 'black']
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x * 30, y * 30)
            turtle.dot(6, colors[i % len(colors)])
    turtle.done()



data = [list(map(float, line.split())) for line in open('27data/27-2a.txt')]
clasters = clasterisation(data, 0.7)
print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clasters]
x, y = sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)
print(x * 10000, y * 10000)

data = [list(map(float, line.split())) for line in open('27data/27-2b.txt')]
clasters = clasterisation(data, 0.7)
print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clasters]
x, y = sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)
print(x * 10000, y * 10000)