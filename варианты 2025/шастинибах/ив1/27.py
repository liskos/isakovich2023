import math, turtle

def clasterisation2(data):
    clasters = [[], [], []]
    for x, y in data:
        if x < 5 and y < 10:
            clasters[0].append([x, y])
        elif x > 15:
            clasters[1].append([x, y])
        else:
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
    colors = ['red', 'green', 'yellow', 'purple']
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x * 30, y * 30)
            turtle.dot(6, colors[i % len(colors)])
    turtle.done()

data = [list(map(float, line.split())) for line in open('27a.txt')]
clasters = clasterisation2(data)
print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clasters]
plot = [len(c) / 16 for c in clasters]
print(plot)
print(sum(plot) / 3 * 1000, math.dist(centrs[0], centrs[1]) * 1000)

