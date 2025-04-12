import turtle, math


def clasterisation(data, r):
    clasters = [[], [], []]
    for x, y in data:
        a = math.atan((y - 5) / (x - 5)) * 180 / 3.14
        if 0 < a < 90:
            clasters[0].append([x, y])
        elif  a < 0 and x < 5:
            clasters[1].append([x, y])
        else:
            clasters[2].append([x, y])

    return clasters

def clasterisation2(data):
    clasters = [[], [], [], [], []]
    for x, y in data:
        if x > 10 and y < 10:
            clasters[0].append([x, y])
        elif  x > 10 and y > x:
            clasters[1].append([x, y])
        elif  x > 10 and y < x:
            clasters[2].append([x, y])
        elif y < x:
            clasters[3].append([x, y])
        else:
            clasters[4].append([x, y])

    return clasters



def get_centroid(claster):
    r = []
    for p1 in claster:
        r += [(sum(math.dist(p1, p2) for p2 in claster), p1)]
    return min(r)[1]

def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ['red', 'green', 'yellow', 'purple', 'pink', 'brown', 'black', 'cyan', 'orange']
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x * 10, y * 10)
            turtle.dot(6, colors[i % len(colors)])
    turtle.done()

data = [list(map(float, line.split())) for line in open('27data/27-63a.txt')]
clasters = clasterisation(data, 0.6)

print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clasters]
x, y = sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)
print(x * 100000, y * 100000)

data = [list(map(float, line.split())) for line in open('27data/27-63b.txt')]
clasters = clasterisation2(data)
print([len(c) for c in clasters])
visual(clasters)
centrs = [get_centroid(c) for c in clasters]
x, y = sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)
print(x * 100000, y * 100000)
