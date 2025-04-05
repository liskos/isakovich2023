import math, turtle

def clasterisation(data, r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if math.dist(p1, p2) <= r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters

def clasterisation2(data):
    clasters = [[], [], []]
    for x, y in data:
        if x < 5 and y > 5:
            clasters[0].append([x, y])
        elif 1 < x < 6 and 1 < y < 5:
            clasters[1].append([x, y])
        elif 7 < x < 11 and 2 < y < 7:
            clasters[2].append([x, y])
    return clasters


def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [(sum(math.dist(p1, p2) for p2 in claster), p1)]
    return min(r)[1]


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ['red', 'green', 'blue', 'yellow', 'brown', 'black', 'pink']
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x * 30, y * 30)
            turtle.dot(6, colors[i % len(colors)])
    turtle.done()

def minmax(claster1, claster2):
    pmin = 10 ** 10
    pmax = 0
    for p1 in claster1:
        for p2 in claster2:
            s = math.dist(p1, p2)
            pmin = min(s, pmin)
            pmax = max(s, pmax)
    return pmin, pmax

data = [list(map(float, line.split())) for line in open('27data/27-21a.txt')]
clasters = clasterisation(data, 1)

print([len(c) for c in clasters])
x, y = minmax(clasters[0], clasters[1])
print(x * 10000, y * 10000)
data = [list(map(float, line.split())) for line in open('27data/27-21b.txt')]
clasters = clasterisation2(data)
mi1, ma1 = minmax(clasters[0], clasters[1])
mi2, ma2 = minmax(clasters[2], clasters[1])
mi3, ma3 = minmax(clasters[0], clasters[2])
print([len(c) for c in clasters])
visual(clasters)
print(min(mi1, mi2, mi3) * 10000, max(ma1, ma2, ma3) * 10000)

