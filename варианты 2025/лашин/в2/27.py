import math, turtle

def clasterisation(data, r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for p1 in clasters[-1]:
            sosedi = [p2 for p2 in data if math.dist(p2, p1) <= r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters


def clasterisation2(data):
    clasters = [[], [], []]
    for x, y in data:
        if x > 2:
            clasters[0].append([x, y])
        elif y > 0:
            clasters[1].append([x, y])
        else:
            clasters[2].append([x, y])
    return clasters

def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [(sum(math.dist(p1, p2) for p2 in claster), p1)]
    return min(r)[1]
def get_anticentroid(claster):
    r = []
    for p1 in claster:
        r += [(sum(math.dist(p1, p2) for p2 in claster), p1)]
    return max(r)[1]

def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ['red', 'green', 'yellow', 'purple']
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x * 30, y * 30)
            turtle.dot(6, colors[i % len(colors)])
    turtle.done()

data = [list(map(float, line.split())) for line in open('27A.txt')]
clasters = clasterisation(data, 0.7)
print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clasters]
anticentrs = [get_anticentroid(c) for c in clasters]
a1 = math.dist(centrs[0], anticentrs[0])
a2 = math.dist(centrs[1], anticentrs[1])
print(a1 * 10000, a2 * 10000)

data = [list(map(float, line.split())) for line in open('27B.txt')]
clasters = clasterisation2(data)
print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clasters]
anticentrs = [get_anticentroid(c) for c in clasters]
a1 = math.dist(centrs[1], anticentrs[1])
a2 = math.dist(centrs[0], anticentrs[0])
print(a1 * 10000, a2 * 10000)
