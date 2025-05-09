import math, turtle


def clasterisation(data, r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if math.dist(p1, p2) < r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [(sum(math.dist(p2, p1) for p2 in claster), p1)]
    return max(r)[1]

def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ['green', 'red', 'brown', 'yellow']
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x * 10, y * 10)
            turtle.dot(3, colors[i % len(colors)])

def retran(data, centrs):
    t = [0, 0]
    s = 0
    for p1 in data:
        d = sum(math.dist(p1, p2) for p2 in centrs)
        if d > s:
            t = p1
            s = d
    return t

data = [list(map(float, line.split())) for line in open('27_a.txt')]
clasters = clasterisation(data.copy(), 2)
print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clasters]
# visual(clasters)
# for x,y in centrs:
#     turtle.goto(x*10, y*10)
#     turtle.dot(3, "orange")
# turtle.done()
x, y = retran(data, centrs)
print(int(abs(x * 10000)), int(abs(y * 10000)))

data = [list(map(float, line.split())) for line in open('27_b.txt')]
clasters = clasterisation(data, 2)
print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clasters]
x, y = retran(data, centrs)
print(int(abs(x * 10000)), int(abs(y * 10000)))
