def f(n):
    while '333' in n or '555' in n:
        if '555' in n:
            n.replace('555', '3', 1)
        else:
            n.replace('333','5', 1)
    return n


a = []
for i in range(4, 10000):
    s = '3'+ i * '5'
    if sum(map(int, f(s))):
        a.append(i)
print(max(a))