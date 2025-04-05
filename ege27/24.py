import turtle

def clasterisation(data, r):
    clasters = []
    while data:
        clasters.append([data.pop()])
        for x1, y1 in clasters[-1]:
            sosedi = [[x2, y2] for x2, y2 in data if abs(x1 - x2) + abs(y1 - y2) <= r]
            clasters[-1].extend(sosedi)
            for p in sosedi:
                data.remove(p)
    return clasters


def get_centroid(claster):
    r = []
    for x1, y1 in claster:
        r += [(sum(abs(x1 - x2) + abs(y1 - y2) for x2, y2 in claster), [x1, y1])]
    return min(r)[1]


def visual(clasters):
    turtle.up()
    turtle.tracer(0)
    colors = ['red', 'green', 'blue', 'yellow', 'brown', 'black', 'pink', 'purple', 'orange']
    for i, claster in enumerate(clasters):
        for x, y in claster:
            turtle.goto(x * 15, y * 15)
            turtle.dot(6, colors[i % len(colors)])
    turtle.done()


data = [list(map(float, line.split())) for line in open('27data/27-24a.txt')]
clasters = clasterisation(data, 0.5)
print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clasters]
x, y = sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)
print(x * 10000, y * 10000)

data = [list(map(float, line.split())) for line in open('27data/27-24b.txt')]
clasters = clasterisation(data, 0.4)
print([len(c) for c in clasters])
centrs = [get_centroid(c) for c in clasters]
x, y = sum(p[0] for p in centrs) / len(centrs), sum(p[1] for p in centrs) / len(centrs)
print(x * 10000, y * 10000)
visual(clasters)