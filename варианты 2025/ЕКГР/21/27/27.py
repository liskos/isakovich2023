import turtle, math
from re import match


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ['red', 'green', 'blue', 'yellow', 'pink', 'orange']
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x * 10, y * 10)
            turtle.dot(5, colors[i % len(colors)])
    turtle.done()


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

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [(sum(math.dist(p1, p2) for p2 in claster), p1)]
    return min(r)[1]


data = [list(map(float, line.split())) for line in open('27a.txt')]
clasters = clasterisation(data, 2)
centroid = [get_centroid(x) for x in clasters]
x, y = sum(x[0] for x in centroid) / len(centroid), sum(x[1] for x in centroid) / len(centroid)
print(x*10000, y*10000)

data = [list(map(float, line.split())) for line in open('27b.txt')]
clasters = clasterisation(data, 3)
print([len(x) for x in clasters])
visual(clasters)
centroid = [get_centroid(x) for x in clasters]
x, y = sum(x[0] for x in centroid) / len(centroid), sum(x[1] for x in centroid) / len(centroid)
print(x*10000, y*10000)