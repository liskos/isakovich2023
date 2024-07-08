def f(n):
    while '4444' in n or '777' in n:
        if '777' in n:
            n = n.replace('777', '4', 1)
        else:
            n = n.replace('4444', '7', 1)
    return n


b = []
for i in range(4, 10000):
    b.append(sum(map(int,f('4' + i * '7'))))
print(max(b))

