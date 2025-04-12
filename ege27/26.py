import math, turtle

def clasterisation(data, r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if math.dist(p1[:-1], p2[:-1]) <= r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters


def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [(sum(math.dist(p1[:-1], p2[:-1]) * p2[-1] for p2 in claster), p1)]
    return min(r)[1]


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ['red', 'green', 'blue', 'yellow', 'brown', 'black', 'pink', 'purple', 'orange']
    for i, claster in enumerate(clasters):
        for x, y, z in claster:
            turtle.goto(x//2, y//2)
            turtle.dot(6, colors[i % len(colors)])
    for i in range(-1000, 1000, 10):
        turtle.up()
        turtle.goto(-1000, i)
        turtle.down()
        turtle.goto(1000, i)
    for i in range(-1000, 1000, 10):
        turtle.up()
        turtle.goto(i, -1000 )
        turtle.down()
        turtle.goto(i, 1000)

    turtle.done()


data = [list(map(float, line.split())) for line in open('27data/27-26a.txt')]
clasters = clasterisation(data, 30)
print([len(c) for c in clasters])
visual(clasters)
centrs = [get_centroid(c) for c in clasters[1:-2]]
x, y = sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)
print(x * 100000, y * 100000)

data = [list(map(float, line.split())) for line in open('27data/27-26b.txt')]
clasters = clasterisation(data, 30)
print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clasters]
x, y = sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)
print(x * 100000, y * 100000)
